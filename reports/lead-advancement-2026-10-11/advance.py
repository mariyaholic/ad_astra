"""Specialist follow-up adapter using existing Cygnus scientific implementations.

Fresh outputs are separate from frozen campaigns. Rejected epochs cannot become
defining events. Nulls are fixed-event diagnostics, not the original blind-search FAP.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

from cygnus.fileio import atomic_write_json, sha256_file

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / 'reports/lead-resolution-2026-09-30'
SCRATCH = Path('D:/AO_Artifacts/cygnus_scratch')
CONFIG = json.loads((BASE / 'config.json').read_text())


def checked_product(path, digest):
    if sha256_file(path) != digest:
        raise ValueError('source product checksum mismatch: ' + path.name)
    return path


def defining_events(lead):
    rejected = {tuple(x) for x in lead.get('rejected', [])}
    events = [tuple(x) for x in lead['events']]
    if any(x in rejected for x in events):
        raise ValueError('rejected event appears in defining selection')
    return events


def validate_archive_body(body):
    if body.lstrip().startswith(b'{'):
        payload = json.loads(body)
        if payload.get('status') == 'error':
            raise ValueError('archive error response: ' + str(payload.get('msg')))


def known_veto(row, siblings):
    periodic = [r for r in siblings if r.get('pl_orbper') and r.get('pl_tranmid')]
    if periodic:
        p = periodic[0]
        return {'kind':'ephemeris','period_days':float(p['pl_orbper']),'t0_bjd':float(p['pl_tranmid']),'veto_phase':.02,
                'source_toi':p['toi']}
    if row.get('pl_tranmid'):
        return {'kind':'single_epoch','t0_bjd':float(row['pl_tranmid']),'veto_hours':4.,'source_toi':row['toi']}
    return None


def legacy():
    source = BASE / 'resolve_leads.py'
    s = importlib.util.spec_from_file_location('existing_lead_methods', source)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    m.HERE = HERE
    return m


def source_row(cid):
    data = json.loads((HERE / 'archive_refresh.json').read_text())
    query = next(q for q in data['queries'] if q['label'] == cid + ':toi')
    if query['state'] != 'answered':
        raise ValueError('fresh exact TOI row unavailable: ' + cid)
    rows = query['result']
    if isinstance(rows, list):
        # Some TICs have sibling rows; select the exact TOI identifier below.
        toi = float(cid.split('-', 1)[1].replace('-', '.'))
        row = next(r for r in rows if abs(float(r['toi']) - toi) < 1e-6)
    else:
        names = [m['name'] for m in rows['metadata']]
        toi = float(cid.split('-', 1)[1].replace('-', '.'))
        row = next(dict(zip(names, r)) for r in rows['data'] if abs(float(dict(zip(names, r))['toi']) - toi) < 1e-6)
    return row


def event_null():
    from cygnus.campaign.runner import Context
    from cygnus.campaign.steps import step_event_null
    from cygnus.campaign.lightcurve import read_spoc
    import numpy as np
    import yaml

    output = {}
    for lead in CONFIG['leads']:
        cid = lead['slug']
        row = source_row(cid)
        fresh = json.loads((HERE / 'archive_refresh.json').read_text())
        sibling_rows = next(q['result'] for q in fresh['queries'] if q['label']==cid + ':toi')
        if not isinstance(sibling_rows,list):
            names = [m['name'] for m in sibling_rows['metadata']]
            sibling_rows = [dict(zip(names,r)) for r in sibling_rows['data']]
        old = json.loads((ROOT / 'campaigns' / cid / 'sky_record.json').read_text())
        original = yaml.safe_load((ROOT / 'campaigns' / (cid + '.yaml')).read_text())
        target = dict(original['targets'][0])
        target.update(period_days=row.get('pl_orbper'), t0_bjd=row.get('pl_tranmid'), duration_h=lead['duration_h'])
        target['source'] = 'archive_refresh.json exact TOI row; frozen events retained as fixed test hypotheses'
        spec = {'campaign_id': cid + '-advance-2026-10-11', 'outputs': f'reports/{HERE.name}/{cid}',
                'targets': [target], 'random_seed': 20261011,
                'veto': known_veto(row,sibling_rows)}
        ctx = Context(spec, None, ROOT)
        candidates, products = [], {}
        for sector, mid in defining_events(lead):
            p = next(p for p in old['products'] if f'-s{sector:04d}-' in p['id'] and p.get('format') == 'spoc_lc')
            path = checked_product(SCRATCH / ('campaign_' + cid) / p['id'], p['sha256'])
            lc = read_spoc(path)
            assert lc.primary.get('TICID') == lead['tic'], 'TIC identity mismatch'
            assert np.nanmin(lc.time_bjd) <= mid <= np.nanmax(lc.time_bjd), 'event outside product'
            products[p['id']] = {'path': 'scratch:campaign_' + cid + '/' + p['id'], 'sha256': p['sha256'], 'target': target['name']}
            candidates.append({'product': p['id'], 'event_bjd': mid})
        ctx._results = {'fetch_products': {'products': products}, 'period_aliases': {'candidates': candidates}}
        params = {'degree': 2, 'n_null': 1000, 'n_inject': 200, 'min_n': 100, 'exclude_days': 1.5, 'max_frac': .05, 'min_recovery': .9}
        result = step_event_null(ctx, params)
        output[cid] = {'checks': ctx.checks, 'result': result, 'spec': spec, 'params': params, 'products': products,
                       'source_row': row, 'method': 'existing cygnus.campaign.steps.step_event_null; random event-free centres preserve local time ordering; no blind search-wide calibration'}
        atomic_write_json(HERE / 'event_null_summary.json', output)
        print(cid, ctx.checks, flush=True)


def localization():
    import numpy as np
    from astropy.io import fits
    from scipy.ndimage import binary_dilation
    from cygnus.analysis.localize import block_bootstrap_offset

    result = {}
    for lead in CONFIG['leads']:
        cid = lead['slug']
        source_row(cid)
        per = []
        for sector, mid in defining_events(lead):
            path = next((SCRATCH / ('campaign_' + cid) / 'tpf').glob(f'*s{sector:04d}-*.fits'))
            digest = sha256_file(path)
            # Cached pixel reduction: retain fresh hash, exact header and epoch.
            # The metadata-only independent receipt does not assert a prior hash.
            with fits.open(path, memmap=True) as h:
                assert int(h[0].header['TICID']) == lead['tic']
                table = h[1].data
                t = np.asarray(table['TIME'],float) + h[1].header['BJDREFI'] + h[1].header['BJDREFF']
                valid = (table['QUALITY'] == 0) & np.isfinite(t) & (np.abs(t-mid) < .75)
                flux = np.asarray(table['FLUX'][valid],float)
                t = t[valid]
                finite = np.all(np.isfinite(flux.reshape(len(flux),-1)),axis=1)
                t, flux = t[finite], flux[finite]
                aperture = (h[2].data & 2) != 0
                unit = h[1].header.get('TUNIT5','electron/s')
                header = {k:h[0].header.get(k) for k in ('TICID','SECTOR','CAMERA','CCD','PROCVER')}
            dur = lead['duration_h']/24
            event = np.abs(t-mid) <= dur/2
            control = (np.abs(t-mid) > dur) & (np.abs(t-mid) < .5)
            for label, mask in [('pipeline',aperture), ('dilated',binary_dilation(aperture))]:
                for block in (3,10):
                    audit = block_bootstrap_offset(flux,event,control,mask,~mask,flux_unit=unit,block=block,draws=300,seed=20261011,fail_ratio=3.)
                    per.append({'product':path.name,'sha256':digest,'header':header,'event_bjd_tdb':mid,'sector':sector,'aperture':label,
                                'n_event':int(event.sum()),'n_control':int(control.sum()),'result':audit,
                                'distance_arcsec_approx':21 * audit['distance_pix'] if 'distance_pix' in audit else None})
            result[cid] = per
            atomic_write_json(HERE / 'localization_controls.json', result)
            print(cid, sector, [(p['aperture'],p['result']['state']) for p in per[-4:]],flush=True)


def new_sector():
    """Official S107 reduction at the prior timing hypothesis, without rescreening."""
    import requests
    import numpy as np
    from astropy.io import fits
    from cygnus.campaign.runner import Context
    from cygnus.campaign.steps import step_event_null
    from cygnus.campaign.lightcurve import read_spoc
    from cygnus.analysis.events import box_measure
    from cygnus.analysis.localize import block_bootstrap_offset
    from scipy.ndimage import binary_dilation
    from urllib.parse import quote

    metadata = json.loads((HERE / 'S107_PRODUCTS.json').read_text())
    folder = SCRATCH / HERE.name / 's107'
    folder.mkdir(parents=True,exist_ok=True)
    files = {}
    for product in metadata['products']:
        size = int(product['size'])
        if size > 100_000_000:
            raise ValueError('S107 product exceeds 100 MB screened budget')
        name = product['productFilename']
        path = folder / name
        url = 'https://mast.stsci.edu/api/v0.1/Download/file?uri=' + quote(product['dataURI'],safe='')
        if not path.is_file() or path.stat().st_size != size:
            response = requests.get(url,timeout=60,stream=True)
            response.raise_for_status()
            downloaded = 0
            with path.open('wb') as stream:
                for block in response.iter_content(65536):
                    downloaded += len(block)
                    if downloaded > size:
                        raise ValueError('S107 download exceeds metadata size')
                    stream.write(block)
        assert path.stat().st_size == size, 'S107 product size mismatch'
        with fits.open(path,memmap=True) as h:
            h.verify('exception')
            assert int(h[0].header['TICID']) == 70797900 and int(h[0].header['SECTOR']) == 107
            assert h[1].header['TIMESYS'] == 'TDB'
            headers = {k:h[1].header.get(k) for k in ('TIMESYS','BJDREFI','BJDREFF','TIMEDEL','TSTART','TSTOP')}
        files[name] = {'sha256':sha256_file(path),'bytes':size,'url':url,'dataURI':product['dataURI'],'time_headers':headers}
        atomic_write_json(HERE / 'S107_INPUTS.json', {'utc':datetime.now(timezone.utc).isoformat(),'products':files})
        print('S107 product verified',name,size,flush=True)
    # The prior S107 FFI reduction used CCD-centre times; this prediction is a
    # conditional timing family, not a conversion of those times into target BJD.
    mid = 2458365.8437503786 + 92 * 31.57966184
    dur = 1.24729878 / 24
    lc_path = next(folder.glob('*_lc.fits'))
    lc = read_spoc(lc_path)
    u = lc.usable
    t, y = lc.time_bjd[u], lc.pdc[u]/np.nanmedian(lc.pdc[u])
    measurements = [{'shift_days':shift,'degree':degree,'measurement':box_measure(t,y,mid+shift,dur,degree)}
                    for degree in (1,2,3) for shift in (-.02,0.,.02)]
    spec = {'campaign_id':'toi-224-s107-advance','outputs':f'reports/{HERE.name}/toi-224-s107',
            'targets':[{'name':'TOI-224.01','duration_h':1.24729878}],'random_seed':20261011,'veto':None}
    ctx = Context(spec,None,ROOT)
    pid = lc_path.name
    ctx._results = {'fetch_products':{'products':{pid:{'path':'scratch:' + lc_path.relative_to(SCRATCH).as_posix(),'target':'TOI-224.01'}}},
                    'period_aliases':{'candidates':[{'product':pid,'event_bjd':mid}]}}
    null = step_event_null(ctx,{'degree':2,'n_null':1000,'n_inject':200,'min_n':100})
    controls = []
    with fits.open(next(folder.glob('*_tp.fits')),memmap=True) as h:
        table = h[1].data
        tt = np.asarray(table['TIME'],float) + h[1].header['BJDREFI'] + h[1].header['BJDREFF']
        valid = (table['QUALITY']==0) & np.isfinite(tt) & (np.abs(tt-mid)<.75)
        flux, tt = np.asarray(table['FLUX'][valid],float),tt[valid]
        finite = np.all(np.isfinite(flux.reshape(len(flux),-1)),axis=1)
        flux, tt = flux[finite],tt[finite]
        aperture = (h[2].data & 2)!=0
    for label,mask in [('pipeline',aperture),('dilated',binary_dilation(aperture))]:
        for block in (3,10):
            result = block_bootstrap_offset(flux,np.abs(tt-mid)<=dur/2,(np.abs(tt-mid)>dur)&(np.abs(tt-mid)<.5),mask,~mask,
                                            flux_unit='electron/s',block=block,draws=300,seed=20261011)
            controls.append({'aperture':label,'result':result,'distance_arcsec_approx':21*result['distance_pix'] if 'distance_pix' in result else None})
    atomic_write_json(HERE / 'S107_TESTS.json',{'prediction_bjd_tdb':mid,'prediction_source':'historical conditional31.57966184d timing family; not a solved orbit',
                      'same_epoch_as_prior_ffi':True,'sensitivity_trials':9,'measurements':measurements,'native_null':null,'native_checks':ctx.checks,
                      'localization':controls,'caveat':'same sky pixels, independent reduction; selection-touched null diagnostics; no component assignment or search-wide FAP'})
    print('S107 checks',ctx.checks,flush=True)


def access_probe():
    """Bounded documented Level1 list and previously restricted ESO probes."""
    import requests
    old = json.loads((BASE / 'koa_product_screen.json').read_text())
    out = {'utc':datetime.now(timezone.utc).isoformat(),'koa':[],'eso':[],
           'koa_api_source':'PyKOA1.7.2 official source, core.py lines3262-3265; source archive retained in scratch',
           'limits':'three Level1 metadata requests; one formerly401 product per instrument, headers/prefix only; no authentication'}
    for product in old['products']:
        params = {'instrument':'HIRES','koaid':product['koaid'],'filehand':product['tap_metadata']['filehand']}
        row = {'koaid':product['koaid'],'params':params}
        try:
            r = requests.get('https://koa.ipac.caltech.edu/cgi-bin/KoaAPI/nph-getL1list',params=params,timeout=45)
            row.update(url=r.url,http_status=r.status_code)
            r.raise_for_status()
            row['result'] = r.json()
        except Exception as e:
            row['error'] = type(e).__name__ + ': ' + str(e)
        out['koa'].append(row)
        atomic_write_json(HERE / 'ACCESS_PROBES.json',out)
        print('KOA Level1',product['koaid'],row.get('result',{}).get('result',{}).get('nlev1file'),flush=True)
    manifest = json.loads((BASE / 'spectra_manifest.json').read_text())
    seen = set()
    for p in manifest['products']:
        if '401' not in p.get('error',''):
            continue
        instrument = p['source_row']['instrument_name']
        if instrument in seen:
            continue
        seen.add(instrument)
        link = next(l for l in p['links'] if l.get('semantics')=='#this')
        row = {'instrument':instrument,'url':link['access_url'],'target':p['target']}
        try:
            with requests.get(link['access_url'],headers={'Range':'bytes=0-65535'},stream=True,timeout=45) as r:
                row.update(http_status=r.status_code,content_type=r.headers.get('Content-Type'),content_length=r.headers.get('Content-Length'))
                r.raise_for_status()
                prefix = next(r.iter_content(65536),b'')
                row['prefix_bytes'] = len(prefix)
                row['fits_prefix'] = prefix.startswith(b'SIMPLE')
        except Exception as e:
            row['error'] = type(e).__name__ + ': ' + str(e)
        out['eso'].append(row)
        atomic_write_json(HERE / 'ACCESS_PROBES.json',out)
        print('ESO fresh access',instrument,row.get('http_status'),flush=True)


def hires_orders():
    """Inspect bounded red browse orders and QA; no calibrated component RV claim."""
    import requests
    import numpy as np
    from astropy.io import fits
    import matplotlib.pyplot as plt
    from scipy.ndimage import median_filter

    probes = json.loads((HERE / 'ACCESS_PROBES.json').read_text())
    prior = HERE / 'HIRES_ORDER_AUDIT.json'
    if prior.exists() and not (HERE / 'HIRES_ORDER_AUDIT_INITIAL_ROUTE.json').exists():
        atomic_write_json(HERE / 'HIRES_ORDER_AUDIT_INITIAL_ROUTE.json',json.loads(prior.read_text()))
    folder = SCRATCH / HERE.name / 'hires_lev1'
    folder.mkdir(parents=True,exist_ok=True)
    output = {'utc':datetime.now(timezone.utc).isoformat(),'products':[],
              'budget':'only CCD3 flux and QA; <=2 MB/file and 20 MB aggregate; stop after three consecutive retrieval failures',
              'science_limit':'MAKEE browse spectra; not precision-validated component RVs. Two epochs cannot establish an orbit.',
              'format_source':'https://koa.ipac.caltech.edu/UserGuide/HIRES/extracted_products.html'}
    total, failures = 0, 0
    figures = HERE / 'figures'
    figures.mkdir(exist_ok=True)
    for product in probes['koa']:
        result = product.get('result',{}).get('result',{})
        prefix = result.get('lev1subdir_prefix')
        if not prefix:
            continue
        for group in result.get('data',[]):
            if group['subdir'] not in ('binaryfits/ccd3/flux','qa'):
                continue
            for name in sorted(group['lev1files']):
                if group['subdir']=='qa' and '_3_' not in name and '_0_' not in name:
                    continue
                path = folder / name
                params = {'instrument':'HIRES','koaid':product['koaid'],'filehand':prefix + '/' + group['subdir'] + '/' + name}
                row = {'koaid':product['koaid'],'filename':name,'subdir':group['subdir'],'params':params}
                try:
                    cached_valid = path.exists()
                    if cached_valid:
                        try:
                            validate_archive_body(path.read_bytes())
                        except ValueError:
                            cached_valid = False
                    if not cached_valid:
                        with requests.get('https://koa.ipac.caltech.edu/cgi-bin/KoaAPI/nph-dnloadL1data',params=params,stream=True,timeout=45) as r:
                            row['http_status'] = r.status_code
                            r.raise_for_status()
                            body = bytearray()
                            for b in r.iter_content(65536):
                                body.extend(b)
                                if len(body)>2_000_000 or total+len(body)>20_000_000:
                                    raise ValueError('bounded HIRES pilot transfer exceeded')
                            validate_archive_body(body)
                            path.write_bytes(body)
                            total += len(body)
                    row.update(sha256=sha256_file(path),bytes=path.stat().st_size)
                    if group['subdir']=='qa':
                        row['qa_text'] = path.read_text(errors='replace')
                    else:
                        with fits.open(path,memmap=False) as h:
                            h.verify('exception')
                            row['headers'] = {k:h[0].header.get(k,h[1].header.get(k)) for k in
                                              ('TARGNAME','OBJECT','KOAID','EXQUAL','HELIOVEL','VHELIO','VACUUM','SPECSYS','DATE-OBS','UT','EXPTIME','IODIN','IODOUT')}
                            row['columns'] = h[1].columns.names
                            data = h[1].data
                            fields = {k.lower():k for k in row['columns']}
                            wave = np.asarray(data[fields['wave']],float).ravel()
                            flux = np.asarray(data[fields['flux']],float).ravel()
                            row['wave_range_angstrom'] = [float(np.nanmin(wave)),float(np.nanmax(wave))]
                            row['finite_flux_fraction'] = float(np.mean(np.isfinite(flux)))
                            if wave.min()<6718.6<wave.max():
                                keep = (wave>6713)&(wave<6725)&np.isfinite(flux)
                                norm = median_filter(flux,size=201,mode='nearest')
                                mask = keep & (norm>0)
                                row['ca_window'] = {'wave_vacuum_heliocentric_angstrom':wave[mask].tolist(),'flux_normalized':(flux[mask]/norm[mask]).tolist(),
                                                   'interpretation':'line-profile inspection only; rest wavelengths/blends, component identity and calibration errors prevent orbital RV inference'}
                                fig,ax = plt.subplots(figsize=(8,3))
                                ax.plot(wave[mask],flux[mask]/norm[mask],lw=.8)
                                ax.set(xlabel='Wavelength (vacuum, heliocentric Angstrom; KOA convention)',ylabel='Relative flux',title=product['koaid'] + ' — Ca I region (browse)')
                                fig.tight_layout()
                                fig.savefig(figures/(product['koaid']+'.png'),dpi=150)
                                plt.close(fig)
                    failures = 0
                    row['state'] = 'inspected'
                except Exception as exc:
                    failures += 1
                    row.update(state='failed',error=type(exc).__name__ + ': ' + str(exc))
                output['products'].append(row)
                atomic_write_json(HERE / 'HIRES_ORDER_AUDIT.json',output)
                print('HIRES pilot',name,row['state'],row.get('wave_range_angstrom'),flush=True)
                if failures>=3:
                    print('HIRES pilot stopped after three consecutive failures',flush=True)
                    return


def retain():
    """Produce an aggregate sky record and separate conservative per-lead gate views."""
    import importlib.metadata
    import subprocess
    from cygnus.campaign.tiers import decide
    from cygnus.colab import build_manifest, write_manifest
    nulls = json.loads((HERE / 'event_null_summary.json').read_text())
    loc = json.loads((HERE / 'localization_controls.json').read_text())
    checks, targets, products, tiers = [], [], {}, {}
    for lead in CONFIG['leads']:
        cid = lead['slug']
        old = json.loads((ROOT / 'campaigns' / cid / 'sky_record.json').read_text())
        targets.extend(old['targets'])
        for p in old['products']:
            products[p['id']] = p
        per = []
        for name, check in nulls[cid]['checks'].items():
            per.append({'name':name,'state':check['state'],'note':check['note']})
            checks.append({'name':cid + ': ' + name,'state':check['state'],'note':check['note']})
        state = 'failed' if any(r['result']['state']=='failed_localization' for r in loc[cid]) else 'inconclusive'
        per.append({'name':'Independent cached TPF localization (2026-10-11)','state':state,
                    'note':'Two apertures and block lengths3/10; same pixels, descriptive offsets; no resolved component assignment or independent-sky confirmation.'})
        checks.append({'name':cid + ': source localization','state':state,'note':per[-1]['note']})
        combined = dict(old)
        by_name = {c['name']:c for c in old['checks']}
        by_name.update({c['name']:c for c in per})
        combined['checks'] = list(by_name.values())
        spec = dict(nulls[cid]['spec'])
        spec.update(budget='Completed bounded2026-10-11 follow-up: cached inputs,52.7MB newTESS,4.24MB HIRES browse pilot; no extra bulk transfer',
                    discriminating_question='Which component produces the retained dip, and can a validated component orbit explain its epochs?')
        decision = decide(combined,spec=spec)
        tiers[cid] = {'tier':decision.tier,'decision':decision.as_dict(),'comparison':'Historical baseline plus fresh native null/injection and unresolved localization. Canonical record untouched.',
                      'current_checks':per,'spec':spec}
        atomic_write_json(HERE / cid / 'CURRENT_CHECKS.json',tiers[cid])
        summary = f"# {cid}: follow-up disposition\n\nConservative earned tier **{decision.tier}**; evidence remains Unverified lead.\n\n"
        summary += '\n'.join('- '+c['name']+': **'+c['state']+'** — '+c['note'] for c in per)
        summary += '\n\nNext-tier blockers: '+ '; '.join(decision.blockers)+'.\n\nRead ../REPORT.md for spectral access, source alternatives, exact products, uncertainties and limitations. Frozen campaign/candidate records have not been overwritten.\n'
        (HERE / cid / 'FOLLOWUP.md').write_text(summary,encoding='utf-8')
    atomic_write_json(HERE / 'CURRENT_TIERS.json',tiers)
    new = json.loads((HERE/'S107_INPUTS.json').read_text())
    for name,p in new['products'].items():
        products[name] = {'id':name,'archive':'MAST','sha256':p['sha256'],'format':'spoc_lc' if name.endswith('_lc.fits') else 'tpf'}
    spectra = json.loads((HERE/'HIRES_ORDER_AUDIT.json').read_text())
    for p in spectra['products']:
        products[p['filename']] = {'id':p['filename'],'archive':'KOA','sha256':p['sha256'],'format':'QA' if 'qa_text' in p else 'MAKEE browse flux'}
    pare = json.loads((HERE/'PAREDES_SOURCE.json').read_text())
    products['Paredes2022-thesis'] = {'id':'Paredes2022-thesis','archive':'GSU RECONS','sha256':pare['sha256'],'format':'pdf'}
    checks += [{'name':'S107 SPOC source localization','state':'failed','note':'Both apertures offset0.446–0.713arcsec; bootstrap ratios5.22–5.55, without full registration covariance.'},
               {'name':'TOI2666 HIRES2021February red browse QA','state':'passed','note':'10CCD3 flux orders, EXQUAL/QA Pass; browseQA is not RV precision validation.'},
               {'name':'TOI2666 HIRES2021May red browse QA','state':'failed','note':'10CCD3 orders QA Fail; Ca-I order2 absent from extracted list. No componentRV use.'},
               {'name':'TOI2666 eclipse-linked component orbit','state':'not_tested','note':'Paredes Fig157 explicitly NO ORBIT; no numerical componentRV epoch table retrieved; one newly inspected QA-passing red epoch cannot solve orbit.'},
               {'name':'TOI3500 additional precision RV inputs','state':'not_tested','note':'Representative previously restricted HARPS/FEROS science inputs remain401; prior precision-failed measurements not promoted.'},
               {'name':'Original-search false alarms and completeness','state':'not_tested','note':'Fixed-event null/injection tests are not search-wide calibration.'}]
    record = {'schema':'cygnus.sky_record/1','id':HERE.name,'title':'Three specialist leads: native event statistics and archival discrimination',
              'kind':'bounded follow-up analysis','status':'completed','outcome':'lead','evidence':'Unverified lead','date':'2026-10-11',
              'summary':'Local event null/injection checks passed; source/orbit gates remain unresolved. NewS107 official reduction and HIRES browse pilot do not completeT3 or promote evidence.',
              'spec':None,'report':f'reports/{HERE.name}/REPORT.md','search_log':f'reports/{HERE.name}/SEARCH_LOG.md',
              'targets':targets,'products':list(products.values()),'checks':checks}
    atomic_write_json(HERE / 'sky_record.json',record)
    versions = {}
    for name in ('numpy','scipy','astropy','astroquery','matplotlib','pymupdf','pytest'):
        versions[name] = importlib.metadata.version(name)
    head = subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()
    frozen = {str(p.relative_to(ROOT)):sha256_file(p) for lead in CONFIG['leads']
              for p in (ROOT/'campaigns'/lead['slug']/'sky_record.json',ROOT/'campaigns'/(lead['slug']+'.yaml'))}
    atomic_write_json(HERE / 'ENVIRONMENT.json',{'packages':versions,'repository_commit':head,'generated_utc':datetime.now(timezone.utc).isoformat(),
                      'native_sources':{n:sha256_file(ROOT/n) for n in ('src/cygnus/campaign/steps.py','src/cygnus/analysis/events.py','src/cygnus/analysis/localize.py')},
                      'frozen_input_hashes':frozen,'adapter_sha256':sha256_file(Path(__file__))})
    members = [p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='MANIFEST.sha256']
    write_manifest(HERE/'MANIFEST.sha256',build_manifest(HERE,members),comment='New follow-up outputs; frozen campaigns untouched; bulky inputs in designated scratch')
    print('Retained conservative tiers', {cid:r['tier'] for cid,r in tiers.items()},flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',required=True,choices=['archives','event-null','localization','rv-archives','new-sector','access','hires-orders','retain'])
    args = ap.parse_args()
    atomic_write_json(HERE / ('RUN_CONFIG_' + args.mode + '.json'), {'utc':datetime.now(timezone.utc).isoformat(),'mode':args.mode,'config':CONFIG,
                      'adapter_sha256':sha256_file(Path(__file__)),'existing_methods_sha256':sha256_file(BASE/'resolve_leads.py'),
                      'budget':'one target at a time; cached products; metadata timeout 45-60 seconds/request; no redundant bulk transfer',
                      'question':'Which component produces each retained eclipse, and can calibrated component RVs or localization falsify the target interpretation?',
                      'frozen_outputs_untouched':True})
    if args.mode == 'archives': legacy().archives()
    elif args.mode == 'event-null': event_null()
    elif args.mode == 'localization': localization()
    elif args.mode == 'new-sector': new_sector()
    elif args.mode == 'access': access_probe()
    elif args.mode == 'hires-orders': hires_orders()
    elif args.mode == 'retain': retain()
    else:
        legacy().rv_archive(names_only=True)
        legacy().koa_screen()


if __name__ == '__main__':
    main()

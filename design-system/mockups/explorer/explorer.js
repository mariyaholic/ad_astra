/* Cygnus Sky — interactive prototype.
 *
 * Projection: stereographic, ICRS, east to the left (the sky as seen from inside the sphere).
 * Every layer is drawn from data/sky.json and data/fields/*.json, built by build_explorer.py from
 * recorded project files and the catalogue fetches listed in data/PROVENANCE.json.
 * Nothing here invents a position; renditions state what they are generated from.
 */
'use strict';
(() => {
  const D = Math.PI / 180;
  const $ = (s, r = document) => r.querySelector(s);
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const cv = $('#sky');
  const ctx = cv.getContext('2d');
  let W = 0, H = 0, DPR = 1;
  const HOME = { ra: 75 * D, dec: 18 * D, fov: 150 * D };
  const view = { ...HOME };
  const MIN_FOV = 0.25 / 60 * D, MAX_FOV = 200 * D;

  let SKY = null, dirty = true, hover = null, selected = null, anim = null, tour = null;
  const fields = {}, images = {};
  // [on, label, group, swatch class, swatch colour]
  const layers = {
    mw: [true, 'Milky Way · Gaia counts', 'Sky', 'soft', 'linear-gradient(90deg,rgba(200,205,225,.15),rgba(214,220,240,.55))'],
    stars: [true, 'Bright stars · BSC5', 'Sky', 'soft', 'radial-gradient(circle,#fff 30%,transparent 35%) 0 0/8px 8px'],
    consts: [true, 'Constellation names', 'Sky', '', 'transparent'],
    grid: [true, 'RA / Dec grid', 'Sky', '', 'rgba(150,170,210,.5)'],
    ref: [true, 'Ecliptic · galactic plane', 'Sky', 'dash', 'rgba(214,160,102,.8)'],
    patches: [true, 'Query footprints', 'Project', 'multi', ''],
    image: [true, 'Survey images', 'Project', 'soft', 'linear-gradient(135deg,#1b2a4a,#6c5a3a)'],
    gaia: [true, 'Gaia DR3 sources', 'Project', '', 'var(--svc-gaia)'],
  };
  const on = k => layers[k][0];

  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const SVC_COL = {}; // filled after load
  const STATUS_COL = {};

  // ------------------------------------------------------------ vectors & projection
  const vec = (ra, dec) => { const c = Math.cos(dec); return [c * Math.cos(ra), c * Math.sin(ra), Math.sin(dec)]; };
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const radec = p => [Math.atan2(p[1], p[0]) < 0 ? Math.atan2(p[1], p[0]) + 2 * Math.PI : Math.atan2(p[1], p[0]), Math.asin(Math.max(-1, Math.min(1, p[2])))];
  let C, E, N, scale, cosLimit;
  function setup() {
    C = vec(view.ra, view.dec);
    E = [-Math.sin(view.ra), Math.cos(view.ra), 0];
    N = [-Math.sin(view.dec) * Math.cos(view.ra), -Math.sin(view.dec) * Math.sin(view.ra), Math.cos(view.dec)];
    scale = (W / 2) / (2 * Math.tan(view.fov / 4));
    const diag = Math.hypot(W, H) / 2 / scale;          // stereographic radius of the corner
    cosLimit = Math.cos(Math.min(Math.PI * 0.92, 2 * Math.atan(diag / 2) + 2 * D));
  }
  function project(p) {
    const cc = dot(p, C);
    if (cc < cosLimit) return null;
    const k = 2 / (1 + cc);
    return [W / 2 - k * dot(p, E) * scale, H / 2 - k * dot(p, N) * scale];
  }
  function unproject(sx, sy) {
    const X = -(sx - W / 2) / scale, Y = -(sy - H / 2) / scale, rho = Math.hypot(X, Y);
    if (rho < 1e-12) return C.slice();
    const c = 2 * Math.atan(rho / 2), s = Math.sin(c) / rho, k = Math.cos(c);
    return [0, 1, 2].map(i => C[i] * k + (E[i] * X + N[i] * Y) * s);
  }
  // point offset from (ra,dec) by x east, y north (radians, gnomonic tangent plane)
  function offset(ra, dec, x, y) {
    const c = vec(ra, dec), e = [-Math.sin(ra), Math.cos(ra), 0], n = [-Math.sin(dec) * Math.cos(ra), -Math.sin(dec) * Math.sin(ra), Math.cos(dec)];
    const p = [0, 1, 2].map(i => c[i] + e[i] * x + n[i] * y), m = Math.hypot(...p);
    return p.map(v => v / m);
  }
  function keepUnder(p0, sx, sy) { // move the view so sky vector p0 sits under screen point (sx, sy)
    for (let i = 0; i < 3; i++) {
      setup();
      const [ra0, de0] = radec(p0), [ra1, de1] = radec(unproject(sx, sy));
      let dra = ra0 - ra1; if (dra > Math.PI) dra -= 2 * Math.PI; if (dra < -Math.PI) dra += 2 * Math.PI;
      view.ra = (view.ra + dra + 2 * Math.PI) % (2 * Math.PI);
      view.dec = Math.max(-89.9 * D, Math.min(89.9 * D, view.dec + (de0 - de1)));
    }
    setup();
  }

  // ------------------------------------------------------------ colour
  function kelvinRGB(T) { // blackbody approximation (Helland), good to a few per cent in hue
    const t = Math.max(1000, Math.min(40000, T)) / 100;
    let r = t <= 66 ? 255 : 329.698727446 * Math.pow(t - 60, -0.1332047592);
    let g = t <= 66 ? 99.4708025861 * Math.log(t) - 161.1195681661 : 288.1221695283 * Math.pow(t - 60, -0.0755148492);
    let b = t >= 66 ? 255 : t <= 19 ? 0 : 138.5177312231 * Math.log(t - 10) - 305.0447927307;
    return [r, g, b].map(v => Math.max(0, Math.min(255, v)));
  }
  const teffFromBV = bv => 4600 * (1 / (0.92 * bv + 1.7) + 1 / (0.92 * bv + 0.62));           // Ballesteros 2012
  const teffFromBpRp = c => 5040 / (0.4929 + 0.5092 * c - 0.0353 * c * c);                     // Mucciarelli & Bellazzini 2020, dwarfs
  function starRGB(T, mix = 0.45) { const c = kelvinRGB(T); return c.map(v => Math.round(v * (1 - mix) + 255 * mix)); }
  const rgb = (c, a = 1) => `rgba(${c[0]},${c[1]},${c[2]},${a})`;

  let glow; // pre-rendered soft sprite
  function makeGlow() {
    glow = document.createElement('canvas'); glow.width = glow.height = 64;
    const g = glow.getContext('2d'), gr = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(0.25, 'rgba(255,255,255,.45)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
    g.fillStyle = gr; g.fillRect(0, 0, 64, 64);
  }
  let mwSprite;
  function makeMW() {
    mwSprite = document.createElement('canvas'); mwSprite.width = mwSprite.height = 64;
    const g = mwSprite.getContext('2d'), gr = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr.addColorStop(0, 'rgba(214,220,240,1)'); gr.addColorStop(0.5, 'rgba(200,205,225,.45)'); gr.addColorStop(1, 'rgba(190,195,215,0)');
    g.fillStyle = gr; g.fillRect(0, 0, 64, 64);
  }

  // ------------------------------------------------------------ formatting
  function hms(raDeg, prec = 1) {
    let h = ((raDeg % 360) + 360) % 360 / 15, hh = Math.floor(h), m = (h - hh) * 60, mm = Math.floor(m), s = (m - mm) * 60;
    if (+s.toFixed(prec) >= 60) { s = 0; mm += 1; } if (mm >= 60) { mm = 0; hh = (hh + 1) % 24; }
    return `${String(hh).padStart(2, '0')}ʰ${String(mm).padStart(2, '0')}ᵐ${s.toFixed(prec).padStart(prec ? prec + 3 : 2, '0')}ˢ`;
  }
  function dms(decDeg, prec = 0) {
    const sg = decDeg < 0 ? '−' : '+'; let d = Math.abs(decDeg), dd = Math.floor(d), m = (d - dd) * 60, mm = Math.floor(m), s = (m - mm) * 60;
    if (+s.toFixed(prec) >= 60) { s = 0; mm += 1; } if (mm >= 60) { mm = 0; dd += 1; }
    return `${sg}${String(dd).padStart(2, '0')}°${String(mm).padStart(2, '0')}′${s.toFixed(prec).padStart(prec ? prec + 3 : 2, '0')}″`;
  }
  function angle(deg) {
    if (deg >= 1) return `${+deg.toFixed(deg >= 10 ? 0 : 1)}°`;
    if (deg * 60 >= 1) return `${+(deg * 60).toFixed(deg * 60 >= 10 ? 0 : 1)}′`;
    return `${+(deg * 3600).toFixed(deg * 3600 >= 10 ? 0 : 1)}″`;
  }

  // ------------------------------------------------------------ canvas sizing & loop
  function resize() {
    const r = cv.getBoundingClientRect(); DPR = Math.min(2, window.devicePixelRatio || 1);
    W = r.width; H = r.height; cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
    dirty = true;
  }
  function frame(t) {
    if (anim) stepAnim(t);
    if (dirty) { dirty = false; draw(); }
    for (const fn of rendDraws) fn(t);
    requestAnimationFrame(frame);
  }

  // ------------------------------------------------------------ drawing
  function polyline(pts, close = false) {
    let prev = null, started = false;
    ctx.beginPath();
    for (const p of pts) {
      const s = project(p);
      if (!s) { prev = null; continue; }
      if (!prev || Math.abs(s[0] - prev[0]) > W * 0.6 || Math.abs(s[1] - prev[1]) > H * 0.6) ctx.moveTo(s[0], s[1]);
      else ctx.lineTo(s[0], s[1]);
      prev = s; started = true;
    }
    if (close && started) ctx.closePath();
  }
  const fovDeg = () => view.fov / D;
  const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

  function draw() {
    setup();
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const f = fovDeg();
    if (on('mw')) drawMW(f);
    if (on('grid')) drawGrid(f);
    if (on('ref')) drawRef();
    drawImages(f);
    if (on('stars')) drawStars(f);
    if (on('gaia')) drawGaia(f);
    if (on('consts')) drawConsts(f);
    if (on('patches')) drawPatches(f);
    drawTargets(f);
    updateScale();
  }

  function drawMW(f) {
    const a0 = smooth(3, 14, f);
    if (a0 <= 0 || !SKY.mw.length) return;
    const cell = 1.83 * D * scale * 1.9;
    ctx.globalCompositeOperation = 'lighter';
    for (const c of SKY.mw) {
      const s = project(c.v); if (!s) continue;
      if (s[0] < -cell || s[0] > W + cell || s[1] < -cell || s[1] > H + cell) continue;
      ctx.globalAlpha = a0 * c.a;
      ctx.drawImage(mwSprite, s[0] - cell, s[1] - cell, cell * 2, cell * 2);
    }
    ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over';
  }

  function gridStep(f, list) { for (const s of list) if (f / s >= 3.2) return s; return list[list.length - 1]; }
  function drawGrid(f) {
    const decSteps = [30, 15, 10, 5, 2, 1, 30 / 60, 20 / 60, 10 / 60, 5 / 60, 2 / 60, 1 / 60, 30 / 3600, 10 / 3600];
    const raSteps = [30, 15, 7.5, 5, 2.5, 1.25, 0.5, 0.25, 0.125, 1 / 24, 1 / 48, 1 / 120, 1 / 240];
    const ds = gridStep(f, decSteps), rs = gridStep(f * Math.max(0.2, 1 / Math.max(0.05, Math.cos(view.dec))), raSteps);
    const wide = f > 40, span = f * 1.2;
    const dLo = wide ? -90 : Math.max(-90, view.dec / D - span), dHi = wide ? 90 : Math.min(90, view.dec / D + span);
    const raSpan = wide || Math.abs(view.dec / D) + span > 85 ? 180 : Math.min(180, span / Math.cos(view.dec));
    const r0 = view.ra / D - raSpan, r1 = view.ra / D + raSpan;
    ctx.lineWidth = 1; ctx.font = '11px ' + css('--mono');
    ctx.strokeStyle = 'rgba(150,170,210,.16)'; ctx.fillStyle = 'rgba(170,185,215,.55)';
    const labDec = Math.max(dLo, Math.min(dHi, view.dec / D - f * 0.3));
    for (let d = Math.ceil(dLo / ds) * ds; d <= dHi + 1e-9; d += ds) {
      if (Math.abs(d) > 89.999) continue;
      const pts = []; for (let i = 0; i <= 160; i++) { const r = r0 + (r1 - r0) * i / 160; pts.push(vec(r * D, d * D)); }
      ctx.strokeStyle = Math.abs(d) < 1e-9 ? 'rgba(150,170,210,.34)' : 'rgba(150,170,210,.16)';
      polyline(pts); ctx.stroke();
      const s = project(vec((view.ra / D + f * 0.42 / Math.max(0.1, Math.cos(d * D))) * D, d * D));
      if (s && s[0] > 4 && s[1] > 12 && s[1] < H - 4) ctx.fillText(dms(d, 0).replace(/(′)00″$/, '$1').replace(/°00′$/, '°'), s[0] + 3, s[1] - 3);
    }
    ctx.strokeStyle = 'rgba(150,170,210,.16)';
    const rStart = Math.ceil(r0 / rs) * rs;
    for (let r = rStart; r <= r1 + 1e-9; r += rs) {
      const pts = []; for (let i = 0; i <= 120; i++) { const d = dLo + (dHi - dLo) * i / 120; pts.push(vec(r * D, Math.max(-89.99, Math.min(89.99, d)) * D)); }
      polyline(pts); ctx.stroke();
      const s = project(vec(r * D, labDec * D));
      if (s && s[0] > 4 && s[0] < W - 60) ctx.fillText(hms(r, rs < 0.25 ? 0 : 0).replace(/00ˢ$/, '').replace(/ᵐ$/, 'ᵐ').replace(/ʰ00ᵐ$/, 'ʰ'), s[0] + 3, s[1] + 13);
    }
  }

  const GAL = { ra: 192.85948 * D, dec: 27.12825 * D, l: 122.93192 * D };
  function galToVec(l, b) {
    const sd = Math.sin(GAL.dec) * Math.sin(b) + Math.cos(GAL.dec) * Math.cos(b) * Math.cos(GAL.l - l), dec = Math.asin(sd);
    const y = Math.cos(b) * Math.sin(GAL.l - l), x = Math.cos(GAL.dec) * Math.sin(b) - Math.sin(GAL.dec) * Math.cos(b) * Math.cos(GAL.l - l);
    return vec(GAL.ra + Math.atan2(y, x), dec);
  }
  const EPS = 23.4392911 * D;
  const eclToVec = lam => vec(Math.atan2(Math.sin(lam) * Math.cos(EPS), Math.cos(lam)), Math.asin(Math.sin(EPS) * Math.sin(lam)));
  let GAL_LINE, ECL_LINE;
  function drawRef() {
    ctx.lineWidth = 1.2; ctx.setLineDash([6, 5]);
    ctx.strokeStyle = 'rgba(214,160,102,.45)'; polyline(GAL_LINE); ctx.stroke();
    ctx.strokeStyle = 'rgba(120,170,230,.40)'; polyline(ECL_LINE); ctx.stroke();
    ctx.setLineDash([]);
    if (fovDeg() > 25) {
      ctx.font = 'italic 12px ' + css('--serif');
      label(galToVec(0, 0), 'galactic centre', 'rgba(214,160,102,.8)');
      label(galToVec(Math.PI, 0), 'galactic anticentre', 'rgba(214,160,102,.8)');
      label(eclToVec(90 * D), 'ecliptic', 'rgba(120,170,230,.8)');
      label(eclToVec(270 * D), 'ecliptic', 'rgba(120,170,230,.8)');
    }
  }
  function label(p, text, col) { const s = project(p); if (!s) return; ctx.fillStyle = col; ctx.fillText(text, s[0] + 6, s[1] - 6); }

  function drawStars(f) {
    const boost = Math.max(0.55, Math.min(2.4, Math.pow(60 / f, 0.45)));
    const vLim = f > 110 ? 5.2 : f > 60 ? 6.0 : 7;
    const labelV = f < 12 ? 5 : f < 40 ? 3.2 : f < 100 ? 2.0 : 1.2;
    ctx.font = '11px ' + css('--sans');
    for (const s of SKY.stars) {
      if (s.V > vLim) continue;
      const p = project(s.v); if (!p || p[0] < -8 || p[0] > W + 8 || p[1] < -8 || p[1] > H + 8) continue;
      const r = (0.45 + Math.max(0, 6.8 - s.V) * 0.36) * boost;
      if (s.V < 2.2) { ctx.globalAlpha = 0.5; ctx.drawImage(glow, p[0] - r * 3, p[1] - r * 3, r * 6, r * 6); ctx.globalAlpha = 1; }
      ctx.fillStyle = s.col; ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, 7); ctx.fill();
      if (s.label && s.V < labelV) { ctx.fillStyle = 'rgba(200,205,215,.55)'; ctx.fillText(s.label, p[0] + r + 3, p[1] + 3); }
    }
  }

  function drawConsts(f) {
    if (f < 14 || f > 170) return;
    const a = smooth(14, 30, f) * (1 - smooth(120, 170, f));
    ctx.font = `600 11px ${css('--sans')}`; ctx.fillStyle = `rgba(170,185,215,${0.38 * a})`; ctx.textAlign = 'center';
    for (const c of SKY.consts) { const p = project(c.v); if (p) ctx.fillText(c.name.toUpperCase().split('').join(' '), p[0], p[1]); }
    ctx.textAlign = 'left';
  }

  function targetVisibleAt(t, fmax) { return fovDeg() < fmax && dot(t.v, C) > Math.cos(view.fov * 1.2); }

  function drawImages(f) {
    if (!on('image')) return;
    for (const t of SKY.targets) {
      t._img = null;
      if (!t.image || !targetVisibleAt(t, t.image.fov * 9)) continue;
      const a = 1 - smooth(t.image.fov * 3, t.image.fov * 9, f);
      if (a <= 0) continue;
      let im = images[t.id];
      if (!im) { im = images[t.id] = new Image(); im.onload = () => { dirty = true; }; im.src = t.image.file; }
      if (!im.complete || !im.naturalWidth) continue;
      const c = project(t.v), n = project(vec(t.ra * D, (t.dec + 0.01) * D));
      if (!c || !n) continue;
      const ppd = Math.hypot(n[0] - c[0], n[1] - c[1]) / 0.01, S = t.image.fov * ppd;
      const rot = Math.atan2(n[0] - c[0], -(n[1] - c[1]));
      ctx.save(); ctx.translate(c[0], c[1]); ctx.rotate(rot); ctx.globalAlpha = a;
      ctx.drawImage(im, -S / 2, -S / 2, S, S);
      t._img = { c, rot, S };
      ctx.strokeStyle = 'rgba(232,228,220,.25)'; ctx.lineWidth = 1; ctx.strokeRect(-S / 2, -S / 2, S, S);
      if (S > 160) { ctx.fillStyle = 'rgba(232,228,220,.7)'; ctx.font = '11px ' + css('--sans'); ctx.fillText(t.image.short, -S / 2 + 4, S / 2 - 6); }
      ctx.restore();
    }
  }

  function drawGaia(f) {
    for (const t of SKY.targets) {
      if (!t.field || !targetVisibleAt(t, Math.max(3, t.field.radius * 7))) continue;
      const fs = fields[t.id];
      if (!fs) { loadField(t); continue; }
      const a = 1 - smooth(t.field.radius * 3, t.field.radius * 7, f);
      const imgOn = on('image') && t.image && f < t.image.fov * 5;
      const gRef = Math.min(t.field.gmax + 1.5, 9 + Math.log2(Math.max(1, 30 / f)) * 1.6);
      for (let i = 0; i < fs.n; i++) {
        const p = project(fs.v[i]); if (!p || p[0] < -5 || p[0] > W + 5 || p[1] < -5 || p[1] > H + 5) continue;
        const g = fs.g[i];
        const r = Math.max(0.35, (gRef - g) * 0.32 + 0.5);
        if (imgOn) {
          if (g > gRef - 2.5) continue;
          ctx.strokeStyle = `rgba(106,209,200,${0.42 * a})`; ctx.lineWidth = 0.8;
          ctx.beginPath(); ctx.arc(p[0], p[1], Math.max(3.5, r + 3), 0, 7); ctx.stroke();
        } else {
          ctx.globalAlpha = a * Math.min(1, Math.max(0.2, (gRef + 1 - g) / 3));
          ctx.fillStyle = fs.col[i]; ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, 7); ctx.fill();
          ctx.globalAlpha = 1;
        }
      }
      // proper motion of the target star: Gaia J2016.0 position vs the J2000.0 Sesame position
      if (t.central && f < 0.25) {
        const s0 = project(t.v), s1 = project(vec(t.central.ra2016 * D, t.central.dec2016 * D));
        if (s0 && s1 && Math.hypot(s1[0] - s0[0], s1[1] - s0[1]) > 6) {
          ctx.strokeStyle = 'rgba(255,207,122,.9)'; ctx.fillStyle = 'rgba(255,207,122,.9)'; ctx.lineWidth = 1.2;
          arrow(s0, s1);
          ctx.font = '11px ' + css('--sans');
          ctx.fillText('J2000 → J2016 (proper motion)', s1[0] + 8, s1[1] + 4);
        }
      }
    }
  }
  function arrow(a, b) {
    const ang = Math.atan2(b[1] - a[1], b[0] - a[0]);
    ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(b[0], b[1]);
    ctx.lineTo(b[0] - 7 * Math.cos(ang - 0.4), b[1] - 7 * Math.sin(ang - 0.4));
    ctx.lineTo(b[0] - 7 * Math.cos(ang + 0.4), b[1] - 7 * Math.sin(ang + 0.4)); ctx.closePath(); ctx.fill();
  }

  function patchPath(p) {
    const pts = [];
    if (p.shape === 'circle') {
      const r = p.r * D;
      for (let i = 0; i <= 72; i++) { const a = i / 72 * 2 * Math.PI; pts.push(offset(p.ra * D, p.dec * D, Math.tan(r) * Math.sin(a), Math.tan(r) * Math.cos(a))); }
    } else {
      const w = Math.tan(p.w * D / 2), h = Math.tan(p.h * D / 2);
      const cs = [[-w, -h], [w, -h], [w, h], [-w, h], [-w, -h]];
      for (let k = 0; k < 4; k++) for (let i = 0; i < 8; i++) {
        const t = i / 8; pts.push(offset(p.ra * D, p.dec * D, cs[k][0] + (cs[k + 1][0] - cs[k][0]) * t, cs[k][1] + (cs[k + 1][1] - cs[k][1]) * t));
      }
      pts.push(pts[0]);
    }
    return pts;
  }
  function drawPatches(f) {
    ctx.font = '11px ' + css('--sans');
    const placed = [];
    const place = (x, y, w) => { // nudge labels of coincident footprints apart
      for (let k = 0; k < 12; k++) {
        const yy = y + k * 14;
        if (!placed.some(r => Math.abs(r.y - yy) < 13 && x < r.x + r.w && x + w > r.x)) { placed.push({ x, y: yy, w }); return yy; }
      }
      return y;
    };
    for (const t of SKY.targets) {
      if (dot(t.v, C) < Math.cos(view.fov * 1.2)) continue;
      for (const p of t.patches) {
        const size = (p.r ? p.r * 2 : p.w) * D * scale;
        if (size < 5) continue;
        const col = SVC_COL[p.svc] || '#ccc', failed = !p.states.drive_only;
        ctx.strokeStyle = col; ctx.lineWidth = selected === t ? 1.6 : 1.1;
        ctx.setLineDash(failed ? [4, 4] : []);
        ctx.globalAlpha = Math.min(1, size / 30);
        polyline(p.path, true);
        ctx.fillStyle = col; ctx.globalAlpha *= 0.06; ctx.fill(); ctx.globalAlpha = Math.min(1, size / 30); ctx.stroke();
        ctx.setLineDash([]);
        if (size > 90) {
          const top = project(offset(p.ra * D, p.dec * D, 0, Math.tan((p.r || p.h / 2) * D)));
          if (top) {
            const sv = SKY.services[p.svc] || p.svc, txt = `${sv} · ${p.what.replace(sv.replace(/^(NASA|ESA) /, '') + ' ', '')} · ${p.r ? 'r ' + angle(p.r) : angle(p.w) + ' □'}${failed ? ' · failed' : ''}`;
            const w = ctx.measureText(txt).width, x = top[0] - w / 2, y = place(x, top[1] - 5, w);
            ctx.fillStyle = col; ctx.shadowColor = 'rgba(0,0,0,.9)'; ctx.shadowBlur = 3; ctx.fillText(txt, x, y); ctx.shadowBlur = 0;
          }
        }
        ctx.globalAlpha = 1;
      }
    }
  }

  function drawTargets(f) {
    ctx.font = `600 12.5px ${css('--sans')}`;
    for (const t of SKY.targets) {
      const s = project(t.v); if (!s || s[0] < -20 || s[0] > W + 20 || s[1] < -20 || s[1] > H + 20) continue;
      t.screen = s;
      const col = STATUS_COL[t.status], hot = hover === t || selected === t;
      const R = hot ? 11 : 8.5;
      ctx.strokeStyle = col; ctx.lineWidth = hot ? 2 : 1.4;
      ctx.setLineDash(t.status === 'failed' ? [3, 3] : []);
      ctx.beginPath(); ctx.arc(s[0], s[1], R, 0, 7); ctx.stroke(); ctx.setLineDash([]);
      ctx.beginPath();
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { ctx.moveTo(s[0] + dx * (R + 3), s[1] + dy * (R + 3)); ctx.lineTo(s[0] + dx * (R + 8), s[1] + dy * (R + 8)); }
      ctx.stroke();
      if (t.status === 'analysed') { ctx.fillStyle = col; ctx.beginPath(); ctx.arc(s[0], s[1], 2.4, 0, 7); ctx.fill(); }
      ctx.fillStyle = hot ? '#fff' : 'rgba(232,228,220,.88)';
      ctx.shadowColor = 'rgba(0,0,0,.9)'; ctx.shadowBlur = 4;
      ctx.fillText(t.name, s[0] + R + 11, s[1] + 4);
      ctx.shadowBlur = 0;
    }
  }

  function updateScale() {
    const f = fovDeg(), target = (W * 0.18) / scale / D; // degrees in ~18% of width
    const nice = [90, 60, 30, 20, 10, 5, 2, 1, 30 / 60, 20 / 60, 10 / 60, 5 / 60, 2 / 60, 1 / 60, 30 / 3600, 10 / 3600, 5 / 3600, 1 / 3600];
    const v = nice.find(n => n <= target) || nice[nice.length - 1];
    $('#sb').style.width = `${v * D * scale}px`; $('#sb-l').textContent = angle(v);
    $('#ro-fov').textContent = `field ${angle(f)}`;
  }

  // ------------------------------------------------------------ data
  async function loadField(t) {
    if (fields[t.id] === 'loading') return;
    fields[t.id] = 'loading';
    try {
      const j = await (await fetch(t.field.file)).json();
      const n = j.ra.length, v = new Array(n), col = new Array(n);
      for (let i = 0; i < n; i++) {
        v[i] = vec(j.ra[i] * D, j.dec[i] * D);
        col[i] = rgb(starRGB(j.bp_rp[i] == null ? 5600 : teffFromBpRp(Math.max(-0.3, Math.min(4.5, j.bp_rp[i]))), 0.35));
      }
      fields[t.id] = { n, v, col, g: j.g, bp_rp: j.bp_rp, raw: j };
      dirty = true;
      if (selected === t) renderPanelExtras(t);
    } catch (e) { fields[t.id] = null; console.warn('field load failed', t.id, e); }
  }

  // ------------------------------------------------------------ animation
  function slerp(a, b, t) {
    const d = Math.acos(Math.max(-1, Math.min(1, dot(a, b))));
    if (d < 1e-9) return a.slice();
    const s = Math.sin(d), wa = Math.sin((1 - t) * d) / s, wb = Math.sin(t * d) / s;
    return [0, 1, 2].map(i => a[i] * wa + b[i] * wb);
  }
  function flyTo(ra, dec, fov, ms = 1800) {
    const to = { v: vec(ra, dec), fov: Math.max(MIN_FOV, Math.min(MAX_FOV, fov)) };
    if (reduceMotion) { [view.ra, view.dec] = radec(to.v); view.fov = to.fov; dirty = true; return Promise.resolve(); }
    const from = { v: vec(view.ra, view.dec), fov: view.fov };
    const sep = Math.acos(Math.max(-1, Math.min(1, dot(from.v, to.v))));
    const peak = Math.max(from.fov, to.fov, Math.min(MAX_FOV * 0.7, sep * 1.6));
    return new Promise(res => { anim = { from, to, peak, t0: performance.now(), ms: ms + Math.min(1400, sep / D * 8), res }; });
  }
  function stepAnim(now) {
    const a = anim, u = Math.min(1, (now - a.t0) / a.ms), e = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
    [view.ra, view.dec] = radec(slerp(a.from.v, a.to.v, e));
    const lf = Math.log(a.from.fov), lt = Math.log(a.to.fov), lp = Math.log(a.peak);
    const base = lf + (lt - lf) * e, bump = Math.max(0, lp - Math.max(lf, lt)) * Math.sin(Math.PI * e);
    view.fov = Math.exp(base + bump);
    dirty = true;
    if (u >= 1) { anim = null; a.res(); }
  }

  // ------------------------------------------------------------ interaction
  let drag = null; const pointers = new Map();
  cv.addEventListener('pointerdown', e => {
    if (!SKY || !C) return;
    cv.setPointerCapture(e.pointerId); pointers.set(e.pointerId, [e.offsetX, e.offsetY]);
    stopTour(); anim = null;
    if (pointers.size === 1) drag = { p0: unproject(e.offsetX, e.offsetY), x: e.offsetX, y: e.offsetY, moved: false };
    else if (pointers.size === 2) { const [a, b] = [...pointers.values()]; drag = { pinch: Math.hypot(a[0] - b[0], a[1] - b[1]), fov: view.fov }; }
  });
  cv.addEventListener('pointermove', e => {
    if (!SKY || !C) return;
    const hadPointer = pointers.has(e.pointerId);
    if (hadPointer) pointers.set(e.pointerId, [e.offsetX, e.offsetY]);
    if (drag && drag.pinch && pointers.size === 2) {
      const [a, b] = [...pointers.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]);
      const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, p0 = unproject(mx, my);
      view.fov = Math.max(MIN_FOV, Math.min(MAX_FOV, drag.fov * drag.pinch / d)); keepUnder(p0, mx, my); dirty = true; return;
    }
    if (drag && hadPointer && !drag.pinch) {
      if (Math.hypot(e.offsetX - drag.x, e.offsetY - drag.y) > 3) { drag.moved = true; cv.classList.add('dragging'); }
      if (drag.moved) { keepUnder(drag.p0, e.offsetX, e.offsetY); dirty = true; }
      return;
    }
    hoverAt(e.offsetX, e.offsetY);
  });
  const end = e => {
    pointers.delete(e.pointerId); cv.classList.remove('dragging');
    if (drag && !drag.pinch && !drag.moved && e.type === 'pointerup') {
      const t = hitTarget(e.offsetX, e.offsetY);
      if (t) select(t);
      else { const ti = hitImage(e.offsetX, e.offsetY); if (ti) openCompare(ti, 'side'); }
    }
    if (pointers.size === 0) drag = null;
  };
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);
  cv.addEventListener('pointerleave', () => { $('#ro-pos').textContent = '—'; $('#tip').hidden = true; });
  cv.addEventListener('wheel', e => {
    if (!SKY || !C) return;
    e.preventDefault(); stopTour(); anim = null;
    const p0 = unproject(e.offsetX, e.offsetY);
    view.fov = Math.max(MIN_FOV, Math.min(MAX_FOV, view.fov * Math.exp(e.deltaY * (e.deltaMode ? 0.05 : 0.0015))));
    keepUnder(p0, e.offsetX, e.offsetY); dirty = true;
  }, { passive: false });
  cv.addEventListener('keydown', e => {
    if (!SKY || !C) return;
    const step = view.fov * 0.12;
    const k = { ArrowLeft: () => { view.ra += step / Math.max(0.1, Math.cos(view.dec)); }, ArrowRight: () => { view.ra -= step / Math.max(0.1, Math.cos(view.dec)); },
      ArrowUp: () => { view.dec = Math.min(89.9 * D, view.dec + step); }, ArrowDown: () => { view.dec = Math.max(-89.9 * D, view.dec - step); },
      '+': () => { view.fov = Math.max(MIN_FOV, view.fov / 1.4); }, '=': () => { view.fov = Math.max(MIN_FOV, view.fov / 1.4); },
      '-': () => { view.fov = Math.min(MAX_FOV, view.fov * 1.4); },
      Enter: () => { const t = nearestTarget(); if (t) select(t); } }[e.key];
    if (k) { e.preventDefault(); stopTour(); k(); view.ra = (view.ra + 2 * Math.PI) % (2 * Math.PI); dirty = true; }
  });
  function hitTarget(x, y) {
    let best = null, bd = 16;
    for (const t of SKY.targets) if (t.screen && project(t.v)) { const d = Math.hypot(t.screen[0] - x, t.screen[1] - y); if (d < bd) { bd = d; best = t; } }
    return best;
  }
  function hitImage(x, y) {
    if (!on('image')) return null;
    for (const t of SKY.targets) {
      const m = t._img; if (!m || !t.image || fovDeg() > t.image.fov * 4) continue;
      const dx = x - m.c[0], dy = y - m.c[1], u = dx * Math.cos(-m.rot) - dy * Math.sin(-m.rot), v = dx * Math.sin(-m.rot) + dy * Math.cos(-m.rot);
      if (Math.abs(u) < m.S / 2 && Math.abs(v) < m.S / 2) return t;
    }
    return null;
  }
  function nearestTarget() { let b = null, bd = -2; for (const t of SKY.targets) { const d = dot(t.v, C); if (d > bd) { bd = d; b = t; } } return b; }
  function hoverAt(x, y) {
    const [ra, de] = radec(unproject(x, y));
    $('#ro-pos').textContent = `α ${hms(ra / D, fovDeg() < 1 ? 1 : 0)}  δ ${dms(de / D, fovDeg() < 1 ? 1 : 0)}  ICRS`;
    const t = hitTarget(x, y);
    if (t !== hover) { hover = t; dirty = true; }
    cv.classList.toggle('pointing', !!t);
    cv.classList.toggle('zoomable', !t && !!hitImage(x, y));
    const tip = $('#tip');
    if (t) {
      const dt = document.createElement('i'); dt.className = `dot ${t.status}`;
      const b = document.createElement('b'); b.append(dt, t.name);
      const sp = document.createElement('span'); sp.textContent = t.statusShort;
      tip.replaceChildren(b, sp); tip.hidden = false; tip.style.left = `${x + 16}px`; tip.style.top = `${y + 14}px`;
    } else if (!t && hitImage(x, y)) {
      const b = document.createElement('b'); b.textContent = 'Compare with generated rendition';
      const sp = document.createElement('span'); sp.textContent = 'click the survey image';
      tip.replaceChildren(b, sp); tip.hidden = false; tip.style.left = `${x + 16}px`; tip.style.top = `${y + 14}px`; return;
    }
    else tip.hidden = true;
  }
  document.querySelectorAll('[data-zoom]').forEach(b => b.addEventListener('click', () => {
    stopTour(); const z = b.dataset.zoom;
    if (z === 'home') flyTo(HOME.ra, HOME.dec, HOME.fov, 1200);
    else flyTo(view.ra, view.dec, view.fov * (z === 'in' ? 1 / 2 : 2), 450);
  }));

  // ------------------------------------------------------------ UI: layers, rail, search, mode
  function buildUI() {
    const lf = $('#layers'), lg = document.createElement('div'); lg.className = 'lg';
    let group = null;
    for (const [k, [v, lab, grp, swc, swv]] of Object.entries(layers)) {
      if (grp !== group) { group = grp; const g4 = document.createElement('h4'); g4.textContent = grp; lg.append(g4); }
      const l = document.createElement('label'), i = document.createElement('input'), sw = document.createElement('span');
      i.type = 'checkbox'; i.checked = v; i.setAttribute('role', 'switch');
      i.addEventListener('change', () => { layers[k][0] = i.checked; dirty = true; });
      sw.className = `sw ${swc}`; if (swc === 'soft') sw.style.background = swv; else if (swc !== 'multi') sw.style.borderTopColor = swv;
      l.append(i, document.createTextNode(lab), sw);
      lg.append(l);
    }
    lf.append(lg);
    const lgd = lf.querySelector('legend');
    lgd.tabIndex = 0; lgd.setAttribute('role', 'button'); lgd.setAttribute('aria-expanded', 'false');
    const toggleLayers = () => { const o = lf.classList.toggle('open'); lgd.setAttribute('aria-expanded', String(o)); };
    lgd.addEventListener('click', toggleLayers);
    lgd.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleLayers(); } });
    const groups = [['analysed', 'Analysed'], ['planned', 'Analysis planned'], ['retrieved', 'Products retrieved'], ['failed', 'Probe only']];
    const list = $('#rail-list'), dl = $('#target-names');
    for (const [st, title] of groups) {
      const ts = SKY.targets.filter(t => t.status === st); if (!ts.length) continue;
      const h = document.createElement('h2'); h.textContent = title; list.append(h);
      for (const t of ts.sort((a, b) => a.ra - b.ra)) {
        const b = document.createElement('button'); b.type = 'button'; b.className = 't'; b.dataset.id = t.id;
        const d = document.createElement('span'); d.className = `dot ${t.status}`;
        const n = document.createElement('span'); n.className = 'n'; n.textContent = t.patches.length ? `${t.patches.length} ▢` : '';
        n.title = `${t.patches.length} query footprints`;
        b.append(d, document.createTextNode(t.name), n);
        b.addEventListener('click', () => { stopTour(); select(t); });
        list.append(b);
      }
    }
    if (SKY.campaigns.length) {
      const hh = document.createElement('h2'); hh.textContent = 'Campaigns, no position yet'; list.append(hh);
      for (const r of SKY.campaigns) {
        const b = document.createElement('button'); b.type = 'button'; b.className = 't';
        const d = document.createElement('span'); d.className = 'dot draft';
        const n = document.createElement('span'); n.className = 'n'; n.textContent = r.status;
        b.append(d, document.createTextNode(r.title.replace(/ \(draft\)$/, '')), n);
        b.addEventListener('click', () => { stopTour(); openCampaign(r); });
        list.append(b);
      }
    }
    for (const t of SKY.targets) { const o = document.createElement('option'); o.value = t.name; dl.append(o); }
    $('#find').addEventListener('change', e => {
      const q = e.target.value.trim().toLowerCase(), t = SKY.targets.find(x => x.name.toLowerCase() === q) || SKY.targets.find(x => x.name.toLowerCase().includes(q));
      if (t) { select(t); e.target.value = ''; }
    });
    $('#rail-toggle').addEventListener('click', e => { const b = e.currentTarget; b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'); });
    $('#mode').addEventListener('click', e => {
      const onN = document.body.classList.toggle('night'); e.currentTarget.setAttribute('aria-pressed', String(onN));
      try { localStorage.setItem('cyg-night', onN ? '1' : '0'); } catch (_) {}
    });
    try { if (localStorage.getItem('cyg-night') === '1') { document.body.classList.add('night'); $('#mode').setAttribute('aria-pressed', 'true'); } } catch (_) {}
    $('#intro-close').addEventListener('click', () => { $('#intro').hidden = true; cv.focus(); });
    $('#tour').addEventListener('click', startTour);
    $('#p-close').addEventListener('click', closePanel);
    document.querySelectorAll('[data-open="sources"]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); openSources(); }));
    const nT = SKY.targets.length, nP = SKY.targets.reduce((s, t) => s + t.patches.length, 0);
    const uniq = new Map([...SKY.targets.flatMap(t => t.records || []), ...SKY.campaigns].map(r => [r.id, r]));
    const nA = SKY.targets.filter(t => t.status === 'analysed').length, nC = [...uniq.values()].filter(r => r.outcome === 'candidate').length;
    $('#counts').textContent = `${nT} positions · ${nP} query footprints · ${SKY.manifest_rows} archive requests · ${uniq.size} analysis records · ${nA} target${nA === 1 ? '' : 's'} analysed · ${nC} candidate${nC === 1 ? '' : 's'}`;
  }

  // ------------------------------------------------------------ tour
  async function startTour() {
    $('#intro').hidden = true;
    const order = [...SKY.targets].sort((a, b) => (a.status === 'analysed' ? -1 : 0) - (b.status === 'analysed' ? -1 : 0) || a.ra - b.ra);
    const my = tour = { i: 0 };
    for (const t of order) {
      if (tour !== my) return;
      await select(t, true);
      await new Promise(r => setTimeout(r, reduceMotion ? 2500 : 5200));
    }
    tour = null;
  }
  function stopTour() { tour = null; }

  // ------------------------------------------------------------ panel
  const h = (tag, attrs = {}, ...kids) => {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) { if (v == null) continue; if (k === 'class') el.className = v; else if (k === 'text') el.textContent = v; else el.setAttribute(k, v); }
    for (const k of kids.flat()) if (k != null) el.append(k.nodeType ? k : document.createTextNode(String(k)));
    return el;
  };
  function closePanel() {
    $('#panel').hidden = true; document.body.classList.remove('panel-open'); selected = null; dirty = true; clearRend();
    document.querySelectorAll('.rail button.t').forEach(b => b.removeAttribute('aria-current'));
    history.replaceState(null, '', location.pathname);
    cv.focus();
  }
  function fitFov(t) { return t.field ? Math.max(0.12, t.field.radius * 2.6) : 0.4; }

  async function select(t, fromTour = false) {
    selected = t; dirty = true;
    $('#intro').hidden = true;
    document.querySelectorAll('.rail button.t').forEach(b => b.toggleAttribute('aria-current', b.dataset.id === t.id));
    document.querySelectorAll('.rail button.t[aria-current]').forEach(b => b.setAttribute('aria-current', 'true'));
    history.replaceState(null, '', '#' + t.id);
    renderPanel(t);
    if (t.field && !fields[t.id]) loadField(t);
    if (t.image && !images[t.id]) { const im = images[t.id] = new Image(); im.onload = () => { dirty = true; }; im.src = t.image.file; }
    await flyTo(t.ra * D, t.dec * D, fitFov(t) * D, fromTour ? 2600 : 1800);
  }

  const KIND = { field: 'Benchmark field', tess: 'Star on the TESS target list', bench: 'Benchmark object', other: 'Engineering sample (JWST / HST)', analysis: 'Target of a recorded analysis' };
  const folds = t => (t.records || []).flatMap(r => (r.plots || []).filter(p => p.type === 'fold').map(p => ({ ...p, rec: r })));
  function renderPanel(t) {
    const P = $('#p-body'); P.replaceChildren();
    $('#panel').hidden = false; document.body.classList.add('panel-open');
    P.append(
      h('h2', { id: 'p-title' }, t.name),
      h('p', { class: 'kind' }, KIND[t.cat] + (t.system ? ` · ${t.system.planets.length} known planet${t.system.planets.length > 1 ? 's' : ''} in the NASA Exoplanet Archive` : '')),
      h('p', { class: 'coord' }, `α ${hms(t.ra, 2)}   δ ${dms(t.dec, 1)}`,
        h('small', {}, t.resolved ? `ICRS, J2000.0 · ${t.resolver} · resolved ${t.resolved.replace('T', ' ').replace('Z', ' UTC')}` : `${t.frame} · position from ${t.resolver}`)),
      h('p', { class: `status ${t.status}` }, t.statusText),
      h('div', { class: 'zooms' },
        zoomBtn('Whole sky', () => flyTo(t.ra * D, t.dec * D, 140 * D)),
        zoomBtn('Constellation', () => flyTo(t.ra * D, t.dec * D, 25 * D)),
        zoomBtn('Field', () => flyTo(t.ra * D, t.dec * D, fitFov(t) * D)),
        t.central ? zoomBtn('Star (2′)', () => flyTo(t.ra * D, t.dec * D, 2 / 60 * D)) : null),
    );
    const rend = h('section', { id: 'rend' }); P.append(rend);
    if (t.records) P.append(recordsSection(t));
    if (t.image) P.append(imageSection(t));
    P.append(patchSection(t));
    if (t.system) P.append(planetTable(t));
    P.append(sourceSection(t));
    renderPanelExtras(t);
    $('#panel').scrollTop = 0;
  }
  function zoomBtn(label, fn) { const b = h('button', { type: 'button', class: 'btn ghost' }, label); b.addEventListener('click', () => { stopTour(); fn(); }); return b; }

  function renderPanelExtras(t) {
    const rend = $('#rend'); if (!rend || selected !== t) return;
    clearRend(); rend.replaceChildren();
    if (t.system) rend.append(...systemRendition(t));
    else if (t.cat === 'field' || /^(NGC|M)\s?\d/.test(t.name)) rend.append(clusterRendition(t));
    else if (t.central) rend.append(starRendition(t));
    else rend.append(h('h3', {}, 'Rendition'), h('p', { class: 'note' }, 'No rendition: this position is an engineering sample for archive access, not a studied object. The survey image below shows the field.'));
  }

  // --- renditions -------------------------------------------------------
  function limbDisc(g, x, y, R, T, glowAmt = 1) {
    const c = starRGB(T, 0.18);
    if (glowAmt) { const gr = g.createRadialGradient(x, y, R * 0.9, x, y, R * 2.6); gr.addColorStop(0, rgb(c, 0.28 * glowAmt)); gr.addColorStop(1, rgb(c, 0)); g.fillStyle = gr; g.beginPath(); g.arc(x, y, R * 2.6, 0, 7); g.fill(); }
    // quadratic limb darkening, generic u1 = 0.40, u2 = 0.25
    const gr = g.createRadialGradient(x, y, 0, x, y, R);
    for (let i = 0; i <= 10; i++) {
      const r = i / 10, mu = Math.sqrt(Math.max(0, 1 - r * r)), I = 1 - 0.40 * (1 - mu) - 0.25 * (1 - mu) ** 2;
      gr.addColorStop(r, rgb(c.map((v, j) => Math.round(v * I * (j === 2 ? 0.92 + 0.08 * I : 1))), 1));
    }
    g.fillStyle = gr; g.beginPath(); g.arc(x, y, R, 0, 7); g.fill();
  }
  function planetColour(teq) {
    if (teq == null) return [160, 160, 170];
    if (teq > 1800) return [70, 38, 30];
    if (teq > 1000) return [150, 110, 80];
    if (teq > 500) return [190, 170, 140];
    if (teq > 250) return [150, 175, 200];
    return [200, 215, 230];
  }
  function mkCanvas(w, hgt) {
    const c = h('canvas', { class: 'rend', width: w * 2, height: hgt * 2, role: 'img' });
    c.style.aspectRatio = `${w} / ${hgt}`;
    const g = c.getContext('2d'); g.scale(2, 2); return [c, g];
  }
  let rendDraws = []; // rendition animators, driven by the main frame loop
  function clearRend() { rendDraws = []; }

  function systemRendition(t) {
    clearRend();
    const st = t.system.star, Ms = st.st_mass || 1, Rs = st.st_rad || 1, Ts = st.st_teff || 5700;
    const pls = t.system.planets.map(p => {
      const aDerived = p.a == null && p.P != null;
      return { ...p, aU: p.a != null ? p.a : Math.cbrt(Ms * (p.P / 365.25) ** 2), aDerived };
    }).filter(p => p.aU);
    const amax = Math.max(...pls.map(p => p.aU)), amin = Math.min(...pls.map(p => p.aU));
    const gamma = amax / amin > 14 ? 0.5 : 1;
    const W2 = 400, H2 = 300, cx = W2 / 2, cy = H2 / 2 - 8, Rmax = 128;
    const rOf = a => Rmax * Math.pow(a / amax, gamma);
    const starR = Math.max(2.5, rOf(Rs * 0.00465047));
    const rMaxE = Math.max(...pls.map(p => p.rade || 1));
    const pScale = 7 / rMaxE;
    const [c1, g1] = mkCanvas(W2, H2);
    c1.setAttribute('aria-label', `Top-down rendition of the ${t.system.host} system: ${pls.map(p => p.name).join(', ')}`);
    const Pmin = Math.min(...pls.map(p => p.P || 1e9));
    const daysPerSec = Pmin / 5;
    // starting phases: WASP-12 b from the archive ephemeris used in the project's analysis; others not measured
    const jdNow = Date.now() / 86400000 + 2440587.5;
    const eph = p => folds(t).find(f => p.P && Math.abs(f.period_days - p.P) / p.P < 1e-3);
    const phase0 = p => { const f = eph(p); return f ? ((((jdNow - f.t0_bjd) / f.period_days) % 1) + 1) % 1 : null; };
    const start = performance.now();
    const drawSys = now => {
      const days = reduceMotion ? 0 : (now - start) / 1000 * daysPerSec;
      g1.clearRect(0, 0, W2, H2); g1.fillStyle = '#02030a'; g1.fillRect(0, 0, W2, H2);
      g1.strokeStyle = 'rgba(232,228,220,.18)'; g1.setLineDash([2, 4]);
      g1.beginPath(); g1.moveTo(cx, cy + 20); g1.lineTo(cx, H2 - 16); g1.stroke(); g1.setLineDash([]);
      g1.fillStyle = 'rgba(232,228,220,.5)'; g1.font = '10.5px ' + css('--sans'); g1.textAlign = 'center';
      g1.fillText('↓ to Earth', cx, H2 - 5);
      limbDisc(g1, cx, cy, starR, Ts, 1);
      pls.forEach((p, i) => {
        const r = rOf(p.aU);
        g1.strokeStyle = 'rgba(232,228,220,.22)'; g1.lineWidth = 1; g1.beginPath(); g1.arc(cx, cy, r, 0, 7); g1.stroke();
        const ph0 = phase0(p), base = ph0 != null ? ph0 : i * 0.137;
        const ang = Math.PI / 2 + 2 * Math.PI * (base + (p.P ? days / p.P : 0));
        const x = cx + r * Math.cos(ang), y = cy + r * Math.sin(ang), pr = Math.max(1.8, (p.rade || 1) * pScale);
        const pc = planetColour(p.teq);
        g1.fillStyle = rgb(pc); g1.beginPath(); g1.arc(x, y, pr, 0, 7); g1.fill();
        // lit side toward the star
        g1.fillStyle = rgb(starRGB(Ts, 0.3), 0.35); g1.beginPath(); g1.arc(x, y, pr, ang + Math.PI / 2, ang + 3 * Math.PI / 2); g1.fill();
        g1.fillStyle = 'rgba(232,228,220,.78)'; g1.textAlign = 'left'; g1.font = '10.5px ' + css('--sans');
        g1.fillText(p.name.replace(t.system.host, '').trim() || p.name, x + pr + 3, y - pr - 1);
      });
      g1.textAlign = 'left'; g1.fillStyle = 'rgba(232,228,220,.55)';
      g1.fillText(reduceMotion ? 'still frame' : `simulated time +${days.toFixed(1)} d`, 8, 14);
    };
    if (reduceMotion) drawSys(performance.now()); else rendDraws.push(drawSys);
    const notes = [];
    notes.push(`Orbits to scale in AU${gamma !== 1 ? ' on a square-root radial scale (the system spans ' + Math.round(amax / amin) + '× in distance)' : ''}; the star disc is to the same scale. Planet discs are enlarged for visibility (largest shown ${rMaxE.toFixed(1)} R⊕ as 7 px).`);
    const wasp = pls.find(p => phase0(p) != null);
    notes.push(wasp ? `${wasp.name}'s position is its predicted phase now, from the ephemeris declared in the project's analysis “${eph(wasp).rec.title}” (P = ${eph(wasp).period_days} d). Other orbital phases and inclinations are not drawn from data.`
      : 'Orbital phases are not measured here and are spread for legibility; eccentricities and inclinations are not drawn.');
    if (pls.some(p => p.aDerived)) notes.push('Semi-major axes marked “derived” in the table come from the period and stellar mass (Kepler’s third law).');
    notes.push('Colours: star from its effective temperature (blackbody approximation); planets keyed to equilibrium temperature, illustrative.');
    const out = [h('h3', {}, 'Rendition · generated from catalogue values'), h('figure', {}, c1, h('figcaption', {}, notes.join(' ')))];
    const tr = pls.filter(p => p.transits && p.rade);
    if (tr.length) out.push(transitRendition(t, tr, Rs, Ts));
    return out;
  }

  function transitRendition(t, tr, Rs, Ts) {
    const W2 = 400, H2 = 210, R = 84, cx = W2 / 2, cy = H2 / 2 - 4;
    const [c, g] = mkCanvas(W2, H2);
    c.setAttribute('aria-label', 'Transit geometry rendition, star and planet discs to scale');
    const pick = tr.find(p => folds(t).some(f => Math.abs(f.period_days - p.P) / p.P < 1e-3)) || tr[0];
    const meas = folds(t).filter(f => f.depth && Math.abs(f.period_days - pick.P) / pick.P < 1e-3);
    const k = pick.rade * 0.0091577 / Rs;
    const start = performance.now();
    const drawT = now => {
      g.clearRect(0, 0, W2, H2); g.fillStyle = '#02030a'; g.fillRect(0, 0, W2, H2);
      limbDisc(g, cx, cy, R, Ts, 0.6);
      const u = reduceMotion ? 0.5 : ((now - start) / 7000) % 1;
      const x = cx + (u * 2 - 1) * (R + k * R + 30);
      g.fillStyle = '#000'; g.beginPath(); g.arc(x, cy, Math.max(1.2, k * R), 0, 7); g.fill();
      g.fillStyle = 'rgba(232,228,220,.6)'; g.font = '10.5px ' + css('--sans');
      g.fillText(`${pick.name}: Rp/R★ = ${k.toFixed(3)}  →  (Rp/R★)² = ${(k * k * 100).toFixed(2)} %`, 8, 14);
      if (meas.length) g.fillText(`in the project's own data: depth ${meas.map(f => (f.depth.value * 100).toFixed(2) + ' %').join(' · ')}`, 8, H2 - 8);
    };
    if (reduceMotion) drawT(performance.now()); else rendDraws.push(drawT);
    const cap = [`Star and planet discs to scale from the archive radii (R★ = ${(+Rs).toFixed(2)} R☉, Rp = ${pick.rade.toFixed(2)} R⊕), crossing at impact parameter 0 (not fetched). Generic quadratic limb darkening.`];
    if (meas.length) cap.push(`Project depths (${meas.map(f => `${f.label}: ${f.depth.n_in} in-transit cadences`).join('; ')}) are ${meas[0].depth.method}. A depth is not (Rp/R★)² exactly, because of limb darkening and impact parameter.`);
    return h('figure', {}, c, h('figcaption', {}, cap.join(' ')));
  }

  function starRendition(t) {
    const s = t.central, T = s.teff || (s.bp_rp != null ? teffFromBpRp(s.bp_rp) : 5700);
    const [c, g] = mkCanvas(400, 190);
    c.setAttribute('aria-label', `Colour rendition of ${t.name} from Gaia photometry`);
    g.fillStyle = '#02030a'; g.fillRect(0, 0, 400, 190);
    limbDisc(g, 110, 95, 58, T, 1);
    g.fillStyle = 'rgba(232,228,220,.8)'; g.font = '12px ' + css('--sans');
    const lines = [`Gaia G = ${s.g.toFixed(2)}`, s.bp_rp != null ? `BP − RP = ${s.bp_rp.toFixed(2)}` : 'BP − RP not available',
      s.teff ? `T_eff (GSP-Phot) = ${s.teff} K` : `T_eff ≈ ${Math.round(T / 10) * 10} K from BP − RP`,
      s.plx ? `parallax ${s.plx.toFixed(2)} mas (≈ ${Math.round(1000 / s.plx)} pc)` : ''];
    lines.forEach((l, i) => g.fillText(l, 210, 62 + i * 20));
    return h('div', {}, h('h3', {}, 'Rendition · generated from Gaia DR3 photometry'), h('figure', {}, c,
      h('figcaption', {}, `Disc colour from the ${s.teff ? 'Gaia GSP-Phot temperature' : 'BP − RP colour (Mucciarelli & Bellazzini 2020 dwarf relation)'} as a blackbody approximation; the size is not to scale. Distance is 1/parallax with no zero-point correction. ${t.system_note || 'No planet parameters are held for this star.'}`)));
  }

  function clusterRendition(t) {
    const wrap = h('div', {}, h('h3', {}, 'Rendition · Gaia DR3 colour–magnitude diagram'));
    const fs = fields[t.id];
    if (!fs || fs === 'loading') { wrap.append(h('p', { class: 'note' }, 'Loading Gaia sources…')); return wrap; }
    const W2 = 400, H2 = 320, ml = 40, mb = 30, mt = 10, mr = 10;
    const [c, g] = mkCanvas(W2, H2);
    const xs = fs.bp_rp, ys = fs.g, gmax = t.field.gmax;
    const x0 = -0.4, x1 = 3.2, y0 = Math.min(...ys) - 0.5, y1 = gmax + 0.3;
    const X = v => ml + (v - x0) / (x1 - x0) * (W2 - ml - mr), Y = v => mt + (v - y0) / (y1 - y0) * (H2 - mt - mb);
    g.fillStyle = '#02030a'; g.fillRect(0, 0, W2, H2);
    g.strokeStyle = 'rgba(232,228,220,.2)'; g.strokeRect(ml, mt, W2 - ml - mr, H2 - mt - mb);
    g.fillStyle = 'rgba(232,228,220,.55)'; g.font = '10.5px ' + css('--sans'); g.textAlign = 'center';
    for (let v = 0; v <= 3; v++) g.fillText(v, X(v), H2 - mb + 13);
    g.fillText('BP − RP (mag)', ml + (W2 - ml - mr) / 2, H2 - 4); g.textAlign = 'right';
    for (let v = Math.ceil(y0); v <= y1; v += 2) g.fillText(v, ml - 5, Y(v) + 4);
    g.save(); g.translate(11, mt + (H2 - mt - mb) / 2); g.rotate(-Math.PI / 2); g.textAlign = 'center'; g.fillText('G (mag)', 0, 0); g.restore();
    let n = 0;
    for (let i = 0; i < fs.n; i++) {
      if (xs[i] == null) continue; n++;
      g.fillStyle = fs.col[i]; g.globalAlpha = 0.8; g.beginPath(); g.arc(X(xs[i]), Y(ys[i]), 1.4, 0, 7); g.fill();
    }
    g.globalAlpha = 1;
    c.setAttribute('aria-label', `Colour–magnitude diagram of ${n} Gaia DR3 sources within ${t.field.radius}° of ${t.name}`);
    wrap.append(h('figure', {}, c, h('figcaption', {}, `${n} Gaia DR3 sources with G < ${gmax} within ${t.field.radius}° of the ${t.name} position (brightest 6000 at most), each dot in its own colour. Field stars are not removed, so the cluster sequence sits on a background population. Zoom into the field on the map to see the same sources on the sky.`)));
    return wrap;
  }

  // --- sections -----------------------------------------------------------
  const OUTCOME = { not_run: 'Not run', pipeline_check: 'Pipeline check', bounded_null: 'Bounded null', lead: 'Lead', candidate: 'Candidate' };
  const STATE = { passed: 'passed', failed: 'failed', inconclusive: 'inconclusive', not_tested: 'not tested' };
  function recordCard(r) {
    const card = h('article', { class: 'record' },
      h('header', {},
        h('span', { class: `chip st-${r.status}` }, r.status),
        h('span', { class: `chip oc-${r.outcome}` }, OUTCOME[r.outcome] || r.outcome),
        r.evidence ? h('span', { class: 'chip ev' }, r.evidence) : null,
        h('span', { class: 'rdate' }, r.date || 'not run')),
      h('h4', {}, r.title),
      h('p', { class: 'rkind' }, r.kind),
      h('p', {}, r.summary));
    for (const pl of r.plots || []) {
      const f = h('figure', { class: 'rplot' }); f.innerHTML = pl.svg; // built from the record's own CSV by cygnus.skyrecord
      const bits = [pl.label + '.', `${pl.n.toLocaleString()} good cadences from ${pl.file}.`];
      if (pl.type === 'fold') bits.push(`Grey: cadences; white: 6-min medians.${pl.veto_phase ? ` Shaded: ±${pl.veto_phase} phase veto window.` : ''}`);
      if (pl.depth) bits.push(`Depth ${(pl.depth.value * 100).toFixed(2)} % (${pl.depth.method}).`);
      f.append(h('figcaption', {}, bits.join(' ')));
      card.append(f);
    }
    if (r.checks && r.checks.length) {
      const tb = h('tbody');
      for (const c of r.checks) tb.append(h('tr', {}, h('td', {}, c.name, c.note ? h('span', { class: 'cnote' }, c.note) : null),
        h('td', {}, h('span', { class: `state s-${c.state}` }, STATE[c.state]), c.reported_as ? h('span', { class: 'cnote' }, `report: “${c.reported_as}”`) : null)));
      const n = st => r.checks.filter(c => c.state === st).length;
      card.append(h('details', { class: 'checks' },
        h('summary', {}, 'Checks ', ...['passed', 'failed', 'inconclusive', 'not_tested'].map(st => h('span', { class: `state s-${st}` }, `${n(st)} ${STATE[st]}`))),
        h('table', {}, h('thead', {}, h('tr', {}, h('th', {}, 'Check'), h('th', {}, 'State'))), tb)));
    }
    const paths = [['Spec', r.spec], ['Report', r.report], ['Search log', r.search_log], ['Record', r._path]].filter(x => x[1]);
    if (paths.length || (r.products || []).length) {
      card.append(h('dl', { class: 'kv' }, ...paths.flatMap(([k, v]) => [h('dt', {}, k), h('dd', {}, v)]),
        ...(r.products || []).flatMap((pr, i) => [h('dt', {}, i ? '' : 'Products'), h('dd', {}, `${pr.archive} · ${pr.id}`)])));
    }
    return card;
  }
  function recordsSection(t) {
    const rs = t.records || [];
    return h('section', {}, h('h3', {}, `Analyses · ${rs.length} record${rs.length === 1 ? '' : 's'}`), ...rs.map(recordCard),
      h('p', { class: 'note' }, 'Collected automatically from the sky_record.json beside each report. States are copied from the reports, including checks that were not tested.'));
  }
  function openCampaign(r) {
    selected = null; dirty = true; clearRend();
    const P = $('#p-body'); P.replaceChildren();
    $('#panel').hidden = false; document.body.classList.add('panel-open');
    P.append(h('p', { class: 'kicker' }, 'Campaign · no sky position yet'), h('h2', { id: 'p-title' }, r.title), recordCard(r),
      h('p', { class: 'note' }, 'This campaign lists no targets yet, so it is not on the map. It appears on the sky as soon as its record names a target.'));
  }
  // --- generated field rendition (Gaia DR3 sources drawn as a synthetic exposure) ----------
  // Same centre, field of view and orientation (TAN, north up, east left) as the survey cutout, so the
  // two can be compared pixel for pixel. Only catalogue stars appear: no nebulosity, galaxies or faint stars.
  function renderField(t, size = 768) {
    const fs = fields[t.id];
    const c = document.createElement('canvas'); c.width = c.height = size;
    const g = c.getContext('2d');
    g.fillStyle = '#04060b'; g.fillRect(0, 0, size, size);
    if (!fs || fs === 'loading') return c;
    const a0 = t.ra * D, d0 = t.dec * D, sd0 = Math.sin(d0), cd0 = Math.cos(d0);
    const pxPerRad = size / (t.image.fov * D);
    const gmax = t.field.gmax, j = fs.raw;
    g.globalCompositeOperation = 'lighter';
    const order = [...fs.g.keys()].sort((x, y) => fs.g[y] - fs.g[x]); // faint first
    for (const i of order) {
      const a = j.ra[i] * D, d = j.dec[i] * D, cosc = sd0 * Math.sin(d) + cd0 * Math.cos(d) * Math.cos(a - a0);
      if (cosc <= 0) continue;
      const xi = Math.cos(d) * Math.sin(a - a0) / cosc, eta = (cd0 * Math.sin(d) - sd0 * Math.cos(d) * Math.cos(a - a0)) / cosc;
      const x = size / 2 - xi * pxPerRad, y = size / 2 - eta * pxPerRad;
      if (x < -60 || x > size + 60 || y < -60 || y > size + 60) continue;
      const dm = Math.max(0, gmax - fs.g[i]), k = size / 768;       // magnitudes brighter than the faintest kept
      const col = starRGB(j.bp_rp[i] == null ? 5600 : teffFromBpRp(Math.max(-0.3, Math.min(4.5, j.bp_rp[i]))), 0.18);
      const Rc = (1.5 + 0.32 * dm + 0.03 * dm * dm) * k, core = Math.min(1, 0.3 + 0.075 * dm);
      let gr = g.createRadialGradient(x, y, 0, x, y, Rc * 1.6);
      gr.addColorStop(0, rgb([255, 255, 255], core)); gr.addColorStop(0.3, rgb(col, core * 0.95)); gr.addColorStop(1, rgb(col, 0));
      g.fillStyle = gr; g.beginPath(); g.arc(x, y, Rc * 1.6, 0, 7); g.fill();
      if (dm > 5) { // scattered-light halo of bright stars, as any camera records them
        const Rh = Rc * (3 + 0.45 * dm), a = Math.min(0.28, 0.035 * (dm - 5));
        gr = g.createRadialGradient(x, y, Rc * 0.5, x, y, Rh);
        gr.addColorStop(0, rgb(col, a)); gr.addColorStop(0.35, rgb(col, a * 0.35)); gr.addColorStop(1, rgb(col, 0));
        g.fillStyle = gr; g.beginPath(); g.arc(x, y, Rh, 0, 7); g.fill();
      }
    }
    g.globalCompositeOperation = 'source-over';
    // the Gaia query was a cone: outside it the rendition is empty by construction
    const rq = t.field.radius / t.image.fov * size;
    if (rq < size * 0.72) {
      g.save(); g.beginPath(); g.rect(0, 0, size, size); g.moveTo(size / 2 + rq, size / 2); g.arc(size / 2, size / 2, rq, 0, 2 * Math.PI, true); g.clip('evenodd');
      g.fillStyle = 'rgba(255,255,255,.035)'; g.fillRect(0, 0, size, size); g.restore();
      g.setLineDash([6, 6]); g.strokeStyle = 'rgba(106,209,200,.5)'; g.lineWidth = size / 768;
      g.beginPath(); g.arc(size / 2, size / 2, rq, 0, 7); g.stroke(); g.setLineDash([]);
    }
    return c;
  }

  function imageSection(t) {
    const real = h('button', { type: 'button', class: 'pair-item', 'aria-label': `Compare the survey image and the generated rendition of ${t.name}` },
      h('img', { src: t.image.file, alt: `${t.image.short} image of the ${t.name} field`, loading: 'lazy' }), h('span', {}, 'Survey image'));
    const genWrap = h('button', { type: 'button', class: 'pair-item', 'aria-label': `Open the generated rendition of ${t.name}` }, h('span', {}, t.field ? 'Generated from Gaia DR3' : 'No catalogue field'));
    const paint = () => {
      if (!t.field) return;
      const fs = fields[t.id];
      if (!fs || fs === 'loading') { setTimeout(paint, 250); return; }
      const cnv = renderField(t, 360); cnv.setAttribute('role', 'img'); cnv.setAttribute('aria-label', `Generated rendition of the ${t.name} field from Gaia DR3 sources`);
      genWrap.prepend(cnv);
    };
    paint();
    real.addEventListener('click', () => openCompare(t, 'side'));
    genWrap.addEventListener('click', () => openCompare(t, 'side'));
    return h('section', {}, h('h3', {}, 'The field · survey image and generated rendition'), h('div', { class: 'pair' }, real, genWrap),
      h('div', { class: 'zooms' }, zoomBtn('Compare', () => openCompare(t, 'side')), zoomBtn('Blink', () => openCompare(t, 'blink')), zoomBtn('Show on sky', () => flyTo(t.ra * D, t.dec * D, t.image.fov * 1.3 * D))),
      h('p', { class: 'note' }, `Left: ${t.image.source}, ${angle(t.image.fov)} across, north up, east left. Right: the same field generated from the Gaia DR3 sources the project fetched (G < ${t.field ? t.field.gmax : '—'}), each drawn with its catalogue colour and brightness. Differences between the two are expected — the rendition has no nebulosity, galaxies or stars fainter than the limit, and uses 2016 positions — and are not findings. ${t.image.terms}. Image retrieved ${t.image.retrieved}.`));
  }

  // --- comparison viewer ---------------------------------------------------
  let blinkTimer = null;
  function openCompare(t, mode = 'side') {
    closeCompare();
    const lb = h('div', { class: 'lightbox', role: 'dialog', 'aria-modal': 'true', 'aria-labelledby': 'lb-title', id: 'lightbox' });
    const real = h('img', { src: t.image.file, alt: `${t.image.short} image of the ${t.name} field` });
    const gen = t.field ? renderField(t, 768) : h('div', { class: 'empty' }, 'No catalogue field fetched for this position.');
    gen.setAttribute && gen.setAttribute('aria-label', `Generated rendition of the ${t.name} field from Gaia DR3`);
    const A = h('figure', { class: 'lb-a' }, real, h('figcaption', {}, `${t.image.short} · epoch ${/Pan-STARRS/.test(t.image.short) ? '2010–2014' : '1997–2001'}`));
    const B = h('figure', { class: 'lb-b' }, gen, h('figcaption', {}, `Generated · Gaia DR3 · ${t.field ? t.field.n.toLocaleString() + ' sources, G < ' + t.field.gmax : ''} · J2016.0`));
    const stage = h('div', { class: `lb-stage mode-${mode}` }, A, B);
    const slider = h('input', { type: 'range', min: '0', max: '100', value: '50', class: 'lb-slider', 'aria-label': 'Swipe position' });
    slider.addEventListener('input', () => stage.style.setProperty('--cut', slider.value + '%'));
    stage.style.setProperty('--cut', '50%');
    const setMode = m => {
      stage.className = `lb-stage mode-${m}`; clearInterval(blinkTimer); blinkTimer = null; stage.classList.remove('show-b');
      lb.querySelectorAll('[data-mode]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === m)));
      slider.hidden = m !== 'swipe';
      if (m === 'blink' && !reduceMotion) blinkTimer = setInterval(() => stage.classList.toggle('show-b'), 800);
    };
    const modes = h('div', { class: 'seg', role: 'group', 'aria-label': 'Comparison mode' },
      ...[['side', 'Side by side'], ['swipe', 'Swipe'], ['blink', 'Blink']].map(([m, l]) => {
        const b = h('button', { type: 'button', 'data-mode': m, 'aria-pressed': String(m === mode) }, l);
        b.addEventListener('click', () => setMode(m)); return b;
      }));
    const close = h('button', { type: 'button', class: 'lb-close', 'aria-label': 'Close comparison' }, '×');
    close.addEventListener('click', closeCompare);
    lb.append(h('div', { class: 'lb-card' },
      h('header', {}, h('div', {}, h('p', { class: 'kicker' }, `${angle(t.image.fov)} field · north up, east left`), h('h2', { id: 'lb-title' }, t.name)), modes, close),
      stage, slider,
      h('p', { class: 'note' }, 'Blink comparison is the classic way to spot what changed or what one view lacks. Here every difference has an ordinary cause first: survey artefacts (halos, spikes, tile seams), missing non-stellar light and faint stars in the rendition, and proper motion between the image epoch and 2016. Nothing in this viewer is a detection.')));
    lb.addEventListener('click', e => { if (e.target === lb) closeCompare(); });
    lb.addEventListener('keydown', e => { if (e.key === 'Escape') closeCompare(); });
    document.body.append(lb);
    setMode(mode);
    close.focus();
  }
  function closeCompare() { clearInterval(blinkTimer); blinkTimer = null; const lb = $('#lightbox'); if (lb) lb.remove(); }

  function patchSection(t) {
    const box = h('section', {}, h('h3', {}, `Where the project queried · ${t.patches.length} footprints`));
    if (!t.patches.length && !t.unshaped.length) { box.append(h('p', { class: 'note' }, 'No archive requests recorded for this position.')); return box; }
    const tb = h('tbody');
    for (const p of t.patches) {
      const ok = p.states.drive_only || 0, bad = (p.states.failed || 0) + (p.states.excluded || 0);
      const sw = h('span', { class: 'svc' }); sw.style.borderColor = SVC_COL[p.svc];
      const row = h('tr', {},
        h('td', {}, sw, SKY.services[p.svc] || p.svc),
        h('td', {}, p.what),
        h('td', { class: 'num' }, p.r ? `r ${angle(p.r)}` : `${angle(p.w)}²`),
        h('td', { class: 'num' }, `${ok}`, bad ? h('span', { class: 'st-failed' }, ` +${bad}✗`) : null));
      row.title = p.products.join('\n');
      row.style.cursor = 'zoom-in'; row.classList.add('fly');
      row.addEventListener('click', () => flyTo(p.ra * D, p.dec * D, Math.max(0.6 / 60, (p.r ? p.r * 2 : p.w) * 1.8) * D));
      tb.append(row);
    }
    box.append(h('table', {}, h('thead', {}, h('tr', {}, h('th', {}, 'Archive'), h('th', {}, 'Query'), h('th', {}, 'Size'), h('th', {}, 'Held'))), tb),
      h('p', { class: 'note' }, 'Shapes are parsed from each request as recorded in the Tier-1 manifest. Click a row to fly to that footprint; ✗ = failed or excluded request (dashed on the map). Products are held in private storage and listed with checksums in the manifest.'));
    if (t.unshaped.length) box.append(h('p', { class: 'note' }, `${t.unshaped.length} further request${t.unshaped.length > 1 ? 's' : ''} recorded without a footprint size (${t.unshaped.map(u => u.id).join(', ')}); not drawn.`));
    return box;
  }
  function planetTable(t) {
    const tb = h('tbody');
    for (const p of t.system.planets) {
      tb.append(h('tr', {},
        h('td', {}, p.name, p.transits ? ' ⊖' : ''),
        h('td', { class: 'num' }, p.P != null ? (p.P < 100 ? p.P.toFixed(4) : p.P.toFixed(1)) : '—'),
        h('td', { class: 'num' }, p.a != null ? p.a.toFixed(4) : 'derived'),
        h('td', { class: 'num' }, p.rade != null ? p.rade.toFixed(2) : '—'),
        h('td', { class: 'num' }, p.teq != null ? Math.round(p.teq) : '—'),
        h('td', {}, p.ref_url ? h('a', { href: p.ref_url, rel: 'noopener', target: '_blank' }, p.ref || 'ref') : (p.ref || '—'))));
    }
    const s = t.system.star;
    return h('section', {}, h('h3', {}, 'Planet parameters (NASA Exoplanet Archive)'),
      h('table', {}, h('thead', {}, h('tr', {}, h('th', {}, 'Planet'), h('th', {}, 'P (d)'), h('th', {}, 'a (AU)'), h('th', {}, 'Rp (R⊕)'), h('th', {}, 'Teq (K)'), h('th', {}, 'Period ref.'))), tb),
      h('p', { class: 'note' }, `Host ${t.system.host}: T_eff ${s.st_teff ?? '—'} K, R★ ${s.st_rad ?? '—'} R☉, M★ ${s.st_mass ?? '—'} M☉${s.sy_dist ? `, ${s.sy_dist.toFixed(1)} pc` : ''}. Composite table (pscomppars): values per planet may come from different papers. ⊖ = transiting; radii of non-transiting planets are archive estimates, not measurements. These are published values, not Cygnus results.`));
  }
  function sourceSection(t) {
    const d = h('details', {}, h('summary', {}, 'Sources for this panel'));
    const items = [`Position: docs/tier1_pack/NAME_RESOLUTIONS.json (${t.resolver}, ${t.frame}).`,
      'Footprints: docs/tier1_pack/MASTER_MANIFEST.csv.'];
    if (t.field) items.push(`Gaia DR3 sources (J2016.0 positions): ${t.field.n} rows, retrieved ${t.field.retrieved}. Query: ${t.field.query}`);
    if (t.image) items.push(`Image: ${t.image.source}, retrieved ${t.image.retrieved}.`);
    if (t.system) items.push('Planets: NASA Exoplanet Archive pscomppars (see data/PROVENANCE.json for the query).');
    d.append(h('pre', {}, items.join('\n\n')));
    return h('section', {}, h('h3', {}, 'Provenance'), d);
  }
  function openSources() {
    selected = null; dirty = true; clearRend();
    const P = $('#p-body'); P.replaceChildren();
    $('#panel').hidden = false; document.body.classList.add('panel-open');
    P.append(h('h2', { id: 'p-title' }, 'Sources'),
      h('p', {}, 'Project records: target positions, query footprints and analyses come from files in the worktree. Background layers come from public catalogues fetched for this map:'));
    const ul = h('ul');
    for (const [k, v] of Object.entries(SKY.provenance)) ul.append(h('li', {}, h('strong', {}, k), ` — ${v.source}. ${v.rows != null ? v.rows + ' rows. ' : ''}Retrieved ${v.retrieved_utc}. ${v.terms || ''}`));
    P.append(ul, h('p', { class: 'note' }, `${SKY.unassigned.length} recorded requests are not tied to a sky position (table schemas, all-sky table extracts, service probes) and are not drawn: ${SKY.unassigned.map(u => u.id).join(', ')}.`),
      h('p', { class: 'note' }, 'The projection is stereographic in ICRS with east to the left. Gaia source positions are at epoch J2016.0; target positions are J2000.0 — for high proper-motion stars the two differ visibly at the closest zoom.'));
  }

  // ------------------------------------------------------------ boot
  async function boot() {
    for (const k of ['mast', 'gaia', 'skyview', 'irsa', 'legacysurvey']) SVC_COL[k] = css(`--svc-${k}`);
    for (const k of ['analysed', 'planned', 'retrieved', 'failed']) STATUS_COL[k] = css(`--st-${k}`);
    makeGlow(); makeMW();
    GAL_LINE = Array.from({ length: 361 }, (_, i) => galToVec(i * D, 0));
    ECL_LINE = Array.from({ length: 361 }, (_, i) => eclToVec(i * D));
    SKY = await (await fetch('data/sky.json')).json();
    SKY.stars = SKY.stars.map(([ra, dec, V, bv, label]) => ({ v: vec(ra * D, dec * D), V, label, col: rgb(starRGB(bv == null ? 5800 : teffFromBV(Math.max(-0.4, Math.min(2, bv))), 0.5)) }));
    SKY.consts = SKY.consts.map(([abbr, name, ra, dec]) => ({ abbr, name, v: vec(ra * D, dec * D) }));
    const ln = SKY.mw.map(c => Math.log(c[2])), lo = Math.min(...ln), hi = Math.max(...ln);
    SKY.mw = SKY.mw.map(([ra, dec, n]) => ({ v: vec(ra * D, dec * D), a: 0.30 * Math.pow((Math.log(n) - lo) / (hi - lo), 1.7) }));
    for (const t of SKY.targets) {
      t.v = vec(t.ra * D, t.dec * D);
      for (const p of t.patches) p.path = patchPath(p);
      if (t.image) t.image.short = /PanSTARRS|Pan-STARRS/.test(t.image.source) ? 'Pan-STARRS1 DR1 colour' : '2MASS J H Ks colour';
      const nOk = t.counts.drive_only || 0, nBad = (t.counts.failed || 0) + (t.counts.excluded || 0);
      const recs = t.records || [], done = recs.filter(r => r.status === 'completed');
      const outcomes = [...new Set(done.map(r => (OUTCOME[r.outcome] || r.outcome).toLowerCase()))].join(', ');
      t.statusShort = t.status === 'analysed' ? `analysed · ${outcomes}` : t.status === 'planned' ? 'analysis planned' : t.status === 'retrieved' ? `${nOk} products retrieved` : 'probe only';
      t.statusText = t.status === 'analysed'
        ? `Analysed in ${done.length} record${done.length === 1 ? '' : 's'}: ${done.map(r => r.kind).join('; ')}. Outcome: ${outcomes}${recs.some(r => r.outcome === 'candidate' || r.outcome === 'lead') ? '' : ' — no candidate'}. ${nOk} archive products retrieved and checksummed.`
        : t.status === 'planned'
          ? `An analysis is recorded but has not completed (${recs.map(r => r.status).join(', ')}). ${nOk} archive products retrieved.`
        : t.status === 'retrieved'
          ? `${nOk} archive product${nOk === 1 ? '' : 's'} retrieved and checksummed${nBad ? `; ${nBad} request${nBad === 1 ? '' : 's'} failed or excluded` : ''}. Not analysed yet — this is a baseline record, not a result.`
          : `Only an exploratory request was recorded (${nBad} failed or excluded); no product is held.`;
    }
    buildUI(); resize(); setup();
    if (matchMedia('(max-width: 760px)').matches) $('#rail-toggle').setAttribute('aria-expanded', 'false');
    const id = decodeURIComponent(location.hash.slice(1)), t0 = SKY.targets.find(t => t.id === id);
    if (t0) { $('#intro').hidden = true; select(t0); }
    requestAnimationFrame(frame);
  }
  window.addEventListener('resize', resize);
  boot().catch(e => { console.error(e); $('#intro').append(h('p', { class: 'note' }, 'The sky data could not be loaded: ' + e.message)); });
})();

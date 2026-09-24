/* Ad Astra components are HTML + CSS patterns rendered by Jinja macros
   (src/cygnus/publish/templates/_macros.html.j2). These types document the
   data each pattern needs; there is no JavaScript component bundle. */

export type AuditState = 'passed' | 'failed' | 'inconclusive' | 'not_tested';
export type EvidenceLevel = 'unverified_lead' | 'vetted_candidate' | 'independently_supported_candidate' | 'established';
export type Availability = 'download' | 'online' | 'link' | 'restricted' | 'withdrawn';
export type Origin = 'project' | 'derived' | 'third_party';
export type RetrievalState = 'held' | 'excluded' | 'failed' | 'unknown';
export type RunStatus = 'open' | 'completed' | 'failed' | 'aborted';
export type ModuleStatus = 'verified' | 'implemented' | 'planned' | 'unknown';

/** m.state(s, label) — glyph + word + reserved colour. */
export interface StateChipProps { state: AuditState | RetrievalState | RunStatus | ModuleStatus; label?: string }
/** m.availability(a) / m.origin(o) / m.collection_status(s) */
export interface BadgeProps { variant?: 'accent' | 'quiet' | 'draft' | 'withdrawn' | 'restricted'; children: string }
/** m.ladder(rank) — rank 0..3 indexes EvidenceLevel. */
export interface EvidenceLadderProps { rank: 0 | 1 | 2 | 3 }
/** m.val(v, missing) — renders .unset when v is null/empty. Never substitute a guess. */
export interface ValueProps { value: string | number | null; missing?: string }
/** m.files(list) */
export interface PublicFile { url: string; filename: string; bytes: number; sha256: string; label: string }
/** m.state_bar(counts, total, name) */
export interface StateBarProps { counts: Partial<Record<RetrievalState, number>>; total: number; name: string }
/** m.related(list, exclude) */
export interface RelatedLink { type: 'collection' | 'document' | 'campaign' | 'candidate'; title: string; url: string }
export interface CalloutProps { tone?: 'note' | 'caution' | 'draft'; title: string; children: string }

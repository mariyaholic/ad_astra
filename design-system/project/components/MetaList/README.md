# MetaList

A two-column `dl.meta`: mono uppercase terms in `ink-3`, values wrapping anywhere.

- Consumer provides term/value pairs. A missing value renders `.unset` ("not recorded", italic `ink-3`) — never a blank, a dash that implies zero, or a guess.
- Use `.id` / `.mono` on values that are identifiers, hashes or timestamps (ISO-8601 UTC with Z).

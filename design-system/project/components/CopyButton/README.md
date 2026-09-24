# CopyButton

A small underlined text button that copies a full checksum or citation; shown only when the Clipboard API exists.

- Consumer provides the full value in `data-copy`; the visible text is truncated (`sha256 61192ae85fc2…`) and the full value sits in `title`.
- On success the label reads "copied" for 1.4s. On failure nothing is claimed; the value stays selectable.

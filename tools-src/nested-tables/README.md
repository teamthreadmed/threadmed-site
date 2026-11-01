# Nested Tables — source

The standalone app served at https://www.threadmed.org/private/nested-tables/ (unlisted, no-index).
Same code is published as the Claude artifact "Nested Tables" (cloud-synced variant).

## Iterate
1. Edit `index.html` (bump `APP_VERSION` near the top of the script; it shows in the status pill).
2. `node build.js` — writes `private/nested-tables/index.html`.
3. Commit and push `main`. GitHub Pages updates the URL in 1–3 minutes. Reload the page; the version pill confirms the build.

User data never lives in these files: it autosaves in each browser's storage. A new build merges any sample project the browser does not have yet (matched by name) and leaves everything else alone. Backups: 💾 Save → JSON in the app; restore with 📥 Import.

## Two URLs
- **Latest**: https://www.threadmed.org/private/nested-tables/ — every build lands here.
- **Master**: https://www.threadmed.org/private/nested-tables/master/ — a frozen known-good copy. Promote with `node build.js master` only when Anthony says the latest is good. If latest breaks, use master (same browser storage, so data is shared).

## Backups
- Repo history (every build is a commit).
- Google Drive folder "Nested Tables Backups": the latest and master HTML plus seed.json / extra.json, uploaded at each release.
- Inside the app: 🕒 manual versions and daily auto-versions per project (IndexedDB in each browser); 💾 JSON export for off-device copies.

## Files
- `index.html` — the app (single file, plain JS, no build step for the app itself)
- `js/` — jsPDF, jsPDF-AutoTable, JSZip (used by PDF / Obsidian exports)
- `extra.json` — projects carried over from the Claude artifact's cloud store (Tool building backlog, captures)
- `seed.json` — the five sample projects (exported from the app; regenerate by loading samples in a fresh copy and exporting JSON)
- `build.js` — inlines seed + libraries + base64 source into one HTML file, so the app can also "Save the app as HTML" from inside itself

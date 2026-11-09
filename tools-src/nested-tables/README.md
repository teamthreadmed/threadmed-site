# Nested Tables — source

The standalone app served at https://www.threadmed.org/private/nested-tables/ (unlisted, no-index).
Same code is published as the Claude artifact "Nested Tables" (cloud-synced variant).

## Iterate
1. Edit `index.html` (bump `APP_VERSION` near the top of the script; it shows in the status pill).
2. `node build.js` — writes `private/nested-tables/index.html`.
3. `node regression.js` (needs Playwright) — 15 checks on an iPhone viewport; every line must say ok before publishing.
4. Commit and push `main`. GitHub Pages updates the URL in 1–3 minutes. Reload the page; the version pill confirms the build.

User data never lives in these files: it autosaves in each browser's storage. A new build merges any sample project the browser does not have yet (matched by name) and leaves everything else alone. Backups: 💾 Save → JSON in the app; restore with 📥 Import.

## Two URLs
- **Clinical (latest)**: https://www.threadmed.org/private/nested-tables/ — every build lands here. Labelled "Nested Tables · Clinical" (Home Screen name "NT Clinical", Master file "Nested Tables MASTER (clinical).json"); storage key unchanged, so data from earlier builds is kept.
- **Master**: https://www.threadmed.org/private/nested-tables/master/ — a frozen known-good copy. Promote with `node build.js master` only when Anthony says the latest is good. If latest breaks, use master (same browser storage, so data is shared).

- **Personal**: https://www.threadmed.org/private/nested-tables/personal/ — the same app built with `node build.js personal`: its own storage (`nested-tables-v3@personal`, IndexedDB `nested-tables@personal`), its own Master file ("Nested Tables MASTER (personal).json"), no clinical samples (only the how-to project). Add it to the Home Screen as a second icon ("NT Personal"). Spaces are defined in `SPACES` in build.js.

## Storage (v2.5)
- Data lives in IndexedDB (store `state`, record `main`) — no 5 MB cap. localStorage keeps a mirror only while it fits (older builds read only that). On load, if both exist the one with the latest edit wins.
- Before v2.5 everything was in localStorage; Safari caps that at ~5 MB (UTF-16, so ~2.5 M characters) and a save past the cap failed with only a pill/toast — new projects then vanished on reload. Now a failed save (both stores) opens a dialog pointing at 💾 Master file → save.
- 💾 Save / Backup shows the storage line: where the data is, size, project count, Home Screen app vs browser tab, space.
- Each browser and each Home Screen app has its own storage; the Master file is the bridge between them.

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

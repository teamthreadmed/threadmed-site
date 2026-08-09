# Deploy guide — Thread Medicine site (low-friction best practice)

Host this site on **GitHub Pages** and point a subdomain at it from
**Squarespace**. Two services, no Cloudflare, no coding, no build server.

## Why this setup

- **Squarespace** — keeps doing what it already does: owns the domain, runs
  DNS, hosts your root `threadmed.org`, carries your Google email. Untouched.
- **GitHub** — stores your site files *and* hosts them (GitHub Pages). One
  account does both jobs.
- **Substack** — stays your newsletter + subscriber list.

You run `build.py` locally as you already do, commit the built files, and
GitHub Pages serves them. Adding an essay later = build + upload.

---

## Step 1 — Create the repo and upload the site (browser only)

1. **github.com** → sign in / create account → note your **username**.
2. **New repository** → name `threadmed-site` → Public → **Create**.
3. **"uploading an existing file"** → drag in the **contents** of this folder
   (`index.html`, the `essays` folder, the `assets` folder) → **Commit**.

## Step 2 — Turn on GitHub Pages

1. In the repo → **Settings** → **Pages**.
2. **Source:** *Deploy from a branch* → Branch: **main** → Folder: **/ (root)**
   → **Save**.
3. Under **Custom domain**, enter `read.threadmed.org` (or `essays.` /
   `tools.` — your call) → **Save**. Leave **Enforce HTTPS** to switch on by
   itself once DNS resolves (a few minutes to a couple hours).

## Step 3 — Add ONE record in Squarespace

1. **Squarespace** → **Settings → Domains** → `threadmed.org` → **DNS settings**.
2. **Add record**: Type **CNAME**, Host **read** (match your subdomain),
   Value `YOUR-USERNAME.github.io` → **Save**.

That's it. `read.threadmed.org` goes live with HTTPS.

> ONLY add that one CNAME. Do not edit or delete the existing records — the
> root `A` records keep your Squarespace site up, and the `MX` records keep
> your Google email working.

## Step 4 — Updating later

Edit/replace a file in the GitHub repo (via the website's upload button) →
GitHub Pages redeploys in about a minute.

### Optional polish (later)

`build.py` can be run automatically by a GitHub Action so you only ever
upload a markdown file — ask and I'll add the workflow. Not needed to launch.

### If you'd rather keep Cloudflare

Everything still works via Cloudflare Pages instead of GitHub Pages (same
GitHub repo, CNAME points to a `pages.dev` address). GitHub Pages is just
fewer moving parts.

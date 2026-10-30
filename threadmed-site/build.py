#!/usr/bin/env python3
"""Thread Medicine static site build.

Usage:  python3 build.py
Reads the essay markdown in SRC and writes HTML into essays/, plus index.html.
Add a new essay by appending an entry to ESSAYS and dropping the .md file in SRC.
"""
import os, re, html, markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700'
         '&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600'
         '&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

MARK = ('<svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">'
        '<path d="M2 15c4 0 4-10 8-10s4 10 8 10" stroke="#1F6F6B" stroke-width="1.5" fill="none"/>'
        '<path d="M2 9c4 0 4-6 8-6s4 6 8 6" stroke="#B8762A" stroke-width="1.2" fill="none" opacity=".65"/>'
        '</svg>')

ESSAYS = [
    dict(
        slug="beyond-the-reference-range",
        src="essay-diagnosis-beyond-reference-range.md",
        num="Essay 01",
        title="Beyond the Reference Range",
        standfirst="From population thresholds to individual diagnosis in male hypogonadism.",
        blurb=("Why a testosterone number is a starting point rather than a diagnosis — ten nuances, "
               "a staged workup, and what mass screening gets wrong in both directions."),
        systems=["Gonadal axis", "Bone", "Adipose", "Fertility", "Population health"],
        date="August 2026",
    ),
    dict(
        slug="testosterone-in-women",
        src="essay-female-testosterone.md",
        num="Essay 02",
        title="The Other Half of the Androgen Story",
        standfirst="Testosterone in women: the evidence, the measurement problem, and why the logistics are the hardest part.",
        blurb=("No validated threshold, no approved product, one evidence-based indication — and a market "
               "filling the gap with implants that cannot be removed."),
        systems=["Gonadal axis", "Bone", "Sexual function", "Menopause", "Regulation"],
        date="August 2026",
    ),
]

ALL_SYSTEMS = []
for e in ESSAYS:
    for s in e["systems"]:
        if s not in ALL_SYSTEMS:
            ALL_SYSTEMS.append(s)


def key(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def shell(title, desc, body, active="", depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="masthead"><div class="wrap">
  <a class="wordmark" href="{up}index.html">{MARK} Thread Medicine</a>
  <nav class="nav">
    <a href="{up}index.html#essays">Essays</a>
    <a href="{up}index.html#tools">Tools</a>
    <a href="{up}index.html#about">About</a>
  </nav>
</div></header>
{body}
<footer class="foot"><div class="wrap">
  <div>
    <strong style="color:#FBFAF7;font-family:Fraunces,Georgia,serif">Thread Medicine</strong><br>
    Anthony Pick, MD, CDCES, CCD, MSCP<br>
    <a href="mailto:hello@threadmed.org">hello@threadmed.org</a>
  </div>
  <div class="disc">
    Written for clinicians. Everything here is general medical education, not individual
    medical advice, and it does not create a physician–patient relationship. Views are the
    author's own.
  </div>
</div></footer>
</body>
</html>
"""


def render_essay(meta):
    with open(os.path.join(SRC, meta["src"]), encoding="utf-8") as f:
        raw = f.read()

    # Drop the markdown title block; the page header replaces it.
    lines = raw.split("\n")
    start = 0
    for i, ln in enumerate(lines[:12]):
        if ln.strip().startswith("*Anthony Pick"):
            start = i + 1
            break
    body_md = "\n".join(lines[start:]).lstrip("\n-\n ")
    body_md = re.sub(r"^\s*---\s*$", "", body_md, count=1, flags=re.M)

    body_html = markdown.markdown(
        body_md, extensions=["tables", "attr_list", "sane_lists", "smarty"]
    )

    tags = "".join(
        f'<span class="tag" data-sys="{key(s)}">{html.escape(s)}</span>' for s in meta["systems"]
    )
    inner = f"""
<article class="article"><div class="wrap">
  <div class="article-head">
    <div class="kicker mono">{meta['num']} &middot; {meta['date']}</div>
    <h1>{html.escape(meta['title'])}</h1>
    <p class="standfirst">{html.escape(meta['standfirst'])}</p>
    <div class="tags" style="margin-bottom:1rem">{tags}</div>
    <div class="byline">Anthony Pick, MD, CDCES, CCD, MSCP</div>
  </div>
  <div class="prose">
{body_html}
  </div>
</div></article>
"""
    out = shell(f"{meta['title']} — Thread Medicine", meta["standfirst"], inner, depth=1)
    with open(os.path.join(HERE, "essays", meta["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(out)


def render_index():
    chips = "".join(
        f'<button class="chip" type="button" aria-pressed="false" data-sys="{key(s)}">{html.escape(s)}</button>'
        for s in ALL_SYSTEMS
    )
    entries = ""
    for e in ESSAYS:
        tags = "".join(
            f'<span class="tag" data-sys="{key(s)}">{html.escape(s)}</span>' for s in e["systems"]
        )
        syskeys = " ".join(key(s) for s in e["systems"])
        entries += f"""
    <a class="entry" href="essays/{e['slug']}.html" data-systems="{syskeys}">
      <div class="num">{e['num']}</div>
      <div>
        <h3>{html.escape(e['title'])}</h3>
        <p>{html.escape(e['blurb'])}</p>
        <div class="tags">{tags}</div>
      </div>
    </a>"""

    weave = """<svg class="hero-weave" viewBox="0 0 1200 420" preserveAspectRatio="none" aria-hidden="true">
  <path d="M-50 300 C 220 300, 260 120, 480 120 S 760 300, 1000 300 1250 180 1250 180" stroke="#1F6F6B" stroke-width="1.1" fill="none" opacity=".85"/>
  <path d="M-50 340 C 240 340, 300 200, 520 200 S 800 330, 1030 330 1250 250 1250 250" stroke="#4E9B95" stroke-width="1" fill="none" opacity=".5"/>
  <path d="M-50 250 C 200 250, 240 60, 470 60 S 720 240, 980 240 1250 120 1250 120" stroke="#B8762A" stroke-width="1" fill="none" opacity=".38"/>
  <path d="M-50 380 C 260 380, 330 270, 560 270 S 830 380, 1060 380 1250 320 1250 320" stroke="#1F6F6B" stroke-width=".8" fill="none" opacity=".3"/>
</svg>"""

    body = f"""
<section class="hero">
  {weave}
  <div class="wrap">
    <div class="eyebrow mono">Applied systems thinking in clinical medicine</div>
    <h1>Medicine cuts the body into departments. Patients arrive with <em>threads</em>.</h1>
    <p>Long-form clinical reasoning on the problems that cross organ systems — written for
    clinicians, held to the evidence, and specific enough to use on a Tuesday afternoon.</p>
  </div>
</section>

<section class="section" id="essays">
  <div class="wrap">
    <div class="section-head"><span class="mono">Essays</span><span class="line"></span></div>
    <div class="filterbar">
      <p class="hint">Filter by the systems an essay runs through.</p>
      <div class="systems">{chips}</div>
    </div>
    <div class="entries" id="entries">{entries}
    </div>
  </div>
</section>

<section class="section" id="tools">
  <div class="wrap">
    <div class="section-head"><span class="mono">Tools</span><span class="line"></span></div>
    <h2 class="display">Decision support that shows its reasoning</h2>
    <p class="lede">The essays describe the reasoning. These make it repeatable — staged workups
    that surface which step drove the conclusion, carry the evidence grade to the point of use,
    and are willing to answer &ldquo;not yet answerable.&rdquo;</p>
    <div class="cols" style="margin-top:2rem">
      <div class="col"><span class="status">In development</span>
        <h3>Individualized androgen workup</h3>
        <p>Staged diagnosis for the man in the gray zone: assay check, binding correction, axis
        localization, reversibility, coherence read.</p></div>
      <div class="col"><span class="status">In development</span>
        <h3>Bone health review</h3>
        <p>DXA interpretation and treatment sequencing, including the sex-steroid contribution
        that standard reports leave out.</p></div>
      <div class="col"><span class="status">Planned</span>
        <h3>Menopause decision support</h3>
        <p>Symptom-led, evidence-graded, and explicit about where the WHI findings do and do not
        apply.</p></div>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap">
    <div class="section-head"><span class="mono">About</span><span class="line"></span></div>
    <h2 class="display">Why this exists</h2>
    <p class="lede">Guidelines answer questions about populations. Clinics see individuals. Most of
    the difficult work in medicine happens in that gap — and almost nobody writes down how it is
    actually done.</p>
    <p class="lede" style="margin-top:1.2rem">Thread Medicine is applied systems biology held to an
    evidence standard, delivered by a team and fitted to a person. Anthony Pick is a
    board-certified endocrinologist (internal medicine, endocrinology, obesity medicine, clinical
    lipidology) with certification in clinical densitometry and diabetes care and education, and a
    Menopause Society Certified Practitioner.</p>
  </div>
</section>

<script>
(function(){{
  var chips = document.querySelectorAll('.chip');
  var entries = document.querySelectorAll('.entry');
  var active = null;
  function apply(){{
    entries.forEach(function(el){{
      var has = !active || el.dataset.systems.split(' ').indexOf(active) > -1;
      el.classList.toggle('dim', !has);
    }});
    document.querySelectorAll('.tag').forEach(function(t){{
      t.classList.toggle('hit', !!active && t.dataset.sys === active);
    }});
  }}
  chips.forEach(function(c){{
    c.addEventListener('click', function(){{
      active = (active === c.dataset.sys) ? null : c.dataset.sys;
      chips.forEach(function(o){{ o.setAttribute('aria-pressed', String(o.dataset.sys === active)); }});
      apply();
    }});
  }});
}})();
</script>
"""
    out = shell(
        "Thread Medicine — applied systems thinking in clinical medicine",
        "Long-form clinical reasoning on problems that cross organ systems, by Anthony Pick MD.",
        body, depth=0,
    )
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


if __name__ == "__main__":
    for e in ESSAYS:
        render_essay(e)
        print("built essays/%s.html" % e["slug"])
    render_index()
    print("built index.html")

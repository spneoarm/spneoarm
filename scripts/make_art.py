"""Draw the profile's pixel art. Run from the repo root: uv run --no-project python scripts/make_art.py"""
from pixel import Canvas

B, F, D, M, L = "#0b0d08", "#161c0a", "#5f7a1f", "#8fbf2a", "#c6ff3d"
BLINK = ".blink{animation:blink 1s step-end infinite}@keyframes blink{0%{opacity:1}50%{opacity:0}}"


def scanlines(c):
    w, h = c.w * c.px, c.h * c.px
    return ('<defs><pattern id="sl" width="4" height="4" patternUnits="userSpaceOnUse">'
            '<rect width="4" height="1" fill="#000" fill-opacity=".3"/></pattern></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#sl)"/>')


def window(c, y, h, title):
    c.rect(0, 0, c.w, c.h, B)
    c.rect(8, y, 304, h, F)
    c.frame(8, y, 304, h, D)
    c.rect(8, y, 304, 9, D)
    for i, col in enumerate(["#ff5ca8", "#ffcf3d", L]):
        c.rect(12 + i * 5, y + 3, 3, 3, col)
    c.text_center(title, 160, y + 1, B)


def banner():
    c = Canvas(320, 90)
    window(c, 6, 78, "~/SPNEOARM  ZSH")
    c.text("> WHOAMI", 16, 20, D)
    c.text("SUPANUT", 16, 31, L, 3, shadow=(D, 1))
    c.text("VIBE CODER / THAILAND", 16, 58, M)
    c.text("AI WRITES. I REVIEW.", 16, 70, D)
    for y in range(20, 79, 3):
        c.rect(176, y, 1, 2, D)

    c.text("$ ./SHIP.SH", 186, 20, D)
    for i, step in enumerate(["PLAN", "BUILD", "CHECK", "REVIEW"]):
        y = 31 + i * 10
        c.text(step, 186, y, M)
        c.text("[ OK ]", 234, y, L, layer=c.layer(f"ok{i + 1}"))
    c.text("SHIP", 186, 71, M)
    c.rect(234, 71, 5, 7, L, c.layer("blink"))

    # Each [ OK ] shows at rest, then the loop reveals them one by one.
    css = BLINK + "".join(
        f".ok{i}{{animation:r{i} 8s step-end infinite}}"
        f"@keyframes r{i}{{0%{{opacity:1}}3%{{opacity:0}}{8 + i * 12}%{{opacity:1}}}}"
        for i in range(1, 5))
    return c.svg("Supanut, vibe coder in Thailand. Ship script: plan, build, check, review, ship.", css, scanlines(c))


def agents():
    c = Canvas(320, 76)
    window(c, 2, 72, "~/SPNEOARM  AGENTS")
    c.text("4", 20, 28, L, 4, shadow=(D, 1))
    c.text("AI AGENTS", 64, 30, L, 2)
    c.text("ONE JOB EACH", 64, 50, M)
    for i in range(4):
        c.rect(250 + i * 12, 40, 5, 5, L, c.layer(f"led{i + 1}"))
    css = "".join(f".led{i}{{animation:blink 2s step-end infinite;animation-delay:-{i * 0.5}s}}" for i in range(1, 5))
    css += "@keyframes blink{0%{opacity:1}50%{opacity:.35}}"
    return c.svg("Four AI agents. Each one has one job.", css, scanlines(c))


for path, svg in [("assets/banner.svg", banner()), ("assets/ai-row.svg", agents())]:
    with open(path, "w") as f:
        f.write(svg)

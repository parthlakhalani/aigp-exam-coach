"""Build the AIGP practice exam pages.

Usage:  python3 practice-exams/_build/build.py            (from the repo root)

Reads exams.json and, for each exam, data/<id>.json, then writes:
  practice-exams/<id>/index.html   one self-contained exam page
  practice-exams/index.html        landing page listing every exam by level

Question file format (data/<id>.json): a list of
  {"n": 1, "q": "question", "options": ["A", "B", "C", "D"] (4 or 5),
   "answer": index of the correct option, "explanation": "...", "c": "II.B"}
where "c" is the AIGP BoK v2.1 competency code (I.A ... IV.C).
Optional: "scenario": "text" for scenario-based questions. Those questions are
shown split screen, with the scenario on the left and the question on the right.
Separate paragraphs in the scenario with a blank line.
"""
import html, json, pathlib

BUILD = pathlib.Path(__file__).resolve().parent
OUT = BUILD.parent
LEVELS = ["Easy", "Medium", "Hard"]
CODES = {"I.A", "I.B", "I.C", "II.A", "II.B", "II.C", "II.D",
         "III.A", "III.B", "III.C", "IV.A", "IV.B", "IV.C"}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""


def check(exam, qs):
    for q in qs:
        n = q.get("n")
        assert len(q["options"]) in (4, 5), f"{exam['id']} Q{n}: needs 4 or 5 options"
        assert 0 <= q["answer"] < len(q["options"]), f"{exam['id']} Q{n}: answer out of range"
        assert q["c"] in CODES, f"{exam['id']} Q{n}: unknown BoK code {q['c']}"
        assert q["q"].strip() and q["explanation"].strip(), f"{exam['id']} Q{n}: empty text"
        assert isinstance(q.get("scenario", ""), str), f"{exam['id']} Q{n}: scenario must be text"


def render_exam(exam, qs, standalone=True):
    t = (BUILD / "template.html").read_text(encoding="utf-8")
    data = json.dumps(qs, ensure_ascii=False).replace("</", "<\\/")
    back = '<p style="margin:8px 0 0"><a class="back" href="../index.html">&larr; All practice exams</a></p>' if standalone else ""
    for k, v in {"__DATA__": data, "__ID__": exam["id"], "__LEVEL__": exam["level"],
                 "__LVLKEY__": exam["level"].lower(), "__SET__": str(exam["set"]),
                 "__COUNT__": str(len(qs)), "__BACKLINK__": back}.items():
        t = t.replace(k, v)
    if not standalone:
        return t
    t = t.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    i = t.index("</style>") + len("</style>")
    return HEAD + t[:i] + "\n</head>\n<body>\n" + t[i:].lstrip() + "\n</body>\n</html>\n"


def render_landing(exams):
    sections = []
    for lvl in LEVELS:
        items = [e for e in exams if e["level"] == lvl]
        cards = "".join(
            f'<a class="ex" href="{e["id"]}/index.html" data-id="{e["id"]}">'
            f'<span class="nm">{lvl} Exam {e["set"]}</span>'
            f'<span class="meta">{e["count"]} questions &middot; 180 min</span>'
            f'<span class="last">Not taken yet</span></a>'
            for e in sorted(items, key=lambda e: e["set"]))
        if not cards:
            cards = '<p class="soon">Coming soon</p>'
        sections.append(f'<section><h2><span class="lvl lvl-{lvl.lower()}">{lvl}</span>'
                        f'<span class="cnt">{len(items)} exam{"s" if len(items) != 1 else ""}</span></h2>'
                        f'<div class="grid">{cards}</div></section>')
    return (BUILD / "landing.html").read_text(encoding="utf-8").replace("__SECTIONS__", "\n".join(sections))


def main():
    exams = json.loads((BUILD / "exams.json").read_text(encoding="utf-8"))
    ids = [e["id"] for e in exams]
    assert len(ids) == len(set(ids)), "duplicate exam id in exams.json"
    for e in exams:
        assert e["level"] in LEVELS, f"{e['id']}: level must be one of {LEVELS}"
        qs = json.loads((BUILD / e["data"]).read_text(encoding="utf-8"))
        check(e, qs)
        e["count"] = len(qs)
        out = OUT / e["id"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render_exam(e, qs), encoding="utf-8")
        print(f"built {out.relative_to(OUT.parent)}  ({len(qs)} questions)")
    (OUT / "index.html").write_text(render_landing(exams), encoding="utf-8")
    print("built practice-exams/index.html")


if __name__ == "__main__":
    main()

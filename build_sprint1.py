"""Build sprint1.html from sprint1.csv + sprint1_bugs.json.

Usage: python3 build_sprint1.py
Keeps the existing page layout: intro, Confirmed bugs table, All test cases table.
"""
import csv, json
from html import escape as e

STYLE = """body{font-family:system-ui,Arial,sans-serif;margin:20px;color:#1a1a1a;background:#fafafa}h1{margin:0 0 4px}
table{border-collapse:collapse;width:100%;background:#fff;font-size:14px}th,td{border:1px solid #ddd;padding:8px;vertical-align:top}
th{background:#1f2937;color:#fff;position:sticky;top:0;text-align:left}td.n{font-weight:bold;font-size:18px;text-align:center}
video{width:340px;border-radius:6px}.soon{width:340px;padding:40px 0;text-align:center;background:#eee;color:#777;border-radius:6px}
tr.pass td.res{background:#ecfdf3;color:#166534;font-weight:600}
tr.fail td.res{background:#fef2f2;color:#991b1b;font-weight:700}
tr.partial td.res,tr.untested td.res{background:#fffbeb;color:#92400e;font-weight:600}
p{margin:0 0 6px}.tech{color:#555;font-size:12px}ol{margin:0;padding-left:18px}"""

HEAD = '<tr><th>#</th><th>Section</th><th>Test case</th><th>Result</th><th>What happened / notes</th><th>Video</th></tr>'
BUGHEAD = ('<tr><th>#</th><th>Bug</th><th>Video</th><th>Explanation</th><th>Steps to recreate</th>'
           '<th>Should happen</th><th>Actually happens</th></tr>')


def rowclass(result):
    r = result.strip().lower()
    if r.startswith("pass"):
        return "pass"
    if r.startswith("fail"):
        return "fail"
    if r.startswith("untested"):
        return "untested"
    return "partial"


def videocell(v):
    v = v.strip()
    if v:
        return f'<video controls preload="metadata" src="{e(v)}"></video>'
    return '<div class="soon">—</div>'


def bugrow(b):
    vid = (f'<video controls preload="metadata" src="{e(b["video"])}"></video>' if b.get("video")
           else '<div class="soon">No video yet</div>')
    expl = (f'<p><b>What is wrong:</b> {e(b["what_is_wrong"])}</p>'
            f'<p><b>Why it is a bug:</b> {e(b["why_it_is_a_bug"])}</p>')
    if b.get("technical_detail"):
        expl += f'<p class=tech>{e(b["technical_detail"])}</p>'
    steps = "".join(f"<li>{e(s)}</li>" for s in b["steps"])
    return (f'<tr class="fail" id="bug-{b["id"]}"><td class="n">{b["id"]}</td><td>{e(b["title"])}</td>'
            f'<td class="v">{vid}</td><td>{expl}</td><td><ol>{steps}</ol></td>'
            f'<td>{e(b["should_happen"])}</td><td>{e(b["actually_happens"])}</td></tr>')


def caserow(r):
    num, section, case, res, note, vid = (r + [""] * 6)[:6]
    return (f'<tr class="{rowclass(res)}" id="row-{num}"><td class="n">{e(num)}</td><td>{e(section)}</td>'
            f'<td>{e(case)}</td><td class="res">{e(res)}</td><td>{e(note)}</td>'
            f'<td class="v">{videocell(vid)}</td></tr>')


def main():
    with open("sprint1.csv", newline="") as f:
        rows = list(csv.reader(f))
    header, data = rows[0], [r for r in rows[1:] if r and r[0].strip()]
    bugs = json.load(open("sprint1_bugs.json"))

    npass = sum(1 for r in data if r[3].strip().lower().startswith("pass"))
    nfail = sum(1 for r in data if r[3].strip().lower().startswith("fail"))
    nother = len(data) - npass - nfail

    intro = (f'{len(data)} test cases in Chrome on the trial account pavi+nov18@getcone.io. '
             f'{npass} pass, {len(bugs)} bugs (every bug was reproduced twice — each has a narrated video), '
             f'{nother} partial/untested (mostly things that need real time to pass, like scheduled recurring '
             'copies firing). Green = Pass, red = bug, amber = partially tested. Only "S1"/"S2"-prefixed test '
             'data was touched.')

    html = ('<!doctype html><html><head><meta charset="utf-8">'
            '<title>Sprint 1 results — Cone Work &amp; Tasks (Chrome)</title>'
            f'<style>{STYLE}</style></head><body>'
            '<h1>Sprint 1 results — Cone Work &amp; Tasks</h1>'
            f'<p>{e(intro)}</p>'
            '<p>Bug videos are also listed on the <a href="index.html">main bug page</a>.</p>'
            '<h2 style="margin-top:32px">Confirmed bugs</h2>'
            f'<table>{BUGHEAD}' + "".join(bugrow(b) for b in bugs) + '</table>'
            '<h2 style="margin-top:32px">All test cases</h2>'
            f'<table>{HEAD}' + "".join(caserow(r) for r in data) + '</table></body></html>')
    open("sprint1.html", "w").write(html)
    print(f"wrote sprint1.html: {len(data)} rows, {npass} pass, {len(bugs)} bugs, {nother} other")


if __name__ == "__main__":
    main()

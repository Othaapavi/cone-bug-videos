"""Build a bug table page from a bugs JSON file.

Usage: python3 build_bug_page.py bugs-chrome.json bugs-chrome.html "Cone bug list — Chrome"
"""
import json, sys
from html import escape as e

STYLE = """body{font-family:system-ui,Arial,sans-serif;margin:20px;color:#1a1a1a;background:#fafafa}h1{margin:0 0 4px}
table{border-collapse:collapse;width:100%;background:#fff;font-size:14px}th,td{border:1px solid #ddd;padding:8px;vertical-align:top}
th{background:#1f2937;color:#fff;position:sticky;top:0;text-align:left}td.n{font-weight:bold;font-size:18px;text-align:center}
video{width:340px;border-radius:6px}.soon{width:340px;padding:40px 0;text-align:center;background:#eee;color:#777;border-radius:6px}
.ok{background:#ecfdf3}.bad{background:#fef2f2}p{margin:0 0 6px}.tech{color:#555;font-size:12px}ol{margin:0;padding-left:18px}
.sev{display:inline-block;margin-left:6px;padding:1px 7px;border-radius:10px;font-size:11px;color:#fff}.high{background:#dc2626}.medium{background:#f59e0b}.low{background:#6b7280}
.meta{color:#555;font-size:12px;margin-top:4px}"""

REQUIRED = ["id", "title", "severity", "what_is_wrong", "why_it_is_a_bug", "steps", "should_happen", "actually_happens"]


def row(b):
    missing = [k for k in REQUIRED if not b.get(k)]
    if missing:
        sys.exit(f"bug {b.get('id')}: missing {missing}")
    if b["severity"] not in ("high", "medium", "low"):
        sys.exit(f"bug {b['id']}: severity must be high, medium or low")
    video = (f'<video controls preload="metadata" src="{e(b["video"])}"></video>' if b.get("video")
             else '<div class="soon">No video yet</div>')
    meta = " · ".join(x for x in [b.get("case_id"), b.get("browser"), b.get("size"), b.get("tries")] if x)
    expl = (f'<p><b>What is wrong:</b> {e(b["what_is_wrong"])}</p>'
            f'<p><b>Why it is a bug:</b> {e(b["why_it_is_a_bug"])}</p>')
    if b.get("technical_detail"):
        expl += f'<p class=tech><b>Technical detail:</b> {e(b["technical_detail"])}</p>'
    steps = "".join(f"<li>{e(s)}</li>" for s in b["steps"])
    return (f'<tr id="bug-{b["id"]}"><td class="n">{b["id"]}</td>'
            f'<td><b>{e(b["title"])}</b><span class="sev {b["severity"]}">{b["severity"]}</span>'
            + (f'<div class="meta">{e(meta)}</div>' if meta else "") + '</td>'
            f'<td class="v">{video}</td><td>{expl}</td><td><ol>{steps}</ol></td>'
            f'<td class="ok">{e(b["should_happen"])}</td><td class="bad">{e(b["actually_happens"])}</td></tr>')


def main(src, out, title):
    bugs = json.load(open(src))
    with_video = sum(1 for b in bugs if b.get("video"))
    html = (f'<!doctype html><html><head><meta charset="utf-8"><title>{e(title)}</title><style>{STYLE}</style></head><body>'
            f'<h1>{e(title)}</h1><p>{len(bugs)} bugs. Videos ready: {with_video}/{len(bugs)}. '
            'Each video has red highlights and a spoken explanation. Green = what should happen, red = what happens now.</p>'
            '<table><tr><th>#</th><th>Bug</th><th>Video</th><th>Explanation</th><th>Steps to recreate</th>'
            '<th>Should happen</th><th>Actually happens</th></tr>'
            + "".join(row(b) for b in bugs) + '</table></body></html>')
    open(out, "w").write(html)
    print(f"wrote {out}: {len(bugs)} bugs")


if __name__ == "__main__":
    main(*sys.argv[1:4])

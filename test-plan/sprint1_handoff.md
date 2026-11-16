# Cone Sprint 1 — session handoff (v3, 16 Nov 2026)

> Use ONLY this file and `sprint1_deep_testplan.md` v3. Ignore any older copy of either file.

## Goal
Exhaustive end-to-end testing of Cone's **Work & Tasks area and client requests** (app.getcone.io + portal.getcone.io) for Pavi (pavi@getcone.io). Chrome first, then Firefox and Brave, then Safari on a real Mac (macOS child session — never Linux "Safari"/WebKit emulation).

### Scope
- IN: Work (Projects, Tasks, Recurring projects, Project templates, time tracking on tasks and the project Time tracking tab; search/filter/sort/group/columns on every list; every text field's limits and special characters; description editor incl. pasted screenshots), client requests (all 5 types), client Files/folders and contacts as used by requests, email templates, the client portal, notifications about requests.
- OUT of Sprint 1 (do not test, do not log): Proposals, Services, Finances/invoices, Reporting, Dashboard, Get started, team members/assigning (Sprint 2), sign-up/login/password-reset flows.

### Screen sizes — laptops and desktops ONLY
Test at exactly these 6 window sizes: **1280×800, 1366×768, 1440×900, 1536×864, 1920×1080, 2560×1440**.
NEVER test phone or tablet sizes (no 390px, no 768px, no device emulation) — Pavi's rule.
Every browser: run every case at 1366×768 (the reference size). Then Section 9: **every screen, tab, dialog, drawer, menu and portal page** from the screen inventory checked visually at all 6 sizes, plus **all request flows end to end at 1280×800 and at 2560×1440**.

## Access
- App: https://app.getcone.io — logged in on the VM's Chrome as **pavi+nov18@getcone.io** (14-day trial). Login needs a human once (captcha) — ask the user to sign in on the VM screen.
- Public results site: https://othaapavi.github.io/cone-bug-videos/ (repo Othaapavi/cone-bug-videos, main, GitHub Pages from root; clone on VM at ~/cone-bug-videos)
- Results page: https://othaapavi.github.io/cone-bug-videos/sprint1.html — **107 rows logged already**
- Throwaway inboxes (maildrop.cc): cone-s1-clienta@, cone-s1-clientb@, cone-s1-clienta2@
- WHY fixed inbox names: the agent must read the client's emails itself (request email arrived? 6-digit portal login code?). Maildrop inboxes need no password, so any agent can open them.
- WARNING: maildrop inboxes are PUBLIC — anyone who knows the name can read them and use the login code. Use them ONLY for test clients; never put a real client's email or real documents on them.

## Test data already in the account (S1/S2-prefixed only)
- Clients: "S1 Chrome client A" (contact cone-s1-clienta@maildrop.cc), "S1 Chrome client B" (cone-s1-clientb@)
- Project "S1 alpha one-time" (id 6abeb29f-d680-408a-8d10-a5ae7fd9fc1f), plus various S1 tasks/requests
- Rule: only create/edit/delete S1-, S2- or browser-prefixed test records (see below) — this is a LIVE product.
- Also existing from the earlier Chrome run (read-only reference, do NOT reuse for new tests): client "Windows Chrome test client 1" (cone-winchrome-c1@maildrop.cc), project "Windows Chrome one-time project 1".

### One set of test data PER BROWSER (so runs never mix)
Each browser run creates its own clients, contacts, inboxes and projects. Chrome Sprint 1 keeps the existing S1/S2 names. Other browsers use:

| Browser | Client A | Contact A inbox | Contact A2 inbox | Client B | Client B inbox | Name prefix |
|---|---|---|---|---|---|---|
| Firefox | S2 Firefox client A | cone-s2-firefox-a@maildrop.cc | cone-s2-firefox-a2@maildrop.cc | S2 Firefox client B | cone-s2-firefox-b@maildrop.cc | `S2 FF` |
| Brave | S2 Brave client A | cone-s2-brave-a@maildrop.cc | cone-s2-brave-a2@maildrop.cc | S2 Brave client B | cone-s2-brave-b@maildrop.cc | `S2 BR` |
| Safari (Mac) | S2 Safari client A | cone-s2-safari-a@maildrop.cc | cone-s2-safari-a2@maildrop.cc | S2 Safari client B | cone-s2-safari-b@maildrop.cc | `S2 SF` |

Every project/task/request/template/folder an agent creates starts with that prefix (e.g. "S2 FF one-time").

## HOW CONE WORKS (domain knowledge for any agent)

### Navigation
- Left sidebar: Get started / Dashboard / Clients hub / Inbox / **Work** (Projects, Tasks, Recurring projects, Time entries) / Proposals / Services / Finances / Reporting / Templates / Messages
- Work → Projects = all projects list (List↔Board toggle, Group by, Add filter, Search, Export, Create Project button top-right)
- Project detail page tabs: **Tasks | Time tracking | Settings**; header has Start timer + ⋮ menu (Edit project / Duplicate / Delete project)
- Work → Tasks ("my-tasks") = all tasks across projects
- Work → Recurring = recurring schedules list
- Clients hub → client workspace shows that client's projects, contacts, files

### Creating a project
- Create Project → 3-step dialog (Basic details / Advanced / Custom fields). Basic: title, description, "Use project template" link, Clients* (checkbox dropdown with search), Project owner*, Project type (One-time | Recurring), Start date*, Due date* (both REQUIRED — no-dates projects can't be created). Advanced: billing (fixed/hourly, price required if billable), budgets. Recurring type adds frequency (daily/weekly/monthly/yearly/custom interval), end option (never/date/count), "create in advance".
- Editing an Ended project silently flips it back to In progress; there is NO reopen button.

### Tasks
- Two create paths: **"Create task"** button (full drawer) and inline **"+ Create task"** row at the bottom of each section
- Task drawer: name, description, checklist (add/tick/reorder/delete), due date, priority, assignee, status, timer, ⋮ menu (Copy task link etc.)
- Task rows show in sections under "Group by: Section"; requests appear as task rows too (person icon vs circle icon)
- Status lists are configurable per project (Settings tab → Task status list); custom lists can be created
- Deleting a task = permanent, no trash. Same generic "Are you sure you want to delete this item?" confirm for sections and projects

### Client requests — the send flow
- Inside a project's Tasks tab → Create task dropdown → request types, OR the request create flow offers: **Upload documents, Fill a form, E-sign, Share documents, Ask a question**
- Send form fields: title, description, checklist items, request type config (e.g. upload folder target — REQUIRED or send fails), recipient contact, due date, **email delivery (send now / schedule later / no email / draft)**, **email template (default or custom)**, **reminders (off/default/custom count+interval)**
- After send: request is LOCKED (title/desc/recipient/email settings can't be edited); there is no Delete on a sent request; statuses include sent/opened/completed/reopened; "Resend request via email" exists in the Share panel
- Client emails come from team@notifications.getcone.io with a "Go to client request" button → portal.getcone.io link
- Portal requires the client to enter their email first (email-entry gate), then OTP/code — old links show the gate, not the request
- Request copy: portal.getcone.io/app/tasks/<uuid>; app deep links: app.getcone.io/pm/work/projects/details/<id>/tasks and /pm/work/projects/task/<uuid>

### Email templates & reminders
- Custom email templates live under **Templates → Email** in the left sidebar (and can be picked in the send flow via "Customize email"); they support placeholders (client name, contact first name, firm, request title, request type, due date, sender, assignee)
- Reminders can be off / default / custom (count + interval); should stop once the client completes. Default first reminder is sent **7 days before the due date**.
- Waiting: never sit idle for days. To make reminders fire within the session, set the request due date so the reminder time is a few minutes/hours away (or use a custom reminder with the shortest interval). For recurring projects use the **daily** frequency. Schedule-for-later: schedule 10–15 min ahead. If something still has not happened by the end of the section, log the row as `Pending — recheck at <time IST>` and recheck before the run ends. Typical email arrival is 3–10 s; treat >2 min as "Delayed" and >20 min as "Not received".
- Verifying emails: maildrop.cc public inboxes — cone-s1-clienta@maildrop.cc, cone-s1-clientb@, cone-s1-clienta2@ (open https://maildrop.cc/inbox/?mailbox=<name> and Refresh)

### Completion rule (Pavi's rule — applies to EVERY request)
A client submitting / marking done is NOT the end. After every client submit, the firm must: open the task → Status → **Completed** → Save. Only then check project progress. Never log progress counts as a bug before doing this.

### Firm-wide settings (they are NOT test data)
Firm defaults (default email template, default reminders, branding, notification preferences) affect real clients and have no S1/S2 prefix. Before changing one: write down the original value in the row notes, change it, test, then **restore it immediately** and confirm it is restored. If restoring is not possible, do not change it — log the row as `Skipped (firm-wide)`.

### Recording tooling (verified on this VM)
- Red click-highlights: inject `*:hover{outline:3px solid #ff0000 !important;outline-offset:2px !important}` via CDP (http://localhost:29229/json to find target id; websocket-client needs `suppress_origin=True`; reinject on navigation via Page.addScriptToEvaluateOnNewDocument). NEVER open DevTools (F12 blanks the page)
- Voiceover: gTTS(text, lang="en", tld="co.uk") → ffmpeg `-i v.mp4 -i a.mp3 -c:v copy -af apad -c:a aac -shortest -movflags +faststart`
- Use the recording_start/annotate_recording/recording_stop tools for annotated videos

## Rules (user's, verbatim)
- Every case goes in the bug sheet as a row (Pass or Fail)
  **Two tries before any verdict (Pavi's rule).**
  - A case that **fails**: try it a 2nd time from scratch (fresh request/task, reload the page, same steps). Fails both times → `Fail (2/2)` = confirmed bug. Fails once, passes once → `Not reproduced (1/2)`, both tries described in Notes.
  - A case that **can't be done** (button missing, page error, email not arrived, login problem): try a 2nd time after a reload, or 10 min later for emails. Still impossible → `Blocked (2/2)` + the reason. Never mark Pass, Fail or Skipped after one try.
  - Known bugs (Section 10): same rule. `Still happens` needs 2 of 2; `Fixed` needs 2 passes.
  
  **Videos (Pavi's rule): every `Fail (2/2)`, every `Not reproduced (1/2)` and every `Blocked (2/2)` gets its own video, with red highlights and a spoken voiceover. No exceptions.**
  - As soon as a case fails or is blocked the first time, take a screenshot, then **start recording before the 2nd try**, so the 2nd try is always on video.
  - Fail (2/2): the video shows the bug. Not reproduced (1/2): the video shows the 2nd try; the voiceover says what went wrong the 1st time (show the 1st-try screenshot in the video) and that it didn't happen again. Blocked (2/2): the video shows what stops the test.
  - Each one goes on the browser's bug page (`bugs-<browser>.json`) with `tries` set to `Fail (2/2)`, `Not reproduced (1/2)` or `Blocked (2/2)`.

## What's DONE
- Sheet: /home/ubuntu/sprint1_results.md → 107 rows (69 pass, 5 confirmed bugs, ~33 partial/untested), built to sprint1.html by /home/ubuntu/build_sprint1.py
- Confirmed bugs (re-recorded w/ voiceover+highlights): due-before-start saves; section delete silently deletes tasks; task drawer discards unsaved edits; "Add filter" button dead on Work → Tasks; deleted-project URL renders phantom page
- Retested-and-fixed: project search row-filtering, my-tasks search input, inline create, copy task link (now copies a portal URL — noted)

- Earlier Chrome run (client "Windows Chrome test client 1"): 22 bugs on https://othaapavi.github.io/cone-bug-videos/ (19 reproduced with videos; #13, #19, #20 did NOT reproduce), plus 3 newer findings (scheduled email never sent, scheduled banner one day early, draft-send email ~5 min late). These are **known bugs**: retest them in test plan Section 10 and update the existing row — do not log them as new bugs.

## What REMAINS (the deep matrix — file sprint1_deep_matrix.md)
Create P1 "S2 one-time no-template" + P2 "S2 recurring no-template", internal tasks + client requests in each, run blocks A/B/C:
- A: internal-task combos (content, checklist, priority, due dates, statuses incl. custom lists, drawer, links, recurring-copy behavior, task chat)
- B: client-request combos × 5 types (send now/schedule/no-email/draft; default/custom/new email templates; reminders off/default/custom + stop-after-complete; due dates incl. past + change-after-send; folders; second contact; portal-side submit/chat/uploads/e-sign/forms)
- C: project-level (statuses, sections, views, filters, recurring schedule edit/stop, notifications, deleted-item links)
- Plus Section 11 (combinations added in v3), Section 9 (6 screen sizes) and Section 10 (known-bug retests)
- Sections 0B and 12–18 (added in v3): screen inventory first, then text-field limits/emoji/symbols, search/filter/sort, statuses, description editor + screenshots, project templates, time tracking, browser behaviour and dates
- Every request row is repeated for each request type it applies to ("Runs for" column) — ≈2 380 result rows in Chrome, ≈2 080 in each other browser
- After Chrome: same plan in Firefox/Brave, then Safari on Mac, each with its own test data (table above); then a playbook with Sprint 2 (team members/assigning) listed separately

## Bug report format (Pavi's format — every confirmed bug, every browser)

Each browser has its own bug file in the repo: `bugs-chrome.json`, `bugs-firefox.json`, `bugs-brave.json`, `bugs-safari.json`. Add one entry per `Fail (2/2)`, `Not reproduced (1/2)` and `Blocked (2/2)` result, then build its page:
`python3 build_bug_page.py bugs-chrome.json bugs-chrome.html "Cone bug list — Chrome"` and link that page from `index.html` (one line under the heading). Do not change the existing 22 rows on `index.html`.

The page shows the same columns as https://othaapavi.github.io/cone-bug-videos/: **# · Bug (title + severity) · Video · Explanation · Steps to recreate · Should happen · Actually happens**.

How to write each field (plain words; the readers are Pavi's team, not developers):
- **title**: what breaks, in under 10 words ("Sidebar links go to the wrong page").
- **severity**: `high` = client or firm can't finish a task, data is lost or wrong data reaches the client · `medium` = feature works wrongly but there is a workaround · `low` = looks wrong / wording only.
- **what_is_wrong**: 1–2 sentences, no jargon.
- **why_it_is_a_bug**: what a real user would run into because of it.
- **technical_detail** (optional): one sentence for developers (URL, element, message).
- **steps**: numbered, starting from "Log in to Cone." Exact button names, the test data used, what to look at. Someone who has never seen Cone must be able to follow them.
- **should_happen** / **actually_happens**: one sentence each.
- **case_id**, **browser**, **size**, **tries** (`Fail (2/2)`), **video** (`<browser>-NN-short-name.mp4`, e.g. `chrome-23-status-filter-empty.mp4`).
- A bug already on the existing page (Section 10) is not added again — note "Still happens in <browser>" in that browser's CSV instead.

Sample entry (this is bug 1 from the existing page):
```json
[
 {
  "id": 1,
  "title": "Sidebar links go to the wrong page",
  "severity": "medium",
  "case_id": "N.2",
  "browser": "Chrome",
  "size": "1366×768",
  "tries": "Fail (2/2)",
  "what_is_wrong": "The menu on the left has links like Projects and Dashboard. Their web addresses are built wrong.",
  "why_it_is_a_bug": "If you right-click a menu link and choose 'Open link in new tab', you land on a wrong or broken page instead of the page you clicked.",
  "technical_detail": "Sidebar uses relative links (href='./work/projects'), so they change depending on the current page.",
  "steps": [
   "Log in to Cone.",
   "Click Work > Projects.",
   "Hover the mouse over 'Projects' in the left menu and look at the address in the bottom-left corner of the browser: it shows /pm/work/work/projects (the word 'work' twice).",
   "Hover 'Dashboard': it shows /pm/work/dashboard.",
   "Open a project, hover 'Tasks': it points inside the project (/pm/work/projects/details/<id>/my-tasks).",
   "Right-click 'Projects' > Open link in new tab."
  ],
  "should_happen": "Each link opens its own page, also in a new tab.",
  "actually_happens": "The new tab opens a wrong or empty/404 page.",
  "video": "bug-01-sidebar-link-targets.mp4"
 }
]
```
Rendered, it looks like the attached `bugs-sample.png`.

## Workflow
0. Results live in the public repo only: `git clone https://github.com/Othaapavi/cone-bug-videos ~/cone-bug-videos`. `sprint1.csv` there is the bug sheet (`#,Section,Test case,Result,What happened / notes,Video`; rows 1–107 exist, next # = 108). There is no build script or results file outside the repo — if `sprint1.html` needs rebuilding from the CSV, write a small script and commit it to the repo (`build_sprint1.py`).
1. Test each case in the current browser; append one CSV row per result row (case ID + type/size suffix in "Test case", e.g. `R.5-ES`; Browser and Size in Notes when not Chrome 1366×768).
2. After each section: rebuild `sprint1.html`, `git add -A && git commit -m "Sprint 1 <section>: <n> rows" && git push`, then report the section to Pavi (pass/fail counts + new bugs).
3. Videos (every `Fail (2/2)`, `Not reproduced (1/2)` and `Blocked (2/2)` — record the 2nd try): annotated screen recording, red-highlight CSS via CDP (target id from `http://localhost:29229/json`), gTTS voiceover merged with ffmpeg, saved in the repo with the name in the bug entry. Then add the bug to `bugs-<browser>.json` in the format above and rebuild the page.
4. Never commit cookies, browser state, passwords or tokens.

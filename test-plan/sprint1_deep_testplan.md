# Cone Sprint 1 — DEEP TEST PLAN (v3, 16 Nov 2026)

> Use ONLY this version. Read `sprint1_handoff.md` v3 first (scope, screen sizes, per-browser test data, completion rule, firm-wide settings rule).

Everything below runs on app.getcone.io as pavi+nov18@getcone.io — Chrome first, then Firefox, Brave and Safari (Mac) with their own test data, at 1366×768 unless a row says otherwise; Section 9 covers the other laptop/desktop sizes. No phone or tablet sizes. Every numbered case becomes ONE row in the bug sheet (Pass / Fail + what happened). A video is recorded only when a bug reproduces twice, with voiceover + red highlights. Only "S2"-prefixed (or browser-prefixed, e.g. "S2 FF") test data is created — nothing real is touched.

**Repeat for every request type (Pavi's rule).** Any row about client requests is run once for EACH type it applies to and logged as one row per type, e.g. `R.5-UP`, `R.5-FM`, `R.5-ES`, `R.5-SD`, `R.5-AQ`.
- Sections 4, 5 and 11: the **Runs for** column lists the types. `UP FM ES SD AQ` = all 5.
- Other sections: rows marked "(run for UP FM ES SD AQ)" run for all 5; every other row runs once.
- If an option does not exist for a type (e.g. no folder picker on forms), still log the row as `N/A — <one-line reason>`. That takes seconds and proves it was checked.

**After every client submit:** firm opens the task → Status → Completed → Save, then checks progress (handoff "Completion rule").

**Results words:** Pass / Fail (2/2) / Not reproduced (1/2) / Blocked (2/2) / Delayed / Pending — recheck at <time> / N/A (reason) / Skipped (reason).

**Two tries before any verdict (Pavi's rule).**
- A case that **fails**: try it a 2nd time from scratch (fresh request/task, reload the page, same steps). Fails both times → `Fail (2/2)` = confirmed bug. Fails once, passes once → `Not reproduced (1/2)`, both tries described in Notes.
- A case that **can't be done** (button missing, page error, email not arrived, login problem): try a 2nd time after a reload, or 10 min later for emails. Still impossible → `Blocked (2/2)` + the reason. Never mark Pass, Fail or Skipped after one try.
- Known bugs (Section 10): same rule. `Still happens` needs 2 of 2; `Fixed` needs 2 passes.

**Videos (Pavi's rule): every `Fail (2/2)`, every `Not reproduced (1/2)` and every `Blocked (2/2)` gets its own video, with red highlights and a spoken voiceover. No exceptions.**
- As soon as a case fails or is blocked the first time, take a screenshot, then **start recording before the 2nd try**, so the 2nd try is always on video.
- Fail (2/2): the video shows the bug. Not reproduced (1/2): the video shows the 2nd try; the voiceover says what went wrong the 1st time (show the 1st-try screenshot in the video) and that it didn't happen again. Blocked (2/2): the video shows what stops the test.
- Each one goes on the browser's bug page (`bugs-<browser>.json`) with `tries` set to `Fail (2/2)`, `Not reproduced (1/2)` or `Blocked (2/2)`.

---

## SECTION 0 — Test setup (do once)

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| S0.1 | Second contact on client A | Add contact "S2 contact two" (cone-s1-clienta2@maildrop.cc) to "S1 Chrome client A" | Contact saves; client now has 2 contacts |
| S0.2 | Upload folder exists | Confirm "Client Uploads" folder exists for request file targets | Present |
| S0.3 | Custom email template | Create email template "S2 custom email" with custom subject/body + tokens | Saves, usable in requests |
| S0.4 | Custom task status list | Create status list "S2 statuses" (e.g. New → Doing → Review → Done) | Saves, assignable to a project |

## SECTION 1 — The two projects (no template)

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| P.1 | One-time project no-template | Create "S2 one-time" on client A, owner Pavithran, one-time, start Nov 16 / due Nov 30, default statuses | Created, appears in list + board |
| P.2 | Recurring project no-template | Create "S2 recurring" on client B, **daily** (so copies appear within the run), start today, end after 3 occurrences | Schedule saves; first copy generates |
| P.3 | Project with NO description | P1 created without description | Allowed, blank shown gracefully |
| P.4 | Required-field blocks | Try saving with no client / no start / no due | Validation errors, no save |
| P.5 | Due before start (known bug 9) | Try due Nov 10 < start Nov 16 | Re-check: still saves silently? |
| P.6 | Past dates | Start + due both in the past | Accepted or flagged? |
| P.7 | Long/special name | Rename P1 to 200-char name with émojis & symbols | Renders everywhere, no truncation break |
| P.8 | Every project status | Set P1 through each status (In progress → On hold → Ended → …) | List/board/header update; ended blocks timers |
| P.9 | Reopen ended project | After Ended, try to reopen | Is there a path back? |
| P.10 | Client workspace view | Open client A workspace — is P1 listed there too | Yes, same project visible |
| P.11 | Settings tab | Change P1's client, owner, task status list (to S2 statuses) | Each change persists after reload |
| P.12 | Custom status list on tasks | New tasks in P1 get the custom statuses | Columns/status pickers show S2 statuses |
| P.13 | Delete status holding tasks | Delete a custom status that still has tasks | Warning? tasks orphaned? |
| P.14 | Duplicate project | ⋮ → Duplicate P1 | Copy appears with tasks/requests? |
| P.15 | Archive vs delete | Archive project → hidden from list? findable? then delete | Archive ≠ delete semantics |
| P.16 | Deleted project URL | Re-test phantom page on S2 project | 404/redirect expected (bug 77 retest) |

## SECTION 2 — Sections inside a project

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| SC.1 | Add/rename/reorder sections | 3 sections in P1; rename; drag reorder | All persist after reload |
| SC.2 | Delete EMPTY section | Delete a section with no tasks | Clean delete |
| SC.3 | Delete section WITH tasks (bug 17 retest) | Delete section holding 2 tasks | Should warn/move — check current behavior |
| SC.4 | Move task between sections | Drag task Default → Section B | Moves, persists |
| SC.5 | Task created inside a section | Create task directly in Section B | Lands in that section |
| SC.6 | Empty section in Board view | Board with an empty column | Renders, droppable |
| SC.7 | Collapse/expand sections | Collapse all, reload | Persisted or reset? |

## SECTION 3 — Internal tasks (in P1; recurring-specific items in P2 copy)

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| T.1 | Create via "Create task" | Bare name only | Created, minimal fields |
| T.2 | Create via inline + row | Name in row, save | Created in that section |
| T.3 | Full-detail task | Desc + 5 checklist + due + High + assigned | All saved, shown on card |
| T.4 | Long description | 3000 chars + pasted formatted text + links | Saves, renders, no break |
| T.5 | Emoji/symbols in name | "S2 task 🚀 <b>&amp;" | Renders as text, no injection |
| T.6 | Checklist add/tick/untick | Add 4, tick 2, untick 1 | Counts persist |
| T.7 | Checklist reorder/delete | Drag reorder, delete item, add empty item | Order kept; empty item handled |
| T.8 | All checklist ticked | SKIP — Pavi's rule "skip checklist-completion verification". Log as `Skipped (rule)` | — |
| T.9 | Priority cycle | none→Low→Med→High→none | Badge updates on card |
| T.10 | Due: none | No due date | No due shown |
| T.11 | Due: today | Today | "Today" chip |
| T.12 | Due: past | Yesterday | Overdue styling (red) |
| T.13 | Due: future | +10 days | Shown correctly |
| T.14 | Change due after create | Future → past → cleared | Updates everywhere incl. project list |
| T.15 | Status walk | Every status incl. custom-list statuses | Transitions persist, board moves card |
| T.16 | Complete → reopen | Mark complete, then reopen | Both ways work, counts update |
| T.17 | Delete task | Delete, check everywhere | Gone; any trash/restore? |
| T.18 | Drawer unsaved-close (bug 30 retest) | Edit name, click X / outside / Esc | Warning expected; currently discards |
| T.19 | Two tabs same task | Edit in tab 1 + tab 2 | Last-save-wins or conflict warning? |
| T.20 | Copy task link | ⋮ → Copy task link → paste | Gets correct app URL (retest bug 43) |
| T.21 | Deep link to task | Paste task URL fresh | Drawer opens on that task |
| T.22 | Unassigned task | Create with no assignee | Allowed, shows unassigned |
| T.23 | Task timer from drawer | Start/stop timer on task | Time logs to entry |
| T.24 | Task chat/comments | Post a comment on internal task | Saved; who gets notified? |
| T.25 | Task in ended project | Add task while project Ended | Blocked or allowed? |
| T.26 | 20+ tasks in project | Bulk-create 20 | List/board performance + grouping |

## SECTION 4 — Client requests: THE BIG MATRIX

Types: **UP**=upload, **FM**=form, **ES**=e-sign, **SD**=share docs, **AQ**=ask question. The **Runs for** column says exactly which types each row is run for (one result row per type). The type named in "What I do" is only the first one to try.

### 4A — Content combos
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.1 | Description only | Send AQ with description, no checklist | Sends; portal shows desc | UP FM ES SD AQ |
| R.2 | Checklist only | Send AQ with 3 checklist items, no desc | Sends; portal shows items | UP FM ES SD AQ |
| R.3 | Both | Desc + checklist | Both shown | UP FM ES SD AQ |
| R.4 | Neither (empty) | Send with nothing | Allowed? What does client see? | UP FM ES SD AQ |

### 4B — Email delivery modes
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.5 | Send now, email ON | UP, send now | Email lands in maildrop ≤2 min | UP FM ES SD AQ |
| R.6 | Schedule for later | SD, schedule +15 min | No email now; fires at time; banner shows right date/time | UP FM ES SD AQ |
| R.7 | Send WITHOUT email | FM with email OFF | No email sent; request exists; document how client reaches it (portal link?) | UP FM ES SD AQ |
| R.8 | Send without email → does reminder fire? | R.7 with default reminders ON | Reminder emails even though send was skipped? | UP FM ES SD AQ |
| R.9 | Draft → send later | Save draft, come back, send | Draft persisted; send works | UP FM ES SD AQ |
| R.10 | Scheduled → edit before send | Edit title/desc of scheduled request | Does scheduled email use old or new content? | UP FM ES SD AQ |
| R.11 | Scheduled → delete before send | Delete scheduled request | Email must NOT fire | UP FM ES SD AQ |

### 4C — Email templates
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.12 | Default template | Send with default | Email has default wording | UP FM ES SD AQ |
| R.13 | Custom template | Send using S2 custom email | Email has custom subject/body, tokens rendered (client name, firm, dates) | UP FM ES SD AQ |
| R.14 | Brand-new template | Create template DURING send flow | Usable immediately | UP FM ES SD AQ |
| R.15 | Edit custom template before send | Edit template, send another | New content used | UP FM ES SD AQ |
| R.16 | Template tokens | Verify every token renders (no raw {{var}}) | No unresolved placeholders | UP FM ES SD AQ |

### 4D — Reminders
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.17 | Reminders OFF | Send, wait — no reminders | Nothing extra arrives | UP FM ES SD AQ |
| R.18 | Default reminders ON | Send with defaults, due date set so the first reminder (7 days before due) falls a few minutes from now — or log the scheduled reminder time and recheck | Reminder email on schedule | UP FM ES SD AQ |
| R.19 | Custom reminders | 2 reminders, shortest custom interval | Both fire at right times (log `Pending — recheck at <time>` if not due yet) | UP FM ES SD AQ |
| R.20 | Reminder CONTENT | Check reminder email text/links | Correct request, working link | UP FM ES SD AQ |
| R.21 | Reminders stop after complete | Client completes; wait past next reminder | No more reminders | UP FM ES SD AQ |
| R.22 | Reminder before vs after due | Set reminder relative to due | Fires in correct direction | UP FM ES SD AQ |

### 4E — Due dates on requests
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.23 | No due date | Send undated | Allowed; portal shows no due | UP FM ES SD AQ |
| R.24 | Due today / future / past | Three requests | Displayed correctly; past = overdue badge? | UP FM ES SD AQ |
| R.25 | Change due AFTER send | Edit due (if editable) | Portal reflects change; notification? | UP FM ES SD AQ |
| R.26 | Due before project start | Request due < project start | Allowed or warned? | UP FM ES SD AQ |
| R.27 | Timezone check | Due shown to client in their tz | Consistent dates | UP FM ES SD AQ |

### 4F — Folders & recipients
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.28 | Existing folder | UP into Client Uploads | Uploads land there | UP FM ES SD AQ |
| R.29 | New folder during send | Create "S2 folder" in send flow | Created + used | UP FM ES SD AQ |
| R.30 | Primary contact | Send to contact 1 | Email to clienta inbox only | UP FM ES SD AQ |
| R.31 | SECOND contact | Send to S2 contact two | Email to clienta2 inbox ONLY — not contact 1 (the case you asked about) | UP FM ES SD AQ |
| R.32 | Second contact portal | Open clienta2 email link | Portal shows only contact-2 requests or all client requests? | UP FM ES SD AQ |
| R.33 | Both contacts | If multi-select exists, send to both | Both get emails, one shared request or two? | UP FM ES SD AQ |
| R.34 | Client with NO contacts | Try request on contactless client | Blocked with clear error | UP FM ES SD AQ |

### 4G — After send (lifecycle)
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.35 | Edit sent request | Try editing title/desc/recipient | Locked? (previously locked — retest) | UP FM ES SD AQ |
| R.36 | Reopen completed | Complete → reopen | Status returns; client re-notified? | UP FM ES SD AQ |
| R.37 | Mark incomplete | On completed request | Allowed? | UP FM ES SD AQ |
| R.38 | Delete sent request | Look for delete | Exists now? Was missing before | UP FM ES SD AQ |
| R.39 | Old email link after complete | Click old portal link | Shows completed state or dies cleanly | UP FM ES SD AQ |
| R.40 | Old email link after delete | Same after deletion | Clean 404, no phantom | UP FM ES SD AQ |
| R.41 | Resend email | "Resend request via email" | Fresh email arrives (earlier test: worked ~2 min) | UP FM ES SD AQ |
| R.42 | Request statuses | Walk every status | Status set by firm vs client correctly | UP FM ES SD AQ |

### 4H — Portal side (as the client)
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.43 | Open-but-don't-submit, return later | Open link, close, reopen | Progress saved? same link works | UP FM ES SD AQ |
| R.44 | Double-click Submit | Submit twice fast | No duplicate submission | UP FM ES SD AQ |
| R.45 | Two tabs same request | Open in 2 tabs, submit in 1 | Other tab handles gracefully | UP FM ES SD AQ |
| R.46 | Client marks done ≠ complete | Client submits → firm opens task → Status → Completed → Save → check progress | Progress counts only after firm sets Completed (by design, not a bug) | UP FM ES SD AQ |
| R.47 | Task chat client→firm | Client posts message in portal chat | Firm sees it + notification email | UP FM ES SD AQ |
| R.48 | Task chat firm→client | Firm replies in Cone | Client sees it + notified; unread counts both sides | UP FM ES SD AQ |
| R.49 | Chat attachments | Attach file in chat | Delivered both directions | UP FM ES SD AQ |
| R.50 | Chat on internal task | Does internal task have client-visible chat? | Must NOT leak to portal | once (UP) |

### 4I — Upload-specific
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.51 | Over 50 MB | Upload 60 MB file | Blocked with clear error | UP FM SD |
| R.52 | Wrong file type | Upload .exe/.zip if restricted | Blocked or accepted — document | UP FM SD |
| R.53 | 0 KB file | Empty file | Rejected or handled | UP FM SD |
| R.54 | Many files | 10 files at once | All upload, progress correct | UP FM SD |
| R.55 | Same filename twice | Upload name.txt twice | Renamed/dupe-handled | UP FM SD |
| R.56 | Special chars in filename | "répört (final) v2.pdf" | Saved correctly | UP FM SD |
| R.57 | Cancel mid-upload | Cancel at 50% | Clean abort, no ghost file | UP FM SD |
| R.58 | Refresh mid-upload | Reload page | State recovers or clear error | UP FM SD |

### 4J — Form-specific
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.59 | Every question type | Form with text/long/number/date/email/phone/dropdown/checkbox/file | All render + submit | FM |
| R.60 | Invalid email/phone | Bad formats | Field validation errors | FM |
| R.61 | Required skip | Submit with required empty | Blocked | FM |
| R.62 | Secure fields | Masked answers | Masked in firm view too? | FM |
| R.63 | Edit form template after send | Change template post-send | Sent copy keeps original questions | FM |
| R.64 | Client edits after submit | Reopen answer | Allowed? versioned? | FM |

### 4K — Forms in depth (all FM; "if it exists" = check first, log `N/A — not offered` if Cone has no such option)

Seen in the Chrome run: Templates → Form builder (Short answer, Single choice, File upload were used), and in the request drawer a **"Use a form template"** button. Building a form without a template has **not** been tried yet. Take the real list of question types and builder options from the Section 0B inventory.

**A. Getting a form into a request (with and without a template)**
| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| FO.1 | Template used as is | Use a form template → pick → Use template → send | Client gets exactly the template's questions, in order | 1 |
| FO.2 | Template, then changed inside the request (if allowed) | Add / remove / edit a question in the drawer after picking the template | Client sees the changed form; **the template itself is unchanged** | 1 |
| FO.3 | **No template: build the form inside the request** (if it exists) | Add questions directly in the drawer | Works the same as a template form | 1 |
| FO.4 | No template, then "save as template" (if it exists) | — | New template appears in Templates → Form | 1 |
| FO.5 | Change your mind | Pick template A, then switch to B; remove the template before sending | Only B's questions sent / clear empty state | 2 |
| FO.6 | Form with no questions | Try to send | Blocked with a clear message | 1 |
| FO.7 | Same template, same client, twice | Send 2 requests from one template | Two separate forms; answers never mix | 1 |
| FO.8 | Same template, two clients | Client A and B | Each sees only their own answers | 1 |
| FO.9 | Template edited between schedule and send | Schedule a form request, edit the template, wait for send | Write down which version the client gets | 1 |
| FO.10 | Template edited / deleted while a draft or scheduled request uses it | — | No broken request; clear message | 2 |
| FO.11 | Template edited after send (was R.63) | — | Sent form keeps its questions; new requests get the new version | 1 |

**B. Form templates**
| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| FO.12 | Save as draft vs publish | — | Only published templates offered in "Use a form template" (or write down) | 2 |
| FO.13 | Rename, duplicate, delete, unpublish a template in use | — | Requests already sent keep working | 4 |
| FO.14 | Library / global form templates (if they exist) | Clone one | Editable copy | 1 |

**C. Form builder** (one row per question type found in the inventory where it says "× types")
| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| FO.15 | Add each question type | Every type in the builder | Saves; shown right in preview and portal | × types (~10) |
| FO.16 | Required on/off for each type | — | Client blocked only on required ones | × types (~10) |
| FO.17 | Question help text / description / placeholder (if they exist) | — | Shown to client | 1 |
| FO.18 | Reorder (drag), duplicate, delete a question | — | Order kept after save and in the portal | 3 |
| FO.19 | Choice options | Add, remove, reorder, 1 option, 30 options, two options with the same text, empty option, "Other" (if it exists) | Sensible; known bug K.15 ("Option 1") retested | 8 |
| FO.20 | Sections / pages / headings in the form (if they exist) | — | Client moves through them correctly | 1 |
| FO.21 | Show a question only if an earlier answer is X (if it exists) | — | Shows/hides correctly; hidden required question doesn't block | 2 |
| FO.22 | Very short and very long forms | 1 question; 50 questions | 50 still usable at 1280×800 | 2 |
| FO.23 | Preview (if it exists) | — | Same as what the client sees | 1 |
| FO.24 | Leave the builder with unsaved changes | — | Warned, or changes kept | 1 |

**D. Client answering** (in the portal)
| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| FO.25 | Every question type: normal answer, empty, edge values | Text: 1 char, 5 000 chars, emoji, `<b>x</b>` · Number: 0, −5, 3.75, 1e12, letters · Date: past, future, invalid, typed vs picked · Email/phone: bad formats, +91 and international numbers · Choices: change answer, select all/none · Dropdown: keyboard | Saved exactly as typed; bad values refused with clear text | × types × 3 (~30) |
| FO.26 | File question | Several files, 0-byte file, 20 MB, over limit, a type the help text doesn't list, remove and replace before submit | Matches help text; known bugs K.17/K.18 retested | 6 |
| FO.27 | Save and come back | Save half, log out, log in again in another browser | Answers kept | 1 |
| FO.28 | Submit with a required question empty (was R.61) | — | "Incomplete form" with the question pointed out | 1 |
| FO.29 | Double-click Submit | — | One submission | 1 |
| FO.30 | Edit after submit (was R.64) | — | Allowed? Firm sees which version? | 1 |
| FO.31 | Two contacts of one client answer the same form (if a request can go to 2 contacts) | Both open it at the same time | No answer silently lost | 1 |

**E. Firm side after submit**
| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| FO.32 | Answers in Cone | Drawer + View PDF + download | Every type shown correctly (emoji, long text, choices, numbers, dates, file names) | 3 |
| FO.33 | Where the answers PDF and the uploaded files are saved | Client → Files | Write down; uploaded files findable (K.18) | 2 |
| FO.34 | Firm reopens / asks for changes (if it exists) | — | Client sees earlier answers and can change them | 1 |
| FO.35 | Firm notification + email on submit | — | Arrives and names the right form | 1 |
| FO.36 | Form request in a recurring project / project template | Each new copy | New empty form each time; old answers untouched | 2 |
| FO.37 | Firm sets Completed (Pavi's rule) | — | Progress counts it | 1 |

### 4K — E-sign specific
| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| R.65 | Multiple fields+pages | 3 fields across 2 pages | All fill + sign | ES |
| R.66 | Draw vs Upload signature | Both methods | Both accepted | ES |
| R.67 | "My signature" saved sig | Reuse saved signature | Loads + applies | ES |
| R.68 | Use different PDF | Swap the PDF before send | Correct file sent | ES |
| R.69 | Signed PDF output | Open completed signed PDF | Signatures embedded; sane filename | ES |
| R.70 | Decline path | Client declines (if supported) | Firm notified, status correct | ES |

### 4L — CROSS-COMBINATION MATRIX (content × template × reminders × delivery)

Cross every content variant with every email template and reminder setting, on send-now AND no-email deliveries — the exact combos like "description + custom template" you flagged:

| # | Case | Combo | Expected | Runs for |
|---|------|-------|----------|---|
| R.71 | Desc-only + DEFAULT template + reminders OFF + send now | AQ | Email = default wording; no reminders | UP FM ES SD AQ |
| R.72 | Desc-only + CUSTOM template + reminders DEFAULT + send now | AQ | Email = custom subject/body; default reminders fire | UP FM ES SD AQ |
| R.73 | Desc-only + CUSTOM template + reminders CUSTOMIZED + send now | UP | Custom email + custom reminder cadence + both emails correct | UP FM ES SD AQ |
| R.74 | Checklist-only + CUSTOM template + reminders ON + send now | FM | Custom email; portal shows only checklist | UP FM ES SD AQ |
| R.75 | Checklist-only + NO email + reminders ON | AQ | No send email; do reminders still fire? (key edge) | UP FM ES SD AQ |
| R.76 | Both + CUSTOM template + reminders ON + schedule later | ES | Nothing now; custom email at scheduled time + reminders after | UP FM ES SD AQ |
| R.77 | Neither + CUSTOM template + send now | AQ | Empty request + custom email — what does client get? | UP FM ES SD AQ |
| R.78 | Neither + NO email | SD | Request exists silently; reachable only via portal? | UP FM ES SD AQ |
| R.79 | Desc-only + NO email + due in past | UP | Silent request already overdue — badge/due shown? | UP FM ES SD AQ |
| R.80 | Checklist + CUSTOM template + due changed AFTER send | AQ | Portal + any follow-up email reflect new due | UP FM ES SD AQ |
| R.81 | Desc + custom template + second contact | AQ | Custom email lands in clienta2 inbox ONLY | UP FM ES SD AQ |
| R.82 | Both + draft saved → edited → sent with custom template | FM | Draft keeps edits; final email = latest custom template | UP FM ES SD AQ |
| R.83 | Custom template + reminders ON → client completes → reminders stop? | UP | Post-completion reminder must NOT fire | UP FM ES SD AQ |

## SECTION 5 — Requests inside the RECURRING project (P2)

| # | Case | What I do | Expected | Runs for |
|---|------|-----------|----------|---|
| X.1 | Request in recurring copy | AQ with checklist + rel due (+2d) in P2 template | Copy 2 carries request with shifted due | UP FM ES SD AQ |
| X.2 | Email behavior per copy | In copies, are request emails re-sent/scheduled/silent? | Document actual behavior per settings | UP FM ES SD AQ |
| X.3 | Edit recurring setup | Change schedule → banner "future copies only" | Copy 1 unchanged, copy 2 uses new | once |
| X.4 | Stop recurring | Stop mid-series | No more copies; existing copies intact | once |
| X.5 | Task in recurring | Task with rel due in template | Copies get shifted due | once |
| X.6 | Manual edit in copy 1 | Edit copy-1 task; wait for copy 2 | Copy-1 edits don't affect copy 2 | once |

## SECTION 6 — Project surface (list/board/toolbar, both projects)

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| V.1 | List vs Board | Toggle, drag card between status columns | Moves persist, status changes |
| V.2 | Group by | Every grouping option | Regroups correctly |
| V.3 | Add filter (project page) | Field + value + Apply | Works (recently fixed — retest) |
| V.4 | Add filter (Work→Tasks) | Same on my-tasks | Bug: button dead (retest) |
| V.5 | Search rows (project) | Matching + zero-match query | Filters rows (retest bug 12) |
| V.6 | Manage columns | Hide/show/reorder cols | Persists |
| V.7 | Sort | Each sortable column both directions | Correct order |
| V.8 | Mixed types in section | Task + request same section | Both render, reorderable |
| V.9 | Filters on Tasks page | status/due/priority/assignee filters | Correct combined results |
| V.10 | Overdue & Today views | Filter to overdue/today | Right tasks |
| V.11 | Edit here↔project | Edit task on Tasks page → check project (and reverse) | Synced both ways |
| V.12 | Request vs internal on Tasks page | Both listed, distinguishable | Icons/labels correct |

## SECTION 7 — Notifications & misc

| # | Case | What I do | Expected |
|---|------|-----------|----------|
| N.1 | Firm notified on submit (run for UP FM ES SD AQ) | Client submits → firm email/notification | Arrives, correct link |
| N.2 | Unread badges | New client activity → badge counts | Accurate, clears on read |
| N.3 | Email content check (run for UP FM ES SD AQ) | Subject, sender name, firm name, links | All correct, no broken links |
| N.4 | Back/forward with drawer | Drawer open → browser Back | Sane navigation |
| N.5 | Slow network | Throttle → submit task | No duplicate create |
| N.6 | Esc everywhere | Esc on dialogs/menus/drawer | Consistent close behavior |

## SECTION 8 — Every adjacent surface (the deep sweep I missed)

### 8A — Folders & file management + visibility
| # | Case | What I do | Expected |
|---|------|-----------|----------|
| F.1 | Create folder in Files area | New folder outside send flow | Created, empty |
| F.2 | Create folder during send | "S2 folder" in request config | Created + targeted |
| F.3 | Use existing folder | Reuse for next request | Files accumulate there |
| F.4 | Folder visibility: VISIBLE | Set visible → client portal | Client sees folder/contents |
| F.5 | Folder visibility: HIDDEN | Set hidden → check portal | Client sees nothing |
| F.6 | Folder visibility: SHARED | Shared setting semantics | Document who sees it (firm only? specific clients?) |
| F.7 | Upload into hidden folder | Client uploads to request targeting hidden folder | File lands; does client see their own upload after? |
| F.8 | Change visibility after files inside | Visible→hidden with files | Existing files hidden too? |
| F.9 | Visibility per-client | Client A folder — check client B's portal | No cross-client leak (security check) |
| F.10 | Delete folder with files | Delete non-empty folder | Warning? files orphaned/deleted? |
| F.11 | Rename/move folder; move files between folders | Reorg | Persist, files follow |
| F.12 | Download/delete a client-uploaded file | Firm side file actions | Works; does client get notified? |

### 8B — Clients & contacts (feed everything else)
| # | Case | What I do | Expected |
|---|------|-----------|----------|
| C.1 | Add contact to client | 2nd contact with email | Saved, selectable as recipient |
| C.2 | Primary vs secondary contact | Which is default recipient; change primary | Routing follows |
| C.3 | Contact portal access toggle | If per-contact portal access exists: off → send request | Does sending auto-enable or fail? |
| C.4 | Disable portal access mid-request (run for UP FM ES SD AQ) | Client has active request, firm disables | What does client see — blocked? |
| C.5 | Delete contact with active request (run for UP FM ES SD AQ) | Try deleting contact 2 mid-request | Blocked or cascade? |
| C.6 | Client profile edit | Change client name/email → check request emails | New name in emails? old links still work? |
| C.7 | Client with 0 contacts | Project + request on contactless client | Clear error, no silent failure |

### 8C — Portal experience (client side, per request type)
| # | Case | What I do | Expected |
|---|------|-----------|----------|
| PO.1 | Email-entry gate (run for UP FM ES SD AQ) | Old link → enter email → OTP | Lands on the right request only |
| PO.2 | OTP/token expiry | Reuse old code, expired link | Clear expired message, resend path |
| PO.3 | Portal home | After login, does client see ALL their requests or one? | Document scope |
| PO.4 | Portal shows hidden vs visible folders | Same client, both folder types | Only visible items listed |
| PO.5 | Client A vs client B portal isolation | Client A's portal never shows B's data | Hard boundary (security) |
| PO.6 | Portal on the smallest laptop size | Portal at 1280×800: task list, task drawer, Chats, PDF viewer | Nothing cut off, no horizontal scrollbar (no phone sizes — Pavi's rule) |
| PO.7 | Request due dates in portal (run for UP FM ES SD AQ) | Overdue/today/future display | Correct badges |
| PO.8 | Client resubmits edited answer (run for UP FM ES SD AQ) | After reopen | New answer saved, firm sees update |

### 8D — Firm-side settings that change request behavior
| # | Case | What I do | Expected |
|---|------|-----------|----------|
| ST.1 | Default email template setting | Change firm default → send **Firm-wide: record original, restore immediately (handoff rule).** | New default used |
| ST.2 | Default reminder setting | Change firm default → send **Firm-wide: record original, restore immediately.** | New cadence |
| ST.3 | Branding (logo/name) in emails | "Yesss" showed as sender name — check branding **Firm-wide: look only, do not change branding.** | Emails show firm name correctly |
| ST.4 | Custom fields on client/project | Custom fields step in project create — set + verify | Values saved, shown, filterable |
| ST.5 | Notification preferences | Firm's own notification settings **Firm-wide: record original, restore immediately.** | Request events respect them |

### 8E — Inbox / Messages / Notifications surfaces
| # | Case | What I do | Expected |
|---|------|-----------|----------|
| N.7 | Inbox items | Client request events in Inbox | Listed, deep-link works |
| N.8 | Notification center | Badge count ↔ items | Accurate, mark-read works |
| N.9 | Messages area | Any client-request-related messages there | Consistent with portal chat |

## SECTION 9 — Screen sizes (laptop/desktop only)

Sizes: **1280×800, 1366×768, 1440×900, 1536×864, 1920×1080, 2560×1440**. Never phone or tablet sizes. Log as e.g. `SZ.1-INV.12 @1440×900`.

What to look for on every check: text or buttons cut off, horizontal scrollbar, overlapping elements, labels wrapping badly, huge empty areas or content stretched across 2560px, dialogs/drawers/menus not fitting or not scrollable, Save/Send buttons off-screen, tooltips and dropdowns opening off-screen.

| # | Check | What I do | Rows |
|---|-------|-----------|------|
| SZ.1 | **Every screen and state from the Section 0B inventory, at all 6 sizes** | For each inventory item that is a screen, tab, dialog, drawer, dropdown/menu, date picker, toast, empty state, error message or portal page: open it at each size, screenshot, check the list above. Includes every Create project step, task drawer, each request type's drawer and its sub-dialogs (folder picker, Customize email, schedule, reminders, e-sign field placement, form builder), Templates editors, client Files/Chats/Settings, portal Home/Tasks/Chats/Files, PDF viewer, e-sign and form pages, notifications. | inventory items × 6 (≈ 80 × 6 = ~480) |
| SZ.2 | **All request flows end to end at 1280×800** | Repeat R.1–R.5 (create → email → portal → client submits → firm sets Completed) for UP FM ES SD AQ, plus schedule (R.6) and draft (R.9) | 35 |
| SZ.3 | **All request flows end to end at 2560×1440** | Same as SZ.2 | 35 |
| SZ.4 | Long content at 1280×800 and 2560×1440 | 200-char names, 30+ tasks, long descriptions with images (from Sections 12/15) | 2 × ~10 = 20 |
| SZ.5 | Resize while open | Drag the window from 2560 down to 1280 with a drawer/dialog open | ~10 |
| SZ.6 | Emails | Request, reminder and chat emails viewed in maildrop at 1280×800 and 2560×1440 | 6 |

## SECTION 10 — Known bugs: retest (do NOT log as new)

From the earlier Chrome run (https://othaapavi.github.io/cone-bug-videos/). For each: try twice in the current browser (two-tries rule), recording the 2nd try; result = `Still happens` / `Fixed` / `Not reproduced`. Update the existing bug — do not add a new bug row.

| # | Known bug | Quick retest |
|---|-----------|--------------|
| K.1 | Sidebar links point to wrong addresses | Hover Projects / Tasks, read status-bar URL |
| K.2 | Project Custom fields step says "client information" | Create project → step 3 text |
| K.3 | Empty Projects page cut off at ~1270px | See SZ.1 |
| K.4 | Email "Go to client request" opens task list, not the request, when the client must log in first | Logged-out portal → click email button → log in |
| K.5 | Request description loses first letters typed | Type into description without clicking it first |
| K.6 | "Completed by client –" shows no name | Any completed request |
| K.7 | Client can submit upload request without ticking checklist | UP with checklist, submit unticked |
| K.8 | Client uploads show "Uploaded by: Firm" | Client → Files after any upload |
| K.9 | Placeholder "Client Request type" renders empty | Placeholder template email |
| K.10 | Due date in two formats in one email | Placeholder template email |
| K.11 | Email request card "Sender" shows email, not name | Any request email |
| K.12 | Enter after last checklist item adds a blank item | Add checklist, press Enter |
| K.13 | (Not reproduced earlier) E-sign checklist ticks lost after signing | ES with checklist |
| K.14 | Completed e-sign still shows "Sign document"; Submit spins ~20 s | ES complete |
| K.15 | New form option starts with "Option 1" text | Form template editor |
| K.16 | Clicking a choice's words doesn't select it (only the circle) | Portal form radio label |
| K.17 | Upload box lists PDF/DOCX/XLSX/CSV/images but accepts anything | Upload a .zip |
| K.18 | File uploaded inside a form isn't in Client → Files | FM with file question |
| K.19 | (Not reproduced earlier) Form request shows empty Checklist in Cone | FM with checklist |
| K.20 | (Not reproduced earlier) Portal reopens previous task after reload | Open task, reload |
| K.21 | Chat email for a question says "Review and sign", "Expires on –", no message text | AQ chat message |
| K.22 | Portal Chats → Tasks says "No conversations" | All requests completed, active chat, ~1270px |
| K.23 | E-sign fields all dropped on the same spot | Add Signature + Initials + Date |
| K.24 | Esc doesn't close portal PDF viewer | SD → open PDF → Esc |
| K.25 | Scheduled request goes live but email never sent | R.6 |
| K.26 | Scheduled banner shows one day earlier than the picked date | R.6 drawer banner |
| K.27 | Email ~5 min late after sending a draft | R.9 |
| K.28 | Saving a draft shows "Task created" | R.9 |
| K.29 | Schedule-for-later defaults to tomorrow 2:30 AM, after the due date, no warning | R.6 |
| K.30–K.34 | Sprint 1 rows: due-before-start saves; section delete deletes tasks; drawer discards unsaved edits; Work → Tasks "Add filter" dead; deleted-project URL phantom page | P.5, SC.3, T.18, V.4, P.16 |

## SECTION 0B — Screen inventory (do this FIRST on every screen — it is how we stop missing things)

Before testing a screen, write down **every** button, field, menu item (⋮ menus too), tab, filter field, sort option, column and keyboard shortcut on it, in `inventory.md` (one list per screen). After testing, tick each item against a case ID. **Any item with no case gets a new row** in Section 18 ("Found in inventory") — never skip it because the plan didn't list it. Screens: Work → Projects, Work → Tasks, project page (List, Board, Time tracking, Settings tabs), task drawer, client request drawer (each type), Create project dialog (3 steps), Templates → Projects, Templates → Email, Templates → Forms, client page (Overview, Projects/Work, Files, Contacts, Chats, Settings), portal (Home, Tasks, Chats, Files), notifications/inbox.

## SECTION 12 — Every text field × every kind of input

**Input set (IN.1–IN.14):** IN.1 empty · IN.2 only spaces · IN.3 one character · IN.4 leading/trailing spaces (are they trimmed?) · IN.5 **find the length limit**: paste 50, 100, 255, 256, 500, 1 000, 5 000 and 10 000 characters, write down where it stops or errors and whether the user is told · IN.6 one over that limit · IN.7 emoji `🚀 👍🏽 👨‍👩‍👧 🇮🇳` · IN.8 symbols `~!@#$%^&*()_+{}|:"<>?` and `` `-=[]\;',./ `` · IN.9 accents + other scripts `é ü ñ ß 中文 日本語 हिन्दी` and right-to-left `العربية עברית` · IN.10 typed HTML `<b>x</b>` and `<script>alert(1)</script>` (must show as plain text, no popup) · IN.11 line breaks pasted into a one-line field · IN.12 same name as an existing item (duplicate allowed? warned?) · IN.13 text pasted from Word / Google Docs (formatting kept or cleaned?) · IN.14 numbers only / very long single word with no spaces (does it wrap or overflow?)

For each: does it save, how is it shown everywhere it appears (list, drawer, board card, breadcrumb, browser tab title, email subject/body, portal, search results), and is it still right after reload?

| # | Field | Where it also shows | Rows |
|---|-------|---------------------|------|
| TX.1 | Project name | Projects list, header, breadcrumb, client page, portal, emails | 14 |
| TX.2 | Project description | Project page | 14 |
| TX.3 | Section name | Project list + board column | 14 |
| TX.4 | Internal task name | List, board, Work → Tasks, notifications | 14 |
| TX.5 | Internal task description | Drawer | 14 |
| TX.6 | Checklist item | Drawer, portal | 14 |
| TX.7 | Client request title (each type: log as TX.7-UP … TX.7-AQ) | Portal, email subject/body | 70 |
| TX.8 | Client request description (each type) | Portal, email | 70 |
| TX.9 | Email template name / subject / body | Template list, email | 42 |
| TX.10 | Folder name | Client Files, folder picker, portal Files | 14 |
| TX.11 | Form template name / question / choice option | Form builder, portal, answers PDF | 42 |
| TX.12 | Chat message (firm → client, client → firm) | Both sides + notification email | 28 |
| TX.13 | Client's answer to "Ask a question" | Firm side, email | 14 |
| TX.14 | Comment on internal task | Drawer | 14 |
| TX.15 | Custom status name | Status menus, filters, board | 14 |
| TX.16 | Project template name + template task names | Templates list, created projects | 28 |
| TX.17 | Every search box (Section 13) | Results | 14 |
| TX.18 | Client name + contact name (only test-prefixed clients) | Everywhere the name appears, emails, portal | 28 |

Firefox / Brave / Safari: run only IN.5, IN.7, IN.9, IN.10 and IN.13 for each field (browser-dependent behaviour); the rest is the same in every browser.

## SECTION 13 — Search, filters, sort, group, columns on every list

Run on each list: **LS.A** Work → Projects · **LS.B** Work → Tasks · **LS.C** project task list · **LS.D** project board · **LS.E** client → projects/tasks · **LS.F** client → Files · **LS.G** Templates (Projects, Email, Forms) · **LS.H** portal task list · **LS.I** portal Chats. Log as e.g. `SR.3-LS.B`. Set up first: 30+ tasks across 3 projects with mixed statuses, priorities, due dates, types, sections.

| # | Check | What I do | Expected | Rows |
|---|-------|-----------|----------|------|
| SR.1 | Search exact name | Type a full task/project name | Only that item | 9 |
| SR.2 | Search part of a word, any case | "statem", "STATEM" | Matches regardless of case | 9 |
| SR.3 | Search what? | Search text that is only in a description / client name / checklist | Write down which fields search covers | 9 |
| SR.4 | Search special input | Emoji, symbols, é, 中文, leading space | No error; sensible result | 9 |
| SR.5 | No results + clear | Nonsense text, then clear (× and backspace) | Clear empty state; full list returns | 9 |
| SR.6 | Search + filter together | Search while a filter is on | Both applied | 9 |
| SR.7 | Search kept? | Reload / go back after searching | Write down whether it is kept; no stale results | 9 |
| FL.1 | **Every filter field × every option** | From the inventory: each field in "Add filter" (status, priority, due date, assignee, client, project, type, …) × each operator/value | Only matching rows; count correct | ~60 (count from inventory) |
| FL.2 | Two and three filters combined | e.g. Status = Waiting on client AND Priority = High | AND logic, correct rows | 9 |
| FL.3 | Remove one filter / clear all | — | List updates correctly | 9 |
| FL.4 | Filter that matches nothing | — | Clear empty state | 9 |
| FL.5 | Filter kept after reload / navigation / new tab | — | Write down; no half-applied state | 9 |
| FL.6 | Quick views (My tasks, Overdue, Today, This week …) | Each view offered | Right rows; counts match | ~8 |
| SO.1 | **Sort by every column, both directions** | Name, due date, priority, status, created, client, project … | Correct order; empty values placed consistently; ties stable | ~40 |
| SO.2 | Sort + filter + search together | — | All three applied | 9 |
| SO.3 | Sort kept after reload / adding a task | — | New task appears in the right place | 9 |
| GR.1 | Group by every option | Status, priority, section, assignee, project … | Groups and counts right; empty groups shown/hidden consistently | ~15 |
| GR.2 | Collapse groups, drag between groups | Drag a task to another status/priority group | Field actually changes and saves | ~10 |
| CO.1 | Columns show / hide / reorder / resize | Manage columns | Kept after reload; nothing overlaps at 1280×800 | 9 |
| PG.1 | Long lists | 30+ items: scroll / pagination / load more | No missing or doubled rows | 9 |
| BK.1 | Select several rows (if it exists) | Bulk status, bulk delete, bulk move | All selected change, others don't | ~6 |

## SECTION 14 — Statuses (tasks, client requests, projects)

| # | Case | What I do | Expected | Runs for | Rows |
|---|------|-----------|----------|----------|------|
| SS.1 | Every task status, set by firm | Walk each status in the list (incl. Waiting on client, Completed) | Saves; icon/colour right in list, board, Work → Tasks, client page | internal + UP FM ES SD AQ | 6 |
| SS.2 | Status set from list, drawer, board drag | 3 ways | Same result each way | internal + UP FM ES SD AQ | 18 |
| SS.3 | What the client sees per firm status | Firm sets each status | Portal shows a sensible state; Completed requests not still asking for action | UP FM ES SD AQ | 5 |
| SS.4 | Status after client submits | Client submits | Firm status changes to? Firm still sets Completed (Pavi's rule) | UP FM ES SD AQ | 5 |
| SS.5 | Completed → back to In progress | Firm reopens | Portal reopens? client notified? progress drops | UP FM ES SD AQ + internal | 6 |
| SS.6 | Custom status list: create, rename, recolour, reorder | Project Settings → task statuses | Changes show everywhere at once | once | 4 |
| SS.7 | Delete a status in use / the last status | — | Blocked or tasks moved — no task left without a status | once | 2 |
| SS.8 | Status filter + sort + group | Uses Section 13 | Order follows status list order | once | 3 |
| SS.9 | Every project status (In progress, On hold, Ended …) | Set each | Shown right in Projects list, client page, portal; what can still be done in each | once | ~5 |
| SS.10 | Progress bar | Mix of statuses | "% – x/y tasks" counts only firm-Completed tasks | once | 1 |

## SECTION 15 — Description editor: formatting, screenshots, files

Runs for: project description, internal task, each request type (UP FM ES SD AQ), email template body = 8 places. Log as e.g. `DE.3-ES`.

| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| DE.1 | Every toolbar button | Bold, italic, underline, strike, headings, bullet/numbered list, quote, code, link — whatever exists | Each works; kept after save and reload | 8 |
| DE.2 | Keyboard shortcuts | Ctrl/Cmd+B, I, U, K, Z, Shift+Z | Work as in other editors (Cmd on Safari) | 8 |
| DE.3 | **Paste a screenshot** | Take screenshot → Ctrl/Cmd+V into the description | Image appears, saves, still there after reload | 8 |
| DE.4 | Drag & drop an image file | PNG, JPG, GIF | Same as DE.3 | 8 |
| DE.5 | Image through toolbar/attach button (if it exists) | — | Same as DE.3 | 8 |
| DE.6 | Large image (~10 MB) / very wide image | — | Accepted with limit message, or scaled; no broken layout | 8 |
| DE.7 | Non-image file in the description | PDF, DOCX | Attached, refused clearly, or not offered — write down | 8 |
| DE.8 | Where the image shows | For requests: portal + request email; for templates: the email | Client actually sees the image (not a broken icon) | 7 |
| DE.9 | Remove image / undo | Delete image, Ctrl+Z | Works; removed image not still shown to client | 8 |
| DE.10 | Paste formatted text | From Word, Google Docs, a web page | Readable; no hidden junk styles | 8 |
| DE.11 | Links | Paste a URL, add link via button | Clickable; opens in new tab; also in portal/email | 8 |
| DE.12 | Typing before clicking into the editor | Known bug K.5 | — | 8 |
| DE.13 | Edit description after a request is sent | — | Allowed? Client sees new text? | 5 |

## SECTION 16 — Project templates

| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| PT.1 | Clone a global template | Templates → library → duplicate | Copy appears in my templates, editable | 1 |
| PT.2 | Create template from scratch | Name, sections, internal tasks, one client request of each type | Saves | 6 |
| PT.3 | Relative due dates | Tasks due +0, +3, −2 days from start | Created project gets correct real dates | 3 |
| PT.4 | Assignee placeholders | Placeholder labels replaced at project creation | Correct names | 1 |
| PT.5 | Publish / unpublish | — | Only published offered in "Use project template" | 2 |
| PT.6 | Use template → one-time project | — | All sections/tasks/requests copied; requests NOT sent automatically (or write down) | 1 |
| PT.7 | Use template → recurring project (daily) + dynamic project name | — | Names follow the pattern; tasks shifted per copy | 2 |
| PT.8 | Edit template after projects were made from it | — | Existing projects unchanged | 1 |
| PT.9 | Delete template in use | — | Existing projects unaffected | 1 |
| PT.10 | Template with billing (fixed / hourly) | — | Billing copied into project | 2 |

## SECTION 17 — Time tracking on tasks

| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| TT.1 | Start/stop timer from Work → Tasks and from the drawer | — | Entry saved with correct duration | 2 |
| TT.2 | Two timers at once | Start on 2 tasks | Both run; both saved | 1 |
| TT.3 | Timer survives reload / closing the tab / switching pages | — | Keeps counting or clearly stops | 3 |
| TT.4 | View time entries (⋮ → View time entries) | — | Entries listed, right task | 1 |
| TT.5 | Edit / delete an entry; manual entry (if it exists) | Negative, 0, 25 h, decimals | Validated | 4 |
| TT.6 | Project → Time tracking tab totals | — | Sum matches entries | 1 |
| TT.7 | Timer on a completed / deleted task | — | Sensible behaviour | 2 |
| TT.8 | Billable vs non-billable project | — | Hours shown accordingly | 2 |

## SECTION 18 — Browser behaviour, dates and safety nets

| # | Case | What I do | Expected | Rows |
|---|------|-----------|----------|------|
| BR.1 | Browser zoom 80%, 100%, 125%, 150% at 1366×768 | Main screens | Usable, nothing cut off | 4 |
| BR.2 | Reload mid-edit in each dialog (Create project, task drawer, request drawer, template editor) | — | Warned or draft kept; no half-saved item | 4 |
| BR.3 | Back / forward through project → task → request | — | Correct pages, drawer state sensible | 1 |
| BR.4 | Double-click every Save / Create / Send button | — | Exactly one item created / one email sent | 6 |
| BR.5 | Lose network while saving (DevTools offline) | — | Clear error, nothing lost silently, retry works | 3 |
| BR.6 | Logged out in another tab, then save here | — | Asked to log in; work not silently lost | 1 |
| BR.7 | Keyboard only | Tab through Create project and request drawer; Enter/Esc | Focus visible, order logical, everything reachable | 2 |
| BR.8 | Copy a task/project URL into a new tab and a different browser | — | Opens the same item (after login) | 2 |
| DT.1 | Date picker: type a date vs pick one | dd/mm vs mm/dd, invalid "31/02" | Valid only; format consistent everywhere | 3 |
| DT.2 | Edge dates | 29 Feb 2028, 31 Dec → 1 Jan, month ends | Correct | 3 |
| DT.3 | Time zones | Firm and portal in different OS time zones (change VM time zone) | Due date same day both sides | 1 |
| DT.4 | Numbers in billing/budget fields | 0, negative, decimals, 1e9, letters | Validated | 5 |
| UN.1 | Delete project / section / task / request — can it be undone or restored? | — | Write down; warning says what will be lost | 4 |
| FI.1 | "Found in inventory" | One row for every inventory item not covered elsewhere (Section 0B) | — | ~20 (from inventory) |

## SECTION 19 — Past results that still need a video or a finish (do this right after Section 0B)

Nothing from earlier runs is skipped. Each item below uses the two-tries rule and the video rule above. Log as e.g. `PB.3`.

| # | Past item | Where it came from | What to do | Rows |
|---|-----------|--------------------|------------|------|
| PB.1 | Bug 13 — e-sign checklist ticks disappear after signing | Bug page, no video (not reproduced) | ES request with 2 checklist items; tick, sign, submit; check the firm drawer. Two tries, record; video whatever the result | 1 |
| PB.2 | Bug 19 — form request shows an empty Checklist in Cone | Bug page, no video | FM with checklist; two tries, record | 1 |
| PB.3 | Bug 20 — closed portal task opens again after reload | Bug page, no video | Open a task in the portal, close it, reload; two tries, record | 1 |
| PB.4 | K.23 e-sign fields dropped on the same spot | Chrome run, no video | Record | 1 |
| PB.5 | K.24 Esc doesn't close the portal PDF viewer | Chrome run, no video | Record | 1 |
| PB.6 | K.25 scheduled request goes live but email never sent | Chrome run, no video | Schedule 10 min ahead; record the mailbox at send time and 20 min later | 1 |
| PB.7 | K.26 scheduled banner shows the previous day | Chrome run, no video | Record | 1 |
| PB.8 | K.27 email ~5 min late after sending a draft | Chrome run, no video | Record with a visible clock | 1 |
| PB.9 | K.28 saving a draft says "Task created" | Chrome run, no video | Record | 1 |
| PB.10 | K.29 schedule date defaults after the due date, no warning | Chrome run, no video | Record | 1 |
| PB.11 | Portal Chats squeezed at ~1270px (client name wraps, side scrollbar) | Chrome run, no video | Record at 1280×800 | 1 |
| PB.12 | Sprint 1 row 94 — first request email and manual "Send reminder email" never arrive ("Request sent" shown) | sprint1.csv, Partial-FAIL suspect | Two tries, record | 1 |
| PB.13 | Sprint 1 row 86 — "Reminder sent" toast but no reminder email | sprint1.csv, Partial | Two tries, record | 1 |
| PB.14 | Sprint 1 row 43 — "Copy task link" on an internal task gives a portal.getcone.io link | sprint1.csv, changed behaviour | Retest; new video if it still happens | 1 |
| PB.15 | Sprint 1 Partial rows 45, 46, 52, 56, 72, 85, 88, 93, 106 | sprint1.csv | Finish the parts the notes say were not exercised; one result row per CSV row | 9 |
| PB.16 | Sprint 1 Untested rows 49, 61, 68, 73, 79, 82, 83, 84, 87, 89, 90, 91, 92, 96, 97, 98, 99, 100, 101, 102, 103, 105, 107 | sprint1.csv | Run each (they map to Section 4/11/16/17/18 rows — write the plan ID next to it so it isn't run twice) | 23 |
| PB.17 | Bugs 1–12, 14–18, 21, 22 and Sprint 1 rows 9, 17, 30, 37, 77 (already have videos) | Bug page | Retested in Section 10; if one now passes twice, record a short "Fixed" video | 0 extra |

## SECTION 11 — Combinations not covered above

These come from general QA practice, not from Cone's code. First check that the option exists in Cone; if it does not, log `N/A`. Each row runs for every listed type × every listed variant: log as e.g. `M.1-ES-High`. "If it exists" = log `N/A` if Cone has no such option.

| # | Combination | Variants | What I check | Runs for | Rows |
|---|-------------|----------|--------------|----------|------|
| M.1 | Priority | None, Low, Medium, High | Saves; icon in task list; sort/filter by priority; what the client sees | UP FM ES SD AQ | 20 |
| M.2 | Where the request is created | Top "Create task" button, lower "Create task" arrow | Same options offered, same result | UP FM ES SD AQ | 10 |
| M.3 | Client clicks the email button | Already logged in to portal, logged out | Opens THAT request (known bug K.4 when logged out) | UP FM ES SD AQ | 10 |
| M.4 | Where the document comes from | Uploaded from computer, picked from client's Cone Files | Right file reaches the client | ES SD | 4 |
| M.5 | Document size | ~300 KB, 2 MB, ~20 MB | Uploads, opens in portal, signed/returned copy correct | UP ES SD | 9 |
| M.6 | Document type | PDF, DOCX, JPG/PNG | Accepted or clearly refused; portal viewer opens it | ES SD | 6 |
| M.7 | E-sign fields | Signature only, Initials only, Date only, all three on 2 pages | Each fills; none overlap (known bug K.23); signed PDF shows them | ES | 4 |
| M.8 | Share documents action | View only, + "Request to upload documents" | Client can only view / can view and upload; upload lands in the chosen folder | SD | 2 |
| M.9 | Folder made in Client → Files first, then picked in the send flow | — | Listed in the picker; files land there | UP ES SD (FM: N/A expected) | 4 |
| M.10 | Delivery × template | Schedule later + placeholder template; Draft + default template | Placeholders filled at send time with current values; draft email uses default wording | UP FM ES SD AQ | 10 |
| M.11 | Changing a not-yet-sent request | Delete a draft; change a scheduled time; "Send now" on a scheduled request | Deleted draft never emails; new time used; send-now sends once (not twice at the old time) | UP FM ES SD AQ | 15 |
| M.12 | Text edge cases | 300-char title; very long description; emoji; é ü 中文; `<b>x</b>` typed in title/description/checklist | Saved; email + portal show it as plain text, nothing broken | UP FM ES SD AQ | 5 |
| M.13 | Partial client work | Client does part (1 of 2 checklist items / 1 of 2 files / half the form) and leaves | Request stays waiting; firm sees partial progress; client can finish later | UP FM ES SD AQ | 5 |
| M.14 | Firm sets Completed BEFORE the client submits | — | What the portal shows; can the client still submit; do reminders stop | UP FM ES SD AQ | 5 |
| M.15 | Duplicate a request (only if Cone offers it) | — | Copy keeps type and content and is not sent until the firm sends it | UP FM ES SD AQ | 5 |
| M.16 | Request inside a project template (only if Cone offers it) | Template → new project from it | Request copied into the new project; document whether it is sent automatically | UP FM ES SD AQ | 5 |
| M.17 | Two requests to the same client within 1 minute | UP then ES | Both emails arrive, right content each, both in portal | once | 1 |
| M.18 | Request in a project whose status is Completed (only if Cone allows sending) | — | Document what happens; no confusing state for the client | once (UP) | 1 |
| M.19 | One email address on two clients (only if Cone allows) | Add the same maildrop contact to "S2 shared X" and "S2 shared Y" | Each client's requests stay separate; document how the portal handles it | once | 1 |
| M.20 | Contact's email changed after a request was sent | — | Document whether old email links still open the request and where reminders go | once (UP) | 1 |
| M.21 | Client archived/deleted and restored with an open request (only if Cone has these options) | Archive; delete + restore | Document what the portal shows and whether reminders stop | once (UP) | 2 |

## Totals (result rows, after repeating per request type)
| Part | Chrome | Firefox / Brave / Safari |
|---|---|---|
| Sections 0–8 (195 case IDs, repeated per type) | 491 | 491 |
| Section 4K — forms in depth (with/without template, builder, answers) | ~110 | ~110 |
| Section 11 — missed combinations | 125 | 125 |
| Section 12 — every text field × 14 inputs | 462 | ~165 (5 browser-dependent inputs) |
| Section 13 — search, filters, sort, group, columns on 9 lists | ~274 | ~274 |
| Section 14 — statuses | ~55 | ~55 |
| Section 15 — description editor, screenshots, files | 100 | 100 |
| Section 16 — project templates | 20 | 20 |
| Section 17 — time tracking | 16 | 16 |
| Section 18 — browser behaviour, dates, safety nets | ~59 | ~59 |
| Section 19 — past items finished / recorded | 46 | 46 |
| Section 9 — every screen at 6 sizes + request flows at 1280×800 and 2560×1440 | ~590 | ~590 |
| Section 10 — known-bug retests | 34 | 34 |
| **Total** | **≈ 2 380** | **≈ 2 080** |

"~" rows depend on what the Section 0B inventory finds (number of filter fields, sortable columns, etc.); fix the count after the inventory.

## Explicitly NOT re-running (already verified in rows 1–107)
Send pipeline basics, edit-lock after send, no-delete-on-sent-requests (retest only), completed/reopen, template relative dates, timer behaviors, list sections ops that passed.

Running order: Section 0 → 0B (inventory) → 19 (past items) → 1 → 2 → 3 (P1) → 12 → 15 → 4 (big matrix) → 5 → 11 → 14 → 16 → 17 → 6 → 13 → 7 → 8 → 18 → 10 → 9. Report after each section. Bugs → video after 2nd repro → added to the sheet.

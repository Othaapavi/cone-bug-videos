# Screen inventory — Chrome 1366×768 (Sprint 1, Section 0B)
Every button, field, menu item, tab, filter, sort option, column and shortcut seen per screen. `[x]` = covered by a test case, `[ ]` = needs a row (Section 18 FI).

## Global chrome (present on all firm screens)
- Sidebar: Create new (dropdown), Get started, Dashboard, Clients hub (expandable: Clients, Contacts, Deals), Inbox (expandable), Work (expandable: Projects, Tasks, Recurring projects, Time entries), Proposals (expandable), Finances (expandable), Reporting, Templates, Messages
- Sidebar bottom: Notifications (bell + unread count badge), Help center, user profile menu (Pavithran S), Collapse button
- Top: trial banner "Welcome to your 14-day trial" + Upgrade Now + dismiss X; Learn dropdown on list pages
- Bottom-left overlay: Start timer bar with expand/hide buttons

## Work → Projects
- Tabs: Projects / Tasks / Recurring; Learn dropdown
- View switcher: List | Board | + View | view-settings gear
- Toolbar: Group by: Status (dropdown), Add filter, Search projects, Export, Create Project
- List columns: Project (sort asc + collapse-all groups), Client, Project owner, Start date, Due date, Progress, Time, Hours budget, Amount budget, Status, Completed date — all sortable
- Groups by status (e.g. "In progress 7") collapsible; project name links to project page; client name opens client
- Board view exists (cards per status column)

## Work → Tasks (my tasks)
- Same tabs + view switcher (List/Board/+View/settings gear)
- Toolbar: Group by: Due date, saved-filter chips (Tasks → Assignee Is Me; Tasks → Show completed Equals False), Add filter (KNOWN BUG K.4: dead button), Clear, Search tasks, Export, Create task (dropdown)
- Columns: Task (sort + collapse-all), Project (link), Client, Time, Priority, Assignee, Due date, Status, Created by, Created at — all sortable
- Date groups (Overdue 9, Today 2) collapsible; inline "Create task" row + ▾ per group
- Row inline controls: complete circle, task name, subtask counter (n/n), project link, client chip, Priority dropdown, Assignee dropdown, Due-date button, Status button

## Task drawer — "Update internal task" (right-side drawer)
- Header: Share, Chat, ⋮ more, Close X
- Body: Task name textarea; "Describe the task" rich area; + Checklist; + Attachment
- Right rail: Client (Select dropdown), Project (Select... disabled until client set), Assignee dropdown, Due date (calendar button + DD/MM/YYYY text + clear X), Priority (None/Low/Medium/High dropdown), Status dropdown, Billable task checkbox
- Footer: Save
- KNOWN BUG K.5-adjacent/bug-30: closing drawer with unsaved edits discards without warning (already logged)
- Row hover in list reveals "Task actions" ⋮ button

## Client-request drawer — "Update client request task" (sent state)
- Header: title + client name; Share, Chat, ⋮, Close X
- Status banner: "Waiting on client — Request sent N ago"; Send reminder email (disabled when reminders off?), Mark as complete
- Title textarea (disabled once sent); description "Describe your request to the client"
- Client recipient * dropdown (disabled)
- Delivery settings: "Send client request email to client" toggle + note
- Client reminders: "Send email reminders to client" toggle; "First reminder will be sent 7 days before due date."; Customize email | Frequency settings links
- Internal details: Project dropdown, Section dropdown, Assignee (Internal), Status (No Status), Due date, Priority
- Footer: Save

## Create new project wizard (3 steps: Basic details / Advanced / Custom fields)
- Step 1 "Project details": Use project template; project name input (required — Continue silently does nothing without it); Description textarea; Clients * multi-select dropdown (Search, Select all, SELECTED/AVAILABLE checkbox list); Project owner * dropdown; Project type toggle One-time / Recurring; Start date * + Due date * (calendar pickers); Task status list dropdown (Default); Cancel / Continue
- Step 2 "Pricing & billing": "This project is billable" toggle; Hours budget (placeholder e.g. 20); Amount budget (e.g. 2,000); Back / Create Project / Continue
- Step 3 "Custom fields": "Get started by creating a custom field" — note "Any fields you create will be visible across all clients... manage inside settings"; Create new field; Back / Create Project (no Cancel on step 3; close via header X)

## Client quick view (right panel, opens from client name anywhere)
- Go to workspace, X close; Basic details (Company name, Company type, Client start date, Fiscal year end); Contacts list (badges Primary/Billing, "Client portal access enabled/disabled", ⋮ per contact); Optional details (VAT/GST/EIN#, Time zone, Registered office address, Client country); Billing settings and automations (Auto-send invoices Enabled + Manage settings; Sync to accounting / Collect payment details / Auto-charge client — Not connected + Connect links)
- NOTE: contact "S2 contact two" has portal access DISABLED — needed later for request/portal tests

## Edit client dialog (3 tabs: Basic details / Business details / Custom fields)
- Import data from integrated apps banner; Company name *; Alias; Client type (Customer/Prospect); Client start date (calendar + DD/MM/YYYY); Contacts list + Add contact; ⋮ per contact (Edit / More options); Cancel / Save / Continue

## Work → Projects list (already in list above) — extras observed
- Client name in row is a button → opens Client quick view
- "In progress N" group-header button (Collapse all inside Project column header)
- Create Project button; row-count columns incl. Time, Hours budget, Amount budget

## Work → Recurring projects list (/pm/work/recurring)
- Tabs shared with Work; Add filter; Manage columns; Search input; columns: Recurring | Client | Frequency | Last run | Next run | Created | Status; row ⋮ "More row actions"; client name → quick view; NO create button visible on list (create via wizard Project type=Recurring or elsewhere — verify)

## Templates → Projects (/pm/templates/projects)
- Sub-nav links: Projects / Folder / Proposals / Proposal sections / Engagement letters / Emails / Form
- Add filter; Manage columns; Template library; Create template; Search template; columns: Name | Last edited | Date created | Status; empty-state buttons: Create template / Explore template library

## Templates → Form (/pm/templates/form) + editor (/pm/templates/form/edit/<id>)
- List: same toolbar as Projects templates; row: Edit + ⋮ More row actions
- Editor: Close; Save changes; Form template name input; Description textarea; per-question card: label input, drag handle, collapse chevron, Settings gear, duplicate, delete; question type dropdown — TYPES (9): Single choice, Multi choice, Short answer, Paragraph, File upload, Multi-file upload, Date, Phone number, Email; Required toggle; "Make it secure" toggle (Short answer); options list with per-option input + remove, "Add option" / "Add Other", "Select an option to set as default answer"; Default value input (Short answer); "+ Add" between/after questions → Add text card / Add question (Add question inserts a new Short-answer question immediately)

## Clients list (/pm/clients/list)
- Create client; type filter pills All/Prospects/Customers; View + View settings; Add filter; Export; columns: Client | Alias | Type | Status | Primary contact | Contact email; per-row: Quick view | Edit | ⋮ More row actions
- Client workspace URL pattern: /pm/clients/list/<client-id>/<tab>

## Client workspace (client A)
- Header: back ← to list; client name switcher dropdown; Project team (avatar group PS SC ST); Quick view; Create ▾ (Proposal / Invoice / Recurring invoice only)
- Tabs: Overview / Tasks / Projects / Files / Notes / Emails / Chat / Forms / Time entries / Billing / Settings
- Overview: Proposals table (Proposal name/Amount/Status/Starts on/Duration sortable); Revenue chart; Payments chart; Email log (Subject/Email type/Sent on/Status, pagination) "Emails sent to <contact>, updated daily"; right rail: Basic details, Contacts (portal access status + ⋮), Optional details, Billing settings and automations — same as quick view

## Project page header (all tabs)
- Back; project name + status pill; tracked time; Start timer; client chip button (→ quick view); owner; dates; progress; hours/amount budgets; tabs Tasks / Time tracking / Settings

## Project → Tasks tab (Board + List views)
- Board/List segmented toggle (with a small ▾ on Board); View; View settings; Group by (Section); Add filter; Search tasks; Create task ▾ (header)
- Board: per-section header = section name + count + ⋮ More actions + Add task; "+ Add section" under last column; task card = ⋮ Task actions, name, status chip dropdown, checklist progress (n/m), priority chip, due chip, assignee chip, time tracked, type icon (client-request shows person icon)
- List: same toolbar; columns Task | Time | Assignee | Priority | Due date | Status | Completed date | Created by | Created at (each sortable); section group rows; Create task at top + per-group + bottom

## Project → Time tracking tab
- Add filter; Search time entries; Manage columns; Export; + Add time entry
- Columns: Task or project | Assignee | Date | Duration | Notes | Billable | Invoicing status; row ⋮ More row actions; "Project-level" entries for project timer

## Project → Settings tab
- Project details (name/client/owner/start/due/description) + Edit; Repeat (starting on, create-in-advance, name suffix) + Edit; Billing + Edit; Budget (hours/amount) + Edit; Status template — Task status list + Update

## Create client request task — drawer, type picker step
- Header: title "Create client request task", client chip (disabled once opened from a project), Close X
- "What would you like to request from the client?" radio fieldset: Request to upload documents (upload-documents) | Request to fill a form (fill-form) | Request an e-signature (e-signature) | Share documents (share-documents) | Ask a question (ask-a-question)
- Cancel / Continue (disabled until a type picked)

## Create client request task — drawer, compose step (shared fields)
- Client request title textarea; "Describe your request to the client" rich area; Checklist; Attachment (absent on Share documents); Client recipient * dropdown; Delivery settings — Send client request email toggle, Email now / Schedule for later radios + Schedule-for-later button, note "An initial client request email will be sent now.", Customize email; Client reminders — Send email reminders toggle, "First reminder will be sent 7 days before due date.", Customize email | Frequency settings; Internal details right rail — Project [D], Section, Assignee (Internal), Status, Due date (calendar+DD/MM/YYYY+clear), Priority; footer Save as draft / Send now
- "Client request action — Add an optional action for your client" secondary block (present on AQ + SD; adds a SECOND action): buttons Request to upload documents / Request to fill a form / Request an e-signature
- Per-type blocks (each with ⋮ menu):
  - UP: "Where should clients upload documents?" — "No folder selected — Change" + "Set up a default destination folder for this client."
  - FM: "Set up a form to send to the client" — Create form / Use a form template
  - ES: "Upload and set up a file with signature fields" — Cone storage / Upload
  - SD: "Add documents to share with your client" — Cone storage / Upload
  - AQ: no extra block (question = title+description)

## Notifications panel (sidebar, badge count)
- "Notifications" heading + "Mark all as read"; tabs All (N) / Alerts / Unread (N); item = icon + title + description + relative time + unread dot; items clickable; scrollable list; closes when another nav item clicked

## Inbox (/pm/inbox/emails + /pm/inbox/chats)
- Sidebar "Inbox" expands to Emails + Chat sub-links
- Tabs: Emails (0) / Chats
- Emails empty state: "Supercharge your inbox" + Connect account
- Chats channel list: General (client-general), Tasks (client-tasks), Team (internal-team), Tasks (internal-tasks), Email (emails)

## Client portal — global (portal.getcone.io, logged in as S1Alpha ContactA)
- Top nav links: Tasks (/app/tasks) | Chats (/app/chats) | Files (/app/files) | Settings (/app/settings)
- Client/workspace picker chip "S1 Chrome client A" (button) + avatar "SC" button; welcome heading "Welcome to <workspace>, <name>! 👋 — Hope you are having a great day!"

## Portal — Tasks (/app/tasks)
- Search tasks input; status group toggle buttons "Not started (N)" | "Waiting on client (N)"
- Table, sortable column buttons: Task name | Request action | Assignee | Due date | Status
- Row: task name + "Basic request" action label + assignee avatar+name + due + status chip; row opens request/task detail

## Portal — Chats (/app/chats, resolves to /app/chats/client-general/<clientId>)
- Sub-links: General (/app/chats/client-general) | Tasks (/app/chats/client-tasks)
- "No conversation yet" empty state + Start Conversation button; client picker chip

## Portal — Files (/app/files/<clientId>)
- "Files" button (upload entry), Search files input
- Table cols: Name | Size | Last modified | Uploaded by | (row actions col)

## Portal — Settings (/app/settings)
- "Personal profile": avatar Upload file / Drop files here, 2 name inputs, email input [disabled], Save

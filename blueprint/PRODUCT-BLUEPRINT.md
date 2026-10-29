# 49GAION Organisation Design and Delivery · product blueprint · `v0.1.3`

**Draft, 20 October 2026.** The blueprint of the first assembly of the 49GAION Library (`49GAION/DR-0025`; Standard §3.1, item 12). It lists the product's parts by pin, how they connect, what goes in, what comes out, what the product is for, what the product itself sets, and its one shared test. The product adds no capability of its own: its features are its parts' features. Every rule here rests on a 49GAION text or on a part's blueprint, cited by section. Nothing here has run. Every fixed test reads `NOT_RUN` until the part is built and run; that is the policy of the Library, not a defect.

> **The product in one page**
>
> **What it is.** One product made of four Library parts placed side by side and connected:
> - **Source Lifecycle** (SL) keeps the organisation's own sources;
> - **Target Operating Model** (TOM) designs what the organisation does and how it is governed;
> - **Process and Position Design** (PPD) designs how the work runs and the positions that carry it;
> - **Delivery and Implementation** (DI) takes the decided design into a running organisation, and runs and improves it with the organisation.
>
> Each of the four is built and kept on its own: Source Lifecycle and the Target Operating Model are offered alone, and Delivery and Implementation runs without the others. Together they are this product.
>
> **What goes in.** The organisation's own documents, and what its people say once they have approved it. A Design Request, approved by the organisation's Requesting Authority, says what should be different. Answers to questions, asked only through Source Lifecycle. Optionally, the running work as an export by role-type and process, or a design made elsewhere.
>
> **What comes out.** A decided design of an organisation of **human positions**, taken into a running organisation:
> - a decided operating model (capabilities, value streams, decision rights, interfaces, a role register, a strategy frame, a value case and priorities);
> - decided processes, positions with job descriptions, units, controls, workload and the crosswalk from today's organisation;
> - a launch package (procedures, briefs, transition plan, go-live criteria);
> - then go-live, stabilisation, one operating rhythm and a living design.
>
> Every release is decided element by element by the organisation's own positions and is filed in Source Lifecycle.
>
> **What it is for.** An organisation, new or existing, goes from its own sources to a working organisation of human positions, with every element traced to a source or a decision.
>
> **What it never does.** It never decides which positions an AI fills: that is the next level (§12). No output names a person, and no stage reads who occupies a position. It never decides for the organisation. AI prepares; human positions decide.
>
> **How to start.** The organisation names its Requesting Authority, arranges the four accountable positions, connects the parts and approves a Design Request. The organisation may stop after any stage, and no stage waits for a later one (§8).

> **Reading (49GAION DR-0041).** The complete definition of 49GAION, approved by its governing seat on 25 October 2026, is `49GAION-FRAMEWORK.md` in `github.com/49g-holding/49GAION`. Where this repository differs from it, the definition governs, and this text is read with it. This product designs an organisation of human positions; how human and how much AI the organisation is, is the `[ORG]AION`'s own design work, prepared by it and decided by the governance seat. Every rule here that names `[ORG]AIOC-OCO` reads as the Top Management Group, the hub of the operation, human and AI. The readings are in [`decisions/DR-0002`](../decisions/DR-0002-the-readings-of-dr-0041.md). Nothing here is removed.

---

## 0. Identity

| Field | Value |
|---|---|
| Name | **49GAION Organisation Design and Delivery** |
| Kind | a Library product: an **assembly**, parts placed side by side and connected (`49GAION/DR-0025`, items 2 and 3; Standard §3.1, item 11) |
| Level | the first level: an organisation of human positions. The AI level is not in this product (§12) |
| Code | none. A product of the Library takes no code; its parts keep theirs (Naming Standard R1, R4, R12) |
| Parts | Source Lifecycle, Target Operating Model, Process and Position Design, Delivery and Implementation (§2) |
| Connections | the release notice contract, from each stage to the next; the design return contract, from each later stage to the stage whose release it reads; the sockets contract of Source Lifecycle, from Source Lifecycle to every stage (§4) |
| Shared test | TEST-DESIGN-CHAIN v2, 15 cases, in the Library register (§10) |
| This repository | `github.com/49g-holding/49GAION-organisation-design-and-delivery`, public. It holds this blueprint and its pins only; no organisation's data, no copy of a part (`decisions/DR-0001`) |
| In an organisation | each organisation installs the four parts as its own AIOCs, `[ORG]AIOC-SL`, `[ORG]AIOC-TOM`, `[ORG]AIOC-PPD` and `[ORG]AIOC-DI`, each from its mother, and keeps its own values in its own repositories. Its branded name is its own (for example `[ORG]AION Organisation Design and Delivery`) |
| Version and status | `v0.1.3` · draft |
| Mother texts | the Standard §3.1, items 3 to 12; the Operating Protocol §13, §17, §19, §20 and §21; the Library register, `49GAION-protocol` `library/README.md` at `32734f1` |

---

## 1. Why one product

1. **Built from the smallest units** (Standard §1.7, item 16; `49GAION/DR-0025`, item 1). Each part is built once and kept, with its own blueprint, card, fixed test, repository and version. A product is made by combining parts, never by rebuilding them.
2. **Each part stands alone** (Protocol §21, item 1; Standard §3.1, item 10). Source Lifecycle is offered alone. The Target Operating Model "is a product on its own" (Protocol §19, item 9). Delivery and Implementation runs without any other part, behind its own gateway (Protocol §20, item 11).
3. **This set is one product because its input and its output are known.** It starts from the organisation's own sources and ends with a decided design of human positions, taken into a running organisation. No part alone covers that whole way.
4. **A part may serve in more than one product** (`49GAION/DR-0025`, item 3). Source Lifecycle also serves in 49GAION Organisation Memory, beside the Operations Event Register (Standard §3.1, item 14). The Operations Event Register is **not** a part of this product.

---

## 2. The parts, by pin

The pins are in `pins/PINS.json` and equal the Library register at `47fb6e1`. `tools/check_pins.py` reads every file back at its commit, checks its SHA-256, and checks that each part's pin equals its row in the Library register (TEST-DESIGN-CHAIN v2, case 10).

| # | Part | In an `[ORG]AION` | Mother repository · path | Version | Commit | Blueprint SHA-256 | Library card | Fixed test |
|---|---|---|---|---|---|---|---|---|
| 1 | 49GAION Source Lifecycle | `[ORG]AIOC-SL` | `49g-holding/49GAION-source-lifecycle` · `blueprint/SL-BLUEPRINT.md` | v0.1.6 | `17f60d1` | `0068e9c0…2ad3` | v4 | TEST-SL v1, 95 cases |
| 2 | 49GAION Target Operating Model | `[ORG]AIOC-TOM` | `49g-holding/49GAION-target-operating-model` · `blueprint/TOM-BLUEPRINT.md` | v0.6.3 | `3b0f5e3` | `07d58284…71ba` | v3 | TEST-TOM v5, 123 cases |
| 3 | 49GAION Process and Position Design | `[ORG]AIOC-PPD` | `49g-holding/49GAION-process-and-position-design` · `blueprint/PPD-BLUEPRINT.md` | v0.5.3 | `d3a6c48` | `b5146e80…3958` | v4 | TEST-PPD v3, 110 live cases |
| 4 | 49GAION Delivery and Implementation | `[ORG]AIOC-DI` | `49g-holding/49GAION-delivery-and-implementation` · `blueprint/DI-BLUEPRINT.md` | v0.2.3, complete (slices 1 to 4) | `e952c80` | `b340abed…6998` | v3 | TEST-DI v1, 94 cases |

**A new version of a part** moves only its pin here; the shared test runs again (`49GAION/DR-0025`, item 3). The part's own blueprint governs everything about the part; this text only says how the parts are put together.

---

## 3. How the product works, step by step

The order is Source Lifecycle, then the Target Operating Model, then Process and Position Design, then Delivery and Implementation (Protocol §21, item 1). No stage waits for a later one.

### Step 0 · Set up

| What | Who | Rule |
|---|---|---|
| Name the **Requesting Authority**: the Cell carrying `[ORG]HOAC-GOV`, or a human Cell it delegates the design decisions to | the GOV position | TOM H-01, PPD H-01, DI H-01. One Requesting Authority for the whole product (§7) |
| The four accountable positions, each carrying `[ORG]HOAC-ACS`: the Source Lifecycle Lead `[ORG]CELL-SLL`, the TOM Design Lead `[ORG]CELL-TDL`, the PPD Design Lead `[ORG]CELL-PDL`, the DI Delivery Lead `[ORG]CELL-DDL` | who holds them, and how: the organisation's own mechanism, outside the system | SL H-01, TOM H-11, PPD H-02, DI H-02. Positions only (`49GAION/DR-0049`) |
| Install the four parts, each through OCO | the Cell carrying `[ORG]HOAC-TM` | Standard §5.3; each part's §13 |
| Sign the connections (§4) | the `[ORG]HOAC-ACS` position over the stage whose releases each connection serves | Protocol §21, item 7; listed type `connect-external-port` |
| Set the product's parameters (§7) | as §7 says | each part's §15 |

### Step 1 · The sources: Source Lifecycle

- **In.** The organisation's documents (files, archives, folders, a corpus import with its manifest), and what its people say, typed or spoken. A spoken account is recorded only after its contributor approves an exact preview, item by item. Silence and "yes to all" record nothing. Every contributor first accepts an agreement (SL §4.3, §5.1).
- **The Design Request.** A source in Source Lifecycle, approved by the Requesting Authority. It holds nine fields: the requesting seat, the entities in view, what should be different, why now, the known limits, what is out, the request kind, the earlier release it continues, and the run depth (light, standard or deep). With no written brief, Source Lifecycle's Chief of Staff builds it through explainers (TOM `docs/ASKING-CATALOGUE.md`, DRQ-01; `docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §1.4).
- **Beside it.** The **essentials checklist**: strategy, plan, measures, structure of positions, processes, meetings, dictionary. Source Lifecycle shows the essentials still missing beside the Design Request; it flags them and never drafts them (SL Annex F.2). The **organisation dictionary** is served by reference to every stage (SL Annex F.1).
- **Out.** Sources by reference: ID, version, SHA-256, held or not held, at a pinned snapshot `SLM-<sha256>` (SL §5.8; Protocol §13, item 9).

### Step 2 · The operating model: Target Operating Model

- **Starts** from one Work Item of the Requesting Authority's Cell that carries only the reference of an approved Design Request (TOM §1, §6). Gate T0 checks, among others, that the connections are signed, Source Lifecycle's card declares the sockets contract, and enough engines are eligible: at least three reviewer engines from at least two families, none of an author's family (TOM Annex C.2 (g); TOM H-05).
- **Reads** only sources served by reference from Source Lifecycle, sealed into an Input Pack. It asks what is missing only through Source Lifecycle's Chief of Staff, at most twelve rows a pass (TOM §4.3, §5.2; Protocol §19, items 2 and 3). Where the organisation admitted an export of its running work by role-type and process, it reads it as the activity profile; with none, it reads `no observation` (TOM Annex H.8).
- **Produces** the TOM Release: the Design Brief; the decided structure and slice; per entity, the Blueprint and the Rationale and Evidence Brief (capabilities with their delivery model and maturity, value streams with their criticality, decision domains, interfaces); hand-offs, counterparties and the legal and regulatory perimeter; the **role register** (role-types only); the strategy frame; the outside parties' journeys; the value case; the priority of every element; the activity profile; the walkthrough report and the quality checks (TOM `docs/OUTPUT.md`; Protocol §19, items 4 and 12).
- **Decided** element by element by the Requesting Authority, `ACCEPT`, `CORRECT` or `REJECT`, each with a priority (must, should or could), then the value case and the final status. Purpose and values, where no source in force states them, are signed by the GOV Cell (Protocol §19, item 12). Silence decides nothing (TOM §5.9; Annex C.4).
- **Filed** in Source Lifecycle as origin kind `operating model`. Once it reads back, a **release notice** goes to Process and Position Design (TOM step 8a; Protocol §21, item 3).

### Step 3 · Processes and positions: Process and Position Design

- **Starts** from a Work Item that carries one TOM Release reference. The release is admitted only if its manifest validates, its status is decided, its hash equals the copy filed in Source Lifecycle, and its role register re-compiles (PPD §4.3, part 3).
- **Reads** the role register first, then every value-stream phase, capability, decision domain, hand-off and crossing, the strategy frame, journeys, value case, activity profile, delivery models, maturity, criticality and priority. Other sources come only from Source Lifecycle; questions go only through its Chief of Staff (PPD §5.1, §5.2).
- **Produces** the PPD Release: process architecture (levels 1 to 3), the process book, the policy register (names, not texts), the position register with job families and levels, **job descriptions** with competence profiles, the decision-rights register and authority matrix, reporting lines and organisation charts, the forum register and review calendar, the **crosswalk** from today's organisation, the workload register, the controls catalogue and segregation-of-duties check, the objectives cascade, the peak-load check, the unit register and unit charters, and the Decision Package (PPD Annex A).
- **Decided** element by element by the Requesting Authority (PPD §5.10, rule 1). The release holds no person, no pay, nothing on what fills a position and no policy text (PPD §5.10, rule 4).
- **Filed** in Source Lifecycle as origin kind `process and position design`. A release notice goes to Delivery and Implementation, naming the TOM release it rests on (Protocol §17, item 12).

### Step 4 · Into a running organisation: Delivery and Implementation

- **Starts** on the Requesting Authority's request, which opens the run, its mode and its scope (Protocol §20, item 2; DI H-09). In mode A, once the PPD release notice has arrived, it reads the PPD release, and the TOM release it rests on, by reference from Source Lifecycle (DI §4.3, part 1).
- **Slice 1, Launch.** Admit, map, diagnose, prepare, decide and file:
  - the design map;
  - the gap report in two tiers;
  - the health check;
  - the procedures under each process;
  - briefs for counsel and finance: policies, pay structure, contract templates, authority instruments, obligations register, control matrix, systems, data and suppliers;
  - a cost draft, every amount cited;
  - the transition plan and go-live criteria;
  - the Decision Package (DI Annex A.1 to A.8).
- **Slice 2, Accompany and Operate.** Implementation plan, change impact, learning paths, readiness, rehearsal, the go or no-go package, stabilisation; then one operating rhythm with single logs, forum packs, measures, versions and a value register with gates L0 to L5 (DI Annex A.9 to A.19).
- **Slice 3, Improve.** Conformance, proposals and trials, the quarterly health check, hand-over and a yearly drill that proves the organisation runs without DI (DI Annex A.21 to A.24).
- **Decided** by the organisation's deciding positions: the Requesting Authority, the go or no-go position, counsel, finance, data protection, the owner, process owners and forum chairs. DI decides nothing; a draft enters a record only when a position inserts it (DI §5.10; Annex G).
- **Filed** in Source Lifecycle as origin kind `delivery and implementation`, the launch package and each later decided version of the living design.

### Returns · every defect goes back to the stage that made it

- A later stage that finds a defect in a release returns it, directly, to the stage that made the release, under the design return contract, with a filed copy of the same hash in Source Lifecycle as a `design report`. Process and Position Design returns to the Target Operating Model; Delivery and Implementation returns process, position, unit and control defects to Process and Position Design, and operating-model defects to the Target Operating Model (Protocol §21, item 4).
- Only the elements a return touches are held; the rest of the work goes on.
- **Every return ends**, in one of four ends: answered by release, answered by decision, set aside by decision (carried forward as a known defect or a decided assumption), or withdrawn. Past its deadline or its rounds, it goes to the Requesting Authority and the Cell carrying `[ORG]HOAC-TM`. Silence ends nothing (Protocol §21, item 5).
- **No loop.** A return is answered on its own Work Item; no stage opens a new item back (Protocol §21, item 6).

### Throughout

- **One home.** Every release is frozen, content-addressed and filed in Source Lifecycle; every stage reads every other by reference. No stage keeps or edits another's release (Protocol §21, item 2).
- **What one stage leaves open, no later stage fills** (`49GAION/DR-0023`, item 6; Protocol §21, item 12).
- **The priority and the value case of the operating model** reach Process and Position Design and Delivery and Implementation unchanged (Protocol §21, item 12).
- **Checked by many engines.** Every step after Source Lifecycle is checked by three or more engines from two or more model families, each alone first; code settles; no vote (Protocol §21, item 8).
- **Positions only.** No output names a person, and no record of the work about a person enters any stage (Protocol §21, items 9 and 12).

---

## 4. The connections

| From | To | What passes | Contract (pinned in `pins/PINS.json`) | Signed by |
|---|---|---|---|---|
| Source Lifecycle | every later stage | sources by reference at a pinned snapshot; answers to needs requests; notices on supersession, revocation or reclassification; the write scope to file the stage's own origin kinds | the sockets contract: needs request, needs answer, needs status, Missing Report, source reference, filing receipt (drafts in `49g-holding/49GAION-target-operating-model` `4271eb5`, named by hash in SL `contracts/README.md`; Proposed until SL H-02) | the Source Lifecycle Lead, at the tool gateway, as one organisation-design grant per stage: read, filing of its own kinds, needs requests (SL §5.8) |
| Target Operating Model | Process and Position Design | the release notice: the release (ID, version, manifest hash), the releases it rests on, the filed reference, the final status, the release it supersedes and the returns it answers; no release text (Protocol §21, item 3) | release notice (`library/contracts/release-notice.schema.json`) | the TOM Design Lead |
| Process and Position Design | Delivery and Implementation | the release notice, naming the TOM release it rests on | release notice | the PPD Design Lead |
| Process and Position Design | Target Operating Model | a design return | design return (`library/contracts/design-return.schema.json`) | the TOM Design Lead: the connection that serves TOM's releases to PPD (TOM H-35; PPD H-06) |
| Delivery and Implementation | Process and Position Design; Target Operating Model | a design return | design return | the PPD Design Lead for the connection that serves PPD's releases to DI (PPD H-16); the TOM Design Lead for the connection that serves TOM's releases to DI (TOM H-35; DI H-05) |

A return travels on the same connection as the notice it answers: each connection is signed by the `[ORG]HOAC-ACS` position over the stage whose releases it serves (Protocol §21, item 7).

**What each stage may file in Source Lifecycle** (Protocol §13, item 9; SL §5.8):

| Stage | Origin kinds |
|---|---|
| Target Operating Model | `operating model`; `design report` |
| Process and Position Design | `process and position design`; `design report` |
| Delivery and Implementation | `delivery and implementation`; `design report` |

**A revocation** takes effect at once; after it, a notice or return through that link is refused at the gateway, and each stage still runs alone (Protocol §21, item 7; TEST-DESIGN-CHAIN v2, case 7).

---

## 5. What goes in

| Input | Enters through | Required |
|---|---|---|
| The organisation's documents | Source Lifecycle's Input socket, one converter per type, under a contributor agreement | no: an organisation with no documents starts from conversation |
| What its people say | Source Lifecycle's Conversation Recorder, preview and approval item by item | no |
| The Design Request | a source in Source Lifecycle, approved by the Requesting Authority | **yes**, to start the Target Operating Model |
| Answers to questions | needs requests, only through Source Lifecycle's Chief of Staff; a non-delegable row goes only to its position | as each stage asks |
| The running work, by role-type and process | an export in Source Lifecycle, after its impact assessment and the decision of the position that holds data protection (HF-17); one that says who did the work is refused | no; without it the stages read `no observation` |
| A design made elsewhere | a source in Source Lifecycle, read by Delivery and Implementation in mode B | no (§8) |

---

## 6. What comes out

**At each stage**, a decided release, filed in Source Lifecycle and read by reference:

| After | The organisation holds |
|---|---|
| Source Lifecycle | its sources, each with one valid version and a traceable origin; its dictionary; its essentials checklist; an approved Design Request |
| Target Operating Model | a decided operating model: what it does, for whom, how it is governed, with its role register, strategy frame, journeys, value case and priorities |
| Process and Position Design | decided processes, positions with job descriptions, units, decision rights and authority matrix, controls, workload and the crosswalk from today |
| Delivery and Implementation | a decided launch package; then go-live decided by its position, stabilisation, one operating rhythm, a living design with each decided version filed, a value register traced to the value case, the capability handed over, and a full export that re-imports with every trace |

**What is left to the organisation** (DI §5.12; Annex G): every decision and signature; every task of the implementation plan, each owned by a position; final legal texts by its counsel and every amount by its finance; consultation with workers and every statement or notice; appointing and hiring people into positions; paying; and marking physical steps done.

**What it is for.** To design an organisation of human positions from the organisation's own sources, decided by its own positions, and to take that design into a running organisation, with every element traced to a source or a decision. It serves a new organisation and an existing one; the crosswalk and the transition plan carry an existing one from today's organisation to the designed one.

---

## 7. What the product sets

Each part keeps its own Configuration (each part's §15). The product sets only what must be the same across its parts, so that one organisation runs one product:

| Setting | Value for the product | Set by | Parts it sets |
|---|---|---|---|
| `requesting_authority_cell` | one Cell for all three design stages: the GOV Cell or one human Cell it delegated the design decisions to | the GOV position | TOM, PPD, DI |
| The four accountable positions | arranged before the first run | the Cell carrying `[ORG]HOAC-TM` | all |
| `return_round_deadline`, `return_rounds_max` | one value across TOM, PPD and DI, so that every return in the chain ends on the same rule | the Cell carrying `[ORG]HOAC-TM` | TOM, PPD, DI |
| `review_engines`, `review_families_min` | the same floor in every stage: at least 3 engines from at least 2 families | each part's own Lead, within the floor (each part's §15) | TOM, PPD, DI |
| `reduced_review_permitted` | `no` in every stage | the Cell carrying `[ORG]HOAC-TM` | TOM, PPD, DI |
| `rows_per_pass` | at most 12 rows a pass in every stage, since every question goes through Source Lifecycle's one Chief of Staff | each part's own Lead, within the floor | TOM, PPD, DI |
| `non_response_passes` | one value across the stages | the Cell carrying `[ORG]HOAC-TM` | TOM, PPD, DI |
| The engine register | one register, at the tool gateway, for every stage | the GOV position with the Cell carrying `[ORG]HOAC-TM` | all |
| The pins of the parts | `pins/PINS.json` | 49GAION, by pull request | all |
| Which parts are installed, and which runs are opened | §8 | installing: the Cell carrying `[ORG]HOAC-TM` (TOM H-10, PPD H-03, DI H-03); opening a run: the Requesting Authority | all |

**The parameters an organisation chooses for each use** (the parts' own settings, named here so the whole is visible):

| Parameter | Where | Values |
|---|---|---|
| Run depth | the Design Request, field 9; capped by `run_depth_permitted` | light, standard (default) or deep (TOM Annex F) |
| Cost limit | `budget_cap`, `review_budget_per_run` | set by the Cell carrying `[ORG]HOAC-TM`; at the limit the run is held |
| Entities in view and slice | the Design Request; TOM S1 (entities) and S2 (the slice; TOM H-21) | a continuation release holds every slice designed so far, carried forward by hash (TOM `docs/OUTPUT.md` §14) |
| Mode into delivery | DI `modes_enabled` | A (the decided releases), B (a design made elsewhere), C (no design, a light design with the owner; enabled only after DI H-21) |
| Default confidentiality and the contributor agreement | Source Lifecycle | set by the GOV Cell (SL H-03, H-04) |
| Reference models | each design stage's catalogue pin | unavailable, or a pin by commit and SHA-256; a method, never evidence |
| Structure scenarios | PPD `structure_scenarios` | 1 (default) to 3 |
| Language | DI `language` | the organisation's |

---

## 8. Ways to use the product

The organisation may stop after any stage, and no stage waits for a later one (Protocol §21, item 1). Every stage after the first reads Source Lifecycle; Process and Position Design needs a decided TOM release, and Delivery and Implementation in mode A needs both releases (`upstream/PROPOSALS.md`, item 5).

| Use | Stages | Output |
|---|---|---|
| **The whole product** | SL → TOM → PPD → DI (mode A) | a decided design of human positions, taken into a running organisation |
| **Design only** | SL → TOM → PPD | a decided operating model, processes and positions; no launch |
| **Operating model only** | SL → TOM | a decided operating model, or only its decided Design Brief, or a Readiness Report (TOM `docs/OUTPUT.md` §14) |
| **Bring your own design** | SL → DI (mode B) | a design made elsewhere, mapped onto the structure of positions and processes without rewriting it, taken into a running organisation |
| **Small business** | SL → DI (mode C) | a light design built with the owner, every element provisional, taken into a running organisation; grows into mode A at its growth triggers. Mode C stays off until DI H-21 |
| **Sources only** | SL | the organisation's sources, dictionary and essentials, as a product on its own |

**Another source in place of Source Lifecycle, in later phases.** In the stages after the first, another source of documents or knowledge may stand beside Source Lifecycle, read only, through the reading stage's own adapter, once it uses the same sockets and passes the joining test. It answers by reference (ID, version and hash), "held" or "not held", within the approved scope (Protocol §13, item 7; SL §2.2). Asking and filing stay with Source Lifecycle. A source that **replaces** Source Lifecycle needs the Protocol first to name the new asking route (Protocol §13, item 10); none is named yet (`upstream/PROPOSALS.md`, item 3).

**A part replaced by another part.** Built like a puzzle (Protocol §2): any other part may be replaced by one that offers the same ports and contracts, once it passes the joining test (Standard §3.2, item 4; Protocol §11, item 1). Its pin moves here, and the shared test runs again.

---

## 9. The decisions the product needs, by position

| Position | Decides |
|---|---|
| The GOV position | names the Requesting Authority; signs purpose and values where no source in force states them; sets the default confidentiality and the contributor agreement; the engine register, with the Cell carrying `[ORG]HOAC-TM` |
| The Cell carrying `[ORG]HOAC-TM` | arranges the four accountable positions; installs the parts; sets the budgets, the permitted run depth, reduced review, the non-response and return settings, and the modes of delivery |
| Each accountable position over a part (its Lead) | signs the connections that serve its part's releases (§4); sets its part's review engines and rows per pass within the product's floor; attests its part's method |
| The Requesting Authority | approves the Design Request; opens each run; decides every element row and the final status of every release; decides each return row; opens the delivery service |
| The position that holds data protection (HF-17) | admits each export of the running work, after its impact assessment |
| The go or no-go position | decides the go-live |
| Counsel, finance, the owner, process owners, forum chairs | decide what Delivery and Implementation puts to them |

---

## 10. The shared test

**TEST-DESIGN-CHAIN v2**, 15 cases, held in the Library register (`49GAION-protocol` `library/README.md`, at `47fb6e1`). It is the product's one shared test (`49GAION/DR-0025`, item 4). This repository keeps no copy. Each part's own fixed test passes first (case 11). Every case reads `NOT_RUN` until the parts are built and run.

In short, the cases cover:

1. each stage alone;
2. filing and read-back;
3. the notices;
4. returns to the stage that made the release;
5. every return ends;
6. no loop;
7. revocation;
8. many engines;
9. no person named;
10. the pins read back;
11. the four stages together;
12. the dictionary;
13. what is left open stays open;
14. the priority and the value case unchanged;
15. nothing about a person.

**Run here on every pull request.** Case 10 runs on every pull request of this repository: `tools/check_pins.py` reads back every part and contract at its pinned commit and checks its SHA-256.

---

## 11. What must be true before the first real run

These come from the parts' own texts. Until each holds, the joining test of the part concerned fails.

1. **Source Lifecycle adopts its sockets contract** (SL H-02, PRD D-20). Until then the Target Operating Model's gate T0 fails with `SL contract not supported`.
2. **Each stage's additions to Source Lifecycle are accepted**: TOM's SL-A1 to SL-A13 (TOM H-15), PPD's and DI's origin kinds (PPD H-05, DI H-04).
3. **The connections are signed** by the accountable positions (§4).
4. **In an `[ORG]AION`**, the Charter is installed first and holds the tool gateway, the records and the Work Item queue (Protocol §23). Outside an `[ORG]AION`, Delivery and Implementation runs behind its own gateway, which fails closed (DI §8); Source Lifecycle may run with no gateway (SL §15, `gateway present: no`; SL H-05); the Target Operating Model and Process and Position Design assume one.
5. **Enough engines are eligible** in the engine register: at least three reviewer engines from at least two families, none of an author's family; with two author families that means at least four families (TOM Annex C.2 (g); TOM H-05).
6. **The positions are arranged** and the Requesting Authority is named (§3, step 0).

---

## 12. The next level, not in this product

This product designs an organisation of **human positions**. It does not decide which positions an AI fills, which a human fills, or which both fill (`49GAION/DR-0025`, item 5). That is the next level, the path of an `[ORG]AION`. It will read this product's decided releases (the role register, the processes, the positions and the units) as its input. Nothing in this blueprint prepares or limits that level.

---

## 13. Lessons and gaps found while writing it

Each is a draft for 49GAION, in `upstream/PROPOSALS.md`, not yet proposed. None changes a part here.

---

## 14. Change log

| Version | Date | Change |
|---|---|---|
| v0.1.0 | 2026-10-20 | First blueprint of 49GAION Organisation Design and Delivery, the first assembly of the Library (`49GAION/DR-0025`), in its own repository (`decisions/DR-0001`): the parts by pin at the Library register `32734f1`, the steps, the connections, the input and the output, what the product sets, the ways to use it, the decisions by position, the shared test TEST-DESIGN-CHAIN v2, and what must hold before the first real run |
| v0.1.1 | 2026-10-25 | The pins of Target Operating Model, Process and Position Design and Delivery and Implementation, and of the sockets contract drafts, move to the parts' own mother repositories at their merged commits (`49GAION/DR-0044`; `decisions/DR-0003`); the Library register pin moves to `26d7443`. Every path, version and SHA-256 unchanged; no rule changes |
| v0.1.2 | 2026-10-29 | Released on the governing seat's word (`decisions/DR-0005`): it carries the records since v0.1.1, `decisions/DR-0002` (the readings of `49GAION/DR-0041`) and `decisions/DR-0004` (positions only, `49GAION/DR-0048`, `DR-0049`). The pins of the four parts move to their releases of 29 October 2026 at their merged commits (Source Lifecycle v0.1.5, Target Operating Model v0.6.2, Process and Position Design v0.5.2, Delivery and Implementation v0.2.2), equal to the Library register at `d44e4fc`; the contract pins are unchanged; the Protocol pin moves to the Operating Protocol `v2.1.0`. No other rule changes. |
| v0.1.3 | 2026-10-29 | Released on the governing seat's word (`decisions/DR-0006`). The pins of the four parts move to their releases under `49GAION/DR-0052` at their merged commits (Source Lifecycle v0.1.6, Target Operating Model v0.6.3, Process and Position Design v0.5.3, Delivery and Implementation v0.2.3), equal to the Library register at `47fb6e1`; the contract pins are unchanged; the Protocol pin moves to the Operating Protocol `v2.2.0` (`afc91b6`), and the checks gain `links`. It also carries the removal of the withdrawn wording from `upstream/PROPOSALS.md`, on `main` since `v0.1.2`. No rule of this product changes. |

*49GAION Organisation Design and Delivery · product blueprint v0.1.3 · Powered by 49GAION*

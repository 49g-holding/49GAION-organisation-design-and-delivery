# DR-0004 · Organisation Design and Delivery product: positions only, brought into line with 49GAION/DR-0048 and DR-0049

- **Date:** 2026-10-28
- **Decided by:** the governing seat (GOV) of 49GAION
- **Source:** `49GAION/DR-0048`, the complete definition `v2.1.0`: the system recognises only AI, organised in AIOCs, and human positions carrying a HOAC label; no natural person and no person's name is recorded in it; each organisation's own mechanism, outside the system, decides how its positions are assigned and administered and who holds them. `49GAION/DR-0049` brings the texts into line. The record is prepared by the AI hub; the governing seat's merge is the decision.
- **Relation:** builds on DR-0003. Where an earlier record of this repository sets the mechanism behind a human position (who occupies it, an acting filler, a deputy, "the governance seat appoints Top Management directly"), this record supersedes it; those records are frozen and are read with this one.

## Decision

1. **Positions only.** Every human place in this repository is a position. Who holds it, and how (successors, deputies, boards and the credentials with which a position signs included), is the organisation's own mechanism, outside the system; no part of it ever sees it.
2. **Withdrawn.** The acting filler and the signature type `appoint-acting-filler`, which leaves every `authority_scope`; deputies of human seats (the positions table's Deputy column becomes Cover, which stays meaningful for AI positions); occupancy, handover and arrangement entries; the holders register; a compensating control for one person behind several positions. What stays: two positions are two parties; the Overseen link between positions; `succeeded_by`; the duty deputy, an AI part.
3. **The changes.** Each place below is changed in its file; its former wording is kept here, verbatim.

   - `blueprint/PRODUCT-BLUEPRINT.md`, under “Step 0 · Set up”, Step 0, the four accountable positions:
     ```text
     | Arrange the four accountable positions, each carrying `[ORG]HOAC-ACS`: the Source Lifecycle Lead `[ORG]CELL-SLL`, the TOM Design Lead `[ORG]CELL-TDL`, the PPD Design Lead `[ORG]CELL-PDL`, the DI Delivery Lead `[ORG]CELL-DDL` | the Cell carrying `[ORG]HOAC-TM` | SL H-01, TOM H-11, PPD H-02, DI H-02. Positions only; who occupies them is top management's own mechanism |
     ```

4. **No cards** are held in this repository.
5. **The version.** Unreleased. The blueprint keeps its version label; the version and the Library pin move at the next release, by a pull request, on the governing seat's word.

*Powered by 49GAION*

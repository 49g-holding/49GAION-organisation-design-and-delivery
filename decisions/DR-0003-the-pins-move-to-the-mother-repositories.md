# DR-0003 · Organisation Design and Delivery product: the pins move to the mother repositories

- **Date:** 2026-10-25
- **Decided by:** the governing seat (GOV) of 49GAION
- **Source:** `49GAION/DR-0044`, the mothers of the design chain in repositories of 49GAION, approved by the governing seat on 25 October 2026; the Library register of `49GAION-protocol` at `26d7443`, which re-pins the three parts.
- **Relation:** builds on DR-0001 and DR-0002; it supersedes nothing and removes nothing.

## Decision

1. **The pins move.** In `pins/PINS.json` and in the blueprint's table of parts, Target Operating Model, Process and Position Design and Delivery and Implementation are pinned at their own mother repositories, `49GAION-target-operating-model` (`4271eb5`), `49GAION-process-and-position-design` (`cfad1c5`) and `49GAION-delivery-and-implementation` (`ffec236`), at their merged commits. Each mother is a byte-identical copy of the text pinned before: every path, version and SHA-256 is unchanged.
2. **The sockets contract drafts** (needs request, needs answer, needs status, Missing Report, source reference, filing receipt), held as drafts in the Target Operating Model's repository, are pinned at the same mother repository and commit, with their SHA-256 unchanged.
3. **The Library register pin** of the shared test moves to `26d7443`, the register that carries the re-pinned rows. `tools/check_pins.py` (TEST-DESIGN-CHAIN v2, case 10) reads every file back at its new commit and compares each part with its register row there.
4. **The version.** The product blueprint is `v0.1.1`: the pins and their mentions only. No rule changes.

*Powered by 49GAION*

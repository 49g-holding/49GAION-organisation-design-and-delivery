# DR-0005 · Organisation Design and Delivery product — release `v0.1.2`

- **Date:** 2026-10-29
- **Decided by:** the governing seat (GOV) of 49GAION.
- **Source:**
  - The governing seat's word of 29 October 2026 (translated): "Finish all the work. Now check that everything is right and finished."
  - `decisions/DR-0004`: the version and the pins move at the next release, by a pull request, on the governing seat's word.
  - The record is prepared by the AI hub; the governing seat's merge is the decision.

## Decision

1. **Released.** The product blueprint takes `v0.1.2`. It carries the records since `v0.1.1`, unreleased until now:
   - `DR-0002`: the readings of 49GAION/DR-0041, the complete definition;
   - `DR-0004`: positions only, brought into line with 49GAION/DR-0048 and DR-0049.
   No other rule changes.
2. **The parts' pins.** The four parts move to their releases of 29 October 2026, each at its merged commit with its SHA-256: Source Lifecycle `v0.1.5`, Target Operating Model `v0.6.2`, Process and Position Design `v0.5.2`, Delivery and Implementation `v0.2.2`. They equal the Library register of `49GAION-protocol` at `d44e4fc`, which also holds the shared test, TEST-DESIGN-CHAIN v2. The contract pins do not change.
3. **The Protocol pin.** `PROTOCOL-PIN` and every `uses:` line of the checks move to the Operating Protocol `v2.1.0` (`a2e5f50`).

Powered by 49GAION

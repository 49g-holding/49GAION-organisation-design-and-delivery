# DR-0006 · Organisation Design and Delivery product — release `v0.1.3`

- **Date:** 2026-10-29
- **Decided by:** the governing seat (GOV) of 49GAION.
- **Source:**
  - The governing seat's word of 29 October 2026 (translated from Persian): "Check it too: see what is useful and what needs a decision, then build it all at once; combine both and go through one correction round."
  - `49GAION/DR-0052`: two reviews of `v2.1.0` corrected in one round; each mother touched took a patch version by its own record, and the Library register re-pinned them.
  - The record is prepared by the AI hub; the governing seat's merge is the decision.

## Decision

1. **Released.** The product blueprint takes `v0.1.3`. It carries the removal of the withdrawn wording from `upstream/PROPOSALS.md`, on `main` since `v0.1.2`. No rule of this product changes.
2. **The parts' pins.** The four parts move to their releases under `49GAION/DR-0052`, each at its merged commit with its SHA-256: Source Lifecycle `v0.1.6`, Target Operating Model `v0.6.3`, Process and Position Design `v0.5.3`, Delivery and Implementation `v0.2.3`. They equal the Library register of `49GAION-protocol` at `47fb6e1`, which also holds the shared test, TEST-DESIGN-CHAIN v2. The contract pins do not change.
3. **The Protocol pin.** `PROTOCOL-PIN` and every `uses:` line of the checks move to the Operating Protocol `v2.2.0` (`afc91b6`), and the checks gain `links`: every relative link resolves.

Powered by 49GAION

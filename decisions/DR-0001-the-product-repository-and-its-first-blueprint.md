# DR-0001 · The product repository of 49GAION Organisation Design and Delivery, and its first blueprint

- **Date:** 2026-10-20
- **Decided by:** the governing seat (GOV) of 49GAION
- **Sources:**
  - GOV's direction of 20 October 2026 (translated): "so that no one else gets it wrong, make a repository with this same name, and write how these four combine and work together, what the input is, what the product's output is and what it is for. Each is a product alone, but this set is also a product whose output is known and whose input is known. It also has parameters: in later phases, a similar source in place of Source Lifecycle."
  - The name: GOV's answer the same day that the name 49GAION Organisation Design and Delivery stays.
  - The rules: `49GAION/DR-0025` (Parts and Products; the first assembly), `DR-0019` (the Library register), `DR-0024` (mother repositories); Protocol §21.

## Decision

1. **This repository.** `github.com/49g-holding/49GAION-organisation-design-and-delivery`, public, is the product repository of 49GAION Organisation Design and Delivery.
   - It holds the product's blueprint and its pins only: no organisation's data, and no copy of any part.
   - It is laid out and checked like a mother repository: its pins, no organisation names, no Persian.
2. **The first product blueprint.** `blueprint/PRODUCT-BLUEPRINT.md` `v0.1.0` covers:
   - the four parts by pin;
   - how they combine and work, step by step;
   - the connections and their contracts;
   - what goes in and what comes out;
   - what the product is for;
   - what the product itself sets, and the parameters an organisation chooses;
   - the ways to use it, including another source beside Source Lifecycle;
   - the decisions by position;
   - the shared test;
   - what must hold before the first real run.

   It adds no capability: its features are its parts' features (`49GAION/DR-0025`, item 3).
3. **The level.** This product designs an organisation of human positions. Which positions an AI fills is the next level, outside this product (`49GAION/DR-0025`, item 5).
4. **The shared test.** TEST-DESIGN-CHAIN v2, held in the Library register. This repository keeps no copy. Case 10 runs here on every pull request (`tools/check_pins.py`).
5. **The Library pin.** Once merged, this blueprint is pinned in the Products section of `49GAION-protocol` `library/README.md`, by repository, path, version, commit and SHA-256. Where an assembly's blueprint lives is recorded in the 49GAION Standard by its own decision record (`upstream/PROPOSALS.md`, item 1).

*Powered by 49GAION*

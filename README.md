# 49GAION Organisation Design and Delivery

The product repository of **49GAION Organisation Design and Delivery**, the first assembly of the 49GAION Library (`49GAION/DR-0025`; Standard §3.1, item 12). Public. It holds the product's blueprint and its pins only: no organisation's data, and no copy of any part.

**What the product is.** Four Library parts, placed side by side and connected:
- **Source Lifecycle** keeps the organisation's own sources.
- **Target Operating Model** designs what the organisation does and how it is governed.
- **Process and Position Design** designs how the work runs and the positions that carry it.
- **Delivery and Implementation** takes the decided design into a running organisation.

Each part is also a product on its own.

**What goes in.** The organisation's own documents and approved words, and a Design Request approved by its Requesting Authority.

**What comes out.** A decided design of an organisation of **human positions**, decided element by element by the organisation's own positions and taken into a running organisation.

**What it does not do.** It does not decide which positions an AI fills. That is the next level.

The one-page summary is at the top of the blueprint.

## What is here

| Path | What it is |
|---|---|
| [`blueprint/PRODUCT-BLUEPRINT.md`](blueprint/PRODUCT-BLUEPRINT.md) | the product blueprint, `v0.1.0`: the parts by pin, how they combine and work, the input, the output, what it is for, what it sets, the ways to use it, the shared test |
| [`pins/PINS.json`](pins/PINS.json) | the four parts and the contracts, each by repository, path, version, commit and SHA-256 |
| [`tools/check_pins.py`](tools/check_pins.py) | reads every pin back at its commit and checks its SHA-256 (TEST-DESIGN-CHAIN v2, case 10) |
| [`decisions/`](decisions/) | the decision records of this repository |
| [`upstream/PROPOSALS.md`](upstream/PROPOSALS.md) | drafts of proposals to 49GAION, not yet proposed |

## Where other things live

- **Each part** in its own mother repository, pinned in `pins/PINS.json`: `49g-holding/49GAION-source-lifecycle`, `49g-holding/49aioc-tom`, `49g-holding/49aioc-ppd`, `49g-holding/49aioc-di`.
- **The shared test**, TEST-DESIGN-CHAIN v2, and the Library register: `49GAION-protocol`, `library/README.md`.
- **The rules**: the 49GAION Standard (`49GAION`) and the Operating Protocol (`49GAION-protocol`), §13, §17, §19, §20 and §21.
- **An organisation's own copy** of the product: in that organisation's own repositories, never here.

## Checks

On every pull request and on main (`.github/workflows/checks.yml`):

```
python3 tools/check_pins.py                                       # every pin reads back with its SHA-256
bash <49GAION-protocol>/.github/scripts/no-org-names.sh          # no organisation name, host or prefixed code
```

and no Persian or Arabic-script character in any tracked file.

*Powered by 49GAION*

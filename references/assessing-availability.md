# Assessing whether a service or feature is available

Use this page to answer "can I use X on S3NS or Berlin?", whether for a client or in a code
review. It says which source answers which question, which source wins when they disagree,
and how to word the answer.

## Four questions, four sources

"Available" covers four separate questions. They have different answers, so never merge them
into one word.

| Question | Source | Where |
|----------|--------|-------|
| Is it **documented** as supported, and with which restrictions? | The product's `tpc-differences` page, `/products` | [product-differences.md](product-differences.md), [services.md](services.md) |
| Is it **SecNumCloud 3.2 qualified** (S3NS only)? | The PREMI3NS status page | [services.md](services.md) |
| Is it **enabled for this organization**? | `gcloud services list --available` | One organization's list on one date. S3NS adds services to it over time |
| Is it **served** right now? | DNS, discovery documents, probes, a real call | [empirical-observations.md](empirical-observations.md) |

A service can be documented and qualified but missing from an organization's list, or routed
in DNS before anyone offers it. Each of these is a real situation, not noise.

## Which source wins

**The documentation is the truth until a real call proves it wrong.** It outranks discovery
documents, DNS and probes, and loses only to a functional test: a real operation that succeeds,
or fails with an explicit "not supported".

When an observation contradicts the documentation:
1. Keep the documented answer.
2. Note the contradiction, with its evidence and date.
3. Test it with a real call, if the answer matters.
4. If the documentation is wrong, open a support ticket so the page is corrected.

Within the documentation, the scraped page wins over any summary written from it. The page
carries its "Last updated" date. A hand-written section of this skill can lag behind.

## Reading a differences page

A `tpc-differences` page lists what is **unavailable**. A feature it does not list is presumed
available: say so, and suggest a test before depending on it. Features in preview are not
available.

## Verdicts

Use one of these:

- **Available.** Documented, or proven by a real call.
- **Unavailable.** Documented as unavailable, or a real call fails with "not supported".
- **Not enabled for this organization.** Documented, but missing from the organization's
  `services list --available`. The organization or the operator can enable it.
- **Routed, not offered.** The host resolves or answers, but the service is neither
  documented nor offered. S3NS routes some services before it offers them.
- **Undetectable.** No API call can show the property, for example data residency, an
  encryption default or client-side URL signing. Say that it cannot be observed, never that
  it is unavailable.
- **Not applicable.** The surface cannot exist in a sovereign region (see below).

Never write "not available on S3NS" for a service that is only missing from one
organization's list.

## Global does not mean unavailable

A sovereign universe runs the **foundational global control plane**. IAM, Resource Manager,
Cloud Billing, Cloud DNS and Compute Engine's global resources are served.

What cannot exist is the **edge tier** that depends on Google's global network: Cloud CDN,
global and classic external load balancers, global Cloud Armor policies and Anycast IPs. The
Load Balancing and Cloud Armor differences pages confirm it for those two products. Only that
tier is "not applicable".

The split runs inside one API, resource by resource. `compute` has both
`globalForwardingRules` and `forwardingRules`, `securityPolicies` and `regionSecurityPolicies`,
`globalAddresses` and `addresses`, `urlMaps` and `regionUrlMaps`. The global variant takes no
`region` parameter. Judge the regional and the global variant separately, never the whole API.

Never confuse "cannot exist here" with "not there yet". A feature that is merely absent is
unavailable, and stays a gap that can close.

## Testing on the live surface

- **Verify with a read-only call** (`list`, `get`), never with a `create`. A create fails for
  many reasons (request body, quota, permissions), so its failure says little. A list that
  returns is clear, and changes nothing.
- **A failure caused by permissions, quota or setup is not a verdict.** Only an explicit
  "not supported" or "not implemented" makes a feature unavailable.
- **A product can span several APIs.** BigQuery is `bigquery`, `bigqueryconnection`,
  `bigquerydatapolicy`, `bigquerydatatransfer` and `bigqueryreservation`, and the differences
  page marks some of them unavailable. Check the API that carries the feature.
- **A product can span API versions.** Cloud Run serves `run` v1 and v2. Check every version
  before calling a method absent.
- **A discovery document listing a method, or a host that resolves, proves nothing on its
  own.** See [empirical-observations.md](empirical-observations.md) for what each kind of
  evidence proves.

## Answering

- Name the source and its date: "the BigQuery differences page, last updated 2026-11-10, lists
  scheduled queries as unavailable."
- Keep the four questions apart: "this service is documented and in SecNumCloud
  qualification, but your organization's list does not include it yet."
- Give the evidence strength: documented, tested, or presumed from a page that does not list
  it.

# Google Cloud Dedicated (GCD) & Cloud de Confiance by S3NS — Agent Skill

An [Agent Skill](https://agentskills.io) that gives AI coding agents expertise in Google Cloud's sovereign cloud platforms - Google Cloud Dedicated (Berlin) and Cloud de Confiance by S3NS (France). Works with Claude Code, Cursor, Gemini CLI, VS Code Copilot, and any other agent that supports the agentskills standard.

These sovereign clouds are separate products from public Google Cloud, running in isolated regions with strict data residency guarantees. Developers moving from GCP regularly hit differences in service availability, API endpoints, authentication, and tooling. This skill catches those issues before they become wasted hours.

## Supported regions

| Region | Product name | Identifier | Docs |
|---|---|---|---|
| Berlin, Germany | Google Cloud Dedicated in Germany | `u-germany-northeast1` | `berlin.devsitetest.how` |
| France | Cloud de Confiance by S3NS | `u-france-east1` | `documentation.s3ns.fr` |

## What it does

When activated, the skill provides:

- Sovereign-cloud-specific guidance for architecture, authentication, Terraform, and developer tooling
- Automatic detection of public GCP patterns that won't work in sovereign clouds (wrong endpoints, unavailable services, missing universe domain config)
- Per-product difference details for available services in each region
- Multi-region awareness with region-specific identifiers (endpoints, project prefixes, SA domains, image projects)

## Installation

### Claude Code - as a project skill (recommended)

Clone the repo and symlink it into your project's `.claude/skills/` directory:

```bash
# Clone the skill repo
git clone https://github.com/romain-bailleul/gcd-skill.git

# From your project root, create the skills directory and symlink
mkdir -p .claude/skills
ln -s /path/to/gcd-skill .claude/skills/gcd
```

The skill activates automatically when Claude detects sovereign-cloud-related work in that project. You can also invoke it directly with `/gcd`.

To share with your team, commit the symlink:

```bash
git add .claude/skills/gcd
git commit -m "Add GCD skill"
```

### Claude Code - as a personal skill

Symlink into your personal skills directory so the skill is available across all projects:

```bash
git clone https://github.com/romain-bailleul/gcd-skill.git
mkdir -p ~/.claude/skills
ln -s /path/to/gcd-skill ~/.claude/skills/gcd
```

### Claude Code - as a plugin

The repo includes a `.claude-plugin/plugin.json` manifest, so it can be loaded as a plugin:

```bash
# Load via additional directory
claude --add-dir /path/to/gcd-skill

# Or place in skills dir and it auto-loads as a skills-directory plugin
mkdir -p ~/.claude/skills
ln -s /path/to/gcd-skill ~/.claude/skills/gcd
```

### Gemini CLI / Antigravity

Clone the repo and symlink it into your personal Gemini skills directory (`~/.gemini/skills/`):

```bash
git clone https://github.com/romain-bailleul/gcd-skill.git
mkdir -p ~/.gemini/skills
ln -s /path/to/gcd-skill ~/.gemini/skills/gcd
```

### Cursor / VS Code Copilot / Other agents

The skill follows the open [agentskills.io](https://agentskills.io) standard and requires no agent-specific configuration:

```bash
# Project-level skill (Cursor, Copilot, Windsurf, etc.)
mkdir -p .claude/skills
ln -s /path/to/gcd-skill .claude/skills/gcd
```

Or copy/symlink `SKILL.md` and the `references/` directory into your agent's custom instructions or skills directory.

## Structure

```
gcd-skill/
  SKILL.md                              # Main skill (agentskills standard)
  .claude-plugin/
    plugin.json                         # Claude Code plugin manifest
  references/
    overview.md                         # Architecture, regions, zones, sovereignty model
    key-differences.md                  # Top-level sovereign cloud vs public GCP differences
    services.md                         # Available services and limitations
    product-differences.md              # Per-product sovereign cloud vs GCP differences
    authentication.md                   # Identity, credentials, ADC, tokens
    developer-guide.md                  # gcloud CLI, client libraries, API endpoints
    terraform.md                        # Terraform/IaC configuration
    organization-setup.md               # Org setup, IdP, Fabric FAST toolkit
    quotas.md                           # Quota management, monitoring, CLI
    gotchas.md                          # Critical pitfalls and common mistakes
    empirical-observations.md           # Dated facts from probing the live S3NS API surface
  scripts/
    scrape-gcd-docs.py                  # Documentation scraper (HTTP SSR + optional Playwright)
    sync-skill.py                       # Synchronizes SKILL.md, references/, and README.md from scraped docs
    check-skill.py                      # Integrity checks on what agents load (run in CI)
    docs-release-note.py                # Writes the daily note of what changed in the scraped docs
  docs-changes/                         # One release note per day the docs changed (YYYY-MM-DD.md)
  docs-raw/                             # Scraped Berlin (GCD) docs
    _manifest.json                      # Page inventory with metadata
    _last_updated.json                  # Per-page last-updated dates
  docs-raw-s3ns/                        # Scraped S3NS (Cloud de Confiance) docs
    _manifest.json
    _last_updated.json
    _secnumcloud_status.json            # PREMI3NS SecNumCloud 3.2 qualification catalog
  LICENSE                               # Apache-2.0
```

## Documentation coverage

The skill's reference files are synthesized and automatically synchronized from scraped pages covering both sovereign cloud documentation sites (`/products`, `/release-notes`, `/docs/*`, and all product documentation hubs).

### Reference files

| Reference file | Content |
|---|---|
| `product-differences.md` | Per-product sovereign cloud vs GCP differences across all 38 product `tpc-differences` pages (Compute, BigQuery, Bigtable, Cloud Run, GKE, IAM, Secret Manager, Composer, Managed Spark, Filestore, Storage Transfer, Networking, etc.) |
| `services.md` | Complete catalog of available and unavailable services by Technology Area, plus auto-synced documentation inventory |
| `terraform.md` | Provider config, state storage, resources, best practices |
| `quotas.md` | Quota management, monitoring, gcloud CLI examples |
| `authentication.md` | Workforce Identity Federation, ADC, tokens, client libraries |
| `developer-guide.md` | gcloud CLI setup, client libraries, API endpoints, Discovery API |
| `overview.md` | Architecture, universes, regions, zones, billing, support |
| `organization-setup.md` | Org setup paths (minimal/basic/enterprise), IdP, Fabric FAST |
| `key-differences.md` | Comprehensive top-level sovereign cloud vs GCP differences |
| `gotchas.md` | Synthesized from all sources |
| `empirical-observations.md` | Dated, evidence-backed facts from probing the live S3NS API surface (discovery documents, DNS, status codes, offered services) |

### Technology Areas covered

Every item in the sovereign cloud docs "Technology Areas" menu is covered:

- Access and resource management
- AI and ML (Agent Platform / BigQuery ML)
- Application development
- Application hosting
- Compute
- Data analytics
- Databases
- Networking technologies
- Observability and monitoring
- Security
- Storage
- Infrastructure as code
- SDK, languages, frameworks, and tools

### Per-product differences covered

Each available service has its `tpc-differences` page plus region-specific sub-pages scraped and synchronized into `references/product-differences.md`:

<!-- AUTO-SYNC:COVERAGE-TABLE:START -->
Total scraped pages: **436** in `docs-raw/` (Berlin GCD) and **435** in `docs-raw-s3ns/` (S3NS Cloud de Confiance).

| Product | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Includes |
|---|---:|---:|---|---|
| Access Context Manager | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, access levels, policies |
| Access Transparency | 7 | 7 | Qualification en cours | Landing, overview, logs, access approvals |
| Agent Platform (Gemini Enterprise Agent Platform) | 7 | 7 | Qualification en cours | Landing, differences, Model Garden, online inference, open-weight models |
| API Keys | 4 | 4 | — | Landing, API key restrictions, quotas, REST reference |
| Artifact Registry | 6 | 6 | Qualifié SecNumCloud 3.2 | Landing, differences, Docker/Apt/NPM/Yum, access control, quickstarts |
| BigQuery | 16 | 16 | Qualifié SecNumCloud 3.2 | Landing, differences, bq CLI, quotas, quickstarts, data loading, reservations |
| Bigtable | 14 | 14 | Qualification en cours | Landing, differences, instances, replication, backups, CMEK, change streams |
| Cloud Armor | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, security policies, WAF rules, rate limiting |
| Cloud Billing | 7 | 7 | — | Landing, differences, BigQuery billing export, access control |
| Cloud DNS | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, private zones, records, forwarding, peering |
| Cloud Interconnect | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, Dedicated & Partner Interconnect, MACsec |
| Cloud KMS | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, software keys, EKM, CMEK, key import |
| Cloud Load Balancing | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, regional Application & Network Load Balancers |
| Cloud Logging | 10 | 10 | Qualifié SecNumCloud 3.2 | Landing, differences, audit logs, log buckets, sinks, queries |
| Cloud Monitoring | 4 | 4 | Qualifié SecNumCloud 3.2 | Landing, differences, PromQL, Prometheus export, client libraries |
| Cloud NAT | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, Public NAT, GCE/GKE configuration |
| Cloud NGFW | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, firewall rules, hierarchical & network policies |
| Cloud Quotas | 29 | 29 | Qualification en cours | Landing, differences, quota viewing, adjustment requests, REST API |
| Cloud Router | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, regional dynamic BGP routing |
| Cloud Run | 14 | 14 | Qualification en cours | Landing, differences, container services & jobs, Direct VPC egress |
| Cloud SQL | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, MySQL & PostgreSQL Enterprise Plus, C3 series |
| Cloud Storage | 10 | 10 | Qualifié SecNumCloud 3.2 | Landing, differences, single-region buckets, uploads, FUSE, HMAC |
| Cloud VPN | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, HA VPN topologies and tunnels |
| Compute Engine | 12 | 12 | Qualifié SecNumCloud 3.2 | Landing, differences, C3/M3/A3 VMs, Hyperdisk, Shielded VM, OS images |
| Container-Optimized OS | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, H100 GPU drivers, release notes |
| Filestore | 16 | 16 | Qualification en cours | Landing, differences, Regional tier NFS, Direct Peering, GKE CSI |
| Google Kubernetes Engine (GKE) | 9 | 9 | Qualifié SecNumCloud 3.2 | Landing, differences, Autopilot clusters, Workload Identity, Storage FUSE |
| IAM | 18 | 18 | Qualifié SecNumCloud 3.2 | Landing, differences, Workforce/Workload Identity, service accounts, custom roles |
| Managed Airflow (Cloud Composer 3) | 18 | 18 | Qualification en cours | Landing, differences, Composer 3 HA environments, DAGs, plugins |
| Managed Service for Apache Spark (Dataproc) | 10 | 10 | Qualification en cours | Landing, differences, GCE Spark clusters (image 2.3+), jobs, CMEK |
| Network Service Tiers | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, Premium Tier overview |
| Organization Policy | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, managed & custom constraints |
| Pub/Sub | 11 | 11 | Qualifié SecNumCloud 3.2 | Landing, differences, topics, push/pull subscriptions, IAM |
| Resource Manager | 11 | 11 | Qualifié SecNumCloud 3.2 | Landing, differences, organizations, folders, projects, tags |
| Secret Manager | 10 | 10 | Qualification en cours | Landing, differences, global & regional secrets, v1 API, CMEK |
| Service Usage | 9 | 9 | Qualifié SecNumCloud 3.2 | Landing, differences, enabling/disabling services, REST reference |
| Storage Transfer Service | 7 | 7 | Qualification en cours | Landing, differences, GCS transfers, agent-based S3 transfers |
| Terraform | 32 | 32 | — | Landing, differences, provider universe_domain, GCS state backend |
| VPC | 7 | 7 | Qualifié SecNumCloud 3.2 | Landing, differences, subnets, Private Google Access, Private Service Connect |
| VPC Service Controls | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, service perimeters, ingress/egress rules |
<!-- AUTO-SYNC:COVERAGE-TABLE:END -->

## Updating the docs

The scraper uses parallel HTTP SSR requests (with automatic product discovery from `/products`, `/release-notes`, and `/docs/*` Technology Area hubs) and tracks last-updated dates for each page. An optional `--use-playwright` flag is available if headless browser rendering is needed.

### Run the scraper and synchronize the skill

```bash
# Scrape Berlin only (default)
python3 scripts/scrape-gcd-docs.py --region berlin

# Scrape S3NS only
python3 scripts/scrape-gcd-docs.py --region s3ns

# Scrape both regions
python3 scripts/scrape-gcd-docs.py --region all

# Synchronize SKILL.md, references/services.md, references/product-differences.md, and README.md
python3 scripts/sync-skill.py
```

Each region's docs are scraped into their respective output directory (`docs-raw/` for Berlin, `docs-raw-s3ns/` for S3NS). Running `python3 scripts/sync-skill.py` parses both regions' manifests and `*_tpc-differences.md` pages, automatically updating product inventories, coverage tables, and injecting new product difference sections whenever new services are added to the documentation.

## Continuous integration

Two workflows run in `.github/workflows/`:

| Workflow | Runs on | What it does |
|---|---|---|
| `ci.yml` | every pull request, pushes to `main` | Python lint and unit tests, skill integrity, workflow lint and security |
| `update-docs.yml` | every day at 05:17 Paris time, manual dispatch | Scrapes both regions, re-syncs the skill, checks it, writes the day's release note, and merges the result through a pull request |

The `ci.yml` jobs, and the failure each one prevents:

- **Python lint and tests:** `ruff` flags undefined names and syntax errors. Those would otherwise surface only when the scheduled scrape reaches the broken path. The unit tests cover `check-skill.py`, plus a smoke test of product discovery on the committed data.
- **Skill integrity:** `scripts/check-skill.py` fails on any of these:
  - SKILL.md frontmatter that agents reject.
  - SKILL.md over its 500-line budget. It is loaded in full on every activation.
  - Broken relative links, or reference files SKILL.md never links.
  - Unbalanced, duplicated or missing `AUTO-SYNC` markers. A missing marker makes `sync-skill.py` silently stop updating that section.
  - Bidi-control and tag characters, and HTML comments other than the sync markers: text an agent reads but a reviewer does not see. Linter directives such as `<!-- prettier-ignore -->` count too. Zero-width characters are reported as warnings.

  `sync-skill.py --check` then confirms the generated blocks match the scraped docs.
- **Workflow lint and security:** `actionlint` catches workflow syntax and expression errors. `zizmor` catches unpinned actions, injection risks and over-broad permissions.

### Scheduled docs update

The skill must hold all of the published documentation, current by the next day: a page published on day J is in the skill on day J+1. No person reviews the scraped text before it lands, because the skill answers from the public documentation as it is. A page that is wrong is reported to the documentation owner through a support ticket, not left out of the skill.

Each day, `update-docs.yml`:
1. Scrapes both regions and re-syncs the skill.
2. Runs `check-skill.py`, `sync-skill.py --check` and the unit tests on the result. These check that the files are intact and stay inert for agents, not what the docs say.
3. Writes the day's release note, `docs-changes/YYYY-MM-DD.md` (see below).
4. Commits everything to the `automation/docs-update` branch, opens or updates a pull request, and **merges it itself** (squash). The pull request is the dated record of the day, and reverting its commit undoes the day.

A day with no change commits nothing and writes no note. A second run on the same day writes `YYYY-MM-DD-2.md`, so the first note is kept.

**Release note.** For each region, from the previous and the new `_manifest.json`:
- pages added and removed;
- pages whose text changed, with line counts and the sections the changes fall under;
- the number of pages only re-dated: the "Last updated" line moved but the text did not;
- SecNumCloud 3.2 qualification moves, for S3NS.

The pull request body carries the same note. Scraped titles, headings and names are shown in code spans, so the note cannot mention people, link issues or carry markup.

**When something goes wrong, the run turns red**, which is what GitHub emails you about, since nobody reads the pull request:
- One region's scrape failed. The other region is still merged, and the note opens with a warning. The failed region keeps its previous pages.
- `main` moved during the scrape. The pull request stays open and the next run rebuilds it, so generated files always match the code they were made with.
- The merge was refused, for example by a branch rule.

The branch is rebuilt from `main` on every run. Do not push to it: the next run overwrites it.

To refresh at once, run the workflow by hand: **Actions → Update sovereign cloud docs → Run workflow**, on `main`.

Two repository settings matter:
- **Settings → Actions → General → Workflow permissions:** enable *Allow GitHub Actions to create and approve pull requests*. It is off by default on personal repositories, and without it the job fails when it opens the pull request.
- **`main` must not require a review or status checks** for this merge. Workflows do not start on a pull request opened with `GITHUB_TOKEN`, so `ci.yml` never runs on it and required checks would never arrive. The job runs those checks itself before it commits.

Run the same checks locally:

```bash
python -m pip install --require-hashes --no-deps -r requirements-ci.txt
ruff check
python -m unittest discover -s tests -t .
python3 scripts/check-skill.py
python3 scripts/sync-skill.py --check
```

Dependabot keeps the SHA-pinned actions and the CI tools in `requirements-ci.txt` current, waiting 7 days after each release. The actionlint image is a `docker://` reference that Dependabot does not track, so bump it by hand.

## Credits & Acknowledgments

Originally based on [rochacbruno/gcd-claude-skill](https://github.com/rochacbruno/gcd-claude-skill) by Bruno Rocha, and subsequently extended and maintained independently with dynamic service discovery, parallel HTTP SSR scraping, S3NS PREMI3NS SecNumCloud 3.2 qualification tracking, and automated reference synchronization.

## License

Apache-2.0

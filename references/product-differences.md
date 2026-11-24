# Sovereign Cloud Product Differences vs Public GCP

Per-product differences and limitations when running on Google Cloud Dedicated (Berlin, `u-germany-northeast1`) and Cloud de Confiance by S3NS (France, `u-france-east1`) compared to public Google Cloud. Each section lists what is unavailable or changed.

All products share these platform-wide constraints:
- **Single region with three zones:** `u-germany-northeast1` (`-a`, `-b`, `-c`) for Berlin; `u-france-east1` (`-a`, `-b`, `-c`) for S3NS. No multi-region features or cross-region failover.
- **Project IDs:** Prefixed with `eu0:` (Berlin) or `s3ns:` (S3NS).
- **Service endpoints:** `*.apis-berlin-build0.goog` (Berlin) or `*.s3nsapis.fr` (S3NS) instead of `*.googleapis.com`.
- **No Cloud Identity or Google Accounts:** Use Workforce Identity Federation or service accounts.
- **No Cloud Shell:** Install `gcloud` and CLI tools locally or on a sovereign cloud VM.

<!-- AUTO-SYNC:TPC-DIFFERENCES-INDEX:START -->
> **Auto-synced coverage:** 40 product-specific `tpc-differences` guides tracked across Berlin (`docs-raw/`) and S3NS (`docs-raw-s3ns/`), latest upstream update `2026-11-24`.

<details>
<summary>Tracked <code>tpc-differences</code> inventory (40 guides)</summary>

| Product | S3NS SecNumCloud 3.2 | Differences File | Last Updated | Digest |
|---|---|---|---|---|
| Access Context Manager | Qualifié SecNumCloud 3.2 | `access-context-manager_tpc-differences.md` | 2026-11-10 | `74571076b2` |
| Agent Platform (Gemini Enterprise Agent Platform) | Qualification en cours | `gemini-enterprise-agent-platform_tpc-differences.md` | 2026-11-20 | `9cf6ccf3df` |
| Artifact Registry | Qualifié SecNumCloud 3.2 | `artifact-registry_tpc-differences.md` | 2026-11-10 | `881c6a448e` |
| BigQuery | Qualifié SecNumCloud 3.2 | `bigquery_tpc-differences.md` | 2026-11-10 | `40eb9066e7` |
| Bigtable | Qualification en cours | `bigtable_tpc-differences.md` | 2026-11-10 | `8399e6dd61` |
| Cloud Armor | Qualifié SecNumCloud 3.2 | `armor_tpc-differences.md` | 2026-11-10 | `82802e7d6b` |
| Cloud Asset Inventory | — | `asset-inventory_tpc-differences.md` | 2026-11-10 | `8b17425588` |
| Cloud Billing | — | `billing_tpc-differences.md` | 2026-11-10 | `c908f78403` |
| Cloud Build | — | `build_tpc-differences.md` | 2026-11-10 | `e394f41ba4` |
| Cloud DNS | Qualifié SecNumCloud 3.2 | `dns_tpc-differences.md` | 2026-11-10 | `fbb94d9e80` |
| Cloud Interconnect | Qualifié SecNumCloud 3.2 | `network-connectivity_interconnect_tpc-differences.md` | 2026-11-10 | `e8eefa543b` |
| Cloud KMS | Qualifié SecNumCloud 3.2 | `kms_tpc-differences.md` | 2026-11-18 | `407d108d82` |
| Cloud Load Balancing | Qualifié SecNumCloud 3.2 | `load-balancing_tpc-differences.md` | 2026-11-10 | `0b3869431a` |
| Cloud Logging | Qualifié SecNumCloud 3.2 | `logging_tpc-differences.md` | 2026-11-23 | `3c7ede3f89` |
| Cloud Monitoring | Qualifié SecNumCloud 3.2 | `monitoring_tpc-differences.md` | 2026-11-23 | `64c4c68e30` |
| Cloud NAT | Qualifié SecNumCloud 3.2 | `nat_tpc-differences.md` | 2026-11-10 | `355f0cd2d2` |
| Cloud NGFW | Qualifié SecNumCloud 3.2 | `firewall_tpc-differences.md` | 2026-11-10 | `b038ad3e50` |
| Cloud Quotas | Qualification en cours | `quotas_tpc-differences.md` | 2026-11-10 | `8ab8f5aa35` |
| Cloud Router | Qualifié SecNumCloud 3.2 | `network-connectivity_router_tpc-differences.md` | 2026-11-10 | `539f8b73c2` |
| Cloud Run | Qualification en cours | `run_tpc-differences.md` | 2026-11-18 | `a9f3e4b762` |
| Cloud SQL | Qualifié SecNumCloud 3.2 | `sql_tpc-differences.md` | 2026-11-24 | `7ceca2ae72` |
| Cloud Storage | Qualifié SecNumCloud 3.2 | `storage_tpc-differences.md` | 2026-11-17 | `f5a3d260b4` |
| Cloud VPN | Qualifié SecNumCloud 3.2 | `network-connectivity_vpn_concepts_tpc-differences.md` | 2026-11-10 | `09d1827aa5` |
| Compute Engine | Qualifié SecNumCloud 3.2 | `compute_tpc-differences.md` | 2026-11-20 | `ce63190ccb` |
| Container-Optimized OS | Qualifié SecNumCloud 3.2 | `container-optimized-os_tpc-differences.md` | 2026-11-10 | `e4ae3ed663` |
| Filestore | Qualification en cours | `filestore_tpc-differences.md` | 2026-11-19 | `63ca06de02` |
| Google Kubernetes Engine (GKE) | Qualifié SecNumCloud 3.2 | `kubernetes-engine_tpc-differences.md` | 2026-11-19 | `d79a61c00c` |
| IAM | Qualifié SecNumCloud 3.2 | `iam_tpc-differences.md` | 2026-11-17 | `bc966fb7ef` |
| Managed Airflow (Cloud Composer 3) | Qualification en cours | `composer_tpc-differences.md` | 2026-11-10 | `8b00656c51` |
| Managed Service for Apache Spark (Dataproc) | Qualification en cours | `managed-spark_tpc-differences.md` | 2026-11-24 | `4fd95170bf` |
| Network Service Tiers | Qualifié SecNumCloud 3.2 | `network-tiers_tpc-differences.md` | 2026-11-10 | `2dbc42433d` |
| Organization Policy | Qualifié SecNumCloud 3.2 | `organization-policy_tpc-differences.md` | 2026-11-10 | `4208565439` |
| Pub/Sub | Qualifié SecNumCloud 3.2 | `pubsub_tpc-differences.md` | 2026-11-10 | `d649238759` |
| Resource Manager | Qualifié SecNumCloud 3.2 | `resource-manager_tpc-differences.md` | 2026-11-10 | `4ae45cb244` |
| Secret Manager | Qualification en cours | `secret-manager_tpc-differences.md` | 2026-11-10 | `40aa632c10` |
| Service Usage | Qualifié SecNumCloud 3.2 | `service-usage_tpc-differences.md` | 2026-11-10 | `c466abb91d` |
| Storage Transfer Service | Qualification en cours | `storage-transfer_tpc-differences.md` | 2026-11-19 | `70383282c9` |
| Terraform | — | `terraform_tpc-differences.md` | 2026-11-10 | `bcb0fd2998` |
| VPC | Qualifié SecNumCloud 3.2 | `vpc_tpc-differences.md` | 2026-11-10 | `06a8de4766` |
| VPC Service Controls | Qualifié SecNumCloud 3.2 | `vpc-service-controls_tpc-differences.md` | 2026-11-10 | `1f38179c73` |

</details>
<!-- AUTO-SYNC:TPC-DIFFERENCES-INDEX:END -->

---

## Access Context Manager

- Only **basic** access levels are supported. Advanced and custom access levels (CEL expressions) are unavailable.
- Only **IP subnetworks** and **geographic location** conditions are available. Other conditions (device attributes, request time) are unavailable.

---

## Access Transparency

- Available in both regions under `/assured-workloads/access-transparency/docs` to provide near real-time logs when sovereign cloud operator personnel access customer content during support cases.
- Does not have a separate `tpc-differences` page beyond platform-wide logging and organization constraints.

---

## Agent Platform (Gemini Enterprise Agent Platform)

- **Available components:** Only Model Garden, Model Registry, and synchronous Online inference (`Predict` and `RawPredict` APIs) are available.
- **Models:** Only open-weight models (such as Gemma and Mistral) via self-deploy to Agent Platform endpoints are available. Gemini models, proprietary models, and Model-as-a-Service (MaaS) endpoints are unavailable.
- **Unavailable inference & training features:**
  - Fine-tuning and custom model training
  - Batch inference
  - Streaming and chat completion APIs (`StreamPredict`, `StreamRawPredict`, `DirectPredict`, `DirectRawPredict`, `StreamDirectPredict`, `StreamDirectRawPredict`, `Explain`, `GenerateContent`, `StreamGenerateContent`, `ChatCompletions`, `EmbedContent`)
- **SDKs and tools:** Vertex AI SDK and Google Gen AI SDK are **unavailable**. Use the console, `gcloud`, or REST API calls against the regional endpoint.

---

## Artifact Registry

- **Supported formats:** Docker, Apt, NPM, and Yum only. All other formats (Maven, Python, Go, Generic, Helm, etc.) are unavailable.
- **Repository modes:** Only standard mode. Remote and virtual repositories are unavailable.
- **Domain:** Use `pkg-berlin-build0.goog` (Berlin) or `s3nsregistry.fr` (S3NS) instead of `pkg.dev`.
- **GPG Keys** for Apt and Yum repositories are unavailable.
- **Cleanup policies** are unavailable.
- **Client tools:** Only Docker CLI, `crictl`, Apt client, and Yum client.
- **Vulnerability scanning** with Artifact Analysis is unavailable.

---

## BigQuery

**Unavailable APIs and services:**
- Dataform API, Migration API, Analytics Hub API, Data Transfer API

**Unavailable features:**
- Data masking
- Column-level access control
- Scheduled queries
- Saved queries and notebooks
- Gemini in BigQuery
- BigQuery ML external models (internal models only)
- BigQuery public datasets
- Terraform support for BigQuery resources (check provider compatibility)
- Cloud Asset Inventory integration
- Committed use discounts (CUDs)

**Other limitations:**
- CMEK provisioning requires manual service account setup.
- Data Transfer Service: email notifications unavailable.
- No cross-region replication or failover.

---

## Bigtable

**Locations and replication:**
- Single region only (`u-germany-northeast1` or `u-france-east1`).
- **Available:** Multi-zone replication within the single region, and multi-cluster app profiles for automatic failover across zones in the same region.
- **Unavailable:** Cross-region replication and cross-region backups.

**Compute and storage:**
- **Available:** SSD and HDD storage (choice is permanent at instance creation).
- **Unavailable:** Tiered storage and Large nodes (2x capacity).

**Backups:**
- **Available:** Automated backups, hot backups, and copying a backup within the same project or another project in the same region.

**Unavailable querying, views, and analytics:**
- GoogleSQL for Bigtable (cannot query Bigtable using SQL, client libraries, or the Bigtable Studio query editor)
- Logical views and continuous materialized views
- BigQuery federation (cannot query Bigtable as an external table from BigQuery)
- Data Boost (serverless compute for batch read jobs/queries)

**Unavailable observability and tooling:**
- Key Visualizer, `ListHotTablets` API, and client-side metrics
- Bigtable Studio (Explorer and Query Editor in the console)
- Terraform provisioning for Bigtable resources
- LangChain integration (`BigtableVectorStore`, `BigtableLoader`, `BigtableChatMessageHistory`)

**Available security and governance:**
- CMEK, VPC Service Controls, IAM, Authorized views, Change streams, and Audit logging.

---

## Cloud Armor

- **Tier:** Only **Cloud Armor Standard** is available. Cloud Armor Enterprise is unavailable.
- **Supported backends:** Only **regional external Application Load Balancers** (`rxlb`) are supported. Global load balancers are unavailable.
- **Unavailable features:**
  - Adaptive Protection
  - Bot management (reCAPTCHA integration)
  - Threat intelligence and named IP lists
  - Rate limiting with `enforceOnKeyConfigs` (basic rate limiting is available)
  - Network edge security policies and advanced network DDoS protection

---

## Cloud Asset Inventory
<!-- AUTO-GENERATED-PRODUCT:asset-inventory:START -->

**Workflows and tools:**
- **API availability:** The following APIs are unavailable in Cloud de Confiance by S3NS: - Analysis APIs: These APIs are linked to Policy Analyzer, which is unavailable in Cloud de Confiance by S3NS. Policy Analyzer lets you find out which principals (for example, users, service accounts, groups, and domains) have what access to which resources based on your IAM allow policies. - Feed APIs: These APIs let you set up real-time notifications about resource and policy changes through [Pub/Sub](https://documentation.s3ns.fr/pubsub/docs/overview). - Query APIs: These APIs let you query your assets using a [BigQuery](https://documentation.s3ns.fr/bigquery/docs/introduction) SQL-compatible dialect.
- **Asset Query UI:** The **Asset Query** interface for building SQL queries in the Cloud de Confiance console is unavailable.
- **Asset type availability:** [Asset types](https://documentation.s3ns.fr/asset-inventory/docs/asset-types) from products and features that aren't available in Cloud de Confiance by S3NS are similarly unavailable. For a list of available products, see [Products and Services](https://documentation.s3ns.fr/products).

**Insights and observability:**
- **Overview:** The Cloud Asset Inventory **Overview** dashboard in the Cloud de Confiance console is unavailable.

<!-- AUTO-GENERATED-PRODUCT:asset-inventory:END -->
---

## Cloud Billing

- **Account management:** Billing accounts and invoicing are managed by the sovereign cloud operator (not self-service in Google Cloud).
- **Discounts:** Spend-based Committed Use Discounts (CUDs) require contacting operator support. Resource-based CUDs, Sustained Use Discounts (SUDs), and free tier/trial credits are unavailable.
- **Unavailable features:**
  - Cloud Billing budgets and cost alerts
  - Cost Table, Cost Breakdown, and Pricing reports in the console (BigQuery billing export is the primary way to analyze costs)
  - Gemini Cloud Assist in Billing

---

## Cloud Build
<!-- AUTO-GENERATED-PRODUCT:build:START -->

**Key differences:**
- Only the [default pool](https://documentation.s3ns.fr/build/docs/overview#default_pools_and_private_pools) is available. Private pools aren't available.
- You can only create builds directly, using the `CreateBuild` API or `gcloud builds submit` from the command line. You can't use triggers.
- Default Cloud Storage buckets [aren't fully supported](#observability-differences) for storing log files.

**Hardware and OS:**
- **Machine types:** Only c3-standard-4 machines are available.
- **Storage:** Hyperdisk Balanced is the only available storage option for Cloud Build. The `diskSizeGb` field is not available.

**Integrations:**
- **Provenance:** Cloud Build doesn't support provenance.
- **Builders:** Cloud Build builders aren't available or supported.
- **Build notifications:** open-source Cloud Build notifiers don't work without modification.
- **Image types:** Docker is the only artifact type supported for uploading to Artifact Registry.
- **Configuration:** There is no Terraform provider for managing Cloud Build resources.

**Security and access control:**
- **Secrets:** There is no Secret Manager integration with Cloud Build.
- **Customer Managed Encryption Keys (CMEK):** Cloud Build doesn't support CMEK.

**Network:**
- **Service Networking:** Private networking isn't available.

**Workflows and tools:**
- **Creating builds:** You can create builds using the Cloud Build API or the Google Cloud CLI only. Triggers aren't available.
- **Worker pools:** Only the [default pool](https://documentation.s3ns.fr/build/docs/overview#default_pools_and_private_pools) is available. You can't create or use private pools.
- **Scheduled builds:** Scheduled builds aren't available.
- **Google Cloud CLI:** The only gcloud CLI commands available are those for creating and managing builds, and `get-default-service-account`.
- **Cloud de Confiance console:** The only pages available in the Cloud de Confiance console are the Builds page and the Permissions page. The Dashboard, Repositories, Triggers, and Worker Pool pages aren't available.

**Insights and observability:**
- **Logging:** Unlike in Google Cloud, build logs aren't automatically stored in a default Cloud de Confiance by S3NS-owned Cloud Storage bucket. Instead, if you don't specify the `LogsBucket` option in your build config, Cloud Build uses a user-owned default Cloud Storage bucket in the same region as your build. Alternatively, you can specify a user-created Cloud Storage bucket. To use Cloud Storage to store logs, configure your builds to use one of the following: - A user-created Cloud Storage bucket - A user-owned default logs bucket in a project that's in the same region as the build `LEGACY_BUCKET` is not available as a value for `DefaultLogsBucketBehavior` in the build configuration file.

<!-- AUTO-GENERATED-PRODUCT:build:END -->
---

## Cloud DNS

- **Only private DNS zones** are supported. Public DNS zones are unavailable.
- Reverse DNS lookup of public IPv4/IPv6 addresses is not supported.
- Supported private zone types: forwarding zones, peering zones, managed reverse lookup zones, Service Directory zones.
- DNS server policies and response policy zones are fully available.

---

## Cloud Interconnect

- **Available types:** Only **Dedicated Interconnect** and **Partner Interconnect** (and MACsec for Dedicated Interconnect) are available.
- **Unavailable types:** Cross-Cloud Interconnect (including partner Cross-Cloud Interconnect) is unavailable.
- **SLA / Resiliency:** Critical production 99.99% availability topology (which requires multiple regions) is unavailable; multi-zone deployment within the single region is supported.

---

## Cloud KMS

**Unavailable protection levels:**
- `HSM` (multi-tenant Cloud HSM keys)
- `HSM_SINGLE_TENANT` (single-tenant Cloud HSM)
- `EXTERNAL` (EKM over internet; only EKM via VPC is supported where applicable)

**Unavailable features:**
- Cloud KMS Autokey (requires Cloud HSM)
- Key tracking and key usage tracking (including dashboard and Inventory API)
- `generateRandomBytes` method

**Location constraints:**
- Only the single regional location (`u-germany-northeast1` or `u-france-east1`).
- `global` location exists for API compatibility but maps to the single region only.
- Multi-regions other than `global` are not supported.
- CMEK integrations are limited to services available in the sovereign cloud.

---

## Cloud Load Balancing

- **Regional load balancers only:** All global load balancers and classic load balancers are unavailable.
- **Available load balancers:**
  - Regional external Application Load Balancer
  - Regional internal Application Load Balancer
  - Regional external proxy Network Load Balancer
  - Regional internal proxy Network Load Balancer
  - Regional external passthrough Network Load Balancer
  - Regional internal passthrough Network Load Balancer
- **Network tier:** Only **Premium Tier** is available (Standard Tier is unavailable).
- **Unavailable backends and integrations:**
  - Backend buckets (Cloud Storage cannot be used as a load balancer backend)
  - Serverless NEGs, internet NEGs, and hybrid connectivity NEGs (only zonal NEGs and Private Service Connect NEGs are supported)
  - Cloud CDN
  - Cloud Trace
  - Certificate Manager and Google-managed SSL certificates (use self-managed certificates)
  - Service Extensions


---

## Cloud NAT

- **Available:** Only **Public NAT** with IPv4-to-IPv4 translation on **Premium Network Tier**.
- **Unavailable:**
  - Private NAT (NAT between VPC networks or hybrid networks)
  - NAT64 / DNS64 (IPv6-to-IPv4 translation)
  - Standard Network Tier IP addresses

---

## Cloud NGFW (Next Generation Firewall)

- **Tiers:** Only **NGFW Essentials** (VPC firewall rules, hierarchical firewall policies, global/regional network firewall policies, IAM tags) and **NGFW Standard** (FQDN objects, geolocation objects, threat intelligence lists) are available.
- **Unavailable:** **NGFW Enterprise** (intrusion prevention service / IPS, TLS inspection, security profiles, and firewall endpoints) is unavailable.

---

## Cloud Quotas

- **Quota increase requests:** Automated self-service quota increases via the console are unavailable. To request a quota adjustment, contact operator support (`support.s3ns.fr` for S3NS or the GCD support portal for Berlin) with the project ID/number, service name, quota name, dimensions, desired value, and justification.

---

## Cloud Router

- **Routing mode:** Only **regional dynamic routing mode** is supported (global dynamic routing is unavailable because there is only one region).
- **Subnet advertisement and learned routes:** Scoped to the single region only.
- **Unavailable features:**
  - Classic VPN dynamic routing (use HA VPN)
  - Network Connectivity Center (NCC) imported transit dynamic routes and VPC spokes for full-mesh VPC connectivity
  - BGP route policies, BFD (Bidirectional Forwarding Detection), MD5 authentication, named BGP sessions, subinterfaces, and IPv6 BGP sessions

---

## Cloud Run

- **Deployment sources:** Only **Cloud Run services** and **Cloud Run jobs** deployed from container images stored in **Artifact Registry** are supported.
- **Unavailable deployment modes and runtimes:**
  - Deploying from source code (Cloud Build and Buildpacks are unavailable)
  - Cloud Run functions
  - Worker pools and instances
  - Multi-container sidecars that depend on unavailable integrations
- **Assigned URLs and domains:**
  - Services use `*.run-berlin-build0.goog` (Berlin) or `*.s3nsrun.fr` (S3NS) instead of `*.run.app`.
  - Only deterministic URLs are used, and **service names cannot exceed 50 characters**.
  - Custom domain mappings are unavailable (use a regional external Application Load Balancer if custom domains are needed).
- **Networking:**
  - **Direct VPC egress is required** (you must specify a VPC network when deploying; Serverless VPC Access connectors are unavailable).
  - Outbound traffic to the public internet requires **Cloud NAT** on the VPC network.
- **Execution environment & hardware:**
  - Only **2nd generation (`gen2`)** execution environment is available (1st generation is unavailable).
  - Cloud Run GPUs are unavailable.
- **Unavailable integrations:**
  - Cloud Scheduler (for triggering jobs/services on a schedule)
  - Eventarc
  - Identity-Aware Proxy (IAP) and Binary Authorization
  - SLO Monitoring, Error Reporting, and Cloud Trace

---

## Cloud SQL

**Database engines:**
- MySQL and PostgreSQL only. SQL Server is unavailable.

**Edition and versions:**
- Only Enterprise Plus edition (Enterprise edition is unavailable).
- Supported versions: MySQL `8.0`, `8.4`, `9.7` and PostgreSQL `12` through `18` (MySQL `5.6`/`5.7` and PostgreSQL `9.6`/`10`/`11` are unavailable).

**Machine types:** C3 series only:
- `db-perf-optimized-N-4`, `db-perf-optimized-N-8`, `db-perf-optimized-N-22`, `db-perf-optimized-N-44`, `db-perf-optimized-N-88`, `db-perf-optimized-N-176`

**Storage:** Hyperdisk Balanced and Hyperdisk Balanced High Availability only. Data cache is unavailable.

**Networking:**
- Private Service Connect is available.
- Private Service Connect with service automation is unavailable.
- Private services access is unavailable.

**Organization policies:**
- Built-in constraints `constraints/sql.restrictPublicIp`, `constraints/sql.restrictAuthorizedNetworks`, and `constraints/gcp.restrictCmekCryptoKeyProjects` are available.
- Requiring CMEK via `constraints/gcp.restrictNonCmekServices` and custom/managed Cloud SQL constraints (`constraints/sql.managed.*`, `sqladmin.googleapis.com/*`) are unavailable.

**Unavailable features:**
- Database Migration Service
- Serverless export operations
- Query insights
- Maintenance notifications
- Managed Service for Microsoft Active Directory
- User account and group IAM authentication (service account IAM auth only)

**Maintenance caveat:** Instances configured with maintenance windows do not receive automatic updates. Apply updates manually via instance restart or self-service maintenance.


---

## Cloud Storage

**Location and availability:**
- Single region only. Dual-region, multi-region, and bucket relocation are unavailable.
- Rapid Bucket (zone-level placement) is unavailable.
- You must specify a location when creating a bucket (`u-germany-northeast1` or `u-france-east1`) - no default location.

**Unavailable features:**
- Storage Insights
- Domain-named buckets and custom domain content serving (A/CNAME redirects)
- Regional and locational endpoints
- Rapid Cache
- User account HMAC keys (use service account HMAC keys)
- Usage logs and storage logs (legacy logging)
- Legacy storage classes (Multi-Regional, Regional, DRA)
- Cannot set a default project for interoperability access

**Cloud Storage FUSE:**
- Supported on GKE >= 1.36.0-gke.1266000 with `custom-endpoint` and `skipCSIBucketAccessCheck` (see GKE section).
- Standalone authentication must use a Compute Engine VM in the same project or a service account key file.

<!-- AUTO-SYNC:UPSTREAM-DIFFS:storage:START -->
**Latest upstream documentation updates (`2026-11-11`):**
- Cloud de Confiance does not support features that use multiple locations, such as dual-regions, bucket relocation, and turbo replication.
- Cloud de Confiance does not support Storage Insights.
- Cloud de Confiance does not support domain-named buckets.
- **Locations, availability, and disaster recovery — Locations:** Cloud de Confiance has only a [single region](https://documentation.s3ns.fr/storage/docs/locations) as an available bucket location. Features that use more than one region are not supported, such as dual-regions, multi-regions, and bucket relocation. Rapid Bucket, which places buckets in zones, is also not supported.
- **Locations, availability, and disaster recovery — Default location:** When creating a bucket in Cloud de Confiance, you must include a location parameter as part of the process. Cloud de Confiance does not support creating buckets in a default location.
- **Integrations — Storage Insights:** The Storage Insights feature is not available in Cloud de Confiance.
- **Integrations — Default projects:** You can't set a default project in Cloud de Confiance for interoperability access.
- **Security and access control — User account HMAC keys:** User account HMAC keys are not available in Cloud de Confiance. Use service account HMAC keys instead.
- **Network — Rapid Cache:** The Rapid Cache feature is not available in Cloud de Confiance.
- **Network — Regional and locational endpoints:** Regional and locational endpoints are not available in Cloud de Confiance.
- **Network — Custom domains:** Using buckets as backends for content serving to custom domains through `A` and `CNAME` redirects are not available in Cloud de Confiance. Additionlly, creating buckets with domain names is not supported.
- **Workflows and tools — Cloud Storage FUSE:** When using [Cloud Storage FUSE](https://documentation.s3ns.fr/storage/docs/cloud-storage-fuse/overview), the authentication for the Cloud de Confiance bucket must be done either by using Cloud Storage FUSE in a Compute Engine virtual machine that's contained in the same project as the bucket or by specifying a service account key file for a service account that has permission to read and write data within the bucket. The service account key file can be specified either in the [configuration file](https://documentation.s3ns.fr/storage/docs/cloud-storage-fuse/config-file) or by using the `--key-file` flag in individual commands.
- **Insights and observability — Cloud Storage usage logs and storage logs:** Usage logs and storage logs, which are legacy logging features specific to Cloud Storage, are not supported in Cloud de Confiance.
- **Other differences — Legacy storage classes:** The legacy storage classes Multi-Regional storage, Regional storage, and Durable Reduced Availability (DRA) storage are not available in Cloud de Confiance.
<!-- AUTO-SYNC:UPSTREAM-DIFFS:storage:END -->

---

## Cloud VPN

- **Available:** Only **HA VPN** is supported.
- **Unavailable:** Classic VPN is unavailable. Multi-region features and cross-region failover are unavailable.

---

## Compute Engine

**Machine types:** Only three series available:
- **C3** - up to 176 vCPUs (bare metal instances unavailable)
- **M3** - up to 128 vCPUs (memory-optimized)
- **A3 Edge** - `a3-edgegpu-8g-nolssd` only (NVIDIA H100 GPUs, no local SSD)

All other series (N2, E2, T2A, etc.), AMD, and Arm-based types are unavailable. TPUs are unavailable.

**Disks:** **Hyperdisk Balanced** (zonal) and **Hyperdisk Balanced High Availability** (regional synchronous replication across two zones in the same region) only. All other disk types (Persistent Disk, Local SSD, etc.) are unavailable.

**OS images available:** Debian, Ubuntu LTS, Rocky Linux, Container-Optimized OS.
- Image projects use `eu0-system:` (Berlin) or `s3ns-system:` (S3NS) prefix (e.g. `eu0-system:debian-cloud` or `s3ns-system:debian-cloud`).
- Arm image families, SCSI interfaces, IDPF interfaces are not supported.
- Enterprise OS (Windows, RHEL, SLES) requires BYOL via image adaptation.

**Unavailable instance types:** Bare metal instances, Confidential VMs.

**Unavailable VM features:**
- OS Login, VM Manager
- Interactive serial console access, IAP TCP forwarding
- Future reservations (on-demand reservations are available)

**Cost:** Spot VMs available (up to 60% discount). Preemptible VMs, CUDs, and SUDs are unavailable.

**Networking:** No default network created for new projects. Only zonal DNS names (no global DNS).

**Migration:** Image adaptation is the only supported path. All other migration options are unavailable.

**Backup:** Snapshots and clones only.

**Encryption:** CMEK available. Customer-supplied encryption keys (CSEK) unavailable.

<!-- AUTO-SYNC:UPSTREAM-DIFFS:compute:START -->
**Latest upstream documentation updates (`2026-11-20`):**
- Only four machine type series are available in Cloud de Confiance
- Hyperdisk Balanced and Hyperdisk Balanced High Availability are the only disk types available in Cloud de Confiance
- Image adaptation is the only supported migration path into Cloud de Confiance
- **Hardware and OS — Machine types:** Only the following machine series and machine types are available in Cloud de Confiance: - [C4](https://documentation.s3ns.fr/compute/docs/general-purpose-machines#c4_series) machine types with up to 288 vCPUs. C4 bare metal instances aren't available. - [C3](https://documentation.s3ns.fr/compute/docs/general-purpose-machines#c3_series) machine types with up to 176 vCPUs. C3 bare metal instances aren't available. - [M3](https://documentation.s3ns.fr/compute/docs/memory-optimized-machines#m3_series) machine types with up to 128 vCPUs. - [A3](https://documentation.s3ns.fr/compute/docs/accelerator-optimized-machines#a3-vms) Edge machine type: `a3-edgegpu-8g-nolssd` - [A3](https://documentation.s3ns.fr/compute/docs/accelerator-optimized-machines#a3-vms) High machine types: - `a3-highgpu-1g-nolssd` - `a3-highgpu-2g-nolssd` - `a3-highgpu-4g-nolssd` - `a3-highgpu-8g-nolssd` All other machine series, including AMD and Arm-based machine types are unavailable. For recommendations about how to adapt your machine usage in Cloud de Confiance, see the [recommendations section](#recommendations). The following instance types are available in Cloud de Confiance: - [Virtual machine (VM) instances](https://documentation.s3ns.fr/compute/docs/instances) - [Managed and unmanaged instance groups](https://documentation.s3ns.fr/compute/docs/instance-groups) - [Sole tenant nodes](https://documentation.s3ns.fr/compute/docs/nodes/sole-tenant-nodes) All other instance types are unavailable, including the following: - Bare metal instances - Confidential VM instances
- **Hardware and OS — GPUs and TPUs:** Only the following GPUs are available in Cloud de Confiance: - NVIDIA H100 GPUs (`nvidia-h100-80gb`) are available with the [A3 Edge machine type](https://documentation.s3ns.fr/compute/docs/gpus#h100-gpus), with the following differences: - Supported machine type: `a3-edgegpu-8g-nolssd` - Attached Local SSD (Gib): 0. Local SSD isn't supported in Cloud de Confiance - Maximum network bandwidth (Gbps): 800 - NVIDIA H100 GPUs (`nvidia-h100-80gb`) are available with the [A3 High machine type](https://documentation.s3ns.fr/compute/docs/gpus#h100-gpus), with the following differences: - Supported machine types: - `a3-highgpu-1g-nolssd` - `a3-highgpu-2g-nolssd` - `a3-highgpu-4g-nolssd` - `a3-highgpu-8g-nolssd` - Attached Local SSD (Gib): 0. Local SSD isn't supported in Cloud de Confiance All other GPU machine types are unavailable. TPUs are unavailable.
- **Hardware and OS — Disks and encryption:** The following disk types are available in Cloud de Confiance: - [Hyperdisk Balanced](https://documentation.s3ns.fr/compute/docs/disks/hd-types/hyperdisk-balanced) - [Hyperdisk Balanced High Availability](https://documentation.s3ns.fr/compute/docs/disks/hd-types/hyperdisk-balanced-ha) All other disk types are unavailable. For recommendations about how to adapt your disk usage in Cloud de Confiance, see the [recommendations section](#recommendations). [ Compute Engine automatically encrypts customer content at rest](https://documentation.s3ns.fr/compute/docs/disks/disk-encryption). The following key encryption key (KEK) methods are additionally available in Cloud de Confiance: - [Customer-managed encryption keys (CMEK)](https://documentation.s3ns.fr/compute/docs/disks/customer-managed-encryption) All other KEK encryption methods are unavailable.
- **Hardware and OS — Operating system images:** The following Linux operating systems are available in Cloud de Confiance: - [Debian](https://documentation.s3ns.fr/compute/docs/images/os-details#debian) - [Ubuntu LTS](https://documentation.s3ns.fr/compute/docs/images/os-details#ubuntu_lts) - [Rocky Linux](https://documentation.s3ns.fr/compute/docs/images/os-details#rocky_linux) - [Container-Optimized OS](https://documentation.s3ns.fr/compute/docs/images/os-details#container-optimized_os_cos) Arm image families are unavailable in Cloud de Confiance. If you want to use enterprise operating systems, you must bring your own licenses (BYOL). You can import BYOL images for Windows, Red Hat Enterprise Linux (RHEL), and SUSE Linux Enterprise Server (SLES) into Compute Engine by [adapting operating systems for Cloud de Confiance](https://documentation.s3ns.fr/compute/docs/import/image-import). This import process isn't supported for other operating systems.
- **Hardware and OS — Operating system details:** The following differences apply to [OS images](https://documentation.s3ns.fr/compute/docs/images/os-details) in Cloud de Confiance: - Image project: - Debian: `s3ns-system:debian-cloud` - Ubuntu LTS: `s3ns-system:ubuntu-os-cloud` - Rocky Linux: `s3ns-system:rocky-linux-cloud` - Container-Optimized OS: `s3ns-system:cos-cloud` - Arm image family: Not supported - SCSI interfaces: Not supported - IDPF interfaces: Not supported - Guest environment: Supported. You are responsible for installation and updates. - gcloud CLI: Supported. You are responsible for installing and updating. - OS Login: Not supported - VM Manager: Not supported - Import: [Adapting operating systems for Cloud de Confiance](https://documentation.s3ns.fr/compute/docs/import/image-import) is supported - License: No licenses are required
- **Networking — VM networking:** [Zonal DNS names](https://documentation.s3ns.fr/compute/docs/networking/zonal-dns) are available in Cloud de Confiance. Global DNS names are unavailable. Public DNS PTR records for VM instances are unavailable. There is no default network created when you create a project. Some examples assume that you have a default network. If you need a default network you can [manually create an equivalent auto mode network called `default`](https://documentation.s3ns.fr/vpc/docs/create-modify-vpc-networks#create-default-network). For detailed information about networking differences in Cloud de Confiance, see the following documents: - [VPC in Cloud de Confiance](https://documentation.s3ns.fr/vpc/docs/tpc-differences) - [Cloud NAT in Cloud de Confiance](https://documentation.s3ns.fr/nat/docs/tpc-differences) - [Cloud Load Balancing in Cloud de Confiance](https://documentation.s3ns.fr/load-balancing/docs/tpc-differences) - [Cloud NGFW in Cloud de Confiance](https://documentation.s3ns.fr/firewall/docs/tpc-differences) - [Network Service Tiers in Cloud de Confiance](https://documentation.s3ns.fr/network-tiers/docs/tpc-differences) - [Cloud VPN in Cloud de Confiance](https://documentation.s3ns.fr/network-connectivity/docs/vpn/concepts/tpc-differences)
- **Availability and Disaster Recovery — Regions and zones:** Cloud de Confiance has multiple zones in a single region. Multi-region features and cross-region failover are not supported. Deployment across multiple zones for resiliency is supported. We recommend that you use off-cloud data replication to ensure business continuity in case of an outage.
- **Availability and Disaster Recovery — Disks:** To protect your applications from a zonal outage, use [Hyperdisk Balanced High Availability](https://documentation.s3ns.fr/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volumes for your boot and data disks. Hyperdisk Balanced High Availability volumes synchronously replicate data across two zones in the same region. For more information, see [About synchronous disk replication](https://documentation.s3ns.fr/compute/docs/disks/about-regional-persistent-disk).
- **Availability and Disaster Recovery — Reservations:** [On-demand reservations](https://documentation.s3ns.fr/compute/docs/instances/reservations-single-project) are available in Cloud de Confiance. Future reservations are not available.
- **Cost management — Cost saving features:** [Spot VMs](https://documentation.s3ns.fr/compute/docs/instances/spot) are available for all machine series (C4, C3, M3, and A3) in Cloud de Confiance at discounts up to 60% off the on-demand price. Spot VMs pricing is updated quarterly. For the latest prices, see the [pricing page](https://documentation.s3ns.fr/spot-vms/pricing). Preemptible VMs, which are the legacy version of Spot VMs, aren't available in Cloud de Confiance. Cloud de Confiance by S3NS offers compute flexible committed use discounts (CUDs) for eligible spend across Compute Engine, GKE, and Cloud Run. To purchase spend-based commitments, contact [ Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/). For more information, see the [billing differences page](https://documentation.s3ns.fr/billing/docs/tpc-differences). All other cost-savings features aren't available in Cloud de Confiance, including resource-based CUDs and sustained use discounts (SUDs).
- **Security and access control — VM security features:** The following VM security features are available in Cloud de Confiance: - [VPC Service Controls](https://documentation.s3ns.fr/compute/docs/instances/protecting-resources-vpc-service-controls) - [Shielded VMs](https://documentation.s3ns.fr/compute/docs/about-shielded-vm) All other security features are unavailable, including the following: - Confidential VMs
- **Workflows and tools — Migration:** [Image adaptation](https://documentation.s3ns.fr/compute/docs/import/image-import) is available in Cloud de Confiance. All other migration options are unavailable.
- **Workflows and tools — Backup and restoration:** The following backup options are available in Cloud de Confiance: - [Snapshots](https://documentation.s3ns.fr/compute/docs/disks/snapshots) - [Clones](https://documentation.s3ns.fr/compute/docs/disks/clone-duplicate-disks) All other backup and restoration options are unavailable.
- **Workflows and tools — Disk replication:** [Hyperdisk Balanced High Availability](https://documentation.s3ns.fr/compute/docs/disks/hd-types/hyperdisk-balanced-ha) is the only supported option to replicate disk data to another zone in the same region. If you use Persistent Disk, then create Hyperdisk Balanced High Availability volumes from your Persistent Disk volumes by following the steps in [Change a zonal disk to a regional Hyperdisk](https://documentation.s3ns.fr/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha).
- **Workflows and tools — VM and user management:** The following VM and user management options are unavailable in Cloud de Confiance: - VM Manager - OS Login - Interactive serial console access - Identity-Aware Proxy (IAP) TCP forwarding
<!-- AUTO-SYNC:UPSTREAM-DIFFS:compute:END -->

---

## Container-Optimized OS

- **Image project:** `eu0-system:cos-cloud` (Berlin) or `s3ns-system:cos-cloud` (S3NS).
- **Container registry:** `pkg-berlin-build0.goog` (Berlin) or `s3nsregistry.fr` (S3NS).
- **Available:** NVIDIA H100 GPU driver installation on A3 VMs, Cloud Logging via `fluent-bit`.
- **Unavailable:**
  - COS milestones 113 and earlier
  - Arm-based COS images
  - Automatic OS updates
  - Launching containers at VM startup via the `konlet` workflow (`gce-container-declaration` metadata)
  - Node Problem Detector and OSConfig agent

---

## Filestore

- **Service tiers:** Only the **Regional** service tier (1 TiB to 9.75 TiB capacity) is available. Basic HDD, Basic SSD, Zonal, and Enterprise tiers are unavailable.
- **Protocols:** NFSv3 and NFSv4.1 are available. However, **Managed Microsoft AD is unavailable**, so NFSv4.1 Kerberos authentication with Managed AD is unsupported (use RPCSEC_GSS / system auth within supported bounds).
- **Networking:** Only **Direct Peering** is supported for VPC connectivity. Private Services Access and Private Service Connect are unavailable for Filestore.
- **GKE integration:** The Filestore CSI driver is supported on GKE Autopilot clusters.

---

## IAM

**Supported principal types only:**
- Service accounts
- Workforce Identity Federation identities
- Workload Identity Federation identities
- GKE service accounts

Google Accounts, Google Groups, and Cloud Identity are unavailable.

**Unavailable features:**
- Principal access boundary (PAB) policies
- Privileged Access Manager (PAM)
- Policy Intelligence tools (Activity Analyzer, Policy Analyzer, Policy Simulator, Policy Troubleshooter, role recommendations, service account insights)
- Gemini role suggestions in the IAM role picker

**Service account domains differ:**
- User-managed: `PROJECT_ID.eu0.iam.gserviceaccount.com` (Berlin) or `PROJECT_ID.s3ns.iam.gserviceaccount.com` (S3NS)
- Compute default: `developer.eu0-system.iam.gserviceaccount.com` (Berlin) or `developer.s3ns-system.iam.gserviceaccount.com` (S3NS)
- Service agents: `eu0-system.iam.gserviceaccount.com` / `eu0-system.system.gserviceaccount.com` (Berlin) or `s3ns-system.iam.gserviceaccount.com` / `s3ns-system.system.gserviceaccount.com` (S3NS)

<!-- AUTO-SYNC:UPSTREAM-DIFFS:iam:START -->
**Latest upstream documentation updates (`2026-11-13`):**
- Only Workforce Identity Federation and Workload Identity Federation identities can be used as [principal identifiers](https://documentation.s3ns.fr/iam/docs/principal-identifiers).
- Policy Intelligence capabilities are unavailable.
- Principal Access Boundary (PAB) policies are unavailable.
- Privileged Access Manager (PAM) is unavailable.
- **Integrations — Organization Policy Service:** Organization Policy gives you centralized, programmatic control over your organization's resources. In Cloud de Confiance, predefined organization policies are provided and can be used; however, you can't do the following: - You can't create and use your own custom constraints. - You can't use managed constraints.
- **Security and access control — Supported principal types:** Only the following types of [principal types](https://documentation.s3ns.fr/iam/docs/principals-overview) are supported when creating policies in Cloud de Confiance: - Individual service accounts - Workforce Identity Federation identities - Workload Identity Federation identities - GKE service accounts
- **Security and access control — SCIM provisioning for Workforce Identity Federation:** SCIM provisioning for Workforce Identity Federation is unavailable in Cloud de Confiance.
- **Security and access control — Managed workload identities:** Managed workload identities let you bind strongly attested identities to your Compute Engine and GKE workloads. Managed workload identities are unavailable in Cloud de Confiance.
- **Security and access control — Agent Identity:** Agent Identity provides strongly attested identities that are tied to the lifecycle of agentic workloads. Agent Identity is unavailable in Cloud de Confiance.
- **Security and access control — Principal Access Boundary policies:** Principal Access Boundary policies let you define the resources that principals can access. These policies are unavailable in Cloud de Confiance.
- **Security and access control — Privileged Access Manager:** You can use Privileged Access Manager to control just-in-time temporary privilege elevation for select principals, and to view audit logs afterwards to find out who had access to what and when. This feature is unavailable in Cloud de Confiance.
- **Workflows and tools — Gemini assistance in the IAM role picker:** The IAM role picker lets you ask Gemini which roles to grant to your principals. In Cloud de Confiance, role suggestions from Gemini are unavailable.
- **Workflows and tools — Permission error messages:** In the Cloud de Confiance console, permission error messages provide basic remediation guidance. They don't provide the option to resolve permission errors directly from the error message.
- **Insights and observability — Policy Intelligence:** Policy Intelligence tools help you understand and manage your policies to proactively improve your security configuration. Policy Intelligence tools are unavailable in Cloud de Confiance. As a result, the following features are unavailable: - Activity Analyzer - Policy Analyzer - Policy Simulator - Policy Troubleshooter - Role recommendations - Service account insights
<!-- AUTO-SYNC:UPSTREAM-DIFFS:iam:END -->

---

## Kubernetes Engine (GKE)

**Cluster modes:** Autopilot only. Standard clusters are unavailable.

**Compute:** C3 and A3 machine series only. GPU available on A3 Edge (`a3-edgegpu-8g-nolssd`) with custom ComputeClass. TPUs unavailable.

**Storage:** Hyperdisk Balanced only. No fallback to Persistent Disk.

**Node configuration unavailable:** Arm workloads, Spot VMs, compact placement.

**Release channels:** Stable and Regular only. Rapid channel features may be preview-only.

**Networking:**
- VPC-native clusters only (no route-based)
- Maximum 32 Pods per node
- Regional external load balancer (`rxlb`) used instead of global (`gxlb`)
- Multi Cluster Ingress and multi-cluster Services (MCS) unavailable
- Cloud Service Mesh unavailable
- Network policies for pod/service communication control unavailable
- Cannot disable control plane endpoints or add authorized networks
- GKE Dataplane V2 observability tools unavailable

**Security unavailable:**
- GKE security posture, Binary Authorization, Confidential GKE Nodes
- GKE control plane authority, Policy Controller
- Connect gateway
- Privileged workload admission allowlists
- Secure kernel module loading

**Workload identity:** Uses `eu0.svc.id.goog` (Berlin) or `s3ns.svc.id.goog` (S3NS) domain instead of `svc.id.goog`.

**Service agent provisioning:** JIT (just-in-time) on first resource creation, not on API enablement. For Shared VPC setup, manually create service agents and grant default roles.

**Cloud Storage FUSE CSI driver:** Supported on GKE >= 1.36.0-gke.1266000. Requires:
- Setting `custom-endpoint=storage.apis-berlin-build0.goog:443` (Berlin) or `custom-endpoint=storage.s3nsapis.fr:443` (S3NS) in mount options
- Setting `skipCSIBucketAccessCheck: "true"` in volume attributes

**Unavailable:**
- Backup for GKE, GKE Hypercluster
- Config Sync, Config Connector, Config Controller
- Fleets and fleet management
- Google Cloud Observability integrations and dashboards
- Cluster notifications, workload metrics
- Ray Operator, Parallelstore
- Performance HPA profile, VPA InPlaceOrRecreate mode

<!-- AUTO-SYNC:UPSTREAM-DIFFS:kubernetes-engine:START -->
**Latest upstream documentation updates (`2026-11-19`):**
- **GKE modes:** Only GKE Autopilot clusters are available. GKE Standard clusters are unavailable.
- **Storage:** Only Hyperdisk Balanced storage types are available. Other storage types are unavailable.
- **Compute Engine virtual machines:** Only the C3 and A3 machine series are available. Other machine types are unavailable.
- **GPUs and TPUs:** GPUs are available on A3 machine types only. TPUs are not available.
- **Hardware and OS — Modes of operation:** Only GKE Autopilot clusters are available. GKE Standard clusters are unavailable.
- **Hardware and OS — Compute Engine virtual machines:** Only the C3 and A3 machine series are available. Other machine types are unavailable.
- **Hardware and OS — GPUs and TPUs:** GPUs are available on A3 machine types. The only available Edge machine type is `a3-edgegpu-8g-nolssd` and it must be set explicitly by using a [custom ComputeClass](https://documentation.s3ns.fr/kubernetes-engine/docs/how-to/autopilot-gpus#request-machine-custom). TPUs are unavailable.
- **Hardware and OS — Node pools:** The following node configuration features are unavailable: - Arm workloads - Spot VMs - Compact placement
- **Hardware and OS — Release channels:** Only the Stable and Regular release channels are available. For clusters enrolled in the Rapid channel, the features might be available in preview.
- **Hardware and OS — GKE Hypercluster:** GKE Hypercluster isn't available.
- **Availability and disaster recovery — Regions and zones:** Cloud de Confiance has only a single region, though with multiple zones. Multi-region features and cross-region failover are not supported. Deployment across multiple zones for resiliency is supported.
- **Availability and disaster recovery — Storage:** The only storage type available is Hyperdisk Balanced. All other storage types are unavailable. Because other storage types are unavailable, using automated disk type selection with a fallback to Persistent Disk is unavailable.
- **Availability and disaster recovery — Backup for GKE:** Backup for GKE is unavailable.
- **Availability and disaster recovery — Autoscaling:** Some customization options are unavailable: - The Performance HPA profile is unavailable. - The VPA `InPlaceOrRecreate` mode is unavailable.
- **Availability and disaster recovery — Cluster upgrade visibility and scheduled upgrades:** Cluster upgrade visibility and scheduled upgrades are unavailable.
- **Cost management — Cost optimization metrics:** Some cost optimization recommendations might be unavailable.
- **Cost management — Committed use discounts (CUDs):** Cloud de Confiance by S3NS offers compute flexible committed use discounts (CUDs) for eligible spend on GKE. To purchase compute flexible commitments, contact [ Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/). For more information, see the [billing differences page](https://documentation.s3ns.fr/billing/docs/tpc-differences).
- **Integrations — Cloud Storage:** Transferring data from Cloud Storage by using GKE Volume Populator is unavailable.
- **Integrations — Cloud Storage FUSE:** The [Cloud Storage FUSE](https://documentation.s3ns.fr/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) CSI driver is supported on clusters and node pools running GKE version 1.36.0-gke.1266000 or later. Configuration requirements depend on your GKE version: - **GKE version 1.36.0-gke.2684000 or later**: specify the `skipCSIBucketAccessCheck: "true"` volume attribute. The `custom-endpoint` mount option is not required because the CSI driver automatically discovers the storage endpoint. - **GKE versions between 1.36.0-gke.1266000 and 1.36.0-gke.2684000**: specify both the `skipCSIBucketAccessCheck: "true"` volume attribute and the `custom-endpoint` mount option. To configure these settings: - Specify the `skipCSIBucketAccessCheck: "true"` volume attribute in the PersistentVolume specification or Pod's ephemeral storage volume attributes. For example: `` volumeAttributes : skipCSIBucketAccessCheck : "true" `` - *(Versions between 1.36.0-gke.1266000 and 1.36.0-gke.2684000 only)* Specify the `custom-endpoint` mount option in the volume's `mountOptions`, either in a Pod's ephemeral storage volume or in a PersistentVolume, to point to the Cloud Storage API endpoint for your environment: `storage.s3nsapis.fr:443`. You can use either the [CLI flag format](https://documentation.s3ns.fr/storage/docs/cloud-storage-fuse/cli-options#custom-endpoint) or the [configuration file format](https://documentation.s3ns.fr/storage/docs/cloud-storage-fuse/config-file#format-and-fields). Both formats are parsed directly by the driver as mount options, so you don't need to supply a separate configuration file. - **CLI format**: `custom-endpoint=storage.s3nsapis.fr:443` - **Configuration file format**: `gcs-connection:custom-endpoint:storage.s3nsapis.fr:443` For more information about specifying mount options, see [Configure mount options](https://documentation.s3ns.fr/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options).
- **Integrations — Filestore:** The [Filestore CSI driver](https://documentation.s3ns.fr/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) is available only with the Filestore regional service tier by [creating a custom StorageClass](https://documentation.s3ns.fr/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver#storage-class). Automatically installed Filestore StorageClasses and Filestore multishares for GKE are unavailable. For more information, see the [Filestore differences page](https://documentation.s3ns.fr/filestore/docs/tpc-differences).
- **Security — Security features:** The following security features are unavailable: - GKE security posture - Binary Authorization for GKE - Confidential Google Kubernetes Engine Nodes - GKE control plane authority - Policy Controller - Agent Identity for GKE (Preview)
- **Security — Authentication:** Connect gateway is unavailable.
- **Security — Workload identity:** Workload identity pool domains (and the Kubernetes principal identifiers that use them) are specified slightly differently in Google Cloud and Cloud de Confiance by S3NS, using `s3ns.svc.id.goog` rather than `svc.id.goog`. So, for example, when specifying a Kubernetes ServiceAccount using Workload Identity Federation for GKE in an [IAM policy](https://documentation.s3ns.fr/kubernetes-engine/docs/concepts/workload-identity#kubernetes-resources-iam-policies), you use `.../ PROJECT_ID .s3ns.svc.id.goog/subject/ns/ NAMESPACE /sa/ KUBERNETES_SERVICE_ACCOUNT `.
- **Security — Node security:** Secure kernel module loading is unavailable.
- **Security — Service agent provisioning:** In Cloud de Confiance, service agents (universe-managed service accounts) are provisioned **Just-In-Time (JIT)** when you create your first resource for a service, rather than when the API is enabled. If you need to grant permissions to a service agent before creating resources (for example, when configuring a [Shared VPC](https://documentation.s3ns.fr/kubernetes-engine/docs/how-to/cluster-shared-vpc)), you must manually create the service agent and grant it the required default roles. For instructions on how to manually trigger service agent creation grant roles, see [Create and grant roles to service agents](https://documentation.s3ns.fr/iam/docs/create-service-agent). Then, grant the default `Kubernetes Engine Service Agent` (`service- PROJECT_NUMBER @container-engine-robot.s3ns-system.iam.gserviceaccount.com`) to the agent that you create.
- **Security — GKE Sandbox:** In Cloud de Confiance, only the gVisor sandbox type has been tested for use with GKE Pods.
- **Network — IP addressing:** Only VPC-native clusters are supported. Route-based clusters are unavailable.
- **Network — Maximum Pods per node:** There is a maximum limit of 32 Pods per node.
- **Network — Network isolation:** The following customization options for network isolation are unavailable: - Disabling internal and external endpoints of the control plane. - Assigning additional Pod IPv4 ranges to a cluster. - Restricting egress traffic from the API server.
- **Network — Application exposure:** When using the GKE Ingress controller, the global Google Cloud external application load balancer (`gxlb`) is not used. In Cloud de Confiance by S3NS, a regional external load balancer (`rxlb`) is used.
- **Network — Multi-cluster networking:** Multi Cluster Ingress and multi-cluster Services (MCS) are unavailable.
- **Network — Observability:** GKE Dataplane V2 observability tools are unavailable.
- **Network — Cloud Service Mesh:** Cloud Service Mesh is unavailable.
- **Network — Load balancing:** The following load balancing features are unavailable: - Weighted load balancing. - Zonal affinity for Internal passthrough Network Load Balancer. - Utilization-based load balancing.
- **Network — IP ranges:** The available IP address ranges, such as for [ingress firewall rules](https://documentation.s3ns.fr/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws), depend on your environment, as follows: - 177.222.80.0/23 - 177.222.87.0/26 - 177.222.87.64/26
- **Workloads — Predefined compute classes:** Only the general-purpose compute class is available. All other predefined compute classes are unavailable.
- **Workloads — Image streaming:** Image streaming is unavailable.
- **Insights and observability — Logging and monitoring:** Workload metrics are unavailable.
- **Insights and observability — Google Cloud Observability:** All Google Cloud Observability integrations and dashboards are unavailable.
- **Insights and observability — Cluster notifications:** Cluster notifications are unavailable.
- **Insights and observability — Google Cloud Managed Service for Prometheus:** Google Cloud Managed Service for Prometheus is unavailable.
- **AI/ML features — Ray Operator:** The Ray Operator for GKE is unavailable.
- **Resource management — Config Sync:** Config Sync is available with only the [manual installation method](https://documentation.s3ns.fr/kubernetes-engine/config-sync/docs/how-to/installing-kubectl). Because the GKE Hub (Fleet) API is unavailable, the following management and observability features are not supported: - Fleet-level defaults and fleet packages (`ConfigDelivery`). - Centralized management through the Config Sync dashboard in the Cloud de Confiance console. - Integrated dashboards and Cloud Monitoring metrics in the Cloud de Confiance console. You can use local Prometheus scraping (port 8675) for metrics and alerting instead.
- **Resource management — Config Connector, Config Controller:** Config Connector and Config Controller are unavailable.
- **Multi-cluster management — Fleets:** Fleets, fleet dashboards, and fleet team management are unavailable.
<!-- AUTO-SYNC:UPSTREAM-DIFFS:kubernetes-engine:END -->

---

## Logging

**Available:** Audit Logs, Logs Explorer, log buckets (with CMEK and custom retention), log views, log regionalization, aggregated log sinks, default settings configuration.

**Log collection:** Only from sovereign cloud resources and applications using client libraries or the Logging API. Ops Agent, legacy Logging agent, and open-source frameworks are unavailable.

**Log sink destinations available:** Sovereign cloud project, log bucket, Pub/Sub topic.
**Log sink destinations unavailable:** BigQuery datasets, Cloud Storage buckets.

**Unavailable features:**
- Observability Analytics and linked BigQuery datasets
- Log-based metrics (creation and visualization)
- Alerting policies on logs
- Streaming and tailing log entries
- Dashboard log visualization
- Custom indexing
- Retroactive log export
- Configuring log scopes via console

---

## Managed Airflow (Cloud Composer)

- **Version:** Only **Managed Airflow Gen 3 (Cloud Composer 3)** is available. Composer 1 and Composer 2 are unavailable.
- **Resiliency and sizing:**
  - Only **Highly Resilient (HA)** mode is available (Standard resilience mode is unavailable).
  - Only the **Large** environment size and **Custom** environment preset are available (Small and Medium presets are unavailable).
- **Maintenance caveat:** Custom maintenance windows configured on the environment do **not** apply to the underlying Cloud SQL database instance.
- **Airflow operators:** Only operators for services available in the sovereign cloud work. Operators targeting external Google services (Google Docs, Sheets, Ads) or third-party clouds (AWS, Azure, Snowflake) are unavailable.

---

## Managed Service for Apache Spark (Dataproc)

- **Deployment mode:** Only **cluster deployment on Compute Engine** (image version `2.3` and later) is available.
- **Unavailable deployment modes:**
  - Serverless for Apache Spark (batches and interactive sessions) is **unavailable**.
  - Managed Spark on GKE clusters is **unavailable**.
- **Supported machine types & storage:**
  - Only `m3`, `c3-highcpu`, `c3-highmem`, `c3-standard`, and `a3` (with NVIDIA H100 SXM GPUs) machine types.
  - Only **Hyperdisk** boot disks (Persistent Disk and Local SSD are unavailable).
  - Secondary workers **cannot** use Spot or Preemptible VMs.
- **Unavailable cluster & job features:**
  - Autoscaling policies
  - Initialization actions and custom images
  - Optional open-source components (Component Gateway, Jupyter Notebooks, Persistent History Server)
  - Enhanced Flexibility Mode (EFM)
  - Workflow templates
  - Granular IAM and Kerberos / secure multi-tenancy

---

## Monitoring

**Available:** Listing metric/resource types, listing metric values, PromQL queries, Prometheus API export.

**All other Cloud Monitoring API methods are unavailable.**

**Metric collection:** Only from sovereign cloud services. The following are unavailable:
- Ops Agent, legacy Monitoring agent
- Client libraries, OpenTelemetry, open-source frameworks
- On-prem/hybrid-cloud metrics
- Prometheus metrics collection
- Custom metrics

**Unavailable features:**
- Alerting policies, uptime checks, synthetic monitors
- Charts and dashboards
- Multi-project aggregation (metrics scopes)

**Recommendation:** Use PromQL with Grafana for querying and visualization.

---

## Network Service Tiers

- Only **Premium Tier** is available. Standard Network Service Tier is unavailable.

---

## Organization Policy

- **Available constraints:** All legacy managed constraints are available, along with a subset of managed constraints and custom constraints for supported services.
- **Unavailable features:**
  - Dry-run organization policies
  - Policy Intelligence tools (Policy Simulator, Policy Analyzer, Policy Troubleshooter)

---

## Pub/Sub

*Source: `/pubsub/docs/tpc-differences` on S3NS and Berlin, both last updated 2026-10-26, same
content in both regions.*

**Unavailable features:**
- Authentication for push subscriptions
- Schemas
- AI Inference Single Message Transforms (SMTs). Other SMTs are not listed as unavailable.
- Import topics from Amazon Kinesis Data Streams, Azure Event Hubs, Amazon MSK and Confluent Cloud
- Pub/Sub Lite

**Unsupported integrations:** Dataflow, Cloud Functions, App Engine and Cloud Run. For
third-party integrations, check with the vendor.

**Availability:** single region, zonal separation supported. No multi-region features and no
cross-region failover.

**Architecture:** data is not globally available, only in the universe's region. Resource
location restrictions are not supported.

**Not listed as unavailable:** dead-letter topics, exactly-once delivery, filtering, ordering
keys, snapshots and seek, BigQuery and Cloud Storage subscriptions, push payload unwrapping,
and Cloud Storage import topics. The page lists only what is unavailable, so treat these as
available, and test one before depending on it.
Features in preview are not available.

---

## Resource Manager

- Project IDs are automatically prefixed with `eu0:` (Berlin) or `s3ns:` (S3NS).
- Organizations are provided by the platform operator. You cannot create your own organization. Google Workspace and Cloud Identity orgs are unavailable.
- Guided organization setup flow in the console is unavailable.

---

## Secret Manager

- **Replication:** Both **automatic replication** (scoped to the sovereign cloud universe) and **regional secrets** are available. User-managed replication is unavailable.
- **Regional secret endpoint difference:** Regional secrets use the global base URL (`https://secretmanager.apis-berlin-build0.goog/v1/projects/PROJECT_ID/locations/REGION/secrets...` or `https://secretmanager.s3nsapis.fr/v1/projects/PROJECT_ID/locations/REGION/secrets...`) rather than a regional `secretmanager.REGION.rep.googleapis.com` endpoint.
- **API versions:** Only the `v1` API is available (`v1beta1` and `v1beta2` are unavailable).
- **Discovery document:** Querying the REST discovery endpoint (`/$discovery/rest?version=v1&key=API_KEY`) requires passing an explicit API key.
- **Unavailable features and integrations:**
  - GKE Secret Manager add-on
  - Parameter Manager

---

## Service Usage

- Only sovereign cloud APIs and services can be enabled. Private/third-party APIs created with Cloud Endpoints cannot be enabled.
- Default enabled APIs for new projects include only services available in the sovereign cloud.

---

## Storage Transfer Service

- **Available transfers:** Transfers between Cloud Storage buckets and **agent-based transfers** from Amazon S3 or S3-compatible object storage (using Transfer Service on-premises/self-hosted agents).
- **Unavailable sources and modes:**
  - Agentless transfers from Amazon S3
  - Microsoft Azure Blob Storage transfers
  - Transfers from URL lists
  - Event-driven transfers

<!-- AUTO-SYNC:UPSTREAM-DIFFS:storage-transfer:START -->
**Latest upstream documentation updates (`2026-11-19`):**
- Event-driven transfers and cross-bucket replication are unavailable.
- Agentless transfers from Amazon S3 are unavailable. Agents are required for transfers from S3-compatible sources.
- Transfers from Azure Blob Storage, HDFS, and URL lists are unavailable.
- **Integrations — Data sources:** The following sources are unavailable: - Azure Blob Storage - Hadoop Distributed File System (HDFS) - URL lists Transfers from Amazon S3 and other S3-compatible storage must use transfer agents. Agentless transfers from Amazon S3 are unavailable.
- **Workflows and tools — Event-driven transfers:** Event-driven transfers are unavailable.
- **Workflows and tools — Cross-bucket replication:** Cross-bucket replication is unavailable. Use scheduled or one-time transfers between Cloud Storage buckets instead.
- **Workflows and tools — Object filtering:** Filtering source objects by wildcard (glob pattern) or by Amazon S3 storage class is unavailable.
- **Workflows and tools — Agents:** Transfer agents must be started with the `--universe-domain=s3nsapis.fr` flag so that they contact Cloud de Confiance by S3NS endpoints. `gcloud transfer agents install` sets this flag and pulls the agent image from the Cloud de Confiance by S3NS registry automatically. If you start the agent container with `docker run` or `podman run`, pass this flag explicitly.
- **Workflows and tools — Cloud Shell:** Cloud Shell is not available in Cloud de Confiance by S3NS. You must install and configure the gcloud CLI on a local machine to access Cloud de Confiance by S3NS.
<!-- AUTO-SYNC:UPSTREAM-DIFFS:storage-transfer:END -->

---

## Terraform

- **Provider configuration:** Must set `universe_domain` (`apis-berlin-build0.goog` or `s3nsapis.fr`) and use custom endpoints where required (such as `storage_custom_endpoint` for the GCS state backend).
- **Unavailable CLI tools:**
  - Policy validation with `gcloud beta terraform vet` is unavailable (use native `terraform` checks instead).
  - Bulk resource export with `gcloud beta resource-config bulk-export` is unavailable (use native `terraform import` / configuration generation instead).

---

## VPC (Virtual Private Cloud)

- **No default network:** New projects do not have a `default` VPC network.
- **Auto mode networks:** Create a single subnet in the single sovereign cloud region.
- **Network tier:** Premium Tier only (Standard Tier unavailable).
- **Private Google Access (PGA) domains and VIPs:**
  - Berlin: `private.apis-berlin-build0.goog` and `restricted.apis-berlin-build0.goog`
  - S3NS: `private.s3nsapis.fr` (`177.222.88.0/30`) and `restricted.s3nsapis.fr` (`177.222.88.4/30`)
- **Unavailable features:**
  - Private Services Access (service networking peering; use Private Service Connect or Direct Peering depending on the service)
  - Policy-based routes
  - Network Connectivity Center VPC spokes

---

## VPC Service Controls

- **Access levels:** Only basic access levels bound directly to a policy can be used. Custom access levels and standalone access levels are unavailable.
- **Unavailable perimeter types:** Perimeter bridges are unavailable.
- **Ingress and egress rule limitations:** Ingress and egress rules **cannot** filter by service methods/operations, service identities, or VPC networks.

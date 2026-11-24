# Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS) - Available Services Reference

Google Cloud Dedicated in Germany (`u-germany-northeast1`) and Cloud de Confiance by S3NS in France (`u-france-east1`) are sovereign cloud offerings that provide a subset of Google Cloud services in dedicated, regionally constrained environments. Not all Google Cloud services are available — only the services listed below are supported.

## Available API Services

The following services have confirmed documentation and API availability in the sovereign cloud regions:

<!-- AUTO-SYNC:AVAILABLE-API-SERVICES:START -->
- Access Context Manager
- Access Transparency
- Agent Platform (Gemini Enterprise Agent Platform)
- API Discovery Service
- API Keys
- Artifact Registry
- BigLake
- BigQuery
- BigQuery Data Policy
- BigQuery ML
- BigQuery Reservation
- BigQuery Storage
- Bigtable
- Cloud Armor
- Cloud Asset Inventory
- Cloud Audit Logs
- Cloud Billing
- Cloud Build
- Cloud DNS
- Cloud External Key Manager (EKM)
- Cloud GPUs
- Cloud Interconnect
- Cloud KMS
- Cloud Load Balancing
- Cloud Logging
- Cloud Monitoring
- Cloud NAT
- Cloud NGFW
- Cloud Quotas
- Cloud Router
- Cloud Run
- Cloud SQL
- Cloud Storage
- Cloud VPN
- Compute Engine
- Container-Optimized OS
- Filestore
- Google Cloud CLI (gcloud SDK)
- Google Kubernetes Engine (GKE)
- Hyperdisk
- IAM
- Managed Airflow (Cloud Composer 3)
- Managed Service for Apache Spark (Dataproc)
- Network Service Tiers
- Organization Policy
- Private Service Connect
- Pub/Sub
- Resource Manager
- Secret Manager
- Service Account Credentials
- Service Directory
- Service Usage
- Shielded VM
- Storage Transfer Service
- Terraform
- VPC
- VPC Service Controls
- Workforce Identity Federation
- Workload Identity Federation
<!-- AUTO-SYNC:AVAILABLE-API-SERVICES:END -->

---

## S3NS SecNumCloud 3.2 Qualification Status (PREMI3NS)

On **Cloud de Confiance by S3NS** (`u-france-east1`, PREMI3NS offering), services fall into three ANSSI **SecNumCloud 3.2** qualification categories (source: [s3ns.io/offres/premi3ns-cloud-de-confiance](https://www.s3ns.io/offres/premi3ns-cloud-de-confiance)):

- **Qualifié SecNumCloud 3.2:** Fully covered by the ANSSI SecNumCloud 3.2 qualification visa (and ISO 27001 / HDS certification).
- **Qualification en cours:** Available and documented on S3NS today, with ANSSI SecNumCloud 3.2 qualification currently in progress. Verify compliance requirements with the customer before using these services for workloads strictly mandated to run only on SecNumCloud-qualified services.
- **À venir:** Announced on the S3NS PREMI3NS roadmap; not yet generally available on S3NS.

<!-- AUTO-SYNC:SECNUMCLOUD-STATUS:START -->
**Summary (PREMI3NS catalog):** **29** `Qualifié SecNumCloud 3.2` | **13** `Qualification en cours` | **4** `À venir`

### Qualifié SecNumCloud 3.2 (29 services)

**Access Context Manager**, **Artifact Registry**, **BigQuery**, **BigQuery Reservation**, **Cloud Armor**, **Cloud DNS**, **Cloud Interconnect**, **Cloud Key Management Service**, **Cloud Load Balancing**, **Cloud Logging**, **Cloud Monitoring**, **Cloud NAT**, **Cloud Router**, **Cloud SQL**, **Cloud Storage**, **Cloud VPN**, **Compute Engine**, **Google Kubernetes Engine Autopilot**, **Identity and Access Management**, **Networking**, **Organization Policy**, **Pub/Sub**, **Resource Manager**, **Service Account Credentials**, **Service Directory**, **Service Usage**, **Virtual Private Cloud**, **Workforce identity federation**, **Workload identity federation using the Security Token Service API**.

### Qualification en cours (13 services — available on S3NS, ANSSI qualification in progress)

| Service (PREMI3NS) | Status | Documentation Hub |
|---|---|---|
| Access Transparency | `Qualification en cours` | Access Transparency |
| Bigtable | `Qualification en cours` | Bigtable |
| Cloud Quota | `Qualification en cours` | Cloud Quotas |
| Cloud Run | `Qualification en cours` | Cloud Run |
| Filestore | `Qualification en cours` | Filestore |
| Gemini platform | `Qualification en cours` | Agent Platform (Gemini Enterprise Agent Platform) |
| Managed Service for Apache Airflow | `Qualification en cours` | Managed Airflow (Cloud Composer 3) |
| Managed Service for Apache Spark | `Qualification en cours` | Managed Service for Apache Spark (Dataproc) |
| model garden | `Qualification en cours` | Agent Platform (Gemini Enterprise Agent Platform) |
| model registry | `Qualification en cours` | Agent Platform (Gemini Enterprise Agent Platform) |
| online inference | `Qualification en cours` | Agent Platform (Gemini Enterprise Agent Platform) |
| Secret Manager | `Qualification en cours` | Secret Manager |
| Storage Transfer Service | `Qualification en cours` | Storage Transfer Service |

### À venir (4 services — S3NS roadmap, not yet available)

**Cloud Asset Inventory**, **Cloud Build**, **Cloud Spanner**, **Network Connectivity Center**.
<!-- AUTO-SYNC:SECNUMCLOUD-STATUS:END -->

---

## Services by Category

### Compute & Containers

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Compute Engine | Available | Qualifié SecNumCloud 3.2 | Scalable VMs (`C3`, `M3`, `A3 Edge`) and instance groups |
| Google Kubernetes Engine (GKE) | Available | Qualifié SecNumCloud 3.2 | Managed Kubernetes (Autopilot mode only) |
| Cloud Run | Available | Qualification en cours | Managed serverless container services and jobs (from Artifact Registry) |
| Cloud GPUs | Available | Qualifié SecNumCloud 3.2 | NVIDIA H100 GPU acceleration on `A3` machine series |
| Container-Optimized OS | Available | Qualifié SecNumCloud 3.2 | Optimized OS for running containers on Compute Engine and GKE |
| Shielded VM | Available | Qualifié SecNumCloud 3.2 | Hardened VMs with rootkit/bootkit protection |
| Hyperdisk | Available | Qualifié SecNumCloud 3.2 | High-performance block storage (`hyperdisk-balanced`) for VMs |

**Key limitations:** Machine types (`C3`, `M3`, `A3`), single-region zones, and disk types (`Hyperdisk`) are constrained to the sovereign cloud environment. See [product-differences.md](product-differences.md) for per-service constraints.

### AI & Machine Learning

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Agent Platform (Gemini Enterprise Agent Platform) | Available | Qualification en cours | Model Garden, Model Registry, and synchronous online inference (`Predict`/`RawPredict`) for open-weight models (Gemma, Mistral) |
| BigQuery ML | Available | Qualifié SecNumCloud 3.2 | ML model training and inference via SQL (internal models only) |

**Key limitations:** Proprietary Gemini models, Model-as-a-Service, fine-tuning, batch inference, streaming/chat completion endpoints, and Vertex AI / Google Gen AI SDKs are unavailable.

### Networking

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Virtual Private Cloud (VPC) | Available | Qualifié SecNumCloud 3.2 | Core network for workload connectivity (no default VPC auto-created) |
| Cloud DNS | Available | Qualifié SecNumCloud 3.2 | Managed private DNS zones and DNS server policies |
| Cloud Load Balancing | Available | Qualifié SecNumCloud 3.2 | Regional Application and Network Load Balancers (Premium Tier only) |
| Cloud VPN | Available | Qualifié SecNumCloud 3.2 | HA VPN IPsec tunnels to peer networks |
| Cloud Interconnect | Available | Qualifié SecNumCloud 3.2 | Dedicated Interconnect and Partner Interconnect (with MACsec) |
| Cloud Router | Available | Qualifié SecNumCloud 3.2 | Regional dynamic BGP route exchange |
| Cloud NAT | Available | Qualifié SecNumCloud 3.2 | Public NAT (IPv4-to-IPv4) outbound internet connectivity |
| Private Service Connect | Available | Qualifié SecNumCloud 3.2 | Private access to managed services and sovereign cloud APIs |
| Network Service Tiers | Available | Qualifié SecNumCloud 3.2 | Premium Network Service Tier |
| Cloud Next Generation Firewall (NGFW) | Available | Qualifié SecNumCloud 3.2 | Essentials and Standard tiers distributed firewall |
| VPC Service Controls | Available | Qualifié SecNumCloud 3.2 | Security perimeters for sovereign cloud services |
| Google Cloud Armor | Available | Qualifié SecNumCloud 3.2 | Standard tier DDoS and WAF protection for regional external ALB |
| Service Directory | Available | Qualifié SecNumCloud 3.2 | Service registry and private DNS discovery |

**Key limitations:** Global load balancers, Cloud CDN, Certificate Manager, Classic VPN, Cross-Cloud Interconnect, Private NAT, Standard Network Tier, and NGFW Enterprise (IPS/TLS inspection) are unavailable.

### Storage & Data Transfer

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Cloud Storage | Available | Qualifié SecNumCloud 3.2 | Single-region object storage |
| Filestore | Available | Qualification en cours | Regional tier managed NFS file storage (1 TiB–9.75 TiB, Direct Peering) |
| Storage Transfer Service | Available | Qualification en cours | Bucket-to-bucket transfers and agent-based Amazon S3 transfers |
| Hyperdisk | Available | Qualifié SecNumCloud 3.2 | Scalable high-performance block storage |

**Key limitations:** Multi-region/dual-region buckets, Storage Insights, Basic/Zonal/Enterprise Filestore tiers, and agentless AWS / Azure Storage Transfer are unavailable.

### Databases

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Cloud SQL | Available | Qualifié SecNumCloud 3.2 | Managed relational databases (MySQL and PostgreSQL, Enterprise Plus on C3) |
| Bigtable | Available | Qualification en cours | Managed NoSQL wide-column database (single-region, multi-zone replication, SSD/HDD) |

**Key limitations:** Cloud SQL Server engine, Spanner, Firestore, Memorystore, and AlloyDB are not available. Bigtable GoogleSQL, Data Boost, BigQuery federation, and cross-region replication are unavailable.

### Data Analytics & Orchestration

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| BigQuery | Available | Qualifié SecNumCloud 3.2 | Managed data warehouse with built-in ML |
| BigQuery Data Policy | Available | Qualifié SecNumCloud 3.2 | Data governance and access policies |
| BigQuery Reservation | Available | Qualifié SecNumCloud 3.2 | Capacity reservation management |
| BigQuery Storage | Available | Qualifié SecNumCloud 3.2 | High-throughput read/write API for analytics workloads |
| BigLake | Available | Qualifié SecNumCloud 3.2 | Query external data in Cloud Storage with access delegation |
| Managed Service for Apache Spark (Dataproc) | Available | Qualification en cours | Apache Spark clusters on Compute Engine (image 2.3+, `C3`/`M3`/`A3`) |
| Managed Airflow (Cloud Composer) | Available | Qualification en cours | Managed Apache Airflow Gen 3 (Composer 3, Highly Resilient Large/Custom) |
| Pub/Sub | Available | Qualifié SecNumCloud 3.2 | Regional event stream ingestion and messaging |

**Key limitations:** Serverless Spark, Spark on GKE, Composer 1/2, Dataflow, Dataform, Datastream, and Data Fusion are unavailable.

### Security and Identity

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Identity and Access Management (IAM) | Available | Qualifié SecNumCloud 3.2 | Fine-grained access control for resources |
| Secret Manager | Available | Qualification en cours | Secret storage and versioning (automatic and regional replication, `v1` API) |
| Access Context Manager | Available | Qualifié SecNumCloud 3.2 | Basic attribute-based access levels (IP and geo conditions) |
| Access Transparency | Available | Qualification en cours | Near real-time logs of operator accesses during support cases |
| Cloud KMS | Available | Qualifié SecNumCloud 3.2 | Software key management and CMEK integration |
| Cloud External Key Manager (EKM) | Available | Qualifié SecNumCloud 3.2 | Externally managed encryption keys via VPC |
| API Keys | Available | — | API key creation and management |
| VPC Service Controls | Available | Qualifié SecNumCloud 3.2 | Security perimeters for data protection |
| Organization Policy Service | Available | Qualifié SecNumCloud 3.2 | Programmatic resource governance and constraints |
| Workforce Identity Federation | Available | Qualifié SecNumCloud 3.2 | External identity provider federation for human users |
| Workload Identity Federation | Available | Qualifié SecNumCloud 3.2 | External identity federation for workloads |
| Service Account Credentials | Available | Qualifié SecNumCloud 3.2 | Service account key and token management |
| Cloud Audit Logs | Available | Qualifié SecNumCloud 3.2 | Activity tracking and auditing |

**Key limitations:** Cloud HSM, KMS Autokey, Security Command Center, Binary Authorization, Certificate Authority Service, and Google Identity/Workspace accounts are not available.

### Observability

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Cloud Logging | Available | Qualifié SecNumCloud 3.2 | Log storage, search, analysis, and sinks (Log buckets, Pub/Sub) |
| Cloud Monitoring | Available | Qualifié SecNumCloud 3.2 | Metric listing and PromQL / Prometheus API export |

**Key limitations:** Cloud Trace, Cloud Profiler, Error Reporting, Ops Agent, custom metrics, and native Monitoring dashboards/alerts are unavailable (use PromQL with Grafana).

### Application Development, Billing, and Resource Management

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Artifact Registry | Available | Qualifié SecNumCloud 3.2 | Container (`Docker`), language (`NPM`), and OS package (`Apt`, `Yum`) repositories |
| Resource Manager | Available | Qualifié SecNumCloud 3.2 | Organization, folder, project, and tag management |
| Cloud Billing | Available | — | Operator-managed billing accounts and BigQuery billing export |
| Cloud Quotas | Available | Qualification en cours | Quota inspection and support-assisted quota adjustments |
| Service Usage | Available | Qualifié SecNumCloud 3.2 | API enablement and lifecycle management |
| API Discovery Service | Available | — | API metadata and discovery documents |
| Terraform | Available | — | Infrastructure provisioning via the Google Terraform provider |

<!-- AUTO-SYNC:ADDITIONAL-CATEGORY-SERVICES:START -->
### Newly Discovered Sovereign Cloud Services

| Service | Status | S3NS SecNumCloud 3.2 | Description |
|---------|--------|----------------------|-------------|
| Cloud Asset Inventory | Available | — | Landing, differences, guides, release notes |
| Cloud Build | Available | — | Landing, differences, guides, release notes |
<!-- AUTO-SYNC:ADDITIONAL-CATEGORY-SERVICES:END -->

---

## Discovered Documentation Inventory (Auto-Synced)

<!-- AUTO-SYNC:DISCOVERED-PRODUCTS-TABLE:START -->
Total scraped pages: **468** (Berlin GCD) / **467** (France S3NS).

| Service / Documentation Hub | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Differences Guide | Last Updated |
|---|---:|---:|---|---|---|
| Access Context Manager | 8 | 8 | Qualifié SecNumCloud 3.2 | `access-context-manager_tpc-differences.md` | 2026-11-13 |
| Access Transparency | 7 | 7 | Qualification en cours | — | 2026-11-23 |
| Agent Platform (Gemini Enterprise Agent Platform) | 7 | 7 | Qualification en cours | `gemini-enterprise-agent-platform_tpc-differences.md` | 2026-11-20 |
| API Keys | 4 | 4 | — | — | 2026-11-13 |
| Artifact Registry | 6 | 6 | Qualifié SecNumCloud 3.2 | `artifact-registry_tpc-differences.md` | 2026-11-13 |
| BigQuery | 16 | 16 | Qualifié SecNumCloud 3.2 | `bigquery_tpc-differences.md` | 2026-11-23 |
| Bigtable | 14 | 14 | Qualification en cours | `bigtable_tpc-differences.md` | 2026-11-13 |
| Cloud Armor | 3 | 3 | Qualifié SecNumCloud 3.2 | `armor_tpc-differences.md` | 2026-11-13 |
| Cloud Asset Inventory | 17 | 17 | — | `asset-inventory_tpc-differences.md` | 2026-11-20 |
| Cloud Billing | 7 | 7 | — | `billing_tpc-differences.md` | 2026-11-13 |
| Cloud Build | 14 | 14 | — | `build_tpc-differences.md` | 2026-11-13 |
| Cloud DNS | 8 | 8 | Qualifié SecNumCloud 3.2 | `dns_tpc-differences.md` | 2026-11-13 |
| Cloud Interconnect | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_interconnect_tpc-differences.md` | 2026-11-13 |
| Cloud KMS | 8 | 8 | Qualifié SecNumCloud 3.2 | `kms_tpc-differences.md` | 2026-11-18 |
| Cloud Load Balancing | 3 | 3 | Qualifié SecNumCloud 3.2 | `load-balancing_tpc-differences.md` | 2026-11-16 |
| Cloud Logging | 10 | 10 | Qualifié SecNumCloud 3.2 | `logging_tpc-differences.md` | 2026-11-23 |
| Cloud Monitoring | 4 | 4 | Qualifié SecNumCloud 3.2 | `monitoring_tpc-differences.md` | 2026-11-23 |
| Cloud NAT | 3 | 3 | Qualifié SecNumCloud 3.2 | `nat_tpc-differences.md` | 2026-11-13 |
| Cloud NGFW | 3 | 3 | Qualifié SecNumCloud 3.2 | `firewall_tpc-differences.md` | 2026-11-13 |
| Cloud Quotas | 29 | 29 | Qualification en cours | `quotas_tpc-differences.md` | 2026-11-17 |
| Cloud Router | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_router_tpc-differences.md` | 2026-11-13 |
| Cloud Run | 14 | 14 | Qualification en cours | `run_tpc-differences.md` | 2026-11-23 |
| Cloud SQL | 3 | 3 | Qualifié SecNumCloud 3.2 | `sql_tpc-differences.md` | 2026-11-24 |
| Cloud Storage | 10 | 10 | Qualifié SecNumCloud 3.2 | `storage_tpc-differences.md` | 2026-11-23 |
| Cloud VPN | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_vpn_concepts_tpc-differences.md` | 2026-11-13 |
| Compute Engine | 12 | 12 | Qualifié SecNumCloud 3.2 | `compute_tpc-differences.md` | 2026-11-20 |
| Container-Optimized OS | 3 | 3 | Qualifié SecNumCloud 3.2 | `container-optimized-os_tpc-differences.md` | 2026-11-13 |
| Filestore | 16 | 16 | Qualification en cours | `filestore_tpc-differences.md` | 2026-11-23 |
| Google Cloud CLI (gcloud SDK) | 2 | 2 | — | — | 2026-11-22 |
| Google Kubernetes Engine (GKE) | 9 | 9 | Qualifié SecNumCloud 3.2 | `kubernetes-engine_tpc-differences.md` | 2026-11-23 |
| IAM | 18 | 18 | Qualifié SecNumCloud 3.2 | `iam_tpc-differences.md` | 2026-11-18 |
| Managed Airflow (Cloud Composer 3) | 18 | 18 | Qualification en cours | `composer_tpc-differences.md` | 2026-11-24 |
| Managed Service for Apache Spark (Dataproc) | 10 | 10 | Qualification en cours | `managed-spark_tpc-differences.md` | 2026-11-24 |
| Network Service Tiers | 3 | 3 | Qualifié SecNumCloud 3.2 | `network-tiers_tpc-differences.md` | 2026-11-13 |
| Organization Policy | 3 | 3 | Qualifié SecNumCloud 3.2 | `organization-policy_tpc-differences.md` | 2026-11-13 |
| Pub/Sub | 11 | 11 | Qualifié SecNumCloud 3.2 | `pubsub_tpc-differences.md` | 2026-11-20 |
| Resource Manager | 11 | 11 | Qualifié SecNumCloud 3.2 | `resource-manager_tpc-differences.md` | 2026-11-13 |
| Secret Manager | 10 | 10 | Qualification en cours | `secret-manager_tpc-differences.md` | 2026-11-13 |
| Service Directory | 2 | 2 | Qualifié SecNumCloud 3.2 | — | 2026-11-13 |
| Service Usage | 9 | 9 | Qualifié SecNumCloud 3.2 | `service-usage_tpc-differences.md` | 2026-11-13 |
| Storage Transfer Service | 8 | 8 | Qualification en cours | `storage-transfer_tpc-differences.md` | 2026-11-19 |
| Terraform | 32 | 32 | — | `terraform_tpc-differences.md` | 2026-11-13 |
| VPC | 7 | 7 | Qualifié SecNumCloud 3.2 | `vpc_tpc-differences.md` | 2026-11-13 |
| VPC Service Controls | 3 | 3 | Qualifié SecNumCloud 3.2 | `vpc-service-controls_tpc-differences.md` | 2026-11-13 |
<!-- AUTO-SYNC:DISCOVERED-PRODUCTS-TABLE:END -->

---

## Recent Sovereign Cloud Release Notes (Auto-Synced)

The following table summarizes the most recent sovereign cloud release notes extracted automatically from `docs-raw-s3ns/release-notes.md` and `docs-raw/release-notes.md`:

<!-- AUTO-SYNC:RECENT-RELEASE-NOTES:START -->
| Date | Product | Type | Summary |
|---|---|---|---|
| November 23, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R49) Version updates:** GKE cluster versions have been updated. |
| November 18, 2026 | **Google Kubernetes Engine** | `Issue` | In GKE versions 1.35, 1.36, and 1.37, enabling application-layer secrets encryption (`/kubernetes-engine/docs/how-to/encrypting-secrets`) on a new or existing cluster whose control plane stores cluster state in Spanner encrypts only Kubernetes Secrets (`ENCRYPTED`) instead of all Kubernetes API objects (`ALL_OBJECTS_ENCRYPTION_ENABLED`). |
| November 17, 2026 | **Cloud SQL for MySQL** | `Feature` | Blue-green deployments for Cloud SQL for MySQL are [generally available](https://documentation.s3ns.fr/products#product-launch-stages). |
| November 16, 2026 | **Cloud Build** | `Announcement` | Cloud Build is now available in Google Cloud. For more information, see Cloud Build differences in Google Cloud versus Google Cloud (`/build/docs/tpc-differences`). |
| November 13, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R48) Version updates:** GKE cluster versions have been updated. |
| November 12, 2026 | **Compute Engine** | `Feature` | **Generally available**: In a managed instance group (MIG) with instance flexibility, you can override the instance template's disk and minimum CPU platform properties per instance selection. Overriding these properties lets you combine machine types that require different disk types, boot images, or CPU platforms in a single MIG. For more information, see About instance flexibility in MIGs (`/compute/docs/instance-groups/about-instance-flexibility`). |
| November 12, 2026 | **Google Kubernetes Engine** | `Change` | In GKE version 1.35.1-gke.1516000 or later, GKE Dataplane V2 clusters use a unified `cilium-cni` configuration instead of a chained CNI setup. With this change, Cilium configures the Pod default gateway by using its node-local virtual router interface (`cilium_host`), which has the statically assigned link-local IP address `169.254.4.6`. |
| November 10, 2026 | **Compute Engine** | `Feature` | For your regional managed instance groups (MIGs), you can view planned instance allocations across zones and machine types, check the number of instances waiting for capacity, and configure alerts based on this data. Compute Engine records these details in instance distribution logs in Cloud Logging when you create a regional MIG or increase its target size. For more information, see View instance distribution logs (`/compute/docs/instance-groups/view-instance-distribution-logs`). |
| November 10, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R47) Version updates:** GKE cluster versions have been updated. |
| November 09, 2026 | **Google Kubernetes Engine** | `Feature` | GKE Gateway now supports Server Name Indication (SNI)-based routing with TLS passthrough. You can use TLS protocol-specific rules to route incoming TLS streams from the Gateway to Kubernetes Services based on SNI without terminating TLS at the GKE Gateway load balancer. Application developers can create TLSRoute resources to expose secure TLS traffic to applications that run in the GKE cluster. |
| November 09, 2026 | **Virtual Private Cloud** | `Feature` | **General Availability**: You can create an internal range with the `INTERNAL_ADDRESS` purpose to allocate global internal IPv4 addresses for Private Service Connect endpoints that access global Google APIs (`/vpc/docs/about-accessing-google-apis-endpoints`). |
| November 04, 2026 | **Cloud Storage** | `Feature` | You can pause hard deletions for a bucket when you need more time to restore soft-deleted objects before they're permanently deleted. For more information, see Pause permanent (hard) deletions of soft-deleted objects (`/storage/docs/pause-hard-deletions`). |
<!-- AUTO-SYNC:RECENT-RELEASE-NOTES:END -->

---

## Notable Unavailable Services

The following commonly used Google Cloud services are **NOT** available in GCD or S3NS:

<!-- AUTO-SYNC:NOTABLE-UNAVAILABLE-SERVICES:START -->
- **AI/ML:** Proprietary Gemini APIs, Vertex AI Training/Pipelines/AutoML, Vision AI, Natural Language AI, Translation AI
- **Databases:** Spanner (`À venir` on S3NS roadmap), Firestore, Memorystore (Redis/Memcached), AlloyDB, Database Migration Service
- **Data:** Dataflow, Dataform, Data Fusion, Datastream, Analytics Hub, Serverless Spark
- **Serverless:** App Engine, Cloud Run functions / Cloud Functions, Cloud Scheduler, Cloud Tasks, Eventarc
- **CI/CD:** Cloud Deploy, Cloud Source Repositories
- **Observability:** Cloud Trace, Cloud Profiler, Error Reporting, Ops Agent
- **Security:** Cloud HSM, Security Command Center, Binary Authorization, Certificate Authority Service, Identity-Aware Proxy (IAP), Managed Microsoft AD
- **Networking:** Cloud CDN, Certificate Manager, Classic VPN, Cross-Cloud Interconnect, Network Connectivity Center (`À venir` on S3NS roadmap)
- **Other:** Cloud Shell, Apigee, API Gateway, Firebase
<!-- AUTO-SYNC:NOTABLE-UNAVAILABLE-SERVICES:END -->

---

## Developer Tools and SDK Support

Client libraries are supported for: C#/.NET, C++, Go, Java, JavaScript/Node.js, PHP, Python, Ruby, Rust (always configure `GOOGLE_CLOUD_UNIVERSE_DOMAIN`).

The Google Cloud CLI (`gcloud`) is the primary command-line interface for managing resources when configured with the sovereign cloud universe domain.

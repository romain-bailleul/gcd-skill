# Google Cloud release notes

Source: https://berlin.devsitetest.how/release-notes
Last updated: 2026-11-20

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/tpc-differences) for more details.














- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Documentation

](https://berlin.devsitetest.how/docs)












# Google Cloud release notes 



















The following release notes cover the most recent changes over the last 60 days.
For a comprehensive list of product-specific release notes, see the
[individual product release note pages](/release-notes/all).

You can also see and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes) or you
can programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).















To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/gcp-release-notes.xml) directly.











## November 18, 2026

**Google Kubernetes Engine**

Issue 


In GKE versions 1.35, 1.36, and 1.37, enabling
[application-layer secrets encryption](/kubernetes-engine/docs/how-to/encrypting-secrets)
on a new or existing cluster whose control plane stores cluster state in Spanner
encrypts only Kubernetes Secrets (`ENCRYPTED`) instead of all Kubernetes API
objects (`ALL_OBJECTS_ENCRYPTION_ENABLED`).

- Clusters that already have encryption of all Kubernetes API objects enabled
(`ALL_OBJECTS_ENCRYPTION_ENABLED`) continue to encrypt all objects.

- Clusters where application-layer secrets encryption is in the `ENCRYPTED`
state encrypt only Secrets and require manual Secret re-encryption after a
Cloud KMS key rotation. To check which objects are encrypted in your cluster,
see
[Verify that application-layer secrets encryption is enabled](/kubernetes-engine/docs/how-to/encrypting-secrets#verifying_secrets_encryption).

A fix to restore encryption of all Kubernetes API objects for newly configured clusters is in progress.



## November 17, 2026

**Cloud SQL for MySQL**

Feature 


Blue-green deployments for Cloud SQL for MySQL are
[generally available](https://berlin.devsitetest.how/products#product-launch-stages).

Blue-green deployments let you update databases—such as performing major
version upgrades from MySQL 8.0 to 8.4 and staging hardware or configuration
modifications in a green staging environment—while minimizing downtime.
You can create and manage blue-green deployments using the Google Cloud console,
the gcloud CLI, the Cloud SQL Admin API, or Terraform.

For more information, see [About blue-green deployments in
Cloud SQL](/sql/docs/mysql/about-blue-green-deployments).



## November 16, 2026

**Cloud Build**

Announcement 


Cloud Build is now available in Google Cloud. For more information,
see
[Cloud Build differences in Google Cloud versus Google Cloud](/build/docs/tpc-differences).



## November 13, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R48) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.5166000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.3229000+preview is no longer available in the Rapid channel.




### Regular channel




- The following versions are now available in the Regular channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)




### Stable channel




There are no new releases in the Stable channel.




### Extended channel




- The following versions are now available in the Extended channel:

- [1.32.13-gke.3070000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3070000)

- [1.33.13-gke.2398000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2398000)




### No channel (deprecated)




- The following versions are now available:

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)

- The following node versions are now available:

- [1.32.13-gke.3070000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3070000)

- [1.33.13-gke.2398000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2398000)

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)






Change 

#### (2026-R48) Version updates

There are no new releases in the Stable channel.



Change 

#### (2026-R48) Version updates

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)




Change 

#### (2026-R48) Version updates

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.5166000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.3229000+preview is no longer available in the Rapid channel.




Change 

#### (2026-R48) Version updates

- The following versions are now available:

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)

- The following node versions are now available:

- [1.32.13-gke.3070000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3070000)

- [1.33.13-gke.2398000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2398000)

- [1.34.12-gke.1776000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1776000)

- [1.36.5-gke.2370000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2370000)

- [1.37.2-gke.1325000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1325000)




Change 

#### (2026-R48) Version updates

- The following versions are now available in the Extended channel:

- [1.32.13-gke.3070000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3070000)

- [1.33.13-gke.2398000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2398000)




## November 12, 2026

**Compute Engine**

Feature 


**Generally available**: In a managed instance group (MIG) with instance
flexibility, you can override the instance template's disk and minimum CPU
platform properties per instance selection. Overriding these properties lets you
combine machine types that require different disk types, boot images, or CPU
platforms in a single MIG. For more information, see
[About instance flexibility in MIGs](/compute/docs/instance-groups/about-instance-flexibility).


**Google Kubernetes Engine**

Change 


In GKE version 1.35.1-gke.1516000 or later, GKE Dataplane V2 clusters use a
unified `cilium-cni` configuration instead of a chained CNI setup. With this
change, Cilium configures the Pod default gateway by using its node-local
virtual router interface (`cilium_host`), which has the statically assigned
link-local IP address `169.254.4.6`.

As a result, node-local `kubelet` health checks (`kube-probe` for liveness,
readiness, and startup probes) and NodeLocal DNSCache traffic now originate from
`169.254.4.6` instead of the `.1` address of the node's Pod CIDR range (for
example, `10.x.x.1`).

If your workloads only accept traffic from specific IP address ranges, for
example through application-level IP allowlists or web server ACLs, allow
traffic from `169.254.4.6/32` before you upgrade. Otherwise, health checks for
these workloads might fail.

For more information, see
[Using GKE Dataplane V2](/kubernetes-engine/docs/how-to/dataplane-v2#health-check-source-ip).



## November 10, 2026

**Compute Engine**

Feature 


For your regional managed instance groups (MIGs), you can view planned instance
allocations across zones and machine types, check the number of instances
waiting for capacity, and configure alerts based on this data. Compute Engine
records these details in instance distribution logs in Cloud Logging when you
create a regional MIG or increase its target size. For more information, see
[View instance distribution logs](/compute/docs/instance-groups/view-instance-distribution-logs).


**Google Kubernetes Engine**

Change 

#### (2026-R47) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4814000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1209000

- 1.34.12-gke.1363000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1975000

- 1.35.8-gke.2308000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2377000

- 1.36.5-gke.1259000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.1-gke.1697000

- 1.37.1-gke.3020000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Alpha version 1.38.0-gke.2884000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- 1.34 to [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- 1.35 to [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- 1.35 to [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- 1.36 to [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- 1.37 to [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)




### Regular channel




- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation in the Regular channel.

- The following versions are no longer available in the Regular channel:

- 1.34.12-gke.1011000

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046003

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)




### Stable channel




- Version [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000) is now the default version for cluster creation in the Stable channel.

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1102000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439001

- 1.35.8-gke.1626001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)




### Extended channel




- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.32.13-gke.3004000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3004000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.33.13-gke.2339000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2339000)

- The following versions are no longer available in the Extended channel:

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2906000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2207000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1011000

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046003

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- 1.33 to [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)




### No channel (deprecated)




- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- The following node versions are now available:

- [1.32.13-gke.3004000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3004000)

- [1.33.13-gke.2339000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2339000)

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- The following versions are no longer available:

- 1.34.11-gke.1102000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1363000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.2308000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.5-gke.1259000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.1-gke.3020000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)






Change 

#### (2026-R47) Version updates

- Version [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000) is now the default version for cluster creation in the Stable channel.

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1102000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439001

- 1.35.8-gke.1626001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)




Change 

#### (2026-R47) Version updates

- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation in the Regular channel.

- The following versions are no longer available in the Regular channel:

- 1.34.12-gke.1011000

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046003

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)




Change 

#### (2026-R47) Version updates

- Version [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4814000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1209000

- 1.34.12-gke.1363000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1975000

- 1.35.8-gke.2308000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2377000

- 1.36.5-gke.1259000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.1-gke.1697000

- 1.37.1-gke.3020000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Alpha version 1.38.0-gke.2884000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- 1.34 to [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- 1.35 to [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- 1.35 to [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- 1.36 to [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- 1.37 to [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)




Change 

#### (2026-R47) Version updates

- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- The following node versions are now available:

- [1.32.13-gke.3004000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3004000)

- [1.33.13-gke.2339000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2339000)

- [1.34.12-gke.1698000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1698000)

- [1.35.9-gke.1673000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1673000)

- [1.36.5-gke.2262000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-2262000)

- [1.37.2-gke.1042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-2-gke-1042000)

- The following versions are no longer available:

- 1.34.11-gke.1102000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1363000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.2308000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.5-gke.1259000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.1-gke.3020000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)




Change 

#### (2026-R47) Version updates

- Version [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.32.13-gke.3004000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-3004000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.33.13-gke.2339000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2339000)

- The following versions are no longer available in the Extended channel:

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2906000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2207000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.12-gke.1011000

- 1.34.12-gke.1153000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046003

- 1.36.4-gke.2326000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- 1.33 to [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)




## November 09, 2026

**Google Kubernetes Engine**

Feature 


GKE Gateway now supports Server Name Indication (SNI)-based routing with TLS passthrough. You can use TLS protocol-specific rules to route incoming TLS streams from the Gateway to Kubernetes Services based on SNI without terminating TLS at the GKE Gateway load balancer. Application developers can create TLSRoute resources to expose secure TLS traffic to applications that run in the GKE cluster.

Creating TLSRoute resources requires the Gateway API version 1.5.0 or later CRDs (Standard channel), which are installed in GKE version 1.35.2-gke.1842000 or later.

This feature supports single-cluster and multi-cluster GKE Gateway load balancers by using the following GatewayClass resources:

- `gke-l7-rilb`

- `gke-l7-regional-external-managed`

- `gke-l7-rilb-mc`

- `gke-l7-regional-external-managed-mc`

- `gke-l7-cross-regional-internal-managed-mc`

For more information, see [Deploy a TLS passthrough Gateway](/kubernetes-engine/docs/how-to/deploy-tls-passthrough-gateway).


**Virtual Private Cloud**

Feature 


**General Availability**: You can create an internal range with the
`INTERNAL_ADDRESS` purpose to allocate global internal IPv4 addresses for
[Private Service Connect endpoints that access global Google
APIs](/vpc/docs/about-accessing-google-apis-endpoints).

For more information, see [Internal ranges for Private Service Connect
endpoints](/vpc/docs/internal-ranges#reserve-for-endpoints).



## November 04, 2026

**Cloud Storage**

Feature 


You can pause hard deletions for a bucket when you need more time to restore
soft-deleted objects before they're permanently deleted. For more information,
see
[Pause permanent (hard) deletions of soft-deleted objects](/storage/docs/pause-hard-deletions).



## November 03, 2026

**Virtual Private Cloud**

Feature 


**General Availability**: VPC Flow Logs supports logging for IPv6 encapsulation
flows. For more information, see
[IpConnection field format](/vpc/docs/about-flow-logs-records#IpConnection).



## October 29, 2026

**Identity and Access Management**

Feature 


The Admin (`roles/admin`), Writer (`roles/writer`), and Reader (`roles/reader`)
basic roles are generally available
([GA](https://berlin.devsitetest.how/products#product-launch-stages)). For more
information, see [Basic roles](/iam/docs/roles-overview#basic).

The legacy basic roles—Owner (`roles/owner`), Editor (`roles/editor`), and
Viewer (`roles/viewer`)—are still available for use and are being
actively maintained. However, if you need to grant a basic role, we recommend
granting the Admin, Writer, or Reader role instead of a legacy basic role.
This is because the newer roles support additional features, such as the use of
[IAM Conditions](/iam/docs/conditions-overview).



## October 27, 2026

**Google Cloud Armor**

Feature 


Cloud Armor supports advanced match conditions to include attributes for
inspecting request body content and parameters. This lets you write
custom CEL rules to filter traffic based on raw body content, structured data
(JSON, Form Data, GraphQL), and query parameters. For more information, see
[Attributes](/armor/docs/create-security-policy-rules#attributes) in "Create and view Cloud Armor security policy
rules." This feature is
[generally available (GA)](https://berlin.devsitetest.how/products#product-launch-stages).


**Google Kubernetes Engine**

Change 

#### (2026-R46) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4162000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.2743000+preview is no longer available in the Rapid channel.




### Regular channel




- The following versions are now available in the Regular channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Stable channel




- The following versions are now available in the Stable channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### Extended channel




- The following versions are now available in the Extended channel:

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2759000

- 1.31.14-gke.2825000

- 1.31.14-gke.3042000

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2788000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2074000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- 1.33 to [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)




### No channel (deprecated)




- The following versions are now available:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- The following node versions are now available:

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.






Change 

#### (2026-R46) Version updates

- The following versions are now available in the Stable channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4162000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.2743000+preview is no longer available in the Rapid channel.




Change 

#### (2026-R46) Version updates

- The following versions are now available:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- The following node versions are now available:

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Extended channel:

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2759000

- 1.31.14-gke.2825000

- 1.31.14-gke.3042000

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2788000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2074000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- 1.33 to [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)




## October 26, 2026

**Compute Engine**

Security 


A vulnerability (CVE-2026-85299) about incorrect authorization in
Compute Engine was discovered and has been addressed. For more information,
see the
[GCP-2026-073 security bulletin](/compute/docs/security-bulletins#gcp-2026-073). 

**Google Kubernetes Engine**

Change 

#### (2026-R45) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.3229000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1153000

- 1.35.8-gke.1919000

- 1.36.4-gke.2326000

- 1.37.1-gke.1552000

- Alpha version 1.38.0-gke.2240000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.35 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- 1.37 to [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)




### Regular channel




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### Stable channel




- Version [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)




### Extended channel




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2963000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2701000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1952000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### No channel (deprecated)




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following node versions are now available:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following versions are no longer available:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)






Change 

#### (2026-R45) Version updates

- Version [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R45) Version updates

- Version [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.3229000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1153000

- 1.35.8-gke.1919000

- 1.36.4-gke.2326000

- 1.37.1-gke.1552000

- Alpha version 1.38.0-gke.2240000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.35 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- 1.37 to [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following node versions are now available:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following versions are no longer available:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2963000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2701000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1952000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




## October 21, 2026

**Bigtable**

Feature 


Bigtable is now available in Google Cloud. For more information, see
[Bigtable in Google Cloud versus Google Cloud](/bigtable/docs/tpc-differences).



## October 20, 2026

**Filestore**

Feature 


Filestore is available in Google Cloud. For more information, see [Filestore differences in Google Cloud versus Google Cloud](/filestore/docs/tpc-differences).



## October 19, 2026

**Google Cloud Armor**

Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable`
rulesets. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-v33-stable`

- `xss-v33-stable`

- `lfi-v33-stable`

- `rfi-v33-stable`

- `rce-v33-stable`

- `methodenforcement-v33-stable`

- `scannerdetection-v33-stable`

- `protocolattack-v33-stable`

- `php-v33-stable`

- `sessionfixation-v33-stable`

- `java-v33-stable`

- `nodejs-v33-stable`




Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `stable`
rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-stable`

- `xss-stable`

- `lfi-stable`

- `rfi-stable`

- `rce-stable`

- `methodenforcement-stable`

- `scannerdetection-stable`

- `protocolattack-stable`

- `php-stable`

- `sessionfixation-stable`



**Virtual Private Cloud**

Feature 


**General Availability**: VPC Flow Logs adds the following metadata annotations
and packet drop reasons for Cloud NAT:

- Metadata annotations: `connection.nat_ip`, `connection.nat_port`, and
`nat_gateway_details`

- Drop reasons: `NAT_ENDPOINT_INDEPENDENT_CONFLICT`, `NAT_OUT_OF_CONNECTIONS`,
and `NAT_OUT_OF_PORTS`

For more information, see
[Record format](/vpc/docs/about-flow-logs-records#record_format) and
[Packet drop reasons](/vpc/docs/about-flow-logs-records#drop-reason).



## October 14, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R44) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2884000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1011000

- 1.35.8-gke.1796000

- 1.36.4-gke.2046002

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.0-gke.3503000

- Alpha version 1.38.0-gke.1002000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.34 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.35 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.35 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.36 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### Regular channel




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




### Stable channel




- The following versions are now available in the Stable channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- Version 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)




### Extended channel




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2925000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.31 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.32 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- 1.33 to [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




### No channel (deprecated)




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following node versions are now available:

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available:

- 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.36 to [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)






Change 

#### (2026-R44) Version updates

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- Version 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




Change 

#### (2026-R44) Version updates

- Version [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2884000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1011000

- 1.35.8-gke.1796000

- 1.36.4-gke.2046002

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.0-gke.3503000

- Alpha version 1.38.0-gke.1002000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.34 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.35 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.35 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.36 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following node versions are now available:

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available:

- 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.36 to [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2925000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.31 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.32 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- 1.33 to [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




## October 10, 2026

**Cloud SQL for MySQL**

Change 


MySQL 8.0.46 is now the
[default minor version](/sql/docs/mysql/db-versions#database-version-support)
for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL,
see [MySQL 8.0](/sql/docs/mysql/db-versions#mysql-8.0).



## October 08, 2026

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports the
`innodb_cloudsql_managed_buffer_pool_tuneup_pct` database flag.

Managed buffer pool automatically adjusts the InnoDB buffer pool size to reduce
out-of-memory events. When instance memory usage remains at or below 70% for 10
minutes or longer after prior reductions, Cloud SQL increases the buffer pool
size. You can now use the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` flag
to change this 70% threshold to a different percentage. Increase the threshold
to restore the InnoDB buffer pool size when baseline usage exceeds 70%, or
decrease it to preserve additional RAM allocation for memory spikes.

This flag requires the Cloud SQL maintenance version
[*MYSQL_VERSION*.R20260726.00_05](/sql/docs/mysql/maintenance-changelog)
or later. For more information, see [Enable managed buffer
pool](/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool).


**Google Kubernetes Engine**

Change 

#### (2026-R43) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2743000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495000

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.35 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)




### Regular channel




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### Stable channel




- Version [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000) is now available in the Stable channel.

- Version 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Extended channel




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2825000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.31 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.32 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- 1.33 to [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### No channel (deprecated)




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following node versions are now available:

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following versions are no longer available:

- 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1036000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)






Change 

#### (2026-R43) Version updates

- Version [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000) is now available in the Stable channel.

- Version 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2743000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495000

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.35 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following node versions are now available:

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following versions are no longer available:

- 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1036000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2825000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.31 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.32 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- 1.33 to [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




## October 07, 2026

**Google Kubernetes Engine**

Feature 


The microVM sandbox type is now Generally Available (GA) with GKE Sandbox in
clusters that run version 1.37.0-gke.4713000 and later. MicroVM sandboxes
provide hardware virtualization and isolation for untrusted workloads, AI agent
runtimes, and multi-tenant environments. GKE microVM sandboxes use Kata
Containers and Cloud Hypervisor to provide this isolation while maintaining a
full Linux kernel that includes standard Linux features

For more information, see the
[GKE Sandbox](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/sandbox-pods)
documentation.


**Virtual Private Cloud**

Feature 


Service producers can let service consumers establish more connections to a
Private Service Connect endpoint or backend by
[configuring the target published service (service attachment) to use an additional NAT
IP address](/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint).
For more information, see
[Maximum connections](/vpc/docs/about-vpc-hosted-services#max-connections).



## October 06, 2026

**Google Kubernetes Engine**

Issue 


Starting with GKE version 1.36, the default engine for kube-dns is [CoreDNS](https://coredns.io/). For
Pod IP DNS queries in the ` . .pod.cluster.local` format,
CoreDNS returns NXDOMAIN if the specified ` ` does not exist. The
legacy `kubernetes/dns` implementation skipped checking the existence of the
namespace provided in the ` ` segment in these queries.

Queries in the ` . .pod.cluster.local` format are not part of
the
[Kubernetes DNS specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md).
We can't guarantee that uses outside of those specified in the DNS spec will
remain consistent across releases.

Mitigation:

- **Recommended**: Migrate to supported headless Service DNS records
(` . . .svc.cluster.local`).

- **Workaround**: Ensure the ` ` specified in the DNS query exists in
the cluster.




## October 05, 2026

**Google Kubernetes Engine**

Feature 


GKE support for using the `c4-standard-*` machine types (up to 192 vCPUs) as
Confidential GKE Nodes with Intel TDX is generally available. For more
information, see the following pages:

- To use this feature with GKE , see [Encrypt workload data in-use with
Confidential GKE
Nodes](https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/confidential-gke-nodes).

- To learn more about the feature from Compute Engine, see [Confidential VM
overview](https://berlin.devsitetest.how/confidential-computing/confidential-vm/docs/confidential-vm-overview).

- To see supported configurations, including machine support, see [Supported
configurations](https://berlin.devsitetest.how/confidential-computing/confidential-vm/docs/supported-configurations)
and its "Machine types, CPUs, and zones" section.




## October 02, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R42) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2240000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.35 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)




### Regular channel




- The following versions are now available in the Regular channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




### Stable channel




- Version [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- The following versions are no longer available in the Stable channel:

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)




### Extended channel




- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2759000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.31 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.32 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- 1.33 to [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




### No channel (deprecated)




- The following versions are now available:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following node versions are now available:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following versions are no longer available:

- 1.34.9-gke.1065000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)






Change 

#### (2026-R42) Version updates

- Version [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- The following versions are no longer available in the Stable channel:

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)




Change 

#### (2026-R42) Version updates

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




Change 

#### (2026-R42) Version updates

- Version [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2240000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.35 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)




Change 

#### (2026-R42) Version updates

- The following versions are now available:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following node versions are now available:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following versions are no longer available:

- 1.34.9-gke.1065000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




Change 

#### (2026-R42) Version updates

- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2759000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.31 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.32 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- 1.33 to [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




## September 30, 2026

**Cloud Storage**

Feature 


Cloud Storage client libraries now provide automated, end-to-end checksumming by
default for object read and write operations to help maintain data integrity
from client to storage. For more information, see
[data validation](/storage/docs/data-validation#client-validation-writes).


**Managed Service for Apache Spark**

Announcement 


Managed Service for Apache Spark is now available in Google Cloud. For more information, see [Managed Service for Apache Spark differences in Google Cloud versus Google Cloud](https://documentation.s3ns.fr/managed-spark/docs/tpc-differences).



## September 29, 2026

**Compute Engine**

Feature 


**Generally available**: You can create a standard or archive snapshot of a
disk and protect the snapshot with a customer-managed encryption key
(CMEK), even if the source disk isn't protected with a CMEK. If the source disk
is protected with a CMEK, then you can use a different CMEK to encrypt the new
snapshot.

For more information, see [Create a CMEK-encrypted snapshot](/compute/docs/disks/customer-managed-encryption#create_snapshot).



## September 28, 2026

**Cloud Logging**

Breaking 


Only platform services can write log entries to billing accounts.
These logs have names with the format
`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`.
For more information, see
[`entries.write`](/logging/docs/reference/v2/rest/v2/entries/write).



## September 23, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R40) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.1002000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380000

- 1.36.4-gke.1247000

- 1.37.0-gke.3165000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.35 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.36 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- 1.37 to [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)




### Regular channel




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




### Stable channel




- Version [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000) is now available in the Stable channel.

- Version 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Extended channel




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.31 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.32 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- 1.33 to [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




### No channel (deprecated)




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following node versions are now available:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following versions are no longer available:

- 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1222000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)






Change 

#### (2026-R40) Version updates

- Version [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000) is now available in the Stable channel.

- Version 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




Change 

#### (2026-R40) Version updates

- Version [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.1002000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380000

- 1.36.4-gke.1247000

- 1.37.0-gke.3165000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.35 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.36 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- 1.37 to [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following node versions are now available:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following versions are no longer available:

- 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1222000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.31 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.32 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- 1.33 to [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)
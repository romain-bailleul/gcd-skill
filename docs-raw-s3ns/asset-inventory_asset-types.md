# Asset types

Source: https://documentation.s3ns.fr/asset-inventory/docs/asset-types
Last updated: 2026-11-20

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/asset-inventory/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Cloud Asset Inventory

](https://documentation.s3ns.fr/asset-inventory/docs)






- 








[

Reference

](https://documentation.s3ns.fr/asset-inventory/docs/asset-types)












# Asset types 















This document lists the supported asset types in Cloud Asset Inventory. These
include [resource types](#resource-types) and
[policy types](#policy-types).

You can use these asset types with the following Cloud Asset Inventory operations:

- 

[Export to BigQuery](/asset-inventory/docs/export-bigquery)

- 

[Export to Cloud Storage](/asset-inventory/docs/export-cloud-storage)

- 

[List assets](/asset-inventory/docs/list-assets)

- 

[Search for resources](/asset-inventory/docs/search-resources)

- 

[Search resources for IAM allow policies](/asset-inventory/docs/search-allow-policies)

You might also need to make use of [asset names](/asset-inventory/docs/asset-names)
associated with these asset types when working with Cloud Asset Inventory.

Unless otherwise specified, all resource types are available in the export,
list, monitor,
and search APIs.
Effective tags are supported only in the search APIs.

## Resource types

Cloud Asset Inventory provides eventual consistency on current data and best-effort
consistency on historical data. While rare, it's possible that Cloud Asset Inventory can
miss some data updates. To learn more, see
[Cloud Asset Inventory's consistency model](/asset-inventory/docs/asset-inventory-overview#consistency-model).

Unless noted in the following table, data is synchronized once every few hours.
If a sync fails, data freshness is delayed until the next successful sync.

Cloud Asset Inventory uses the following asset types for the `RESOURCE`
[content type](/asset-inventory/docs/asset-inventory-overview#content_types).









| 
Service | 
Asset type | 
|



















| 




**Access Policy (Access Context Manager)**



To retrieve all access policies in the export, list, and monitor APIs:

- **REST**: Set the `contentType` to `ACCESS_POLICY`.
- **gcloud CLI**: Set the `--content-type` flag to `access-policy`.

| 













- 


[
`accesscontextmanager. googleapis. com/ AuthorizedOrgsDesc`
](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs)

















Not available in the analysis APIs.

















- 


[
`identity. accesscontextmanager. googleapis. com/ AccessLevel`
](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)

























- 


[
`identity. accesscontextmanager. googleapis. com/ AccessPolicy`
](/access-context-manager/docs/reference/rest/v1/accessPolicies)

























- 


[
`identity. accesscontextmanager. googleapis. com/ ServicePerimeter`
](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)























| 
|










| 




**Agent Identity API**


| 





[API reference](https://agentidentity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`agentidentity. googleapis. com/ AuthProvider`
](/iam/docs/reference/agentidentity/rest/v1/projects.locations.authProviders)

















Not available in the analysis APIs.















| 
|



































| 




**API keys**



The `location` field might not be populated for API keys assets.

| 





[API reference](https://apikeys.s3nsapis.fr/$discovery/rest?version=v2)












- 


[
`apikeys.googleapis.com/Key`
](/api-keys/docs/reference/rest/v2/keys)























| 
|


























| 




**App Design Center**


| 





[API reference](https://designcenter.s3nsapis.fr/$discovery/rest)












- 


[
`designcenter. googleapis. com/ Application`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ ApplicationTemplate`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ ApplicationTemplateRevision`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ Catalog`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ CatalogTemplate`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ CatalogTemplateRevision`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ Component`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ Connection`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ Share`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ SharedTemplate`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ SharedTemplateRevision`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions)













Effective tags aren't supported. 

















- 


[
`designcenter. googleapis. com/ Space`
](/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces)













Effective tags aren't supported. 















| 
|











































| 




**Artifact Registry**


| 





[API reference](https://artifactregistry.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`artifactregistry. googleapis. com/ DockerImage`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.dockerImages)

























- 


[
`artifactregistry. googleapis. com/ MavenArtifact`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts)

















Not available in the analysis APIs.

















- 


[
`artifactregistry. googleapis. com/ NpmPackage`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.npmPackages)

















Not available in the analysis APIs.

















- 


[
`artifactregistry. googleapis. com/ PythonPackage`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages)

















Not available in the analysis APIs.

















- 


[
`artifactregistry. googleapis. com/ Repository`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories)

























- 


[
`artifactregistry. googleapis. com/ Rule`
](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules)

















Not available in the analysis APIs.















| 
|












































| 




**BigQuery**


| 





[API reference](https://bigquery.s3nsapis.fr/$discovery/rest?version=v2)












- 


[
`bigquery. googleapis. com/ Dataset`
](/bigquery/docs/reference/rest/v2/datasets)













Effective tags aren't supported. 

















- 


[
`bigquery.googleapis.com/Model`
](/bigquery/docs/reference/rest/v2/models)













Effective tags aren't supported. 

















- 


[
`bigquery. googleapis. com/ Routine`
](/bigquery/docs/reference/rest/v2/routines)













Effective tags aren't supported. 

















- 


[
`bigquery. googleapis. com/ RowAccessPolicy`
](/bigquery/docs/reference/rest/v2/rowAccessPolicies)













Effective tags aren't supported. 

















- 


[
`bigquery.googleapis.com/Table`
](/bigquery/docs/reference/rest/v2/tables)













Effective tags aren't supported. 















| 
|




























| 




**BigQuery Reservation API**


| 





[API reference](https://bigqueryreservation.s3nsapis.fr/$discovery/rest)












- 


[
`bigqueryreservation. googleapis. com/ BiReservation`
](/bigquery/docs/reference/reservations/rest/v1/BiReservation)

















Not available in the analysis APIs.

















- 


[
`bigqueryreservation. googleapis. com/ CapacityCommitment`
](/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments)

















Not available in the analysis APIs.

















- 


[
`bigqueryreservation. googleapis. com/ Reservation`
](/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations)

















Not available in the analysis APIs.

















- 


[
`bigqueryreservation. googleapis. com/ ReservationAssignment`
](/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments)

















Not available in the analysis APIs.

















- 


[
`bigqueryreservation. googleapis. com/ ReservationGroup`
](/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservationGroups)

















Not available in the analysis APIs.















| 
|




























































































































| 




**Cloud DNS**


| 





[API reference](https://dns.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`dns.googleapis.com/ManagedZone`
](/dns/docs/reference/v1/managedZones)






Searchable attributes:





- 
`dnsName`



- 
`peeringConfig. targetNetwork. networkUrl`


























- 


[
`dns.googleapis.com/Policy`
](/dns/docs/reference/v1/policies)

























- 


[
`dns. googleapis. com/ ResourceRecordSet`
](/dns/docs/reference/v1/resourceRecordSets)

















Not available in the analysis APIs.

















- 


[
`dns. googleapis. com/ ResponsePolicy`
](/dns/docs/reference/v1/responsePolicies)

















Not available in the analysis APIs.

















- 


[
`dns. googleapis. com/ ResponsePolicyRule`
](/dns/docs/reference/v1/responsePolicyRules)

















Not available in the analysis APIs.















| 
|




































| 




**Cloud Key Management Service**


| 





[API reference](https://cloudkms.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`cloudkms. googleapis. com/ AutokeyConfig`
](/kms/docs/reference/rest/v1/AutokeyConfig)

























- 


[
`cloudkms. googleapis. com/ CryptoKey`
](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)

























- 


[
`cloudkms. googleapis. com/ CryptoKeyVersion`
](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions)

























- 


[
`cloudkms. googleapis. com/ EkmConfig`
](/kms/docs/reference/rest/v1/projects.locations.ekmConfig)

























- 


[
`cloudkms. googleapis. com/ EkmConnection`
](/kms/docs/reference/rest/v1/projects.locations.ekmConnections)

























- 


[
`cloudkms. googleapis. com/ ImportJob`
](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)

























- 


[
`cloudkms. googleapis. com/ KajPolicyConfig`
](/kms/docs/reference/rest/v1/KeyAccessJustificationsPolicyConfig)

















Not available in the analysis APIs.

















- 


[
`cloudkms. googleapis. com/ KeyHandle`
](/kms/docs/reference/rest/v1/projects.locations.keyHandles)

























- 


[
`cloudkms. googleapis. com/ KeyRing`
](/kms/docs/reference/rest/v1/projects.locations.keyRings)

























- 


[
`cloudkms. googleapis. com/ RetiredResource`
](/kms/docs/reference/rest/v1/projects.locations.retiredResources)

















Not available in the analysis APIs.















| 
|












| 




**Cloud Load Balancing**


| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ AuthzPolicy`
](/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies)

















Not available in the analysis APIs.















| 
|












| 




**Cloud Logging**



Cloud Logging asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://logging.s3nsapis.fr/$discovery/rest?version=v2)












- 


[
`logging.googleapis.com/Link`
](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links)

















Not available in the analysis APIs.

















- 


[
`logging. googleapis. com/ LogBucket`
](/logging/docs/reference/v2/rest/v2/projects.locations.buckets)

























- 


[
`logging. googleapis. com/ LogMetric`
](/logging/docs/reference/v2/rest/v2/projects.metrics)

























- 


[
`logging.googleapis.com/LogSink`
](/logging/docs/reference/v2/rest/v2/projects.sinks)

























- 


[
`logging.googleapis.com/LogView`
](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`logging. googleapis. com/ RecentQuery`
](/logging/docs/reference/v2/rest/v2/projects.locations.recentQueries)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`logging. googleapis. com/ SavedQuery`
](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`logging. googleapis. com/ Settings`
](/logging/docs/reference/v2/rest/v2/Settings)













Effective tags aren't supported. 



Not available in the analysis APIs.










The resource is served only when the Logging update API is called.









| 
|












| 




**Cloud Monitoring**


| 





[API reference](https://monitoring.s3nsapis.fr/$discovery/rest?version=v3)












- 


[
`monitoring. googleapis. com/ AlertPolicy`
](/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)

























- 


[
`monitoring. googleapis. com/ Dashboard`
](/monitoring/api/ref_v3/rest/v1/projects.dashboards)

















Not available in the analysis APIs.

















- 


[
`monitoring. googleapis. com/ NotificationChannel`
](/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)

























- 


[
`monitoring. googleapis. com/ Snooze`
](/monitoring/api/ref_v3/rest/v3/projects.snoozes)

























- 


[
`monitoring. googleapis. com/ UptimeCheckConfig`
](/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)

















Not available in the analysis APIs.















| 
|












| 




**Cloud Next Generation Firewall Enterprise**



Cloud Next Generation Firewall Enterprise asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ AddressGroup`
](/firewall/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies)

























- 


[
`networksecurity. googleapis. com/ FirewallEndpoint`
](/firewall/docs/reference/network-security/rest/v1/organizations.locations.firewallEndpoints)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ FirewallEndpointAssociation`
](/firewall/docs/reference/network-security/rest/v1/projects.locations.firewallEndpointAssociations)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ SecurityProfile`
](/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ SecurityProfileGroup`
](/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ TlsInspectionPolicy`
](/firewall/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies)

















Not available in the analysis APIs.















| 
|












| 




**Cloud OS Config**



Cloud OS Config asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://osconfig.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`osconfig. googleapis. com/ OSPolicyAssignment`
](/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments)













Effective tags aren't supported. 

















- 


[
`osconfig. googleapis. com/ OSPolicyAssignmentReport`
](/compute/docs/osconfig/rest/v1/projects.locations.instances.osPolicyAssignments.reports)













Effective tags aren't supported. 

















- 


[
`osconfig. googleapis. com/ PatchDeployment`
](/compute/docs/osconfig/rest/v1/projects.patchDeployments)













Effective tags aren't supported. 

















- 


[
`osconfig. googleapis. com/ VulnerabilityReport`
](/compute/docs/osconfig/rest/v1/projects.locations.instances.vulnerabilityReports)













Effective tags aren't supported. 



Not available in the analysis APIs.















| 
|




















































| 




**Cloud Service Mesh**


| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ AuthorizationPolicy`
](/service-mesh/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ ClientTlsPolicy`
](/service-mesh/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ ServerTlsPolicy`
](/service-mesh/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies)

















Not available in the analysis APIs.















| 
|












| 




**Cloud SQL**



Cloud SQL asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://sqladmin.s3nsapis.fr/$discovery/rest?version=v1beta4)












- 


[
`sqladmin.googleapis.com/Backup`
](/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns)

















Not available in the analysis APIs.

















- 


[
`sqladmin. googleapis. com/ BackupRun`
](/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns)

























- 


[
`sqladmin. googleapis. com/ Instance`
](/sql/docs/mysql/admin-api/rest/v1beta4/instances)























| 
|












| 




**Cloud Storage**


| 





[API reference](https://storage.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`storage.googleapis.com/Bucket`
](/storage/docs/json_api/v1/buckets)























| 
|












































| 




**Compute Engine**


| 





[API reference](https://compute.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`compute.googleapis.com/Address`
](/compute/docs/reference/rest/v1/addresses)


















Returns global and regional addresses in the search and analysis APIs, and only regional addresses in the list, export, query, and monitor APIs.











- 


[
`compute. googleapis. com/ Autoscaler`
](/compute/docs/reference/rest/v1/autoscalers)

























- 


[
`compute. googleapis. com/ BackendBucket`
](/compute/docs/reference/rest/v1/backendBuckets)

























- 


[
`compute. googleapis. com/ BackendService`
](/compute/docs/reference/rest/v1/backendServices)


















Returns global and regional backend services in the search and analysis APIs, and only regional backend services in the list, export, query, and monitor APIs.











- 


[
`compute. googleapis. com/ Commitment`
](/compute/docs/reference/rest/v1/regionCommitments)

























- 


[
`compute. googleapis. com/ CrossSiteNetwork`
](/compute/docs/reference/rest/v1/crossSiteNetworks)

























- 


[
`compute.googleapis.com/Disk`
](/compute/docs/reference/rest/v1/disks)


















Returns zonal and regional disks in the search and analysis APIs, and only zonal disks in the list, export, query, and monitor APIs.











- 


[
`compute. googleapis. com/ ExternalVpnGateway`
](/compute/docs/reference/rest/v1/externalVpnGateways)

























- 


[
`compute. googleapis. com/ Firewall`
](/compute/docs/reference/rest/v1/firewalls)

























- 


[
`compute. googleapis. com/ FirewallPolicy`
](/compute/docs/reference/rest/v1/firewallPolicies)

















Not available in the analysis APIs.

















- 


[
`compute. googleapis. com/ ForwardingRule`
](/compute/docs/reference/rest/v1/forwardingRules)


















Returns global and regional forwarding rules in the search and analysis APIs, and only regional forwarding rules in the list, export, query, and monitor APIs.











- 


[
`compute. googleapis. com/ GlobalAddress`
](/compute/docs/reference/rest/v1/globalAddresses)



























Not available in the analysis and search APIs.










Use `compute.googleapis.com/Address` instead in the search and analysis APIs.











- 


[
`compute. googleapis. com/ GlobalForwardingRule`
](/compute/docs/reference/rest/v1/globalForwardingRules)



























Not available in the analysis and search APIs.










Use `compute.googleapis.com/ForwardingRule` instead in the search and analysis APIs.











- 


[
`compute. googleapis. com/ HealthCheck`
](/compute/docs/reference/rest/v1/healthChecks)

























- 


[
`compute. googleapis. com/ HttpHealthCheck`
](/compute/docs/reference/rest/v1/httpHealthChecks)

























- 


[
`compute. googleapis. com/ HttpsHealthCheck`
](/compute/docs/reference/rest/v1/httpsHealthChecks)

























- 


[
`compute.googleapis.com/Image`
](/compute/docs/reference/rest/v1/images)

























- 


[
`compute. googleapis. com/ Instance`
](/compute/docs/reference/rest/v1/instances)






Searchable attributes:





- 
`deletionProtection`



- 
`externalIPs`



- 
`internalIPs`



- 
`machineType`



- 
`networkInterfaceNetworks`



- 
`networkInterfaceNames`









The following attributes are from the
[
OS Inventory](/compute/docs/instances/os-inventory-management),
which is attached on this Compute Engine Instance to
provide information on operating system and packages.
Learn more about
[
OS inventory management](/compute/docs/instances/os-inventory-management).






- `osLongName`


- `osShortName`








Supported [metadata](/compute/docs/metadata/overview) fields:





- `block-project-ssh-keys`


- `enable-oslogin`


- `enable-osconfig`


- `serial-port-enable`





















- 


[
`compute. googleapis. com/ InstanceGroup`
](/compute/docs/reference/rest/v1/instanceGroups)

























- 


[
`compute. googleapis. com/ InstanceGroupManager`
](/compute/docs/reference/rest/v1/instanceGroupManagers)

























- 


[
`compute. googleapis. com/ InstanceSettings`
](/compute/docs/reference/rest/v1/instanceSettings)

















Not available in the analysis APIs.

















- 


[
`compute. googleapis. com/ InstanceTemplate`
](/compute/docs/reference/rest/v1/instanceTemplates)

























- 


[
`compute. googleapis. com/ InstantSnapshot`
](/compute/docs/reference/rest/v1/instantSnapshots)

























- 


[
`compute. googleapis. com/ Interconnect`
](/compute/docs/reference/rest/v1/interconnects)

























- 


[
`compute. googleapis. com/ InterconnectAttachment`
](/compute/docs/reference/rest/v1/interconnectAttachments)

























- 


[
`compute.googleapis.com/License`
](/compute/docs/reference/rest/v1/licenses)

























- 


[
`compute. googleapis. com/ MachineImage`
](/compute/docs/reference/rest/v1/machineImages)

























- 


[
`compute.googleapis.com/Network`
](/compute/docs/reference/rest/v1/networks)






Searchable attributes:





- 
`gatewayIPv4`


























- 


[
`compute. googleapis. com/ NetworkAttachment`
](/compute/docs/reference/rest/v1/networkAttachments)






Searchable attributes:





- 
`connectionEndpointsIpAddresses`



- 
`connectionEndpointsIpv6Addresses`


























- 


[
`compute. googleapis. com/ NetworkEdgeSecurityService`
](/compute/docs/reference/rest/v1/networkEdgeSecurityServices)

























- 


[
`compute. googleapis. com/ NetworkEndpointGroup`
](/compute/docs/reference/rest/v1/networkEndpointGroups)

























- 


[
`compute. googleapis. com/ NodeGroup`
](/compute/docs/reference/rest/v1/nodeGroups)

























- 


[
`compute. googleapis. com/ NodeTemplate`
](/compute/docs/reference/rest/v1/nodeTemplates)

























- 


[
`compute. googleapis. com/ PacketMirroring`
](/compute/docs/reference/rest/v1/packetMirrorings)

























- 


[
`compute.googleapis.com/Project`
](/compute/docs/reference/rest/v1/projects)










Supported [metadata](/compute/docs/metadata/overview) fields:





- `block-project-ssh-keys`


- `enable-osconfig`


- `enable-oslogin`


- `serial-port-enable`





















- 


[
`compute. googleapis. com/ PublicAdvertisedPrefix`
](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes)

















Not available in the analysis APIs.

















- 


[
`compute. googleapis. com/ PublicDelegatedPrefix`
](/compute/docs/reference/rest/v1/publicDelegatedPrefixes)

























- 


[
`compute. googleapis. com/ RegionBackendService`
](/compute/docs/reference/rest/v1/regionBackendServices)



























Not available in the analysis and search APIs.










Use `compute.googleapis.com/BackendService` instead in the search and analysis APIs.











- 


[
`compute. googleapis. com/ RegionDisk`
](/compute/docs/reference/rest/v1/regionDisks)



























Not available in the analysis and search APIs.










Use `compute.googleapis.com/Disk` instead in the search and analysis APIs.











- 


[
`compute. googleapis. com/ Reservation`
](/compute/docs/reference/rest/v1/reservations)

























- 


[
`compute. googleapis. com/ ResourcePolicy`
](/compute/docs/reference/rest/v1/resourcePolicies)

























- 


[
`compute.googleapis.com/Route`
](/compute/docs/reference/rest/v1/routes)

























- 


[
`compute.googleapis.com/Router`
](/compute/docs/reference/rest/v1/routers)

























- 


[
`compute. googleapis. com/ SecurityPolicy`
](/compute/docs/reference/rest/v1/securityPolicies)

























- 


[
`compute. googleapis. com/ ServiceAttachment`
](/compute/docs/reference/rest/v1/serviceAttachments)

























- 


[
`compute. googleapis. com/ Snapshot`
](/compute/docs/reference/rest/v1/snapshots)

























- 


[
`compute. googleapis. com/ SslCertificate`
](/compute/docs/reference/rest/v1/sslCertificates)

























- 


[
`compute. googleapis. com/ SslPolicy`
](/compute/docs/reference/rest/v1/sslPolicies)

























- 


[
`compute. googleapis. com/ StoragePool`
](/compute/docs/reference/rest/v1/storagePools)

























- 


[
`compute. googleapis. com/ Subnetwork`
](/compute/docs/reference/rest/v1/subnetworks)






Searchable attributes:





- 
`gatewayAddress`


























- 


[
`compute. googleapis. com/ TargetGrpcProxy`
](/compute/docs/reference/rest/v1/targetGrpcProxies)

























- 


[
`compute. googleapis. com/ TargetHttpProxy`
](/compute/docs/reference/rest/v1/targetHttpProxies)

























- 


[
`compute. googleapis. com/ TargetHttpsProxy`
](/compute/docs/reference/rest/v1/targetHttpsProxies)

























- 


[
`compute. googleapis. com/ TargetInstance`
](/compute/docs/reference/rest/v1/targetInstances)

























- 


[
`compute. googleapis. com/ TargetPool`
](/compute/docs/reference/rest/v1/targetPools)

























- 


[
`compute. googleapis. com/ TargetSslProxy`
](/compute/docs/reference/rest/v1/targetSslProxies)

























- 


[
`compute. googleapis. com/ TargetTcpProxy`
](/compute/docs/reference/rest/v1/targetTcpProxies)

























- 


[
`compute. googleapis. com/ TargetVpnGateway`
](/compute/docs/reference/rest/v1/targetVpnGateways)

























- 


[
`compute.googleapis.com/UrlMap`
](/compute/docs/reference/rest/v1/urlMaps)

























- 


[
`compute. googleapis. com/ VpnGateway`
](/compute/docs/reference/rest/v1/vpnGateways)

























- 


[
`compute. googleapis. com/ VpnTunnel`
](/compute/docs/reference/rest/v1/vpnTunnels)

























- 


[
`compute. googleapis. com/ WireGroup`
](/compute/docs/reference/rest/v1/wireGroups)























| 
|












































































































| 




**DNS Armor**


| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ DnsThreatDetector`
](/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors)

















Not available in the analysis APIs.















| 
|


































| 




**Fault Injection Testing**


| 













- 


[
`faulttesting. googleapis. com/ Experiment`
](/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments)

















Not available in the analysis APIs.

















- 


[
`faulttesting. googleapis. com/ ExperimentTemplate`
](/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates)

















Not available in the analysis APIs.

















- 


[
`faulttesting. googleapis. com/ Validation`
](/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations)

















Not available in the analysis APIs.















| 
|









































































































| 




**Google Cloud Migration Center**


| 





[API reference](https://migrationcenter.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`migrationcenter. googleapis. com/ Asset`
](/migration-center/docs/reference/rest/v1/projects.locations.assets)

















Not available in the analysis APIs.

















- 



`migrationcenter. googleapis. com/ CostAssessmentJob`


















Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ DiscoveryClient`
](/migration-center/docs/reference/rest/v1/projects.locations.discoveryClients)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ Group`
](/migration-center/docs/reference/rest/v1/projects.locations.groups)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ ImportJob`
](/migration-center/docs/reference/rest/v1/projects.locations.importJobs)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ PreferenceSet`
](/migration-center/docs/reference/rest/v1/projects.locations.preferenceSets)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ ReportConfig`
](/migration-center/docs/reference/rest/v1/projects.locations.reportConfigs)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ Settings`
](/migration-center/docs/reference/rest/v1/Settings)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`migrationcenter. googleapis. com/ Source`
](/migration-center/docs/reference/rest/v1/projects.locations.sources)













Effective tags aren't supported. 



Not available in the analysis APIs.















| 
|



























| 




**Google Kubernetes Engine**


| 





[API reference](https://container.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`admissionregistration. k8s. io/ MutatingWebhookConfiguration`
](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/)

























- 


[
`admissionregistration. k8s. io/ ValidatingWebhookConfiguration`
](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/)

























- 


[
`apps.k8s.io/DaemonSet`
](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

























- 


[
`apps.k8s.io/Deployment`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)

























- 


[
`apps.k8s.io/ReplicaSet`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)

























- 


[
`apps.k8s.io/StatefulSet`
](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

























- 


[
`autoscaling. k8s. io/ HorizontalPodAutoscaler`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/)

















Not available in the analysis APIs.










The asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.











- 


[
`batch.k8s.io/CronJob`
](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

























- 


[
`batch.k8s.io/Job`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/)

























- 


[
`container. googleapis. com/ Cluster`
](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters)






Searchable attributes:





- 
`endpoint`


























- 


[
`container. googleapis. com/ NodePool`
](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools)






Searchable attributes:





- 
`locations`


























- 


[
`extensions.k8s.io/DaemonSet`
](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

















Not available in the analysis APIs.

















- 



`extensions.k8s.io/Ingress`


















Not available in the analysis APIs.










In beta for the export, list, and monitor APIs.











- 


[
`gateway. networking. k8s. io/ Gateway`
](https://kubernetes.io/docs/concepts/services-networking/gateway/)

















Not available in the analysis APIs.

















- 


[
`gateway. networking. k8s. io/ GatewayClass`
](https://kubernetes.io/docs/concepts/services-networking/gateway/)

















Not available in the analysis APIs.

















- 


[
`gateway. networking. k8s. io/ HTTPRoute`
](https://kubernetes.io/docs/concepts/services-networking/gateway/)

















Not available in the analysis APIs.

















- 


[
`gateway. networking. k8s. io/ ReferenceGrant`
](https://kubernetes.io/docs/concepts/services-networking/gateway/)

















Not available in the analysis APIs.

















- 


[
`k8s.io/Endpoints`
](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/)

























- 


[
`k8s.io/Namespace`
](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)

























- 


[
`k8s.io/Node`
](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/)

























- 


[
`k8s.io/PersistentVolume`
](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

























- 


[
`k8s.io/PersistentVolumeClaim`
](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

























- 


[
`k8s.io/Pod`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)

























- 


[
`k8s.io/PodTemplate`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)

























- 


[
`k8s.io/ReplicationController`
](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)

























- 


[
`k8s.io/ResourceQuota`
](https://kubernetes.io/docs/concepts/policy/resource-quotas/)

























- 


[
`k8s.io/Secret`
](https://kubernetes.io/docs/concepts/configuration/secret/)



























Not available in the analysis and search APIs.

















- 


[
`k8s.io/Service`
](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)

























- 


[
`k8s.io/ServiceAccount`
](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)

















Not available in the analysis APIs.

















- 


[
`networking.k8s.io/Ingress`
](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/)

















Not available in the analysis APIs.










In beta for the export, list, and monitor APIs.











- 


[
`networking. k8s. io/ NetworkPolicy`
](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)

























- 


[
`policy. k8s. io/ PodDisruptionBudget`
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

























- 


[
`rbac. authorization. k8s. io/ ClusterRole`
](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)

























- 


[
`rbac. authorization. k8s. io/ ClusterRoleBinding`
](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)

























- 


[
`rbac.authorization.k8s.io/Role`
](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/)

























- 


[
`rbac. authorization. k8s. io/ RoleBinding`
](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)

























- 


[
`storage.k8s.io/StorageClass`
](https://kubernetes.io/docs/concepts/storage/storage-classes/)























| 
|










| 




**Google Security Operations**


| 













- 


[
`chronicle. googleapis. com/ Instance`
](/chronicle/docs/reference/rest/v1/projects.locations.instances)













Effective tags aren't supported. 













Not available in the analysis and search APIs.















| 
|



















| 




**Identity and Access Management v1**



IAM data can be stale by up to 7 days.

| 





[API reference](https://iam.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`iam.googleapis.com/OauthClient`
](/iam/docs/reference/rest/v1/projects.locations.oauthClients)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ OauthClientCredential`
](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials)

















Not available in the analysis APIs.

















- 


[
`iam.googleapis.com/Role`
](/iam/docs/reference/rest/v1/roles)






Searchable attributes:





- 
`includedPermissions`


























- 


[
`iam. googleapis. com/ ServiceAccount`
](/iam/docs/reference/rest/v1/projects.serviceAccounts)






Searchable attributes:





- 
`email`



- 
`uniqueId`

















Disabling or enabling a service account can take up to 48 hours to be reflected in Cloud Asset Inventory responses.










- 


[
`iam. googleapis. com/ ServiceAccountKey`
](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkforcePool`
](/iam/docs/reference/rest/v1/locations.workforcePools)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkforcePoolProvider`
](/iam/docs/reference/rest/v1/locations.workforcePools.providers)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkforcePoolProviderKey`
](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkloadIdentityPool`
](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkloadIdentityPoolManagedIdentity`
](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkloadIdentityPoolNamespace`
](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkloadIdentityPoolProvider`
](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers)

















Not available in the analysis APIs.

















- 


[
`iam. googleapis. com/ WorkloadIdentityPoolProviderKey`
](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys)

















Not available in the analysis APIs.















| 
|












| 




**Identity and Access Management v2**


| 





[API reference](https://iam.s3nsapis.fr/$discovery/rest?version=v2)












- 


[
`iam.googleapis.com/PolicyV2`
](/iam/docs/reference/rest/v2/policies)























| 
|












| 




**Identity and Access Management v3**


| 





[API reference](https://iam.s3nsapis.fr/$discovery/rest?version=v3)












- 


[
`iam. googleapis. com/ PolicyBinding`
](/iam/docs/reference/rest/v3/projects.locations.policyBindings)

















Not available in the analysis APIs.






















| 
|




























































































































| 




**Network Connectivity**


| 





[API reference](https://networkconnectivity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networkconnectivity. googleapis. com/ Group`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.groups)













Effective tags aren't supported. 



Not available in the analysis APIs.

















- 


[
`networkconnectivity. googleapis. com/ Hub`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs)

























- 


[
`networkconnectivity. googleapis. com/ HubRoute`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes)

























- 


[
`networkconnectivity. googleapis. com/ InternalRange`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges)

















Not available in the analysis APIs.

















- 



`networkconnectivity. googleapis. com/ PolicyBasedRoute`


























- 


[
`networkconnectivity. googleapis. com/ RegionalEndpoint`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints)

















Not available in the Analysis APIs.

















- 


[
`networkconnectivity. googleapis. com/ RouteTable`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables)

























- 


[
`networkconnectivity. googleapis. com/ Spoke`
](/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes)























| 
|




















| 




**Network Security Integration**



Network Security Integration asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ InterceptDeployment`
](/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ InterceptDeploymentGroup`
](/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ InterceptEndpointGroup`
](/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ InterceptEndpointGroupAssociation`
](/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ MirroringDeployment`
](/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ MirroringDeploymentGroup`
](/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups)

























- 


[
`networksecurity. googleapis. com/ MirroringEndpointGroup`
](/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ MirroringEndpointGroupAssociation`
](/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations)

















Not available in the analysis APIs.















| 
|




























| 




**Organization Policy Service**


| 





[API reference](https://orgpolicy.s3nsapis.fr/$discovery/rest?version=v2)












- 



`orgpolicy. googleapis. com/ Policy`


















Not available in the analysis APIs.















| 
|












| 




**Organization Policy Service v2**


| 













- 


[
`orgpolicy. googleapis. com/ CustomConstraint`
](/organization-policy/reference/rest/v2/organizations.customConstraints)

























- 


[
`orgpolicy. googleapis. com/ Policy`
](/organization-policy/reference/rest/v2/organizations.policies#Policy)























| 
|




































| 




**Pub/Sub**


| 





[API reference](https://pubsub.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`pubsub.googleapis.com/Schema`
](/pubsub/docs/reference/rest/v1/projects.schemas)

























- 


[
`pubsub.googleapis.com/Snapshot`
](/pubsub/docs/reference/rest/v1/Snapshot)

























- 


[
`pubsub. googleapis. com/ Subscription`
](/pubsub/docs/reference/rest/v1/projects.subscriptions)

























- 


[
`pubsub.googleapis.com/Topic`
](/pubsub/docs/reference/rest/v1/projects.topics)























| 
|




















| 




**Resource Manager**


| 





[API reference](https://cloudresourcemanager.s3nsapis.fr/$discovery/rest)












- 


[
`cloudresourcemanager. googleapis. com/ Folder`
](/resource-manager/reference/rest/v2/folders)

























- 


[
`cloudresourcemanager. googleapis. com/ Lien`
](/resource-manager/reference/rest/v3/liens)



































Not available in the analysis, export, list, and monitor APIs.

















- 


[
`cloudresourcemanager. googleapis. com/ Organization`
](/resource-manager/reference/rest/v1/organizations)

























- 


[
`cloudresourcemanager. googleapis. com/ Project`
](/resource-manager/reference/rest/v1/projects)






Searchable attributes:





- 
`projectId`


























- 


[
`cloudresourcemanager. googleapis. com/ TagBinding`
](/resource-manager/reference/rest/v3/tagBindings)



























Not available in the analysis and search APIs.










In search, directly attached and effective tags can be queried and/or returned along with resources. For details, see [Search for resources](/asset-inventory/docs/search-resources#vm-tagkey).











- 


[
`cloudresourcemanager. googleapis. com/ TagKey`
](/resource-manager/reference/rest/v3/tagKeys)

























- 


[
`cloudresourcemanager. googleapis. com/ TagValue`
](/resource-manager/reference/rest/v3/tagValues)























| 
|




























| 




**Secure Web Proxy**



Secure Web Proxy asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.

| 





[API reference](https://networksecurity.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`networksecurity. googleapis. com/ GatewaySecurityPolicy`
](/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ GatewaySecurityPolicyRule`
](/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies.rules)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ TlsInspectionPolicy`
](/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies)

















Not available in the analysis APIs.

















- 


[
`networksecurity. googleapis. com/ UrlList`
](/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.urlLists)

















Not available in the analysis APIs.















| 
|




















































| 




**Service Directory**


| 





[API reference](https://servicedirectory.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`servicedirectory. googleapis. com/ Endpoint`
](/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services.endpoints)

























- 


[
`servicedirectory. googleapis. com/ Namespace`
](/service-directory/docs/reference/rest/v1/projects.locations.namespaces)

























- 


[
`servicedirectory. googleapis. com/ Service`
](/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services)























| 
|




















| 




**Service Networking**


| 





[API reference](https://servicenetworking.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`servicenetworking. googleapis. com/ Connection`
](/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections)























| 
|












| 




**Service Usage**



Service Usage asset change history might be incomplete. The `config` field in the metadata is not supported yet.

| 





[API reference](https://serviceusage.s3nsapis.fr/$discovery/rest?version=v1)












- 


[
`serviceusage. googleapis. com/ Service`
](/service-usage/docs/reference/rest/v1/services)























| 
|

















































































































## Policy types

Cloud Asset Inventory uses the following asset types for the `ACCESS_POLICY`,
`IAM_POLICY`, and `ORG_POLICY`
[content types](/asset-inventory/docs/asset-inventory-overview#content_types).




| 
Service | 
Asset type | 
|



| 

**Access policy (VPC Service Controls policy)**
| 



[
API reference
](/access-context-manager/docs/reference/rest/v1/accessPolicies)




**Supported policy parent**




- 


[
`cloudresourcemanager. googleapis. com/ Organization`
](/resource-manager/reference/rest/v1/organizations)




Not available in the analysis APIs.






**Supported policy scope**




- 


[
`cloudresourcemanager. googleapis. com/ Folder`
](/resource-manager/reference/rest/v1/folders)




Not available in the analysis APIs.



- 


[
`cloudresourcemanager. googleapis. com/ Organization`
](/resource-manager/reference/rest/v1/organizations)




Not available in the analysis APIs.



- 


[
`cloudresourcemanager. googleapis. com/ Project`
](/resource-manager/reference/rest/v1/projects)




Not available in the analysis APIs.




| 
|


| 
**Organization policy** | 



[
API reference
](/resource-manager/reference/rest/v1/Policy)




Supported resource types that organization policies can be
attached to:




- 


[
`cloudresourcemanager. googleapis. com/ Folder`
](/resource-manager/reference/rest/v2/folders)




- 


[
`cloudresourcemanager. googleapis. com/ Organization`
](/resource-manager/reference/rest/v1/organizations)




- 


[
`cloudresourcemanager. googleapis. com/ Project`
](/resource-manager/reference/rest/v1/projects)





| 
|
# Asset names

Source: https://berlin.devsitetest.how/asset-inventory/docs/asset-names
Last updated: 2026-11-19

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/asset-inventory/docs/tpc-differences) for more details.














- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Documentation

](https://berlin.devsitetest.how/docs)






- 








[

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Cloud Asset Inventory

](https://berlin.devsitetest.how/asset-inventory/docs)






- 








[

Reference

](https://berlin.devsitetest.how/asset-inventory/docs/asset-types)












# Asset names 















These asset names belong to the [asset types](/asset-inventory/docs/asset-types)
supported by Cloud Asset Inventory. They use the
[full resource name](/apis/design/resource_names#full_resource_name) format.

You can use these asset names with the following Cloud Asset Inventory operations:

- 

[Get asset history](/asset-inventory/docs/get-asset-history)

- 

[Monitor asset changes with Pub/Sub](/asset-inventory/docs/monitor-asset-changes)

- 

[View effective IAM policy](/asset-inventory/docs/view-resource-policies#view-effective-policies)







| 
Resource type | 
Name format | 
|





























| 

`accesscontextmanager.googleapis.com/AuthorizedOrgsDesc`
| 



`//accesscontextmanager.googleapis.com/accessPolicies/ ACCESS_POLICY_ID /authorizedOrgsDescs/ AUTHORIZED_ORGS_DESCS `

| 
|

















| 

`admissionregistration.k8s.io/MutatingWebhookConfiguration`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/admissionregistration.k8s.io/mutatingwebhookconfigurations/ WEBHOOK_CONFIGURATION `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/admissionregistration.k8s.io/mutatingwebhookconfigurations/ WEBHOOK_CONFIGURATION `

| 
|

















| 

`admissionregistration.k8s.io/ValidatingWebhookConfiguration`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/admissionregistration.k8s.io/validatingwebhookconfigurations/ WEBHOOK_CONFIGURATION `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/admissionregistration.k8s.io/validatingwebhookconfigurations/ WEBHOOK_CONFIGURATION `

| 
|





















































































































































































































































































































































































































































































































































































































































































































| 

`apikeys.googleapis.com/Key`
| 



`//apikeys.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keys/ KEY_ID `

| 
|












































































































| 

`apps.k8s.io/DaemonSet`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/daemonsets/ DAEMONSET `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/daemonsets/ DAEMONSET `

| 
|

















| 

`apps.k8s.io/Deployment`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/deployments/ DEPLOYMENT `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/deployments/ DEPLOYMENT `

| 
|

















| 

`apps.k8s.io/ReplicaSet`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/replicasets/ REPLICASET `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/replicasets/ REPLICASET `

| 
|

















| 

`apps.k8s.io/StatefulSet`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/statefulsets/ STATEFULSET `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apps/statefulsets/ STATEFULSET `

| 
|

















| 

`artifactregistry.googleapis.com/DockerImage`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /repositories/ REPOSITORY /dockerImages/ DOCKER_IMAGE `

| 
|

















| 

`artifactregistry.googleapis.com/MavenArtifact`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /repositories/ REPOSITORY /mavenArtifacts/ MAVEN_ARTIFACT `

| 
|

















| 

`artifactregistry.googleapis.com/NpmPackage`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /repositories/ REPOSITORY /npmPackages/ NPM_PACKAGE `

| 
|

















| 

`artifactregistry.googleapis.com/PythonPackage`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /repositories/ REPOSITORY /pythonPackages/ PYTHON_PACKAGE `

| 
|

















| 

`artifactregistry.googleapis.com/Repository`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /repositories/ REPOSITORY `

| 
|

















| 

`artifactregistry.googleapis.com/Rule`
| 



`//artifactregistry.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /repositories/ REPOSITORY /rules/ RULE `

| 
|






























| 

`autoscaling.k8s.io/HorizontalPodAutoscaler`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /autoscaling/horizontalpodautoscalers/ HORIZONTALPODAUTOSCALER `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /autoscaling/horizontalpodautoscalers/ HORIZONTALPODAUTOSCALER `

| 
|






































































































































| 

`batch.k8s.io/CronJob`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /batch/cronjobs/ CRONJOB `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /batch/cronjobs/ CRONJOB `

| 
|

















| 

`batch.k8s.io/Job`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /batch/jobs/ JOB `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /batch/jobs/ JOB `

| 
|


















































































| 

`bigquery.googleapis.com/Dataset`
| 



`//bigquery.googleapis.com/projects/ PROJECT_ID /datasets/ DATA_SET `

| 
|

















| 

`bigquery.googleapis.com/Model`
| 



`//bigquery.googleapis.com/projects/ PROJECT_ID /datasets/ DATA_SET /models/ MODEL `

| 
|

















| 

`bigquery.googleapis.com/Routine`
| 



`//bigquery.googleapis.com/projects/ PROJECT_ID /datasets/ DATA_SET /routines/ ROUTINE `

| 
|

















| 

`bigquery.googleapis.com/RowAccessPolicy`
| 



`//bigquery.googleapis.com/projects/ PROJECT_ID /datasets/ DATA_SET /tables/ TABLE /rowAccessPolicies/ ROW_ACCESS_POLICY `

| 
|

















| 

`bigquery.googleapis.com/Table`
| 



`//bigquery.googleapis.com/projects/ PROJECT_ID /datasets/ DATA_SET /tables/ TABLE `

| 
|











































| 

`bigqueryreservation.googleapis.com/BiReservation`
| 



`//bigqueryreservation.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /biReservation`

| 
|

















| 

`bigqueryreservation.googleapis.com/CapacityCommitment`
| 



`//bigqueryreservation.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /capacityCommitments/ CAPACITY_COMMITMENT `

| 
|

















| 

`bigqueryreservation.googleapis.com/Reservation`
| 



`//bigqueryreservation.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /reservations/ RESERVATION `

| 
|

















| 

`bigqueryreservation.googleapis.com/ReservationAssignment`
| 



`//bigqueryreservation.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /reservations/ RESERVATION /assignments/ RESERVATION_ASSIGNMENT `

| 
|

















| 

`bigqueryreservation.googleapis.com/ReservationGroup`
| 



`//bigqueryreservation.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /reservationGroups/ RESERVATION_GROUP `

| 
|






































































































































































































































































| 

`chronicle.googleapis.com/Instance`
| 



`//chronicle.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /instances/ INSTANCE `

| 
|




























































































































































































































































































































































































| 

`cloudkms.googleapis.com/AutokeyConfig`
| 



`//cloudkms.googleapis.com/folders/ FOLDER_ID /autokeyConfig`

| 
|

















| 

`cloudkms.googleapis.com/CryptoKey`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys/ CRYPTO_KEY `

| 
|

















| 

`cloudkms.googleapis.com/CryptoKeyVersion`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys/ CRYPTO_KEY /cryptoKeyVersions/ CRYPTO_KEY_VERSION `

| 
|

















| 

`cloudkms.googleapis.com/EkmConfig`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /ekmConfig`

| 
|

















| 

`cloudkms.googleapis.com/EkmConnection`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /ekmConnections/ EKM_CONNECTION `

| 
|

















| 

`cloudkms.googleapis.com/ImportJob`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /importJobs/ IMPORT_JOBS `

| 
|

















| 

`cloudkms.googleapis.com/KajPolicyConfig`
| 



`//cloudkms.googleapis.com/folders/ FOLDER_ID /kajPolicyConfig`



`//cloudkms.googleapis.com/organizations/ ORGANIZATION_ID /kajPolicyConfig`



`//cloudkms.googleapis.com/projects/ PROJECT_NUMBER /kajPolicyConfig`

| 
|

















| 

`cloudkms.googleapis.com/KeyHandle`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keyHandles/ KEY_HANDLE `

| 
|

















| 

`cloudkms.googleapis.com/KeyRing`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING `

| 
|

















| 

`cloudkms.googleapis.com/RetiredResource`
| 



`//cloudkms.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /retiredResources/ RETIRED_RESOURCE `

| 
|






























| 

`cloudresourcemanager.googleapis.com/Folder`
| 



`//cloudresourcemanager.googleapis.com/folders/ FOLDER_ID `

| 
|

















| 

`cloudresourcemanager.googleapis.com/Lien`
| 



`//cloudresourcemanager.googleapis.com/liens/ LIEN_ID `

| 
|

















| 

`cloudresourcemanager.googleapis.com/Organization`
| 



`//cloudresourcemanager.googleapis.com/organizations/ ORGANIZATION_ID `

| 
|

















| 

`cloudresourcemanager.googleapis.com/Project`
| 



`//cloudresourcemanager.googleapis.com/projects/ PROJECT_ID `



`//cloudresourcemanager.googleapis.com/projects/ PROJECT_NUMBER `

| 
|

















| 

`cloudresourcemanager.googleapis.com/TagBinding`
| 



`//cloudresourcemanager.googleapis.com/tagBindings/ TAG_BINDING `

| 
|

















| 

`cloudresourcemanager.googleapis.com/TagKey`
| 



`//cloudresourcemanager.googleapis.com/tagKeys/ TAG_KEY_ID `

| 
|

















| 

`cloudresourcemanager.googleapis.com/TagValue`
| 



`//cloudresourcemanager.googleapis.com/tagValues/ TAG_VALUE_ID `

| 
|
























































| 

`compute.googleapis.com/Address`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /addresses/ ADDRESS `

| 
|

















| 

`compute.googleapis.com/Autoscaler`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /autoscalers/ AUTOSCALER `



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /autoscalers/ AUTOSCALER `

| 
|

















| 

`compute.googleapis.com/BackendBucket`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/backendBuckets/ BACKEND_BUCKET `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /backendBuckets/ BACKEND_BUCKET `

| 
|

















| 

`compute.googleapis.com/BackendService`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/backendServices/ BACKEND_SERVICE `

| 
|

















| 

`compute.googleapis.com/Commitment`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /commitments/ COMMITMENT `

| 
|

















| 

`compute.googleapis.com/CrossSiteNetwork`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/crossSiteNetworks/ CROSS_SITE_NETWORK `

| 
|

















| 

`compute.googleapis.com/Disk`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /disks/ DISK_ID `

| 
|

















| 

`compute.googleapis.com/ExternalVpnGateway`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/externalVpnGateways/ EXTERNAL_VPN_GATEWAY `

| 
|

















| 

`compute.googleapis.com/Firewall`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/firewalls/ FIREWALL `

| 
|

















| 

`compute.googleapis.com/FirewallPolicy`
| 



`//compute.googleapis.com/locations/global/firewallPolicies/ FIREWALL_POLICY_ID `



`//compute.googleapis.com/projects/ PROJECT_ID /global/firewallPolicies/ FIREWALL_POLICY_ID `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /firewallPolicies/ FIREWALL_POLICY_ID `

| 
|

















| 

`compute.googleapis.com/ForwardingRule`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/forwardingRules/ FORWARDING_RULE `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /forwardingRules/ FORWARDING_RULE `

| 
|

















| 

`compute.googleapis.com/GlobalAddress`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/addresses/ ADDRESS `

| 
|

















| 

`compute.googleapis.com/GlobalForwardingRule`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/forwardingRules/ FORWARDING_RULE `

| 
|

















| 

`compute.googleapis.com/HealthCheck`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/healthChecks/ HEALTH_CHECK `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /healthChecks/ HEALTH_CHECK `

| 
|

















| 

`compute.googleapis.com/HttpHealthCheck`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/httpHealthChecks/ HTTP_HEALTH_CHECK `

| 
|

















| 

`compute.googleapis.com/HttpsHealthCheck`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/httpsHealthChecks/ HTTPS_HEALTH_CHECK `

| 
|

















| 

`compute.googleapis.com/Image`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/images/ IMAGE `

| 
|

















| 

`compute.googleapis.com/Instance`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /instances/ INSTANCE `

| 
|

















| 

`compute.googleapis.com/InstanceGroup`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /instanceGroups/ INSTANCE_GROUP `



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /instanceGroups/ INSTANCE_GROUP `

| 
|

















| 

`compute.googleapis.com/InstanceGroupManager`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /instanceGroupManagers/ INSTANCE_GROUP_MANAGER `



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /instanceGroupManagers/ INSTANCE_GROUP_MANAGER `

| 
|

















| 

`compute.googleapis.com/InstanceSettings`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /instanceSettings/InstanceSettings`

| 
|

















| 

`compute.googleapis.com/InstanceTemplate`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/instanceTemplates/ INSTANCE_TEMPLATE `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /instanceTemplates/ INSTANCE_TEMPLATE `

| 
|

















| 

`compute.googleapis.com/InstantSnapshot`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /instantSnapshots/ INSTANT_SNAPSHOT_NAME `



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /instantSnapshots/ INSTANT_SNAPSHOT_NAME `

| 
|

















| 

`compute.googleapis.com/Interconnect`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/interconnects/ INTERCONNECT `

| 
|

















| 

`compute.googleapis.com/InterconnectAttachment`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /interconnectAttachments/ INTERCONNECT_ATTACHMENT `

| 
|

















| 

`compute.googleapis.com/License`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/licenses/ LICENSE `

| 
|

















| 

`compute.googleapis.com/MachineImage`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/machineImages/ MACHINE_IMAGE `

| 
|

















| 

`compute.googleapis.com/Network`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/networks/ NETWORK `

| 
|

















| 

`compute.googleapis.com/NetworkAttachment`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /networkAttachments/ NETWORK_ATTACHMENT `

| 
|

















| 

`compute.googleapis.com/NetworkEdgeSecurityService`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /networkEdgeSecurityServices/ NETWORK_EDGE_SECURITY_SERVICE `

| 
|

















| 

`compute.googleapis.com/NetworkEndpointGroup`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/networkEndpointGroups/ NETWORK_ENDPOINT_GROUP `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /networkEndpointGroups/ NETWORK_ENDPOINT_GROUP `



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /networkEndpointGroups/ NETWORK_ENDPOINT_GROUP `

| 
|

















| 

`compute.googleapis.com/NodeGroup`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /nodeGroups/ NODE_GROUP `

| 
|

















| 

`compute.googleapis.com/NodeTemplate`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /nodeTemplates/ NODE_TEMPLATE `

| 
|

















| 

`compute.googleapis.com/PacketMirroring`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /packetMirrorings/ PACKET_MIRRORING `

| 
|

















| 

`compute.googleapis.com/Project`
| 



`//compute.googleapis.com/projects/ PROJECT_ID `

| 
|

















| 

`compute.googleapis.com/PublicAdvertisedPrefix`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/publicAdvertisedPrefixes/ PUBLIC_DELEGATED_PREFIX `

| 
|

















| 

`compute.googleapis.com/PublicDelegatedPrefix`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/publicDelegatedPrefixes/ PUBLIC_DELEGATED_PREFIX `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /publicDelegatedPrefixes/ PUBLIC_DELEGATED_PREFIX `

| 
|

















| 

`compute.googleapis.com/RegionDisk`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /disks/ DISKS `

| 
|

















| 

`compute.googleapis.com/Reservation`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /reservations/ RESERVATION `

| 
|

















| 

`compute.googleapis.com/ResourcePolicy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /resourcePolicies/ RESOURCE_POLICY `

| 
|

















| 

`compute.googleapis.com/Route`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/routes/ ROUTE `

| 
|

















| 

`compute.googleapis.com/Router`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /routers/ ROUTER `

| 
|

















| 

`compute.googleapis.com/SecurityPolicy`
| 



`//compute.googleapis.com/locations/global/securityPolicies/ SECURITY_POLICY `



`//compute.googleapis.com/projects/ PROJECT_ID /global/securityPolicies/ SECURITY_POLICY `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /securityPolicies/ SECURITY_POLICY `

| 
|

















| 

`compute.googleapis.com/ServiceAttachment`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /serviceAttachments/ SERVICE_ATTACHMENT `

| 
|

















| 

`compute.googleapis.com/Snapshot`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/snapshots/ SNAPSHOT `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /snapshots/ SNAPSHOT `

| 
|

















| 

`compute.googleapis.com/SslCertificate`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/sslCertificates/ SSL_CERTIFICATE `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /sslCertificates/ SSL_CERTIFICATE `

| 
|

















| 

`compute.googleapis.com/SslPolicy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/sslPolicies/ SSL_POLICY `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /sslPolicies/ SSL_POLICY `

| 
|

















| 

`compute.googleapis.com/StoragePool`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /storagePools/ STORAGEPOOL `

| 
|

















| 

`compute.googleapis.com/Subnetwork`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNETWORK `

| 
|

















| 

`compute.googleapis.com/TargetGrpcProxy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/targetGrpcProxies/ TARGET_GRPC_PROXY `

| 
|

















| 

`compute.googleapis.com/TargetHttpProxy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/targetHttpProxies/ TARGET_HTTP_PROXY `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /targetHttpProxies/ TARGET_HTTP_PROXY `

| 
|

















| 

`compute.googleapis.com/TargetHttpsProxy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/targetHttpsProxies/ TARGET_HTTPS_PROXY `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /targetHttpsProxies/ TARGET_HTTPS_PROXY `

| 
|

















| 

`compute.googleapis.com/TargetInstance`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /targetInstances/ TARGET_INSTANCE `

| 
|

















| 

`compute.googleapis.com/TargetPool`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /targetPools/ TARGET_POOL `

| 
|

















| 

`compute.googleapis.com/TargetSslProxy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/targetSslProxies/ TARGET_SSL_PROXY `

| 
|

















| 

`compute.googleapis.com/TargetTcpProxy`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/targetTcpProxies/ TARGET_TCP_PROXY `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /targetTcpProxies/ TARGET_TCP_PROXY `

| 
|

















| 

`compute.googleapis.com/TargetVpnGateway`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /targetVpnGateways/ TARGET_VPN_GATEWAY `

| 
|

















| 

`compute.googleapis.com/UrlMap`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/urlMaps/ URL_MAP `



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /urlMaps/ URL_MAP `

| 
|

















| 

`compute.googleapis.com/VpnGateway`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /vpnGateways/ VPN_GATEWAY `

| 
|

















| 

`compute.googleapis.com/VpnTunnel`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /regions/ REGION /vpnTunnels/ VPN_TUNNEL `

| 
|

















| 

`compute.googleapis.com/WireGroup`
| 



`//compute.googleapis.com/projects/ PROJECT_ID /global/crossSiteNetworks/ CROSS_SITE_NETWORK /wireGroups/ WIRE_GROUP `

| 
|













































































































































































| 

`container.googleapis.com/Cluster`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER `

| 
|

















| 

`container.googleapis.com/NodePool`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /nodePools/ NODE_POOL `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /nodePools/ NODE_POOL `

| 
|






















































































































































































































































































































































































































































































| 

`designcenter.googleapis.com/ApplicationTemplate`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE /applicationTemplates/ APPLICATION_TEMPLATE `

| 
|














| 

`designcenter.googleapis.com/Catalog`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE /catalogs/ CATALOG `

| 
|














| 

`designcenter.googleapis.com/CatalogTemplate`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE /catalogs/ CATALOG /templates/ TEMPLATE `

| 
|














| 

`designcenter.googleapis.com/CatalogTemplateRevision`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE /catalogs/ CATALOG /templates/ TEMPLATE /revisions/ REVISION `

| 
|














| 

`designcenter.googleapis.com/Share`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE /catalogs/ CATALOG /shares/ SHARE `

| 
|














| 

`designcenter.googleapis.com/Space`
| 



`//designcenter.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spaces/ SPACE `

| 
|


























































































































































































































































| 

`dns.googleapis.com/ManagedZone`
| 



`//dns.googleapis.com/projects/ PROJECT_ID /managedZones/ ZONE_NUMBER `

| 
|

















| 

`dns.googleapis.com/Policy`
| 



`//dns.googleapis.com/projects/ PROJECT_ID /policies/ POLICY_NUMBER `

| 
|

















| 

`dns.googleapis.com/ResourceRecordSet`
| 



`//dns.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /managedZones/ ZONE_NUMBER /rrsets/ RESOURCE_RECORD_SET `

| 
|

















| 

`dns.googleapis.com/ResponsePolicy`
| 



`//dns.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /responsePolicies/ RESPONSE_POLICY `

| 
|

















| 

`dns.googleapis.com/ResponsePolicyRule`
| 



`//dns.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /responsePolicies/ RESPONSE_POLICY /rules/ RULE `

| 
|







































































































































































































| 

`extensions.k8s.io/DaemonSet`
| 



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /extensions/daemonsets/ DAEMONSET `

| 
|

















| 

`extensions.k8s.io/Ingress`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /extensions/ingresses/ INGRESS `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /extensions/ingresses/ INGRESS `

| 
|















| 

`faulttesting.googleapis.com/Experiment`
| 



`//faulttesting.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /experiments/ EXPERIMENT `

| 
|














| 

`faulttesting.googleapis.com/ExperimentTemplate`
| 



`//faulttesting.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /experimentTemplates/ EXPERIMENT_TEMPLATE `

| 
|














| 

`faulttesting.googleapis.com/Validation`
| 



`//faulttesting.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /validations/ VALIDATION `

| 
|




















































































































































































































































































| 

`gateway.networking.k8s.io/Gateway`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/gateways/ GATEWAY `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/gateways/ GATEWAY `

| 
|

















| 

`gateway.networking.k8s.io/GatewayClass`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/apis/gateway.networking.k8s.io/gatewayclasses/ GATEWAY_CLASS `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/apis/gateway.networking.k8s.io/gatewayclasses/ GATEWAY_CLASS `

| 
|

















| 

`gateway.networking.k8s.io/HTTPRoute`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/httproutes/ HTTP_ROUTE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/httproutes/ HTTP_ROUTE `

| 
|

















| 

`gateway.networking.k8s.io/ReferenceGrant`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/referencegrants/ REFERENCE_GRANT `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /apis/gateway.networking.k8s.io/referencegrants/ REFERENCE_GRANT `

| 
|





































































































































































































































































































































































































































































































| 

`iam.googleapis.com/OauthClient`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /oauthClients/ OAUTH_CLIENT `

| 
|

















| 

`iam.googleapis.com/OauthClientCredential`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /oauthClients/ OAUTH_CLIENT /credentials/ CREDENTIAL `

| 
|

















| 

`iam.googleapis.com/PolicyBinding`
| 



`//iam.googleapis.com/folders/ FOLDER_NUMBER /locations/ LOCATION /policyBindings/ POLICY_BINDING `



`//iam.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /policyBindings/ POLICY_BINDING `



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /policyBindings/ POLICY_BINDING `

| 
|

















| 

`iam.googleapis.com/PolicyV2`
| 



`//iam.googleapis.com/policies/cloudresourcemanager.googleapis.com%2Ffolders%2F FOLDER_NUMBER /denypolicies/ DENY_POLICY_ID `



`//iam.googleapis.com/policies/cloudresourcemanager.googleapis.com%2Forganizations%2F ORGANIZATION_ID /denypolicies/ DENY_POLICY_ID `



`//iam.googleapis.com/policies/cloudresourcemanager.googleapis.com%2Fprojects%2F PROJECT_NUMBER /denypolicies/ DENY_POLICY_ID `

| 
|































| 

`iam.googleapis.com/Role`
| 



`//iam.googleapis.com/organizations/ ORGANIZATION_ID /roles/ ROLE `



`//iam.googleapis.com/projects/ PROJECT_ID /roles/ ROLE `

| 
|

















| 

`iam.googleapis.com/ServiceAccount`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_EMAIL `



`//iam.googleapis.com/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_ID `

| 
|

















| 

`iam.googleapis.com/ServiceAccountKey`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_ID /keys/ SERVICE_ACCOUNT_KEY `

| 
|

















| 

`iam.googleapis.com/WorkforcePool`
| 



`//iam.googleapis.com/locations/ LOCATION /workforcePools/ WORKFORCE_POOL_ID `

| 
|

















| 

`iam.googleapis.com/WorkforcePoolProvider`
| 



`//iam.googleapis.com/locations/ LOCATION /workforcePools/ WORKFORCE_POOL_ID /providers/ PROVIDER_ID `

| 
|

















| 

`iam.googleapis.com/WorkforcePoolProviderKey`
| 



`//iam.googleapis.com/locations/ LOCATION /workforcePools/ WORKFORCE_POOL_ID /providers/ PROVIDER_ID /keys/ KEY_ID `

| 
|

















| 

`iam.googleapis.com/WorkloadIdentityPool`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /workloadIdentityPools/ WORKLOAD_POOL_ID `

| 
|

















| 

`iam.googleapis.com/WorkloadIdentityPoolManagedIdentity`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /workloadIdentityPools/ WORKLOAD_POOL_ID /namespaces/ NAMESPACE_ID /managedIdentities/ MANAGED_IDENTITY_ID `

| 
|

















| 

`iam.googleapis.com/WorkloadIdentityPoolNamespace`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /workloadIdentityPools/ WORKLOAD_POOL_ID /namespaces/ NAMESPACE_ID `

| 
|

















| 

`iam.googleapis.com/WorkloadIdentityPoolProvider`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /workloadIdentityPools/ WORKLOAD_POOL_ID /providers/ PROVIDER_ID `

| 
|

















| 

`iam.googleapis.com/WorkloadIdentityPoolProviderKey`
| 



`//iam.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /workloadIdentityPools/ WORKLOAD_POOL_ID /providers/ PROVIDER_ID /keys/ KEY_ID `

| 
|






























| 

`identity.accesscontextmanager.googleapis.com/AccessLevel`
| 



`//accesscontextmanager.googleapis.com/accessPolicies/ ACCESS_POLICY_ID /accessLevels/ ACCESS_LEVEL `

| 
|

















| 

`identity.accesscontextmanager.googleapis.com/AccessPolicy`
| 



`//accesscontextmanager.googleapis.com/accessPolicies/ ACCESS_POLICY_ID `

| 
|

















| 

`identity.accesscontextmanager.googleapis.com/ServicePerimeter`
| 



`//accesscontextmanager.googleapis.com/accessPolicies/ ACCESS_POLICY_ID /servicePerimeters/ SERVICE_PERIMETER `

| 
|







































































































































































































| 

`k8s.io/Endpoints`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /endpoints/ ENDPOINT `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /endpoints/ ENDPOINT `

| 
|

















| 

`k8s.io/Namespace`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE `

| 
|

















| 

`k8s.io/Node`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/nodes/ NODE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/nodes/ NODE `

| 
|

















| 

`k8s.io/PersistentVolume`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/persistentvolumes/ PERSISTENT_VOLUME `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/persistentvolumes/ PERSISTENT_VOLUME `

| 
|

















| 

`k8s.io/PersistentVolumeClaim`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /persistentvolumeclaims/ PERSISTENT_VOLUME_CLAIM `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /persistentvolumeclaims/ PERSISTENT_VOLUME_CLAIM `

| 
|

















| 

`k8s.io/Pod`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /pods/ POD `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /pods/ POD `

| 
|

















| 

`k8s.io/PodTemplate`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /podtemplates/ POD_TEMPLATE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /podtemplates/ POD_TEMPLATE `

| 
|

















| 

`k8s.io/ReplicationController`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /replicationcontrollers/ REPLICATION_CONTROLLER `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /replicationcontrollers/ REPLICATION_CONTROLLER `

| 
|

















| 

`k8s.io/ResourceQuota`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /resourcequotas/ RESOURCE_QUOTA `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /resourcequotas/ RESOURCE_QUOTA `

| 
|

















| 

`k8s.io/Secret`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /secrets/ SECRET `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /secrets/ SECRET `

| 
|

















| 

`k8s.io/Service`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /services/ SERVICE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /services/ SERVICE `

| 
|

















| 

`k8s.io/ServiceAccount`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /serviceaccounts/ SERVICEACCOUNT `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /serviceaccounts/ SERVICEACCOUNT `

| 
|


















































































| 

`logging.googleapis.com/Link`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /locations/ LOCATION /buckets/ BUCKET /links/ LINK `



`//logging.googleapis.com/folders/ FOLDER_ID /locations/ LOCATION /buckets/ BUCKET /links/ LINK `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /buckets/ BUCKET /links/ LINK `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /buckets/ BUCKET /links/ LINK `

| 
|

















| 

`logging.googleapis.com/LogBucket`
| 



`//logging.googleapis.com/accessPolicies/ ACCESS_POLICY_ID /locations/ LOCATION /buckets/ BUCKET `



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /locations/ LOCATION /buckets/ BUCKET `



`//logging.googleapis.com/folders/ FOLDER_ID /locations/ LOCATION /buckets/ BUCKET `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /buckets/ BUCKET `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /buckets/ BUCKET `

| 
|

















| 

`logging.googleapis.com/LogMetric`
| 



`//logging.googleapis.com/projects/ PROJECT_NUMBER /metrics/ METRIC `

| 
|

















| 

`logging.googleapis.com/LogSink`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /sinks/ SINK `



`//logging.googleapis.com/folders/ FOLDER_ID /sinks/ SINK `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /sinks/ SINK `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /sinks/ SINK `

| 
|

















| 

`logging.googleapis.com/LogView`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /locations/ LOCATION /buckets/ BUCKET /views/ VIEW `



`//logging.googleapis.com/folders/ FOLDER_ID /locations/ LOCATION /buckets/ BUCKET /views/ VIEW `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /buckets/ BUCKET /views/ VIEW `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /buckets/ BUCKET /views/ VIEW `

| 
|

















| 

`logging.googleapis.com/RecentQuery`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /locations/ LOCATION /recentQueries/ RECENT_QUERY `



`//logging.googleapis.com/folders/ FOLDER_ID /locations/ LOCATION /recentQueries/ RECENT_QUERY `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /recentQueries/ RECENT_QUERY `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /recentQueries/ RECENT_QUERY `

| 
|

















| 

`logging.googleapis.com/SavedQuery`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /locations/ LOCATION /savedQueries/ SAVED_QUERY `



`//logging.googleapis.com/folders/ FOLDER_ID /locations/ LOCATION /savedQueries/ SAVED_QUERY `



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /savedQueries/ SAVED_QUERY `



`//logging.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /savedQueries/ SAVED_QUERY `

| 
|

















| 

`logging.googleapis.com/Settings`
| 



`//logging.googleapis.com/billingAccounts/ BILLING_ACCOUNT_ID /settings`



`//logging.googleapis.com/folders/ FOLDER_ID /settings`



`//logging.googleapis.com/organizations/ ORGANIZATION_ID /settings`



`//logging.googleapis.com/projects/ PROJECT_NUMBER /settings`

| 
|















































































































































































































































































































| 

`monitoring.googleapis.com/AlertPolicy`
| 



`//monitoring.googleapis.com/projects/ PROJECT_NUMBER /alertPolicies/ POLICY_NUMBER `

| 
|

















| 

`monitoring.googleapis.com/Dashboard`
| 



`//monitoring.googleapis.com/projects/ PROJECT_NUMBER /dashboards/ DASHBOARD_ID `

| 
|

















| 

`monitoring.googleapis.com/NotificationChannel`
| 



`//monitoring.googleapis.com/projects/ PROJECT_NUMBER /notificationChannels/ CHANNEL_ID `

| 
|

















| 

`monitoring.googleapis.com/Snooze`
| 



`//monitoring.googleapis.com/projects/ PROJECT_NUMBER /snoozes/ SNOOZE_ID `

| 
|

















| 

`monitoring.googleapis.com/UptimeCheckConfig`
| 



`//monitoring.googleapis.com/projects/ PROJECT_NUMBER /uptimeCheckConfigs/ UPTIMECHECKCONFIGS_ID `

| 
|



















































































































































| 

`networkconnectivity.googleapis.com/Group`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/global/hubs/ HUB /groups/ GROUP `

| 
|

















| 

`networkconnectivity.googleapis.com/Hub`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/global/hubs/ HUB `

| 
|

















| 

`networkconnectivity.googleapis.com/HubRoute`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/global/hubs/ HUB /routeTables/ ROUTE_TABLE /routes/ ROUTE `

| 
|

















| 

`networkconnectivity.googleapis.com/InternalRange`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /internalRanges/ INTERNAL_RANGE `

| 
|

















| 

`networkconnectivity.googleapis.com/PolicyBasedRoutes`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/global/policyBasedRoutes/ POLICY_BASED_ROUTES `

| 
|

















| 

`networkconnectivity.googleapis.com/RegionalEndpoint`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /regionalEndpoints/ REGIONAL_ENDPOINT `

| 
|

















| 

`networkconnectivity.googleapis.com/RouteTable`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/global/hubs/ HUB /routeTables/ ROUTE_TABLE `

| 
|

















| 

`networkconnectivity.googleapis.com/Spoke`
| 



`//networkconnectivity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /spokes/ SPOKE `

| 
|

















| 

`networking.k8s.io/Ingress`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /networking.k8s.io/ingresses/ INGRESS `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /networking.k8s.io/ingresses/ INGRESS `

| 
|

















| 

`networking.k8s.io/Networkpolicy`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /networking.k8s.io/networkpolicies/ NETWORKPOLICY `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /networking.k8s.io/networkpolicies/ NETWORKPOLICY `

| 
|































































































| 

`networksecurity.googleapis.com/AddressGroup`
| 



`//networksecurity.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /addressGroups/ ADDRESS_GROUP `



`//networksecurity.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /addressGroups/ ADDRESS_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/AuthorizationPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /authorizationPolicies/ AUTHORIZATION_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/AuthzPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /authzPolicies/ AUTHZ_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/ClientTlsPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clientTlsPolicies/ CLIENT_TLS_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/DnsThreatDetector`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /dnsThreatDetectors/ DNS_THREAT_DETECTOR `

| 
|

















| 

`networksecurity.googleapis.com/FirewallEndpoint`
| 



`//networksecurity.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /firewallEndpoints/ FIREWALL_ENDPOINT `



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /firewallEndpoints/ FIREWALL_ENDPOINT `

| 
|

















| 

`networksecurity.googleapis.com/FirewallEndpointAssociation`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /firewallEndpointAssociations/ FIREWALL_ENDPOINT_ASSOCIATIONS `

| 
|

















| 

`networksecurity.googleapis.com/GatewaySecurityPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /gatewaySecurityPolicies/ GATEWAY_SECURITY_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/GatewaySecurityPolicyRule`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /gatewaySecurityPolicies/ GATEWAY_SECURITY_POLICY /rules/ RULE `

| 
|

















| 

`networksecurity.googleapis.com/InterceptDeployment`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /interceptDeployments/ INTERCEPT_DEPLOYMENT `

| 
|

















| 

`networksecurity.googleapis.com/InterceptDeploymentGroup`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /interceptDeploymentGroups/ INTERCEPT_DEPLOYMENT_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/InterceptEndpointGroup`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /interceptEndpointGroups/ INTERCEPT_ENDPOINT_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/InterceptEndpointGroupAssociation`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /interceptEndpointGroupAssociations/ INTERCEPT_ENDPOINT_GROUP_ASSOCIATION `

| 
|

















| 

`networksecurity.googleapis.com/MirroringDeployment`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /mirroringDeployments/ MIRRORING_DEPLOYMENT `

| 
|

















| 

`networksecurity.googleapis.com/MirroringDeploymentGroup`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /mirroringDeploymentGroups/ MIRRORING_DEPLOYMENT_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/MirroringEndpointGroup`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /mirroringEndpointGroups/ MIRRORING_ENDPOINT_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/MirroringEndpointGroupAssociation`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /mirroringEndpointGroupAssociations/ MIRRORING_ENDPOINT_GROUP_ASSOCIATION `

| 
|

















| 

`networksecurity.googleapis.com/SecurityProfile`
| 



`//networksecurity.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /securityProfiles/ SECURITY_PROFILE `



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /securityProfiles/ SECURITY_PROFILE `

| 
|

















| 

`networksecurity.googleapis.com/SecurityProfileGroup`
| 



`//networksecurity.googleapis.com/organizations/ ORGANIZATION_ID /locations/ LOCATION /securityProfileGroups/ SECURITY_PROFILE_GROUP `



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /securityProfileGroups/ SECURITY_PROFILE_GROUP `

| 
|

















| 

`networksecurity.googleapis.com/ServerTlsPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /serverTlsPolicies/ SERVER_TLS_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/TlsInspectionPolicy`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /tlsInspectionPolicies/ TLS_INSPECTION_POLICY `

| 
|

















| 

`networksecurity.googleapis.com/UrlList`
| 



`//networksecurity.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /urlLists/ URL_LIST `

| 
|
















































































































































































































































































































































































| 

`orgpolicy.googleapis.com/CustomConstraint`
| 



`//orgpolicy.googleapis.com/organizations/ ORGANIZATION_ID /customConstraints/ CUSTOM_CONSTRAINT `

| 
|

















| 

`orgpolicy.googleapis.com/Policy`
| 



`//orgpolicy.googleapis.com/folders/ FOLDER_ID /policies/ POLICY `



`//orgpolicy.googleapis.com/organizations/ ORGANIZATION_ID /policies/ POLICY `



`//orgpolicy.googleapis.com/projects/ PROJECT_NUMBER /policies/ POLICY `

| 
|

















| 

`osconfig.googleapis.com/OSPolicyAssignment`
| 



`//osconfig.googleapis.com/projects/ PROJECT_ID /locations/ ZONE /osPolicyAssignments/ ASSIGNMENT_NAME `

| 
|

















| 

`osconfig.googleapis.com/OSPolicyAssignmentReport`
| 



`//osconfig.googleapis.com/projects/ PROJECT_ID /locations/ ZONE /instances/ VM_INSTANCE_ID /osPolicyAssignments/ ASSIGNMENT_NAME /report`

| 
|

















| 

`osconfig.googleapis.com/PatchDeployment`
| 



`//osconfig.googleapis.com/projects/ PROJECT_ID /patchDeployments/ PATCH_DEPLOYMENT `

| 
|

















| 

`osconfig.googleapis.com/VulnerabilityReport`
| 



`//osconfig.googleapis.com/projects/ PROJECT_ID /locations/ ZONE /instances/ VM_INSTANCE_ID /VulnerabilityReport`

| 
|
























































| 

`policy.k8s.io/PodDisruptionBudget`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /policy/poddisruptionbudgets/ POD_DISRUPTION_BUDGET `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /policy/poddisruptionbudgets/ POD_DISRUPTION_BUDGET `

| 
|












































































































| 

`pubsub.googleapis.com/Schema`
| 



`//pubsub.googleapis.com/projects/ PROJECT_ID /schemas/ SCHEMA `

| 
|

















| 

`pubsub.googleapis.com/Snapshot`
| 



`//pubsub.googleapis.com/projects/ PROJECT_ID /snapshots/ SNAPSHOT `

| 
|

















| 

`pubsub.googleapis.com/Subscription`
| 



`//pubsub.googleapis.com/projects/ PROJECT_ID /subscriptions/ SUBSCRIPTION `

| 
|

















| 

`pubsub.googleapis.com/Topic`
| 



`//pubsub.googleapis.com/_deleted-topic_`



`//pubsub.googleapis.com/projects/ PROJECT_ID /topics/ TOPIC `

| 
|

















| 

`rbac.authorization.k8s.io/ClusterRole`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/rbac.authorization.k8s.io/clusterroles/ CLUSTER_ROLE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/rbac.authorization.k8s.io/clusterroles/ CLUSTER_ROLE `

| 
|

















| 

`rbac.authorization.k8s.io/ClusterRoleBinding`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/rbac.authorization.k8s.io/clusterrolebindings/ CLUSTER_ROLE_BINDING `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/rbac.authorization.k8s.io/clusterrolebindings/ CLUSTER_ROLE_BINDING `

| 
|

















| 

`rbac.authorization.k8s.io/Role`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /rbac.authorization.k8s.io/roles/ ROLE `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /rbac.authorization.k8s.io/roles/ ROLE `

| 
|

















| 

`rbac.authorization.k8s.io/RoleBinding`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /rbac.authorization.k8s.io/rolebindings/ ROLEBINDING `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/namespaces/ NAMESPACE /rbac.authorization.k8s.io/rolebindings/ ROLEBINDING `

| 
|
























































































































































































































































































































































































































































































| 

`servicedirectory.googleapis.com/Endpoint`
| 



`//servicedirectory.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /namespaces/ NAMESPACE /services/ SERVICE /endpoints/ ENDPOINT `

| 
|

















| 

`servicedirectory.googleapis.com/Namespace`
| 



`//servicedirectory.googleapis.com/projects/ PROJECT_NUMBER /locations/ LOCATION /namespaces/ NAMESPACE `

| 
|

















| 

`servicedirectory.googleapis.com/Service`
| 



`//servicedirectory.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /namespaces/ NAMESPACE /services/ SERVICE `

| 
|











































| 

`servicenetworking.googleapis.com/Connection`
| 



`//servicenetworking.googleapis.com/projects/ PROJECT_ID /global/networks/ NETWORK `

| 
|

















| 

`serviceusage.googleapis.com/Service`
| 



`//serviceusage.googleapis.com/projects/ PROJECT_NUMBER /services/ SERVICE `

| 
|







































































































































































































| 

`sqladmin.googleapis.com/Backup`
| 



`//cloudsql.googleapis.com/projects/ PROJECT_ID /backups/ BACKUP `

| 
|

















| 

`sqladmin.googleapis.com/BackupRun`
| 



`//cloudsql.googleapis.com/projects/ PROJECT_ID /instances/ INSTANCE /backupRuns/ BACKUPRUN `

| 
|

















| 

`sqladmin.googleapis.com/Instance`
| 



`//cloudsql.googleapis.com/projects/ PROJECT_ID /instances/ INSTANCE `

| 
|

















| 

`storage.googleapis.com/Bucket`
| 



`//storage.googleapis.com/ BUCKET `

| 
|

















| 

`storage.k8s.io/StorageClass`
| 



`//container.googleapis.com/projects/ PROJECT_ID /locations/ LOCATION /clusters/ CLUSTER /k8s/storage.k8s.io/storageclasses/ STORAGECLASS `



`//container.googleapis.com/projects/ PROJECT_ID /zones/ ZONE /clusters/ CLUSTER /k8s/storage.k8s.io/storageclasses/ STORAGECLASS `

| 
|
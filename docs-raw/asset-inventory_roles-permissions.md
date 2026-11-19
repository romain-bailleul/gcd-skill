# Roles and permissions

Source: https://berlin.devsitetest.how/asset-inventory/docs/roles-permissions
Last updated: 2026-11-10

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

Guides

](https://berlin.devsitetest.how/asset-inventory/docs/asset-inventory-overview)












# Roles and permissions 















Cloud Asset Inventory uses [Identity and Access Management](/iam/docs) (IAM) for access
control. Every Cloud Asset Inventory API method requires the caller to have the necessary
permissions.

## Roles


















































































































































































To get the permissions that
you need to work with asset metadata,

ask your administrator to grant you the
following IAM roles on the organization, folder, or project:












- 
To view asset metadata:




- [Cloud Asset Viewer ](/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)


- [Service Usage Consumer ](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)







- 
To view asset metadata and work with feeds:




- [Cloud Asset Owner ](/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`)


- [Service Usage Consumer ](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)












For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








These predefined roles contain

the permissions required to work with asset metadata. To see the exact permissions that are
required, expand the **Required permissions** section:






#### Required permissions



The following permissions are required to work with asset metadata:





- 
To view asset metadata:




- 
`cloudasset.assets.*`


- 
`recommender.cloudAssetInsights.get`


- 
`recommender.cloudAssetInsights.list`


- 
`serviceusage.services.use`







- 
To view asset metadata and work with feeds:




- 
`cloudasset.*`


- 
`recommender.cloudAssetInsights.*`


- 
`serviceusage.services.use`
















You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## Permissions

The following table lists the permissions that the caller must have to call each
API method in Cloud Asset Inventory, or to perform tasks using Google Cloud Dedicated in Germany tools that
use Cloud Asset Inventory such as the Google Cloud Dedicated console or gcloud CLI.

The Cloud Asset Viewer (`roles/cloudasset.viewer`) and Cloud Asset Owner
(`roles/cloudasset.owner`) [roles](#roles) include many of these
permissions. If the caller has been granted one of these roles and the
Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) role, they
might already have the permissions they need to use Cloud Asset Inventory.



### RPC




| 
Method | 
Required permissions | 
|



| 
All APIs | 
|

| 
All Cloud Asset Inventory calls | 



All Cloud Asset Inventory calls require the `serviceusage.services.use`
permission.


| 
|



| 
Inventory APIs | 
|

| 


`BatchGetAssetsHistory`

`ExportAssets`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- 


`cloudasset. assets. exportAccessPolicy`



When using the `ACCESS_POLICY` content type.



- 


`cloudasset. assets. exportIamPolicy`



When using the `IAM_POLICY` content type.



- 


`cloudasset. assets. exportOrgPolicy`



When using the `ORG_POLICY` content type.




- 


`cloudasset. assets. exportResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset. assets. exportResource`
permission to a user allows them to export all resource types. To restrict what
resource types a user can export, you can grant permissions for each resource type
instead. For example, you can grant the
`cloudasset.assets.exportComputeDisks` permission by itself to allow a user
to only export the `compute.googleapis.com/Disk` resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.export*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel).







| 
|

| 


`ListAssets`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- `cloudasset. assets. listAccessPolicy`

- `cloudasset. assets. listIamPolicy`

- `cloudasset. assets. listOrgPolicy`

- `cloudasset. assets. listOSInventories`

- 


`cloudasset.assets.listResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset.assets.listResource`
permission to a user allows them to list all resource types. To restrict what resource
types a user can list, you can grant permissions for each resource type instead. For
example, you can grant the `cloudasset.assets.listComputeDisks` permission
by itself to allow a user to only list the `compute.googleapis.com/Disk`
resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.list*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel).





| 
|


| 
Search APIs | 
|

| 


`SearchAllIamPolicies`
| 
`cloudasset. assets. searchAllIamPolicies` | 
|

| 


`SearchAllResources`
| 



`cloudasset. assets. searchAllResources`



You also need
`cloudasset. assets. searchEnrichmentResourceOwners` if
searching for resource owner enrichment.

| 
|



### REST




| 
Method | 
Required permissions | 
|



| 
All APIs | 
|

| 
All Cloud Asset Inventory calls | 



All Cloud Asset Inventory calls require the `serviceusage.services.use`
permission.


| 
|



| 
Inventory APIs | 
|

| 


`batchGetAssetsHistory`

`exportAssets`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- 


`cloudasset. assets. exportAccessPolicy`



When using the `ACCESS_POLICY` content type.



- 


`cloudasset. assets. exportIamPolicy`



When using the `IAM_POLICY` content type.



- 


`cloudasset. assets. exportOrgPolicy`



When using the `ORG_POLICY` content type.




- 


`cloudasset. assets. exportResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset. assets. exportResource`
permission to a user allows them to export all resource types. To restrict what
resource types a user can export, you can grant permissions for each resource type
instead. For example, you can grant the
`cloudasset.assets.exportComputeDisks` permission by itself to allow a user
to only export the `compute.googleapis.com/Disk` resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.export*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel).







| 
|

| 


`assets.list`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- `cloudasset. assets. listAccessPolicy`

- `cloudasset. assets. listIamPolicy`

- `cloudasset. assets. listOrgPolicy`

- `cloudasset. assets. listOSInventories`

- 


`cloudasset.assets.listResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset.assets.listResource`
permission to a user allows them to list all resource types. To restrict what resource
types a user can list, you can grant permissions for each resource type instead. For
example, you can grant the `cloudasset.assets.listComputeDisks` permission
by itself to allow a user to only list the `compute.googleapis.com/Disk`
resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.list*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel).





| 
|


| 
Search APIs | 
|

| 


`searchAllIamPolicies`
| 
`cloudasset. assets. searchAllIamPolicies` | 
|

| 


`searchAllResources`
| 



`cloudasset. assets. searchAllResources`



You also need
`cloudasset. assets. searchEnrichmentResourceOwners` if
searching for resource owner enrichment.

| 
|



### gcloud




| 
Positional statement | 
Required permissions | 
|



| 
All APIs | 
|

| 
All Cloud Asset Inventory calls | 



All Cloud Asset Inventory calls require the `serviceusage.services.use`
permission.


| 
|



| 
Inventory APIs | 
|

| 


`export`

`get-history`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- 


`cloudasset. assets. exportAccessPolicy`



When using the `ACCESS_POLICY` content type.



- 


`cloudasset. assets. exportIamPolicy`



When using the `IAM_POLICY` content type.



- 


`cloudasset. assets. exportOrgPolicy`



When using the `ORG_POLICY` content type.




- 


`cloudasset. assets. exportResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset. assets. exportResource`
permission to a user allows them to export all resource types. To restrict what
resource types a user can export, you can grant permissions for each resource type
instead. For example, you can grant the
`cloudasset.assets.exportComputeDisks` permission by itself to allow a user
to only export the `compute.googleapis.com/Disk` resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.export*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel).







| 
|

| 


`list`
| 



One of the following permissions, depending on the
[
content type](/asset-inventory/docs/asset-inventory-overview#content_types):




- `cloudasset. assets. listAccessPolicy`

- `cloudasset. assets. listIamPolicy`

- `cloudasset. assets. listOrgPolicy`

- `cloudasset. assets. listOSInventories`

- 


`cloudasset.assets.listResource`





When using the `RESOURCE` content type.


#### **Limiting resource access**



Granting the `cloudasset.assets.listResource`
permission to a user allows them to list all resource types. To restrict what resource
types a user can list, you can grant permissions for each resource type instead. For
example, you can grant the `cloudasset.assets.listComputeDisks` permission
by itself to allow a user to only list the `compute.googleapis.com/Disk`
resource type.




These granular permissions only apply to `RESOURCE` and unspecified
[
content types](/asset-inventory/docs/asset-inventory-overview#content_types).




[
View the list of granular `cloudasset.assets.list*` permissions](/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel).





| 
|


| 
Search APIs | 
|

| 


`search-all-iam-policies`
| 
`cloudasset. assets. searchAllIamPolicies` | 
|

| 


`search-all-resources`
| 



`cloudasset. assets. searchAllResources`



You also need
`cloudasset. assets. searchEnrichmentResourceOwners` if
searching for resource owner enrichment.

| 
|



### Console

The Google Cloud Dedicated console uses the `SearchAllResources` API to
request data. To use Cloud Asset Inventory in the Google Cloud Dedicated console, grant the
following permissions:


- `cloudasset. assets. searchAllResources`

- `serviceusage.services.use`
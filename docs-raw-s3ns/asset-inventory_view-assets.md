# View your assets

Source: https://documentation.s3ns.fr/asset-inventory/docs/view-assets
Last updated: 2026-11-10

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

Guides

](https://documentation.s3ns.fr/asset-inventory/docs/asset-inventory-overview)


























# View your assets




This document shows you how to view your assets using Cloud Asset Inventory and the
Google Cloud CLI in Cloud Shell.





## Before you begin



To complete the instructions in this document, you need to enable the
Cloud Asset Inventory API and set up permissions for access to Cloud Asset Inventory and
Compute Engine.






















- 





In the Cloud de Confiance console, on the project selector page,
select or create a Cloud de Confiance project.





**Roles required to select or create a project**




- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.s3nscloud.fr/projectselector2/home/dashboard)












- 


If you're using an existing project for this guide,
[verify that you have
the permissions required to complete this guide](#required-roles). If you created a new
project, then you already have the required permissions.









- 




Enable the Cloud Asset Inventory API, if it is not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.s3nscloud.fr/apis/enableflow?apiid=cloudasset.googleapis.com&redirect=https%3A//console.cloud.google.com)












### Required roles

























































































































































































To get the permissions that
you need to complete these instructions,

ask your administrator to grant you the
following IAM roles on the organization, folder, or project:












- 
To view asset metadata:
[Cloud Asset Viewer ](/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)





- 
To create and delete a Compute Engine VM instance:




- [Compute Instance Admin (v1) ](/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)


- [Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)












For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








These predefined roles contain

the permissions required to complete these instructions. To see the exact permissions that are
required, expand the **Required permissions** section:






#### Required permissions



The following permissions are required to complete these instructions:





- 
To list asset metadata:
`cloudasset.assets.listResource`





- 
To create a Compute Engine VM instance:




- 
`compute.disks.create`


- 
`compute.instances.create`


- 
`compute.instances.delete`


- 
`compute.instances.setServiceAccount`


- 
`compute.projects.get`


- 
`compute.subnetworks.use`


- 
`compute.subnetworks.useExternalIp`


- 
`compute.zoneOperations.get`
















You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).














## View your assets

In a project of your choice, create a Compute Engine VM instance so that
you can view it in Cloud Asset Inventory:

- 

In the Cloud de Confiance console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.s3nscloud.fr/compute/instances)

- 

Click **Create instance**.

- 

Enter a name for the instance.

- 

Click **Create**.

- 

Wait for the instance to be created.

List all the VM instances in your project:

- 

In the Cloud de Confiance console, click
terminal **Activate Cloud Shell**.

- 

In Cloud Shell, run the following command:


```
gcloud asset list \ 
--project = PROJECT_ID \ 
--asset-types = compute.googleapis.com/Instance \ 
--content-type = resource
```


Replace ` PROJECT_ID ` with the ID of the project whose
assets you want to list.

In the previous code sample, an asset type of
`compute.googleapis.com/Instance` is used to only list
Compute Engine VM instances. To view all asset types, see
[Asset types](/asset-inventory/docs/asset-types).

A content type of `resource` has also been set. This specifies that
`resource` metadata should also be returned in the response. If no
content type is set, then only basic information about each asset is
returned, such as the asset name, the last time it was updated, and what
project it's in.






## Clean up





To avoid incurring charges to your Cloud de Confiance account for
the resources used on this page, follow these steps.






- 

In the Cloud de Confiance console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.s3nscloud.fr/compute/instances)

- 

In the same row as the name of the VM instance you created, click
more_vert **More actions**.

- 

Click **Delete**, and then confirm the deletion.






## What's next



- To explore more options related to viewing your assets, see
[List assets](/asset-inventory/docs/list-assets).
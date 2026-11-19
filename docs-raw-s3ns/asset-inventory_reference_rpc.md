# Cloud Asset API

Source: https://documentation.s3ns.fr/asset-inventory/docs/reference/rpc
Last updated: 2026-04-24

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












# Cloud Asset API 


















The Cloud Asset API manages the history and inventory of Cloud de Confiance resources.



## Service: cloudasset.googleapis.com



The Service name `cloudasset.googleapis.com` is needed to create RPC client stubs.




## `[google.cloud.asset.v1.AssetService](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService)`





| 
Methods | 
|



| 

` [BatchGetAssetsHistory](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.BatchGetAssetsHistory)` | 

Batch gets the update history of assets that overlap a time window. | 
|

| 

` [ExportAssets](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ExportAssets)` | 

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. | 
|

| 

` [ListAssets](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ListAssets)` | 

Lists assets with time and resource types and returns paged results in response. | 
|

| 

` [SearchAllIamPolicies](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.SearchAllIamPolicies)` | 

Searches all IAM policies within the specified scope, such as a project, folder, or organization. | 
|

| 

` [SearchAllResources](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.SearchAllResources)` | 

Searches all Cloud de Confiance resources within the specified scope, such as a project, folder, or organization. | 
|






## `[google.longrunning.Operations](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations)`





| 
Methods | 
|



| 

` [CancelOperation](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)` | 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

` [DeleteOperation](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)` | 

Deletes a long-running operation. | 
|

| 

` [GetOperation](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` | 

Gets the latest state of a long-running operation. | 
|

| 

` [ListOperations](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)` | 

Lists operations that match the specified filter in the request. | 
|

| 

` [WaitOperation](/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)` | 

The method `google.longrunning.Operations.WaitOperation` is not available in Cloud de Confiance by S3NS. | 
|
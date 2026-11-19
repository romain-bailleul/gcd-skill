# Cloud Asset API

Source: https://berlin.devsitetest.how/asset-inventory/docs/reference/rpc
Last updated: 2026-04-24

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












# Cloud Asset API 


















The Cloud Asset API manages the history and inventory of Google Cloud Dedicated resources.



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

Searches all Google Cloud Dedicated resources within the specified scope, such as a project, folder, or organization. | 
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

The method `google.longrunning.Operations.WaitOperation` is not available in Google Cloud Dedicated in Germany. | 
|
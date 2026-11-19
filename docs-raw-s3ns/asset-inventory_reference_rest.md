# Cloud Asset API

Source: https://documentation.s3ns.fr/asset-inventory/docs/reference/rest
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




- [REST Resource: v1](#v1)

- [REST Resource: v1.assets](#v1.assets)

- [REST Resource: v1.operations](#v1.operations)





## Service: cloudasset.googleapis.com



To call this service, we recommend that you use the Google-provided [client libraries](https://documentation.s3ns.fr/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://s3nsapis.fr/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://cloudasset.s3nsapis.fr/$discovery/rest?version=v1](https://cloudasset.s3nsapis.fr/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://documentation.s3ns.fr/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://cloudasset.s3nsapis.fr`






## REST Resource: [v1](/asset-inventory/docs/reference/rest/v1/TopLevel)





| 
Methods | 
|



| 

`[batchGetAssetsHistory](/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory)` | 

`GET /v1/{parent=*/*}:batchGetAssetsHistory` 

Batch gets the update history of assets that overlap a time window. | 
|

| 

`[exportAssets](/asset-inventory/docs/reference/rest/v1/TopLevel/exportAssets)` | 

`POST /v1/{parent=*/*}:exportAssets` 

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. | 
|

| 

`[searchAllIamPolicies](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies)` | 

`GET /v1/{scope=*/*}:searchAllIamPolicies` 

Searches all IAM policies within the specified scope, such as a project, folder, or organization. | 
|

| 

`[searchAllResources](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources)` | 

`GET /v1/{scope=*/*}:searchAllResources` 

Searches all Cloud de Confiance resources within the specified scope, such as a project, folder, or organization. | 
|






## REST Resource: [v1.assets](/asset-inventory/docs/reference/rest/v1/assets)





| 
Methods | 
|



| 

`[list](/asset-inventory/docs/reference/rest/v1/assets/list)` | 

`GET /v1/{parent=*/*}/assets` 

Lists assets with time and resource types and returns paged results in response. | 
|






## REST Resource: [v1.operations](/asset-inventory/docs/reference/rest/v1/operations)





| 
Methods | 
|



| 

`[cancel](/asset-inventory/docs/reference/rest/v1/operations/cancel)` | 

`POST /v1/{name=operations/**}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[delete](/asset-inventory/docs/reference/rest/v1/operations/delete)` | 

`DELETE /v1/{name=operations/**}` 

Deletes a long-running operation. | 
|

| 

`[get](/asset-inventory/docs/reference/rest/v1/operations/get)` | 

`GET /v1/{name=*/*/operations/*/**}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/asset-inventory/docs/reference/rest/v1/operations/list)` | 

`GET /v1/{name=operations}` 

Lists operations that match the specified filter in the request. | 
|
# Quotas and limits

Source: https://documentation.s3ns.fr/asset-inventory/docs/quota
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

Resources

](https://documentation.s3ns.fr/asset-inventory/docs/quota)












# Quotas and limits 















## Project quota

Cloud Asset Inventory enforces the rate of incoming requests based on the consumer
project. The default quotas are as follows:




| 
Quota | 
Value | 
|




| 
`BatchGetAssetsHistory` | 
100 per minute per consumer project | 
|


| 
`ExportAssets` | 



60 per minute per consumer project



6000 per day per consumer project

| 
|

| 
`ListAssets` | 
100 per minute per consumer project | 
|


| 
`SearchAllIamPolicies` | 
400 per minute per consumer project | 
|

| 
`SearchAllResources` | 
400 per minute per consumer project | 
|



You can use the
[APIs and services quotas dashboard](https://console.cloud.s3nscloud.fr/apis/api/cloudasset.googleapis.com/quotas?project=_)
to view current quotas and usage for your project.

## Resource organization quota

In addition to the per-project quota, Cloud Asset Inventory also enforces rate
limits on incoming requests based on resource organization. The limits are as
follows:




| 
Quota | 
Value | 
|



| 
`BatchGetAssetsHistory` | 



180 per minute per organization



195,000 per day per organization

| 
|

| 
`ExportAssets` | 



75 per minute per organization



13,000 per day per organization

| 
|

| 
`ListAssets` | 



800 per minute per organization



650,000 per day per organization

| 
|



| 
`SearchAllIamPolicies` | 
3,000 per minute per organization | 
|

| 
`SearchAllResources` | 
1,500 per minute per organization | 
|



## Downstream services

In addition to limits enforced by Cloud Asset Inventory, the number of incoming
requests is also capped by the rate and quota of the downstream services that
Cloud Asset Inventory depends on.

### BigQuery

- 

**Table operations:** BigQuery has a [quota limit](/bigquery/quotas)
for table operations, which defines the maximum number of `ExportAssets` API
requests to the same BigQuery table that can be performed daily.
`ExportAssets` issues 2 table operations per table per request.

- 

**Query jobs:** BigQuery has a concurrent
[rate limit](/bigquery/quotas#query_jobs) for query job, which defines the
maximum number of concurrent `ExportAssets` API requests that can be issued
per project.

## Optimize API usage

To help stay within existing quotas, use the following best practices to
optimize your API usage:

- 

Reduce your query scope to the smallest possible surface.

- 

Slow down your request rate, and implement exponential backoff.

- 

Batch requests where possible.

- 

The [`ListAssets`](/asset-inventory/docs/list-assets) and
[`SearchAllResources`](/asset-inventory/docs/search-resources) APIs are
synchronous, which means that they return results in pages. This forces your
application to make multiple sequential requests to retrieve a large
inventory, which can exhaust your [quota](#project-quota). Where appropriate,
use the following asynchronous methods instead, so that only a single API
request is made:

- 

[Export to BigQuery](/asset-inventory/docs/export-bigquery)

- 

[Export to Cloud Storage](/asset-inventory/docs/export-cloud-storage)

- 

[Create a Pub/Sub feed](/asset-inventory/docs/monitor-asset-changes)
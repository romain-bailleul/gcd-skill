# Get asset histories

Source: https://berlin.devsitetest.how/asset-inventory/docs/get-asset-history
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












# Get asset histories 















You can retrieve up to 35 days of create, update, and delete history for your
assets in Google Cloud Dedicated in Germany projects or organizations. Assets that haven't changed in
the past 35 days report their latest status.

## Before you begin

- 

Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands
from.

[Enable the Cloud Asset Inventory API](https://console.cloud.berlin-build0.goog/apis/library/cloudasset.googleapis.com)

- 

Make sure your account has the
[correct role to call the Cloud Asset Inventory API](/asset-inventory/docs/roles-permissions#roles).
For individual permissions for each call type, see
[Permissions](/asset-inventory/docs/roles-permissions#permissions).

## Limitations

You can only retrieve asset history at the organization and project level.
Folders aren't supported.

## Get your asset histories






#### Console



To get the history of your assets stored in Google Cloud Dedicated in Germany, complete the
following steps.




- 


Go to the **Asset Inventory** page in the
Google Cloud Dedicated console.





[Go to Asset Inventory](https://console.cloud.berlin-build0.goog/iam-admin/asset-inventory/)



- 
Change to the project, folder, or organization you want to search.


- Click the **Resource** tab.

- 
In the **Filter results** panel, select a resource type or location
to filter the results.


- Click a resource in the results panel.

- Click the **Change history** tab.

- Select a **Start time** and **End time** for the report.

- 
Use the **Select a record to compare** list boxes to show a diff
between the records for your selected dates.





After performing a search, the resources matching the query are listed in
the **Results** table. Double-click your query to edit it, or use the
**Filter results** pane to restrict the search results by specific
criteria.



To view the query as a Google Cloud CLI command, click
**View query**.



To export the results, click **Download CSV**.







#### gcloud


```
gcloud asset get-history \ 
-- SCOPE \ 
--asset-names = ASSET_NAME_1 , ASSET_NAME_2 ,... \ 
--content-type = CONTENT_TYPE \ 
--start-time = " START_TIME " \ 
--end-time = " END_TIME " 
```


Provide the following values:



- 


` SCOPE `: Use one of the following values:




- 
`project= PROJECT_ID `, where ` PROJECT_ID ` is the ID
of the project that has the asset that you want to retrieve.


- 


`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
that you want to retrieve.












How to find the ID of a Google Cloud Dedicated in Germany organization 




### Google Cloud Dedicated console



To find the ID of a Google Cloud Dedicated in Germany organization, complete the following steps:





- 


Go to the Google Cloud Dedicated console.



[
Go to the Google Cloud Dedicated console
](https://console.cloud.berlin-build0.goog/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Click the **All** tab. The organization ID is shown next to the organization name.






### gcloud CLI



You can retrieve the ID of a Google Cloud Dedicated in Germany organization with the following command:



```
gcloud organizations describe ORGANIZATION_NAME --format = "value(name.segment(1))" 
```











- 
` ASSET_NAME_# `: A comma-separated list of
[asset full names](/asset-inventory/docs/asset-names).

- 
` CONTENT_TYPE `: The
[content type](/asset-inventory/docs/asset-inventory-overview#content_types) of the
metadata that you want to retrieve. When `--content-type`
isn't specified, only basic information is returned, such as asset names, the last time the
assets were updated, and what projects, folders, and organizations that they belong to.

- 
` START_TIME `: The beginning of the time range, in
[gcloud topic datetime format](/sdk/gcloud/reference/topic/datetimes). The value must
be no more than 35 days in the past.

- 
` END_TIME `: Optional. The finishing point of the time range, in
[gcloud topic datetime format](/sdk/gcloud/reference/topic/datetimes). The value must
be no more than 35 days in the past. When `--end-time`
isn't specified, it's set to the current time.

See the [gcloud CLI reference](/sdk/gcloud/reference/asset/get-history) for all options.

### Example

Run the following command to get the `resource` history metadata of the
`my-instance` Compute Engine instance in the `my-project` project
between January 30, 2024 and February 5, 2024. The instance has the following properties:


- **Instance name**: `my-instance`

- **Project**: `my-project`

- **Location**: `us-central1-a`


```
gcloud asset get-history \ 
--project = my-project \ 
--asset-names = //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance \ 
--content-type = resource \ 
--start-time = "2024-01-30" \ 
--end-time = "2024-02-05" 
```

#### Example response


```
---
asset:
ancestors:
- projects/000000000000
- folders/000000000000
- organizations/000000000000
assetType: compute.googleapis.com/Instance
name: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance
resource:
data:
LATEST_ASSET_METADATA 
discoveryDocumentUri: https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1
discoveryName: Instance
location: us-central1-a
parent: //cloudresourcemanager.googleapis.com/projects/000000000000
version: v1
updateTime: '2024-02-05T16:00:25.259186Z'
window:
endTime: '2024-02-05T16:00:25.259186Z'
startTime: '2024-02-03T16:00:28.854779Z'
---
asset:
ancestors:
- projects/000000000000
- folders/000000000000
- organizations/000000000000
assetType: compute.googleapis.com/Instance
name: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance
resource:
data:
EARLIEST_ASSET_METADATA 
discoveryDocumentUri: https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1
discoveryName: Instance
location: us-central1-a
parent: //cloudresourcemanager.googleapis.com/projects/000000000000
version: v1
updateTime: '2024-02-03T16:00:28.854779Z'
window:
endTime: '2024-02-03T16:00:28.854779Z'
startTime: '2024-01-30T08:00:22.930462Z'
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/ SCOPE_PATH :batchGetAssetsHistory
```


Request JSON body:


```
{ 
"assetNames" : [ 
" ASSET_NAME_1 " , 
" ASSET_NAME_2 " , 
"..." 
], 
"contentType" : " CONTENT_TYPE " , 
"readTimeWindow" : { 
"startTime" : " START_TIME " , 
"endTime" : " END_TIME " 
} 
} 
```


Provide the following values:





- 


` SCOPE_PATH `: Use one of the following values:




- 
`projects/ PROJECT_ID `, where ` PROJECT_ID ` is the
ID of the project that has the asset that you want to retrieve.


- 


`projects/ PROJECT_NUMBER `, where
` PROJECT_NUMBER ` is the number of the project that has the asset that
you want to retrieve.












How to find a Google Cloud Dedicated in Germany project number 




### Google Cloud Dedicated console



To find a Google Cloud Dedicated in Germany project number, complete the following steps:





- 


Go to the **Welcome** page in the Google Cloud Dedicated console.



[
Go to Welcome](https://console.cloud.berlin-build0.goog/welcome)



- Click the **switcher** list box in the menu bar.

- 


Select your organization from the list box, and then search for your project name.
The project name, project number, and project ID are shown near the **Welcome**
heading.




Up to 4,000 resources are displayed. If you don't see the project you're looking for,
go to the
[**Manage resources**](https://console.cloud.berlin-build0.goog//cloud-resource-manager) page and
filter the list using the name of that project.









### gcloud CLI



You can retrieve a Google Cloud Dedicated in Germany project number with the following command:



```
gcloud projects describe PROJECT_ID --format = "value(projectNumber)" 
```









- 


`organizations/ ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
that you want to retrieve.












How to find the ID of a Google Cloud Dedicated in Germany organization 




### Google Cloud Dedicated console



To find the ID of a Google Cloud Dedicated in Germany organization, complete the following steps:





- 


Go to the Google Cloud Dedicated console.



[
Go to the Google Cloud Dedicated console
](https://console.cloud.berlin-build0.goog/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Click the **All** tab. The organization ID is shown next to the organization name.






### gcloud CLI



You can retrieve the ID of a Google Cloud Dedicated in Germany organization with the following command:



```
gcloud organizations describe ORGANIZATION_NAME --format = "value(name.segment(1))" 
```











- 
` ASSET_NAME_# `: An array of [asset
full names](/asset-inventory/docs/asset-names).

- 
` CONTENT_TYPE `: The
[content type](/asset-inventory/docs/asset-inventory-overview#content_types) of the
metadata that you want to retrieve. When `contentType` isn't specified, only basic
information is returned, such as asset names, the last time the assets were updated, and what
projects, folders, and organizations that they belong to.

- 
` START_TIME `: The beginning of the time range, in
[RFC 3339 format](https://www.rfc-editor.org/rfc/rfc3339#section-5.8). The value must
be no more than 35 days in the past.

- 
` END_TIME `: Optional. The finishing point of the time range, in
[RFC 3339 format](https://www.rfc-editor.org/rfc/rfc3339#section-5.8). The value must
be no more than 35 days in the past. When `endTime` isn't specified, it's set to the
current time.



See the [REST reference](/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory) for all options.

### Command examples

Run one of the following commands to get the `resource` history of the
`my-instance` Compute Engine instance in the `my-project` project
between January 30, 2024 and February 5, 2024. The instance has the following properties:


- **Instance name**: `my-instance`

- **Project**: `my-project`

- **Location**: `us-central1-a`




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetNames": ["//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance"], 
"contentType": "RESOURCE", 
"readTimeWindow": { 
"startTime": "2024-01-30T00:00:00Z", 
"endTime": "2024-02-05T00:00:00Z" 
} 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:batchGetAssetsHistory
```




#### PowerShell (Windows)



```
$cred = gcloud auth print-access-token 

$headers = @{ 
"X-HTTP-Method-Override" = "GET" ; 
"Authorization" = "Bearer $cred" 
} 

$body = @" 
{ 
"assetNames": ["//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance"], 
"contentType": "RESOURCE", 
"readTimeWindow": { 
"startTime": "2024-01-30T00:00:00Z", 
"endTime": "2024-02-05T00:00:00Z" 
} 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:batchGetAssetsHistory" | Select-Object -Expand Content 
```



#### Example response


```
{ 
"assets" : [ 
{ 
"window" : { 
"startTime" : "2024-02-03T16:00:28.854779Z" , 
"endTime" : "2024-02-05T16:00:25.259186Z" 
}, 
"asset" : { 
"name" : "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance" , 
"assetType" : "compute.googleapis.com/Instance" , 
"resource" : { 
"version" : "v1" , 
"discoveryDocumentUri" : "https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1" , 
"discoveryName" : "Instance" , 
"parent" : "//cloudresourcemanager.googleapis.com/projects/000000000000" , 
"data" : { 
LATEST_ASSET_METADATA 
}, 
"location" : "us-central1-a" 
}, 
"ancestors" : [ 
"projects/000000000000" , 
"folders/000000000000" , 
"organizations/000000000000" 
], 
"updateTime" : "2024-02-05T16:00:25.259186Z" 
} 
}, 
{ 
"window" : { 
"startTime" : "2024-01-30T08:00:22.930462Z" , 
"endTime" : "2024-02-03T16:00:28.854779Z" 
}, 
"asset" : { 
"name" : "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance" , 
"assetType" : "compute.googleapis.com/Instance" , 
"resource" : { 
"version" : "v1" , 
"discoveryDocumentUri" : "https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1" , 
"discoveryName" : "Instance" , 
"parent" : "//cloudresourcemanager.googleapis.com/projects/000000000000" , 
"data" : { 
EARLIEST_ASSET_METADATA 
}, 
"location" : "us-central1-a" 
}, 
"ancestors" : [ 
"projects/000000000000" , 
"folders/000000000000" , 
"organizations/000000000000" 
], 
"updateTime" : "2024-02-03T16:00:28.854779Z" 
} 
} 
] 
} 
```




#### C#





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
using [ Google.Api.Gax.ResourceNames ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 
using [ Google.Cloud.Asset.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 
using System ; 

public class BatchGetAssetsHistorySample 
{ 
public BatchGetAssetsHistoryResponse BatchGetAssetsHistory ( string [] assetNames , DateTimeOffset startTime , string projectId ) 
{ 
// Create the client. 
[ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_Create) (); 

// Build the request. 
[ BatchGetAssetsHistoryRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.BatchGetAssetsHistoryRequest.html) request = new [ BatchGetAssetsHistoryRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.BatchGetAssetsHistoryRequest.html)
{ 
ParentAsResourceName = [ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) . [ FromProject ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_) ( projectId ), 
ContentType = [ ContentType ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ContentType.html) . [ Resource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ContentType.html#Google_Cloud_Asset_V1_ContentType_Resource) , 
ReadTimeWindow = new [ TimeWindow ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.TimeWindow.html)
{ 
StartTime = [ Timestamp ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html) . [ FromDateTimeOffset ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTimeOffset_System_DateTimeOffset_) ( startTime ) 
} 
}; 
request . [ AssetNames ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.BatchGetAssetsHistoryRequest.html#Google_Cloud_Asset_V1_BatchGetAssetsHistoryRequest_AssetNames) . AddRange ( assetNames ); 

// Call the API. 
[ BatchGetAssetsHistoryResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.BatchGetAssetsHistoryResponse.html) response = client . [ BatchGetAssetsHistory ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_BatchGetAssetsHistory_Google_Cloud_Asset_V1_BatchGetAssetsHistoryRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Return the result. 
return response ; 
} 
} 
```




















#### Go




























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Sample asset-quickstart batch-gets assets history. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"os" 
"time" 

asset "cloud.google.com/go/asset/apiv1" 
"cloud.google.com/go/asset/apiv1/assetpb" 
"github.com/golang/protobuf/ptypes/timestamp" 
) 

func main () { 
ctx := context . Background () 
client , err := asset . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatal ( err ) 
} 
defer client . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close) () 

projectID := os . Getenv ( "GOOGLE_CLOUD_PROJECT" ) 
bucketResourceName := fmt . Sprintf ( "//storage.googleapis.com/%s-for-assets" , projectID ) 
req := & assetpb . BatchGetAssetsHistoryRequest { 
Parent : fmt . Sprintf ( "projects/%s" , projectID ), 
AssetNames : [] string { bucketResourceName }, 
ContentType : assetpb . [ ContentType_RESOURCE ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1/assetpb.html#cloud_google_com_go_asset_apiv1_assetpb_ContentType_CONTENT_TYPE_UNSPECIFIED_ContentType_RESOURCE_ContentType_IAM_POLICY_ContentType_ORG_POLICY_ContentType_ACCESS_POLICY_ContentType_OS_INVENTORY_ContentType_RELATIONSHIP) , 
ReadTimeWindow : & assetpb . TimeWindow { 
StartTime : & timestamp . Timestamp { 
Seconds : time . Now (). Unix (), 
}, 
}, 
} 
response , err := client . BatchGetAssetsHistory ( ctx , req ) 
if err != nil { 
log . Fatal ( err ) 
} 
fmt . Print ( response ) 
} 
```





















#### Java





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Imports the Google Cloud client library 

import com.google.cloud.[ServiceOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) ; 
import com.google.cloud.asset.v1.[AssetServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) ; 
import com.google.cloud.asset.v1.[BatchGetAssetsHistoryRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BatchGetAssetsHistoryRequest.html) ; 
import com.google.cloud.asset.v1.[BatchGetAssetsHistoryResponse](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BatchGetAssetsHistoryResponse.html) ; 
import com.google.cloud.asset.v1.[ContentType](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) ; 
import com.google.cloud.asset.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) ; 
import com.google.cloud.asset.v1.[TimeWindow](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.TimeWindow.html) ; 
import java.util.Arrays ; 

public class BatchGetAssetsHistoryExample { 

// Use the default project Id. 
private static final [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ ServiceOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) . getDefaultProjectId (); 

public static void main ( [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) ... args ) throws Exception { 
// Asset names, e.g.: "//storage.googleapis.com/[BUCKET_NAME]" 
[ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) [] assetNames = args [ 0 ] . [ split ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_) ( "," ); 
try ( [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) . create ()) { 
[ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) parent = [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) . of ( projectId ); 
[ ContentType ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) contentType = [ ContentType ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) . RESOURCE ; 
[ TimeWindow ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.TimeWindow.html) readTimeWindow = [ TimeWindow ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.TimeWindow.html) . newBuilder (). build (); 
[ BatchGetAssetsHistoryRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BatchGetAssetsHistoryRequest.html) request = 
[ BatchGetAssetsHistoryRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BatchGetAssetsHistoryRequest.html) . newBuilder () 
. setParent ( [ parent ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_parent__) . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html#com_google_cloud_asset_v1_ProjectName_toString__) ()) 
. addAllAssetNames ( Arrays . asList ( assetNames )) 
. setContentType ( contentType ) 
. setReadTimeWindow ( readTimeWindow ) 
. build (); 
[ BatchGetAssetsHistoryResponse ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BatchGetAssetsHistoryResponse.html) response = client . batchGetAssetsHistory ( request ); 
System . out . println ( response ); 
} 
} 
} 
```





















#### Node.js





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const assetNames = '//storage.googleapis.com/ ,//storage.googleapis.com/ '; 
// const contentType = 'RESOURCE'; 

const util = require ( 'util' ); 
const { AssetServiceClient } = require ( '[@google-cloud/asset](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html)' ); 

const client = new [ AssetServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html) (); 

async function batchGetAssetsHistory () { 
const projectId = await client . getProjectId (); 
const projectResource = `projects/ ${ projectId } ` ; 
// TODO(developer): Choose asset names, such as //storage.googleapis.com/[YOUR_BUCKET_NAME]. 
// const assetNames = ['ASSET_NAME1', 'ASSET_NAME2', ...]; 

const request = { 
parent : projectResource , 
assetNames : assetNames . split ( ',' ), 
contentType : contentType , 
readTimeWindow : { 
startTime : { 
seconds : Math . floor ( new [ Date ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/asset/protos.google.type.date.html) (). getTime () / 1000 ), 
}, 
}, 
}; 

// Handle the operation using the promise pattern. 
const result = await client . batchGetAssetsHistory ( request ); 
// Do things with with the response. 
console . log ( util . inspect ( result , { depth : null })); 
```





















#### PHP




























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\Asset\V1\BatchGetAssetsHistoryRequest; 
use Google\Cloud\Asset\V1\Client\AssetServiceClient; 
use Google\Cloud\Asset\V1\ContentType; 
use Google\Cloud\Asset\V1\TimeWindow; 
use Google\Protobuf\Timestamp; 

/** 
* @param string $projectId Tthe project Id for list assets. 
* @param string[] $assetNames (Optional) Asset types to list for. 
*/ 
function batch_get_assets_history(string $projectId, array $assetNames): void 
{ 
$client = new AssetServiceClient(); 
$formattedParent = $client->projectName($projectId); 
$contentType = ContentType::RESOURCE; 
$readTimeWindow = new TimeWindow(['start_time' => new Timestamp(['seconds' => time()])]); 
$request = (new BatchGetAssetsHistoryRequest()) 
->setParent($formattedParent) 
->setContentType($contentType) 
->setReadTimeWindow($readTimeWindow) 
->setAssetNames($assetNames); 

$resp = $client->batchGetAssetsHistory($request); 

# Do things with response. 
print($resp->serializeToString()); 
} 
```





















#### Python





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import asset_v1 

# TODO project_id = 'Your Google Cloud Project ID' 
# TODO asset_names = 'Your asset names list, e.g.: 
# ["//storage.googleapis.com/[BUCKET_NAME]",]' 

client = asset_v1 . [ AssetServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html) () 
parent = f "projects/ { project_id } " 
content_type = asset_v1 . [ ContentType ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ContentType.html) . RESOURCE 
read_time_window = asset_v1 . [ TimeWindow ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TimeWindow.html) () 
response = client . [ batch_get_assets_history ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_batch_get_assets_history) ( 
request = { 
"parent" : parent , 
"asset_names" : asset_names , 
"content_type" : content_type , 
"read_time_window" : read_time_window , 
} 
) 
print ( f "assets: { response . assets } " ) 
```





















#### Ruby





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
require "google/cloud/asset" 

# project_id = 'YOUR_PROJECT_ID' 
# asset names, e.g.: //storage.googleapis.com/[YOUR_BUCKET_NAME] 
# asset_names = [ASSET_NAMES, COMMMA_DELIMTTED] 
asset_service = Google :: Cloud :: [ Asset ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html) . [ asset_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)

formatted_parent = asset_service . [ project_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Paths.html) project : project_id 

content_type = :RESOURCE 
read_time_window = { 
start_time : { 
seconds : Time . now . getutc . to_i 
} 
} 

response = asset_service . batch_get_assets_history ( 
parent : formatted_parent , 
content_type : content_type , 
read_time_window : read_time_window , 
asset_names : asset_names 
) 
# Do things with the response 
puts response . assets 
```
# Export asset metadata to Cloud Storage

Source: https://documentation.s3ns.fr/asset-inventory/docs/export-cloud-storage
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












# Export asset metadata to Cloud Storage 















This document shows you how to export the asset metadata of your organization,
folder, or project to a [Cloud Storage bucket](/storage/docs/buckets).

## Before you begin

- 

Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands
from.

[Enable the Cloud Asset Inventory API](https://console.cloud.s3nscloud.fr/apis/library/cloudasset.googleapis.com)

- 

Make sure your account has the
[correct role to call the Cloud Asset Inventory API](/asset-inventory/docs/roles-permissions#roles).
For individual permissions for each call type, see
[Permissions](/asset-inventory/docs/roles-permissions#permissions).

- 

[Create a Cloud Storage bucket](/storage/docs/creating-buckets) to
export to, if you don't have one already.

## Limitations

- 

Cloud Storage buckets encrypted with custom Cloud Key Management Service
(Cloud KMS) keys are not supported.

- 

The Cloud Storage bucket can't have a
[retention policy](/storage/docs/bucket-lock) set.

- 

During export, the operation might create temporary files in the output
folder. Don't remove these temporary files while the operation is in progress.
After the operation is complete, the temporary files are removed
automatically.

- 

The `ACCESS_POLICY` content type can only be exported at the
organization level.

- 

If the file you're exporting to already exists and is in the process of being
exported to, a `400` error is returned.

- 

To test permissions, Cloud Asset Inventory creates an empty file before exporting the
data, which sends out an extra Cloud Storage trigger event of
[`google.cloud.storage.object.v1.finalized`](/functions/docs/calling/storage).

## Export an asset snapshot to Cloud Storage







#### gcloud


```
gcloud asset export \ 
-- SCOPE \ 
--billing-project = BILLING_PROJECT_ID \ 
--asset-types = ASSET_TYPE_1 , ASSET_TYPE_2 ,... \ 
--content-type = CONTENT_TYPE \ 
--snapshot-time = " SNAPSHOT_TIME " \ 
-- OUTPUT_TYPE 
```


Provide the following values:



- 


` SCOPE `: Use one of the following values:




- 
`project= PROJECT_ID `, where ` PROJECT_ID ` is the ID
of the project that has the asset metadata you want to export.


- 


`folder= FOLDER_ID `, where ` FOLDER_ID ` is the ID
of the folder that has the asset metadata you want to export.













How to find the ID of a Cloud de Confiance by S3NS folder 




### Cloud de Confiance console



To find the ID of a Cloud de Confiance by S3NS folder, complete the following steps:





- 


Go to the Cloud de Confiance console.



[
Go to the Cloud de Confiance console
](https://console.cloud.s3nscloud.fr/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Search for your folder name. The folder ID is shown next to the folder name.






### gcloud CLI



You can retrieve the ID of a Cloud de Confiance by S3NS folder that's located at the organization level with the following command:



```
gcloud resource-manager folders list \ 
--organization = $( gcloud organizations describe ORGANIZATION_NAME \ 
--format = "value(name.segment(1))" ) \ 
--filter = '"DISPLAY_NAME":" TOP_LEVEL_FOLDER_NAME "' \ 
--format = "value(ID)" 
```




Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the
folder's name. Remove the `--format` flag to see more information about the
found folders.



The previous command doesn't return the IDs of subfolders within folders. To do so,
run the following command using a top level folder's ID:


```
gcloud resource-manager folders list --folder = FOLDER_ID 
```










- 


`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












How to find the ID of a Cloud de Confiance by S3NS organization 




### Cloud de Confiance console



To find the ID of a Cloud de Confiance by S3NS organization, complete the following steps:





- 


Go to the Cloud de Confiance console.



[
Go to the Cloud de Confiance console
](https://console.cloud.s3nscloud.fr/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Click the **All** tab. The organization ID is shown next to the organization name.






### gcloud CLI



You can retrieve the ID of a Cloud de Confiance by S3NS organization with the following command:



```
gcloud organizations describe ORGANIZATION_NAME --format = "value(name.segment(1))" 
```











- 
` BILLING_PROJECT_ID `: Optional. The project ID that the default Cloud Asset Inventory
service agent is in that has permissions to manage your Cloud Storage buckets.
[
Read more about setting the billing project](/asset-inventory/docs/multiple-projects#orchestrator).

- 
` ASSET_TYPE_# `: Optional. A comma-separated list of
[searchable asset types](/asset-inventory/docs/asset-types).
[RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are
supported. If the regular expression doesn't match any supported asset type, an
`INVALID_ARGUMENT` error is returned. When
`--asset-types` isn't specified, all asset types are
returned.

- 
` CONTENT_TYPE `: Optional. The
[content type](/asset-inventory/docs/asset-inventory-overview#content_types) of the
metadata that you want to retrieve. When `--content-type`
isn't specified, only basic information is returned, such as asset names, the last time the
assets were updated, and what projects, folders, and organizations that they belong to.

- 
` SNAPSHOT_TIME `: Optional. The time at which you want to take a snapshot of
your assets, in [gcloud topic datetime format](/sdk/gcloud/reference/topic/datetimes).
The value must be no more than 35 days in the past. When
`--snapshot-time` isn't specified, a snapshot is taken at
the current time.

- 


` OUTPUT_TYPE `: Use one of the following values:




- 


`--output-path="gs:// BUCKET_NAME / FILE_NAME "` to write the
output to a file, where:





- 
` BUCKET_NAME ` is the name of the Cloud Storage bucket to
write to.


- 
` FILE_NAME ` is the file to write to in your Cloud Storage
bucket.





- 


`--output-path-prefix="gs:// BUCKET_NAME / FOLDER_NAME "` to
write the output to a folder, where:





- 
` BUCKET_NAME ` is the name of the Cloud Storage bucket to
write to.


- 
` FOLDER_NAME ` is the folder to write to in your
Cloud Storage bucket. The output is split into subfolders named after
[asset types](/asset-inventory/docs/asset-types). The subfolders must not already
exist in the folder that you specify.






See the [gcloud CLI reference](/sdk/gcloud/reference/asset/export) for all options.

### Example

Run the following command to export your `resource` metadata as it was on January 30,
2024 in the `my-project` project, to the file `my-file.txt` in the
Cloud Storage bucket `my-bucket`.


```
gcloud asset export \ 
--project = my-project \ 
--billing-project = my-project \ 
--content-type = resource \ 
--snapshot-time = "2024-01-30" \ 
--output-path = "gs://my-bucket/my-file.txt" 
```

#### Example response


```
Export in progress for root asset [projects/my-project].
Use [gcloud asset operations describe projects/000000000000/operations/ExportAssets/RESOURCE/00000000000000000000000000000000] to check the status of the operation.
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/ SCOPE_PATH :exportAssets
```


Headers:


```
X-Goog-User-Project: BILLING_PROJECT_ID 
```


Request JSON body:


```
{ 
"assetTypes" : [ 
" ASSET_TYPE_1 " , 
" ASSET_TYPE_2 " , 
"..." 
], 
"contentType" : " CONTENT_TYPE " , 
"readTime" : " SNAPSHOT_TIME " , 
"outputConfig" : { 
"gcsDestination" : { 
OUTPUT_TYPE 
} 
} 
} 
```


Provide the following values:





- 


` SCOPE_PATH `: Use one of the following values:




- 
`projects/ PROJECT_ID `, where ` PROJECT_ID ` is the
ID of the project that has the asset metadata you want to export.


- 


`projects/ PROJECT_NUMBER `, where
` PROJECT_NUMBER ` is the number of the project that has the asset
metadata you want to export.












How to find a Cloud de Confiance by S3NS project number 




### Cloud de Confiance console



To find a Cloud de Confiance by S3NS project number, complete the following steps:





- 


Go to the **Welcome** page in the Cloud de Confiance console.



[
Go to Welcome](https://console.cloud.s3nscloud.fr/welcome)



- Click the **switcher** list box in the menu bar.

- 


Select your organization from the list box, and then search for your project name.
The project name, project number, and project ID are shown near the **Welcome**
heading.




Up to 4,000 resources are displayed. If you don't see the project you're looking for,
go to the
[**Manage resources**](https://console.cloud.s3nscloud.fr//cloud-resource-manager) page and
filter the list using the name of that project.









### gcloud CLI



You can retrieve a Cloud de Confiance by S3NS project number with the following command:



```
gcloud projects describe PROJECT_ID --format = "value(projectNumber)" 
```









- 


`folders/ FOLDER_ID `, where ` FOLDER_ID ` is the ID
of the folder that has the asset metadata you want to export.













How to find the ID of a Cloud de Confiance by S3NS folder 




### Cloud de Confiance console



To find the ID of a Cloud de Confiance by S3NS folder, complete the following steps:





- 


Go to the Cloud de Confiance console.



[
Go to the Cloud de Confiance console
](https://console.cloud.s3nscloud.fr/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Search for your folder name. The folder ID is shown next to the folder name.






### gcloud CLI



You can retrieve the ID of a Cloud de Confiance by S3NS folder that's located at the organization level with the following command:



```
gcloud resource-manager folders list \ 
--organization = $( gcloud organizations describe ORGANIZATION_NAME \ 
--format = "value(name.segment(1))" ) \ 
--filter = '"DISPLAY_NAME":" TOP_LEVEL_FOLDER_NAME "' \ 
--format = "value(ID)" 
```




Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the
folder's name. Remove the `--format` flag to see more information about the
found folders.



The previous command doesn't return the IDs of subfolders within folders. To do so,
run the following command using a top level folder's ID:


```
gcloud resource-manager folders list --folder = FOLDER_ID 
```










- 


`organizations/ ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












How to find the ID of a Cloud de Confiance by S3NS organization 




### Cloud de Confiance console



To find the ID of a Cloud de Confiance by S3NS organization, complete the following steps:





- 


Go to the Cloud de Confiance console.



[
Go to the Cloud de Confiance console
](https://console.cloud.s3nscloud.fr/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Click the **All** tab. The organization ID is shown next to the organization name.






### gcloud CLI



You can retrieve the ID of a Cloud de Confiance by S3NS organization with the following command:



```
gcloud organizations describe ORGANIZATION_NAME --format = "value(name.segment(1))" 
```











- 
` BILLING_PROJECT_ID `: The project ID that the default Cloud Asset Inventory service
agent is in that has permissions to manage your Cloud Storage buckets.
[
Read more about setting the billing project](/asset-inventory/docs/multiple-projects#orchestrator).

- 
` ASSET_TYPE_# `: Optional. An array of
[searchable asset types](/asset-inventory/docs/asset-types).
[RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are
supported. If the regular expression doesn't match any supported asset type, an
`INVALID_ARGUMENT` error is returned. When `assetTypes` isn't specified, all
asset types are returned.

- 
` CONTENT_TYPE `: Optional. The
[content type](/asset-inventory/docs/asset-inventory-overview#content_types) of the
metadata that you want to retrieve. When `contentType` isn't specified, only basic
information is returned, such as asset names, the last time the assets were updated, and what
projects, folders, and organizations that they belong to.

- 
` SNAPSHOT_TIME `: Optional. The time at which you want to take a snapshot of
your assets, in [RFC 3339 format](https://www.rfc-editor.org/rfc/rfc3339#section-5.8).
The value must be no more than 35 days in the past. When `readTime` isn't specified, a
snapshot is taken at the current time.

- 


` OUTPUT_TYPE `: Use one of the following values:




- 


`"uri": "gs:// BUCKET_NAME / FILE_NAME "` to write the output
to a file, where:





- 
` BUCKET_NAME ` is the name of the Cloud Storage bucket to
write to.


- 
` FILE_NAME ` is the file to write to in your Cloud Storage
bucket.





- 


`"uriPrefix": "gs:// BUCKET_NAME / FOLDER_NAME "` to write the
output to a folder, where:





- 
` BUCKET_NAME ` is the name of the Cloud Storage bucket to
write to.


- 
` FOLDER_NAME ` is the folder to write to in your
Cloud Storage bucket. The output is split into subfolders named after
[asset types](/asset-inventory/docs/asset-types). The subfolders must not already
exist in the folder that you specify.








See the [REST reference](/asset-inventory/docs/reference/rest/v1/TopLevel/exportAssets) for all options.

### Command examples

Run one of the following commands to export your `resource` metadata as it was on
January 30, 2024 in the `my-project` project, to the file `my-file.txt` in
the Cloud Storage bucket `my-bucket`.




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-Goog-User-Project: BILLING_PROJECT_ID " \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"contentType": "RESOURCE", 
"readTime": "2024-01-30T00:00:00Z", 
"outputConfig": { 
"gcsDestination": { 
"uri": "gs://my-bucket/my-file" 
} 
} 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:exportAssets
```




#### PowerShell (Windows)



```
$cred = gcloud auth print-access-token 

$headers = @{ 
"X-Goog-User-Project" = " BILLING_PROJECT_ID " ; 
"Authorization" = "Bearer $cred" 
} 

$body = @" 
{ 
"contentType": "RESOURCE", 
"readTime": "2024-01-30T00:00:00Z", 
"outputConfig": { 
"gcsDestination": { 
"uri": "gs://my-bucket/my-file" 
} 
} 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:exportAssets" | Select-Object -Expand Content 
```



#### Example response


```
{ 
"name" : "projects/000000000000/operations/ExportAssets/RESOURCE/00000000000000000000000000000000" , 
"metadata" : { 
"@type" : "type.googleapis.com/google.cloud.asset.v1.ExportAssetsRequest" , 
"parent" : "projects/000000000000" , 
"readTime" : "2024-01-30T00:00:00Z" , 
"contentType" : "RESOURCE" , 
"outputConfig" : { 
"gcsDestination" : { 
"uri" : "gs://my-bucket/export.txt" 
} 
} 
} 
} 
```




#### C#





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.




























```
using [ Google.Api.Gax.ResourceNames ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 
using [ Google.Cloud.Asset.V1 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.html) ; 

public class ExportAssetsSample 
{ 
public ExportAssetsResponse ExportAssets ( string bucketName , string projectId ) 
{ 
string assetDumpFile = $"gs://{bucketName}/my-assets.txt" ; 
// Create the client 
[ AssetServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) client = [ AssetServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) . [ Create ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_Create) (); 
// Build the request 
[ ExportAssetsRequest ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ExportAssetsRequest.html) request = new [ ExportAssetsRequest ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ExportAssetsRequest.html)
{ 
ParentAsResourceName = [ ProjectName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) . [ FromProject ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_) ( projectId ), 
OutputConfig = new [ OutputConfig ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.OutputConfig.html)
{ 
GcsDestination = new [ GcsDestination ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.GcsDestination.html) { Uri = assetDumpFile } 
} 
}; 
// Start the long-running export operation 
var operation = client . [ ExportAssets ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_ExportAssets_Google_Cloud_Asset_V1_ExportAssetsRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// Wait for it to complete (or fail) 
operation = operation . PollUntilCompleted (); 
// Return the result 
return operation . Result ; 
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
variable to `s3nsapis.fr`.




























```
// Sample asset-quickstart exports assets to given path. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"os" 

asset "cloud.google.com/go/asset/apiv1" 
"cloud.google.com/go/asset/apiv1/assetpb" 
) 

func main () { 
ctx := context . Background () 
projectID := os . Getenv ( "GOOGLE_CLOUD_PROJECT" ) 
client , err := asset . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatal ( err ) 
} 
defer client . [ Close ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close) () 
bucketName := fmt . Sprintf ( "%s-for-assets" , projectID ) 
assetDumpFile := fmt . Sprintf ( "gs://%s/my-assets.txt" , bucketName ) 
req := & assetpb . ExportAssetsRequest { 
Parent : fmt . Sprintf ( "projects/%s" , projectID ), 
OutputConfig : & assetpb . OutputConfig { 
Destination : & assetpb . OutputConfig_GcsDestination { 
GcsDestination : & assetpb . GcsDestination { 
ObjectUri : & assetpb . GcsDestination_Uri { 
Uri : string ( assetDumpFile ), 
}, 
}, 
}, 
}, 
} 
operation , err := client . ExportAssets ( ctx , req ) 
if err != nil { 
log . Fatal ( err ) 
} 
response , err := operation . Wait ( ctx ) 
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
variable to `s3nsapis.fr`.




























```
// Imports the Google Cloud client library 

import com.google.cloud.[ServiceOptions](https://documentation.s3ns.fr/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) ; 
import com.google.cloud.asset.v1.[AssetServiceClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) ; 
import com.google.cloud.asset.v1.[ContentType](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) ; 
import com.google.cloud.asset.v1.[ExportAssetsRequest](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) ; 
import com.google.cloud.asset.v1.[ExportAssetsRequest](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html).Builder ; 
import com.google.cloud.asset.v1.[ExportAssetsResponse](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsResponse.html) ; 
import com.google.cloud.asset.v1.[GcsDestination](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.GcsDestination.html) ; 
import com.google.cloud.asset.v1.[OutputConfig](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) ; 
import com.google.cloud.asset.v1.[ProjectName](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.[TimeUnit](https://documentation.s3ns.fr/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html) ; 
import java.util.concurrent.TimeoutException ; 

public class ExportAssetsExample { 

// Use the default project Id. 
private static final [ String ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ ServiceOptions ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) . getDefaultProjectId (); 

/** 
* Export assets for a project. 
* 
* @param exportPath where the results will be exported to 
* @param contentType determines the schema for the table 
* @param assetTypes a list of asset types to export. if empty, export all. 
*/ 
public static void exportAssets ( [ String ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) exportPath , [ ContentType ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) contentType , [ String ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) [] assetTypes ) 
throws IOException , 
IllegalArgumentException , 
InterruptedException , 
ExecutionException , 
TimeoutException { 
try ( [ AssetServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [ AssetServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) . create ()) { 
[ ProjectName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) parent = [ ProjectName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) . of ( projectId ); 
[ OutputConfig ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) outputConfig = 
[ OutputConfig ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) . newBuilder () 
. setGcsDestination ( [ GcsDestination ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.GcsDestination.html) . newBuilder (). setUri ( exportPath ). build ()) 
. build (); 
Builder exportAssetsRequestBuilder = 
[ ExportAssetsRequest ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) . newBuilder () 
. setParent ( [ parent ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_parent__) . [ toString ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html#com_google_cloud_asset_v1_ProjectName_toString__) ()) 
. setContentType ( contentType ) 
. setOutputConfig ( outputConfig ); 
if ( assetTypes . length > 0 ) { 
exportAssetsRequestBuilder . addAllAssetTypes ( Arrays . asList ( assetTypes )); 
} 
[ ExportAssetsRequest ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) request = exportAssetsRequestBuilder . build (); 
[ ExportAssetsResponse ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsResponse.html) response = client . exportAssetsAsync ( request ). get ( 5 , [ TimeUnit ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html) . MINUTES ); 
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
variable to `s3nsapis.fr`.




























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const dumpFilePath = 'gs://my-bucket/my-assets.txt'; 
// const contentType = 'RESOURCE'; 

const { AssetServiceClient } = require ( '[@google-cloud/asset](https://documentation.s3ns.fr/nodejs/docs/reference/asset/latest/overview.html)' ); 
const client = new [ AssetServiceClient ](https://documentation.s3ns.fr/nodejs/docs/reference/asset/latest/overview.html) (); 

async function exportAssets () { 
const projectId = await client . getProjectId (); 
const projectResource = `projects/ ${ projectId } ` ; 

// TODO(developer): choose the dump file path 
// const dumpFilePath = 'Dump file path, e.g.: gs:// / ' 
const request = { 
parent : projectResource , 
contentType : contentType , 
outputConfig : { 
gcsDestination : { 
uri : dumpFilePath , 
}, 
}, 
}; 

// Handle the operation using the promise pattern. 
const [ operation ] = await client . exportAssets ( request ); 

// Operation#promise starts polling for the completion of the operation. 
const [ result ] = await operation . promise (); 

// Do things with with the response. 
console . log ( result ); 
} 
exportAssets (). catch ( err = > { 
throw err ; 
}); 
```





















#### PHP




























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.




























```
use Google\Cloud\Asset\V1\Client\AssetServiceClient; 
use Google\Cloud\Asset\V1\ExportAssetsRequest; 
use Google\Cloud\Asset\V1\GcsDestination; 
use Google\Cloud\Asset\V1\OutputConfig; 

/** 
* Export assets for given project to specified dump file path. 
* 
* @param string $projectId the project Id for export assets. 
* @param string $dumpFilePath the file path where the assets will be dumped to. 
* e.g.: gs://[bucket-name]/[asset-file-name]. 
*/ 
function export_assets(string $projectId, string $dumpFilePath) 
{ 
$client = new AssetServiceClient(); 

$gcsDestination = new GcsDestination(['uri' => $dumpFilePath]); 
$outputConfig = new OutputConfig(['gcs_destination' => $gcsDestination]); 
$request = (new ExportAssetsRequest()) 
->setParent("projects/$projectId") 
->setOutputConfig($outputConfig); 

$resp = $client->exportAssets($request); 

$resp->pollUntilComplete(); 

if ($resp->operationSucceeded()) { 
print('The result is dumped to $dumpFilePath successfully.' . PHP_EOL); 
} else { 
$error = $resp->getError(); 
printf('There was an error: "%s".' . PHP_EOL, $error?->getMessage()); 
// handleError($error) 
} 
} 
```





















#### Python





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.




























```
from google.cloud import asset_v1 

# TODO project_id = 'Your Google Cloud Project ID' 
# TODO dump_file_path = 'Your asset dump file path' 

client = asset_v1 . [ AssetServiceClient ](https://documentation.s3ns.fr/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html) () 
parent = f "projects/ { project_id } " 
output_config = asset_v1 . [ OutputConfig ](https://documentation.s3ns.fr/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.OutputConfig.html) () 
output_config . gcs_destination . uri = dump_file_path 
request_options = { "parent" : parent , "output_config" : output_config } 

if content_type is not None : 
request_options [ "content_type" ] = content_type 

response = client . [ export_assets ](https://documentation.s3ns.fr/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_export_assets) ( request = request_options ) 
print ( response . result ()) 
```





















#### Ruby





























To learn how to install and use the client library for Cloud Asset Inventory, see
[Cloud Asset Inventory client libraries](/asset-inventory/docs/client-libraries).







To authenticate to Cloud Asset Inventory, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.




























```
require "google/cloud/asset" 

asset_service = Google :: Cloud :: [ Asset ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html) . [ asset_service ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)
# project_id = 'YOUR_PROJECT_ID' 
formatted_parent = asset_service . [ project_path ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Paths.html) project : project_id 
# Assets dump file path, e.g.: gs://[YOUR_BUCKET]/[YOUR_ASSETS_FILE] 
# dump_file_path = 'YOUR_ASSET_DUMP_FILE_PATH' 
output_config = { 
gcs_destination : { 
uri : dump_file_path 
} 
} 

operation = asset_service . export_assets ( 
parent : formatted_parent , output_config : output_config 
) do | op | 
# Handle the error. 
raise op . results . message if op . error? 
end 

operation . wait_until_done! 
response = operation . response 
puts "Exported assets to: #{ response . output_config . gcs_destination . uri } " 
# Do things with the result 
```





















## Check the status of an export

Exports take time to complete. To check if an export is done, you can query the
operation using its operation ID.

Be aware that even if your export is done, someone might have made another
export request to the same destination as a different operation. New export
requests to the same destination can be made after a previous request has
finished, or if more than 15 minutes has elapsed. Export requests made outside
of these conditions are rejected by Cloud Asset Inventory.



### gcloud

To view the status of your export, complete the following instructions:

- 

Get the ` OPERATION_PATH `, which includes the operation
ID, from the response to your export request. The
` OPERATION_PATH ` is shown in the response to the
export, which is formatted as follows:


```
projects/ PROJECT_NUMBER /operations/ExportAssets/ CONTENT_TYPE / OPERATION_ID 
```


- 

To check the status of your export, run following command with the
` OPERATION_PATH `:


```
gcloud asset operations describe OPERATION_PATH 
```




### REST

To view the status of your export, complete the following instructions:

- 

Get the ` OPERATION_PATH `, which includes the operation
ID, from the response to your export request. The
` OPERATION_PATH ` is shown as the value of the `name`
field in the response to the export, which is formatted as follows:


```
projects/ PROJECT_NUMBER /operations/ExportAssets/ CONTENT_TYPE / OPERATION_ID 
```


- 

To check the status of your export, make the following request.



#### REST

HTTP method and URL:


```
GET https://cloudasset.googleapis.com/v1/ OPERATION_PATH 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X GET \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
https://cloudasset.googleapis.com/v1/ OPERATION_PATH 
```




#### PowerShell (Windows)



```
$cred = gcloud auth print-access-token 

$headers = @{ 
"Authorization" = "Bearer $cred" 
} 

Invoke-WebRequest ` 
-Method GET ` 
-Headers $headers ` 
-Uri "https://cloudasset.googleapis.com/v1/ OPERATION_PATH " | Select-Object -Expand Content 
```



#### Example response


```
{ 
"name" : "projects/000000000000/operations/ExportAssets/RESOURCE/00000000000000000000000000000000" , 
"metadata" : { 
"@type" : "type.googleapis.com/google.cloud.asset.v1.ExportAssetsRequest" , 
"parent" : "projects/000000000000" , 
"readTime" : "2024-01-30T00:00:00Z" , 
"contentType" : "RESOURCE" , 
"outputConfig" : { 
"gcsDestination" : { 
"uri" : "gs://my-bucket/export.txt" 
} 
} 
} 
} 
```





## View an asset snapshot

To view your asset snapshot:

- 

Go to the Cloud Storage **Buckets** page in the Cloud de Confiance console.

[Go to Buckets](https://console.cloud.s3nscloud.fr/storage/browser)

- 

Click the name of the bucket you exported your asset snapshot to, and then
click the export filename.

- 

Click **Download** to download your asset snapshot, and open it in your
text editor of choice.
# Search for resources

Source: https://berlin.devsitetest.how/asset-inventory/docs/search-resources
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












# Search for resources 















You can search for resources in a project, folder, or organization, and filter
the returned results using a query.

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

## Construct a query

Before constructing a query, it can be useful to start with a search request
that *doesn't* specify a query. Use the fields and values from the full response
to create a query using the
[search query syntax](/asset-inventory/docs/search-query-syntax), and refine it
until the results you want are returned.

Fields that can be used in a query are detailed in the
[searchAllResources reference documentation](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceSearchResult.FIELDS).

Not all resources can be searched. See
[Resource types](/asset-inventory/docs/asset-types#resource-types)
for resource names and to check if they are available to the search APIs.

## Search for your resources




#### Console



To search for resource metadata, complete the following steps.




- 


Go to the **Asset Inventory** page in the
Google Cloud Dedicated console.





[Go to Asset Inventory](https://console.cloud.berlin-build0.goog/iam-admin/asset-inventory/policies)



- 
Change to the project, folder, or organization you want to search.


- Click the **Resource** tab.

- 


To search resources, enter a query in the **Filter** field. See
[
Search query syntax](/asset-inventory/docs/search-query-syntax) to learn how to write a search query.



To make constructing queries easier, you can click the **Filter**
field to display and add the available searchable fields to your
query.






After performing a search, the resources matching the query are listed in
the **Results** table. Double-click your query to edit it, or use the
**Filter results** pane to restrict the search results by specific
criteria.



To view the query as a Google Cloud CLI command, click
**View query**.



To export the results, click **Download CSV**.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = SCOPE_PATH \ 
--query = " QUERY " \ 
--asset-types = ASSET_TYPE_1 , ASSET_TYPE_2 ,... \ 
--order-by = " ORDER_BY " \ 
--read-mask = " READ_MASK " 
```


Provide the following values:



- 


` SCOPE_PATH `: Use one of the following values:




- 
`projects/ PROJECT_ID `, where ` PROJECT_ID ` is the
ID of the project that has the assets you want to search for.


- 


`projects/ PROJECT_NUMBER `, where
` PROJECT_NUMBER ` is the number of the project that has the assets you
want to search for.












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


`folders/ FOLDER_ID `, where ` FOLDER_ID ` is the ID
of the folder that has the assets you want to search for.













How to find the ID of a Google Cloud Dedicated in Germany folder 




### Google Cloud Dedicated console



To find the ID of a Google Cloud Dedicated in Germany folder, complete the following steps:





- 


Go to the Google Cloud Dedicated console.



[
Go to the Google Cloud Dedicated console
](https://console.cloud.berlin-build0.goog/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Search for your folder name. The folder ID is shown next to the folder name.






### gcloud CLI



You can retrieve the ID of a Google Cloud Dedicated in Germany folder that's located at the organization level with the following command:



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
` ORGANIZATION_ID ` is the ID of the organization that has the assets
you want to search for.












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
` QUERY `: Optional. The query expression. If not specified or empty, all
resources are searched for in the specified scope. To learn how to write a search query, see
[Search query syntax](/asset-inventory/docs/search-query-syntax).

- 
` ASSET_TYPE_# `: Optional. A comma-separated list of
[searchable asset types](/asset-inventory/docs/asset-types).
[RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are
supported. If the regular expression doesn't match any supported asset type, an
`INVALID_ARGUMENT` error is returned. When
`--asset-types` isn't specified, all asset types are
returned.

- 
` ORDER_BY `: Optional. A comma-separated list of fields specifying the
sorting order of the results. The default order is ascending. Add `DESC` after the
field name to indicate descending order. See the
[
reference documentation](/sdk/gcloud/reference/asset/search-all-resources#--order-by) for what fields can be sorted.

- 
` READ_MASK `: Optional. A comma-separated list of fields specifying which
fields to be returned in the results. See the [
reference documentation](/sdk/gcloud/reference/asset/search-all-resources#--read-mask) for the fields that are returned by default, and other conditions to
keep in mind when specifying a read mask.



You can use the [`--format`](/sdk/gcloud/reference#--format) and
[`--flatten`](/sdk/gcloud/reference#--flatten) flags to format the
gcloud CLI output.

See the [gcloud CLI reference](/sdk/gcloud/reference/asset/search-all-resources) for all options.

### Example

Run the following command to get a list of all the Compute Engine instances in the
`my-project` project with the word `instance` followed by a `1`
in their [full resource name](/asset-inventory/docs/asset-names). The results are in
descending order by name, and because of the read mask, only the `name` and
`location` fields are returned.


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "name:instance 1" \ 
--asset-types = compute.googleapis.com/Instance \ 
--order-by = "name DESC" \ 
--read-mask = "name,location" 
```

#### Example response


```
---
location: us-central1-a
name: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-2-1
---
location: us-central1-a
name: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-1
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/ SCOPE_PATH :searchAllResources
```


Request JSON body:


```
{ 
"query" : " QUERY " , 
"assetTypes" : [ 
" ASSET_TYPE_1 " , 
" ASSET_TYPE_2 " , 
"..." 
], 
"orderBy" : " ORDER_BY " , 
"pageSize" : " PAGE_SIZE " , 
"pageToken" : " PAGE_TOKEN " , 
"readMask" : " READ_MASK " 
} 
```


Provide the following values:





- 


` SCOPE_PATH `: Use one of the following values:




- 
`projects/ PROJECT_ID `, where ` PROJECT_ID ` is the
ID of the project that has the assets you want to search for.


- 


`projects/ PROJECT_NUMBER `, where
` PROJECT_NUMBER ` is the number of the project that has the assets you
want to search for.












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


`folders/ FOLDER_ID `, where ` FOLDER_ID ` is the ID
of the folder that has the assets you want to search for.













How to find the ID of a Google Cloud Dedicated in Germany folder 




### Google Cloud Dedicated console



To find the ID of a Google Cloud Dedicated in Germany folder, complete the following steps:





- 


Go to the Google Cloud Dedicated console.



[
Go to the Google Cloud Dedicated console
](https://console.cloud.berlin-build0.goog/)




- Click the **switcher** list box in the menu bar.

- Select your organization from the list box.

- Search for your folder name. The folder ID is shown next to the folder name.






### gcloud CLI



You can retrieve the ID of a Google Cloud Dedicated in Germany folder that's located at the organization level with the following command:



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
` ORGANIZATION_ID ` is the ID of the organization that has the assets
you want to search for.












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
` QUERY `: Optional. The query expression. If not specified or empty, all
resources are searched for in the specified scope. To learn how to write a search query, see
[Search query syntax](/asset-inventory/docs/search-query-syntax).

- 
` ASSET_TYPE_# `: Optional. An array of
[searchable asset types](/asset-inventory/docs/asset-types).
[RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are
supported. If the regular expression doesn't match any supported asset type, an
`INVALID_ARGUMENT` error is returned. When `assetTypes` isn't specified, all
asset types are returned.

- 
` ORDER_BY `: Optional. A comma-separated list of fields specifying the
sorting order of the results. The default order is ascending. Add `DESC` after the
field name to indicate descending order. See the
[
reference documentation](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#body.QUERY_PARAMETERS.order_by) for what fields can be sorted.

- 
` PAGE_SIZE `: Optional. The number of results to return per page. The maximum
is 500. If the value is set to `0` or a negative value, an appropriate default is
selected. A `nextPageToken` is returned to retrieve subsequent results.

- 
` PAGE_TOKEN `: Optional. Long request responses are separated over multiple
pages. When `pageToken` isn't specified, the first page is returned. Subsequent pages
can be called by using the previous response's `nextPageToken` as the
`pageToken` value.

- 
` READ_MASK `: Optional. A comma-separated list of fields specifying which
fields to be returned in the results. See the
[reference documentation](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#body.QUERY_PARAMETERS.read_mask) for
the fields that are returned by default, and other conditions to keep in mind when specifying a
read mask.



See the [REST reference](/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources) for all options.

### Command examples

Run one of the following commands to get a list of all the Compute Engine instances in the
`my-project` project with the word `instance` followed by a `1`
in their [full resource name](/asset-inventory/docs/asset-names). The results are in
descending order by name, and only the `name` and `location` fields are
returned.




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"query": "name:instance 1", 
"assetTypes": ["compute.googleapis.com/Instance"], 
"orderBy": "name DESC", 
"readMask": "name,location" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"query": "name:instance 1", 
"assetTypes": ["compute.googleapis.com/Instance"], 
"orderBy": "name DESC", 
"readMask": "name,location" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```



#### Example response


```
{ 
"results" : [ 
{ 
"name" : "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-2-1" , 
"location" : "us-central1-a" 
}, 
{ 
"name" : "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-1" , 
"location" : "us-central1-a" 
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
using [ Google.Api.Gax ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html) ; 
using [ Google.Cloud.Asset.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.html) ; 
using System.Collections.Generic ; 
using System.Linq ; 

public class SearchAllResourcesSample 
{ 
public SearchAllResourcesResponse SearchAllResources ( string scope , string query ) 
{ 
// Create the client. 
[ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_Create) (); 

// Build the request. 
[ SearchAllResourcesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.SearchAllResourcesRequest.html) request = new [ SearchAllResourcesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.SearchAllResourcesRequest.html)
{ 
Scope = scope , 
Query = query , 
}; 

// Call the API. 
PagedEnumerable , ResourceSearchResult > response = client . [ SearchAllResources ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_SearchAllResources_Google_Cloud_Asset_V1_SearchAllResourcesRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Return the first page. 
IEnumerable byPages = response . AsRawResponses (); 
return byPages . First (); 
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
// Sample search-all-resources searches all resources within the given scope. 
package main 

import ( 
"context" 
"flag" 
"fmt" 
"log" 

asset "cloud.google.com/go/asset/apiv1" 
"cloud.google.com/go/asset/apiv1/assetpb" 
"google.golang.org/api/iterator" 
) 

func main () { 
scope := flag . String ( "scope" , "" , "Scope of the search." ) 
query := flag . String ( "query" , "" , "Query statement." ) 
flag . Parse () 
ctx := context . Background () 
client , err := asset . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatalf ( "asset.NewClient: %v" , err ) 
} 
defer client . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close) () 

req := & assetpb . SearchAllResourcesRequest { 
Scope : * scope , 
Query : * query , 
} 
it := client . SearchAllResources ( ctx , req ) 
for { 
resource , err := it . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
log . Fatal ( err ) 
} 
fmt . Println ( resource ) 
} 
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
import com.google.api.gax.rpc.[ApiException](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ; 
import com.google.api.gax.rpc.[InvalidArgumentException](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) ; 
import com.google.cloud.asset.v1.[AssetServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) ; 
import com.google.cloud.asset.v1.[AssetServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).[SearchAllResourcesPagedResponse](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.SearchAllResourcesPagedResponse.html) ; 
import com.google.cloud.asset.v1.[SearchAllResourcesRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllResourcesRequest.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 

public class SearchAllResourcesExample { 

// Searches for all the resources within the given scope. 
public static void searchAllResources ( String scope , String query ) { 
// TODO(developer): Replace these variables before running the sample. 
String [] assetTypes = {}; 
int pageSize = 0 ; 
String pageToken = "" ; 
String orderBy = "" ; 

[ SearchAllResourcesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllResourcesRequest.html) request = 
[ SearchAllResourcesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllResourcesRequest.html) . newBuilder () 
. setScope ( scope ) 
. setQuery ( query ) 
. addAllAssetTypes ( Arrays . asList ( assetTypes )) 
. setPageSize ( pageSize ) 
. setPageToken ( pageToken ) 
. setOrderBy ( orderBy ) 
. build (); 

// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the "close" method on the client to safely clean up any remaining background resources. 
try ( [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) . create ()) { 
[ SearchAllResourcesPagedResponse ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.SearchAllResourcesPagedResponse.html) response = client . searchAllResources ( request ); 
System . out . println ( "Search completed successfully:\n" + response . getPage (). getValues ()); 
} catch ( IOException e ) { 
System . out . println ( String . format ( "Failed to create client:%n%s" , e . toString ())); 
} catch ( [ InvalidArgumentException ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) e ) { 
System . out . println ( String . format ( "Invalid request:%n%s" , e . toString ())); 
} catch ( [ ApiException ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e ) { 
System . out . println ( String . format ( "Error during SearchAllResources:%n%s" , e . toString ())); 
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
// const scope = ''; 
// const query = ''; 
// const assetTypes = []; 
// const pageSize = 0; 
// const pageToken = ''; 
// const orderBy = ''; 

const util = require ( 'util' ); 
const { AssetServiceClient } = require ( '[@google-cloud/asset](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html)' ); 

const client = new [ AssetServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html) (); 
const projectId = await client . getProjectId (); 

async function searchAllResources () { 
const request = { 
scope : `projects/ ${ projectId } ` , 
query : query , 
assetTypes : assetTypes , 
pageSize : pageSize , 
pageToken : pageToken , 
orderBy : orderBy , 
}; 
const options = { 
autoPaginate : false , 
}; 

// Handle the operation using the promise pattern. 
const result = await client . searchAllResources ( request , options ); 
// Do things with with the response. 
console . log ( util . inspect ( result , { depth : null })); 
} 
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
use Google\Cloud\Asset\V1\Client\AssetServiceClient; 
use Google\Cloud\Asset\V1\SearchAllResourcesRequest; 

/** 
* @param string $scope Scope of the search 
* @param string $query (Optional) Query statement 
* @param string[] $assetTypes (Optional) Asset types to search for 
* @param int $pageSize (Optional) Size of each result page 
* @param string $pageToken (Optional) Token produced by the preceding call 
* @param string $orderBy (Optional) Fields to sort the results 
*/ 
function search_all_resources( 
string $scope, 
string $query = '', 
array $assetTypes = [], 
int $pageSize = 0, 
string $pageToken = '', 
string $orderBy = '' 
): void { 
// Instantiate a client. 
$asset = new AssetServiceClient(); 

// Run request 
$request = (new SearchAllResourcesRequest()) 
->setScope($scope) 
->setQuery($query) 
->setAssetTypes($assetTypes) 
->setPageSize($pageSize) 
->setPageToken($pageToken) 
->setOrderBy($orderBy); 
$response = $asset->searchAllResources($request); 

// Print the resource names in the first page of the result 
foreach ($response->getPage() as $resource) { 
print($resource->getName() . PHP_EOL); 
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
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import asset_v1 

# TODO scope = 'Scope of the search' 
# TODO query = 'Query statement' 
# TODO asset_types = 'List of asset types to search for' 
# TODO page_size = Size of each result page 
# TODO order_by = 'Fields to sort the results' 

client = asset_v1 . [ AssetServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html) () 
response = client . [ search_all_resources ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_search_all_resources) ( 
request = { 
"scope" : scope , 
"query" : query , 
"asset_types" : asset_types , 
"page_size" : page_size , 
"order_by" : order_by , 
} 
) 
for resource in response : 
print ( resource ) 
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

# scope = 'SCOPE_OF_THE_QUERY' 
# query = 'QUERY_STATEMENT' 
# asset_types = 'AN_ARRAY_OF_ASSET_TYPES_TO_SEARCH_FOR' 
# page_size = 'SIZE_OF_EACH_RESULT_PAGE' 
# page_token = 'TOKEN_PRODUCED_BY_THE_PRECEDING_CALL' 
# order_by = 'FIELDS_TO_SORT_THE RESULTS' 
asset_service = Google :: Cloud :: [ Asset ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html) . [ asset_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)

response = asset_service . search_all_resources ( 
scope : scope , 
query : query , 
asset_types : asset_types , 
page_size : page_size , 
page_token : page_token , 
order_by : order_by 
) 
# Do things with the response 
response . page . each do | resource | 
puts resource 
end 
```





















## Additional search examples

The following code samples show specific search queries for both
gcloud and REST to help you to construct your own searches.

### All resources in a project

The following sample shows how to search for all resources in the `my-project`
project.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--format = "table(assetType.basename(), name.basename(), name.scope(projects).segment(0):label=PROJECT_ID, labels)" 
```







#### REST

HTTP method and URL:


```
GET https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X GET \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances by description

The following sample shows how to search for Compute Engine instances in the
`my-project` project with the exact name `instance-prod`.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "description=instance-prod" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, location)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "description=instance-prod" , 
"readMask" : "name,assetType,location" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "description=instance-prod", 
"readMask": "name,assetType,location" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "description=instance-prod", 
"readMask": "name,assetType,location" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






To search for instances that have `instance-prod` in their name (such as
`instance-prod-1` and `instance-prod-2`) instead of an exact match, replace
`=instance-prod` with `:instance-prod`.

### Compute Engine instances by label

The following sample shows how to search for Compute Engine instances in the
`my-project` project with a label named `env`.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "labels.env:*" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, labels)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "labels.env:*" , 
"readMask" : "name,assetType,labels" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "labels.env:*", 
"readMask": "name,assetType,labels" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "labels.env:*", 
"readMask": "name,assetType,labels" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances by TagKey

The following sample shows how to search for Compute Engine instances in the
`my-project` project that have directly attached Tags with a
[`TagKey`](/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey).`namespacedName`
containing `env`.

To search by effective TagKeys instead, replace `tagKeys` with
`effectiveTagKeys`.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "tagKeys:env" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, tags)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "tagKeys:env" , 
"readMask" : "name,assetType,tags" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "tagKeys:env", 
"readMask": "name,assetType,tags" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "tagKeys:env", 
"readMask": "name,assetType,tags" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances by TagValue

The following sample shows how to search for Compute Engine instances in the
`my-project` project that have directly attached Tags where the
[`TagValue`](/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue).`namespacedName`
contains `prod` or `sea`, and the instance name does not contain `instance1`.

To search by effective TagValues instead, replace `tagValues` with
`effectiveTagValues`







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "tagValues:(prod OR sea) (NOT name:instance1)" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, tags)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "tagValues:(prod OR sea) (NOT name:instance1)" , 
"readMask" : "name,assetType,tags" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "tagValues:(prod OR sea) (NOT name:instance1)", 
"readMask": "name,assetType,tags" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "tagValues:(prod OR sea) (NOT name:instance1)", 
"readMask": "name,assetType,tags" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances created after a specific time

The following sample shows how to search for Compute Engine instances in the
`my-project` project that were created after 31 December, 2023.

For more information on datetime comparisons, see
[Numerical and timestamp comparison](/asset-inventory/docs/search-query-syntax#numerical_and_timestamp_comparison).







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "createTime>2023-31-12" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, location)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "createTime>2023-31-12" , 
"readMask" : "name,assetType,location" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "createTime>2023-31-12", 
"readMask": "name,assetType,location" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "createTime>2023-31-12", 
"readMask": "name,assetType,location" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances located in the US

The following sample shows how to search for Compute Engine instances in the
`my-project` project that are located in the US.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "location:us-*" \ 
--asset-types = compute.googleapis.com/Instance \ 
--format = "table(name, assetType, location)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "location:us-*" , 
"readMask" : "name,assetType,location" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "location:us-*", 
"readMask": "name,assetType,location" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "location:us-*", 
"readMask": "name,assetType,location" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### Compute Engine instances that are running

The following sample shows how to search for Compute Engine instances that are
running in the `my-project` project.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "state=RUNNING" \ 
--asset-types = compute.googleapis.com/Instance \ 
--read-mask = "name,assetType,location,versionedResources" \ 
--format = "table(name, assetType, location, versionedResources)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "compute.googleapis.com/Instance" , 
"pageSize" : 1 , 
"query" : "state=RUNNING" , 
"readMask" : "name,assetType,location,versionedResources" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "state=RUNNING", 
"readMask": "name,assetType,location,versionedResources" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "compute.googleapis.com/Instance", 
"pageSize": 1, 
"query": "state=RUNNING", 
"readMask": "name,assetType,location,versionedResources" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






### IAM deny policies

The following sample shows how to search for
[IAM deny policies](/iam/docs/deny-overview) in the `my-project`
project.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--asset-types = iam.googleapis.com/PolicyV2 \ 
--query = "name:denypolicies" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"assetTypes" : "iam.googleapis.com/PolicyV2" , 
"pageSize" : 1 , 
"query" : "name:denypolicies" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"assetTypes": "iam.googleapis.com/PolicyV2", 
"pageSize": 1, 
"query": "name:denypolicies" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"assetTypes": "iam.googleapis.com/PolicyV2", 
"pageSize": 1, 
"query": "name:denypolicies" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






To search for Compute Engine instances that aren't running, replace
`state=RUNNING` with `NOT state:running`.

### Related Google Cloud Dedicated in Germany resources

Relationship queries require access to the
[Security Command Center Premium or Enterprise tier](https://berlin.devsitetest.how/security-command-center/pricing#tier-pricing).

The following sample shows how to search for
[related](/asset-inventory/docs/asset-inventory-overview#relationships)
resources in the `my-project` project, for supported
[relationship types](/asset-inventory/docs/relationship-types). For example,
search for all Compute Engine instances that are part of
[instance groups](/compute/docs/instance-groups) that have `instance-group` in
their full resource names.







#### gcloud


```
gcloud asset search-all-resources \ 
--scope = projects/my-project \ 
--query = "relationships:instance-group" \ 
--format = "table(name, assetType, relationships)" 
```







#### REST

HTTP method and URL:


```
POST https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
```


Request JSON body:


```
{ 
"pageSize" : 1 , 
"query" : "relationships:instance-group" , 
"readMask" : "name,assetType,relationships" 
} 
```

### Command examples




#### curl (Linux, macOS, or Cloud Shell)



```
curl -X POST \ 
-H "X-HTTP-Method-Override: GET" \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"pageSize": 1, 
"query": "relationships:instance-group", 
"readMask": "name,assetType,relationships" 
}' \ 
https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources
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
"pageSize": 1, 
"query": "relationships:instance-group", 
"readMask": "name,assetType,relationships" 
} 
"@ 

Invoke-WebRequest ` 
-Method POST ` 
-Headers $headers ` 
-ContentType : "application/json; charset=utf-8" ` 
-Body $body ` 
-Uri "https://cloudasset.googleapis.com/v1/projects/my-project:searchAllResources" | Select-Object -Expand Content 
```






You can also specify the type of relationship you want to search for. For
example, to search for the `INSTANCE_TO_INSTANCEGROUP` relationship type, use
the query `relationships.INSTANCE_TO_INSTANCEGROUP`. To search for that
relationship type with a full resource name that contains `instance-group`, use
the query `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group`.
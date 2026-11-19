# Cloud Asset Inventory client libraries

Source: https://berlin.devsitetest.how/asset-inventory/docs/client-libraries
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

Reference

](https://berlin.devsitetest.how/asset-inventory/docs/asset-types)












# Cloud Asset Inventory client libraries 

















This page shows how to get started with the Cloud Client Libraries for the
Cloud Asset Inventory API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).



## Install the client library


















### C# 






If you are using Visual Studio 2017 or higher, open the NuGet package manager
window and type the following:


```
Install-Package Google.Cloud.Asset.V1
```


If you are using .NET Core command-line interface tools to install your
dependencies, run the following command:


```
dotnet add package Google.Cloud.Asset.V1
```


If you're using the [Paket](https://fsprojects.github.io/Paket)
command-line interface to install your dependencies, run the following
command:


```
paket add Google.Cloud.Asset.V1
```






For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).






























### Go 





```
go get cloud.google.com/go/asset/apiv1
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).































### Java 






If you are using [Maven](https://maven.apache.org/), add the
following code to the dependencies in your `pom.xml` file:


```
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - asset / artifactId >
version>DESIRED_VERSION_NUMBER / version >
/ dependency >
```


If you are using [Gradle](https://gradle.org/), add the following
code to your dependencies:


```
compile group : ' com . google . cloud ' , name : ' google - cloud - asset ' , version : ' DESIRED_VERSION_NUMBER ' 
```





For more information, see [Setting Up a Java Development Environment](/java/docs/setup).































### Node.js 





```
npm install @google-cloud/asset
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).






























### PHP 





```
composer require google/cloud-asset
```





For more information, see [Using PHP on Google Cloud](/php/docs).































### Python 





```
pip install --upgrade google-cloud-asset
```





For more information, see [Setting Up a Python Development Environment](/python/docs/setup).































### Ruby 





```
gem install google-cloud-asset
```





For more information, see [Setting Up a Ruby Development Environment](/ruby/docs/setup).


























## Set up authentication

To authenticate calls to Google Cloud Dedicated in Germany APIs, client libraries support
[Application Default Credentials (ADC)](/docs/authentication/application-default-credentials);
the libraries look for credentials in a set of defined locations and use those credentials
to authenticate requests to the API. With ADC, you can make
credentials available to your application in a variety of environments, such as local
development or production, without needing to modify your application code.

For production environments, the way you set up ADC depends on the service
and context. For more information, see [Set up Application Default Credentials](/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials
that are associated with your Google Account:











- 







[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```




















- 







Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








A sign-in screen appears. After you sign in, your credentials are stored in the
[
local credential file used by ADC](/docs/authentication/application-default-credentials#personal).















## Use the client library

The following example shows how to use the client library.



















### C# 




























```
using [ Google.Api.Gax ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html) ; 
using [ Google.Api.Gax.ResourceNames ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 
using [ Google.Cloud.Asset.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.html) ; 

public class ListAssetsSample 
{ 
public PagedEnumerable , Asset > ListAssets ( string projectId ) 
{ 
// Create the client. 
[ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_Create) (); 

// Build the request. 
[ ListAssetsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ListAssetsRequest.html) request = new [ ListAssetsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ListAssetsRequest.html)
{ 
ParentAsResourceName = [ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) . [ FromProject ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_) ( projectId ), 
ContentType = [ ContentType ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ContentType.html) . [ Resource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.ContentType.html#Google_Cloud_Asset_V1_ContentType_Resource) , 
}; 

// Call the API. 
PagedEnumerable , Asset > response = client . [ ListAssets ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_ListAssets_Google_Api_Gax_IResourceName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Return the result. 
return response ; 
} 
} 
```


































### Go 




























```
// Sample list-assets list assets. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"os" 

"google.golang.org/api/iterator" 

asset "cloud.google.com/go/asset/apiv1" 
"cloud.google.com/go/asset/apiv1/assetpb" 
) 

func main () { 
ctx := context . Background () 
client , err := asset . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatal ( err ) 
} 
defer client . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close) () 

projectID := os . Getenv ( "GOOGLE_CLOUD_PROJECT" ) 
assetType := "storage.googleapis.com/Bucket" 
req := & assetpb . ListAssetsRequest { 
Parent : fmt . Sprintf ( "projects/%s" , projectID ), 
AssetTypes : [] string { assetType }, 
ContentType : assetpb . [ ContentType_RESOURCE ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1/assetpb.html#cloud_google_com_go_asset_apiv1_assetpb_ContentType_CONTENT_TYPE_UNSPECIFIED_ContentType_RESOURCE_ContentType_IAM_POLICY_ContentType_ORG_POLICY_ContentType_ACCESS_POLICY_ContentType_OS_INVENTORY_ContentType_RELATIONSHIP) , 
} 

// Call ListAssets API to get an asset iterator. 
it := client . ListAssets ( ctx , req ) 

// Traverse and print the first 10 listed assets in response. 
for i := 0 ; i 10 ; i ++ { 
response , err := it . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
log . Fatal ( err ) 
} 
fmt . Println ( response ) 
} 
} 
```



































### Java 




























```
// Imports the Google Cloud client library 

public class ListAssetsExample { 

public static void listAssets () throws IOException , IllegalArgumentException { 
// The project id of the asset parent to list. 
String projectId = "YOUR_PROJECT_ID" ; 
// The asset types to list. E.g., 
// ["storage.googleapis.com/Bucket", "bigquery.googleapis.com/Table"]. 
// See full list of supported asset types at 
// https://cloud.google.com/asset-inventory/docs/supported-asset-types. 
String [] assetTypes = { "YOUR_ASSET_TYPES_TO_LIST" }; 
// The asset content type to list. E.g., ContentType.CONTENT_TYPE_UNSPECIFIED. 
// See full list of content types at 
// https://cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#contenttype 
ContentType contentType = ContentType . CONTENT_TYPE_UNSPECIFIED ; 
listAssets ( projectId , assetTypes , contentType ); 
} 

public static void listAssets ( String projectId , String [] assetTypes , ContentType contentType ) 
throws IOException , IllegalArgumentException { 
try ( AssetServiceClient client = AssetServiceClient . create ()) { 
ProjectName parent = ProjectName . of ( projectId ); 

// Build initial ListAssetsRequest without setting page token. 
ListAssetsRequest request = 
ListAssetsRequest . newBuilder () 
. setParent ( parent . toString ()) 
. addAllAssetTypes ( Arrays . asList ( assetTypes )) 
. setContentType ( contentType ) 
. build (); 

// Repeatedly call ListAssets until page token is empty. 
ListAssetsPagedResponse response = client . listAssets ( request ); 
System . out . println ( response ); 
while ( ! response . getNextPageToken (). isEmpty ()) { 
request = request . toBuilder (). setPageToken ( response . getNextPageToken ()). build (); 
response = client . listAssets ( request ); 
System . out . println ( response ); 
} 
} 
} 
} 
```



































### Node.js 




























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const assetTypes = 'storage.googleapis.com/Bucket,bigquery.googleapis.com/Table'; 
// const contentType = 'RESOURCE'; 

const util = require ( 'util' ); 
const { v1 } = require ( '[@google-cloud/asset](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html)' ); 
const client = new v1 . [ AssetServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/asset/v1.assetserviceclient.html) (); 

const projectId = await client . getProjectId (); 
const projectResource = `projects/ ${ projectId } ` ; 
// TODO(developer): Choose types of assets to list, such as 'storage.googleapis.com/Bucket': 
// const assetTypes = 'storage.googleapis.com/Bucket,bigquery.googleapis.com/Table'; 
// Or simply use empty string to list all types of assets: 
// const assetTypes = ''; 
const assetTypesList = assetTypes ? assetTypes . split ( ',' ) : []; 

async function listAssets () { 
const request = { 
parent : projectResource , 
assetTypes : assetTypesList , 
contentType : contentType , 
// (Optional) Add readTime parameter to list assets at the given time instead of current time: 
// readTime: { seconds: 1593988758 }, 
}; 

// Call cloud.assets.v1.ListAssets API. 
const result = await client . listAssets ( request ); 
// Handle the response. 
console . log ( util . inspect ( result , { depth : null })); 
} 
listAssets (); 
```


































### PHP 




























```
use Google\Cloud\Asset\V1\Client\AssetServiceClient; 
use Google\Cloud\Asset\V1\ListAssetsRequest; 

/** 
* @param string $projectId Tthe project Id for list assets. 
* @param string[] $assetTypes (Optional) Asset types to list for. 
* @param int $pageSize (Optional) Size of one result page. 
*/ 
function list_assets( 
string $projectId, 
array $assetTypes = [], 
int $pageSize = null 
): void { 
// Instantiate a client. 
$client = new AssetServiceClient(); 

// Run request 
$request = (new ListAssetsRequest()) 
->setParent("projects/$projectId") 
->setAssetTypes($assetTypes) 
->setPageSize($pageSize); 
$response = $client->listAssets($request); 

// Print the asset names in the result 
foreach ($response->getPage() as $asset) { 
print($asset->getName() . PHP_EOL); 
} 
} 
```



































### Python 




























```
from google.cloud import asset_v1 

# TODO project_id = 'Your Google Cloud Project ID' 
# TODO asset_types = 'Your asset type list, e.g., 
# ["storage.googleapis.com/Bucket","bigquery.googleapis.com/Table"]' 
# TODO page_size = 'Num of assets in one page, which must be between 1 and 
# 1000 (both inclusively)' 
# TODO content_type ="Content type to list" 

project_resource = f "projects/ { project_id } " 
client = asset_v1 . [ AssetServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html) () 

# Call ListAssets v1 to list assets. 
response = client . [ list_assets ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_list_assets) ( 
request = { 
"parent" : project_resource , 
"read_time" : None , 
"asset_types" : asset_types , 
"content_type" : content_type , 
"page_size" : page_size , 
} 
) 

for asset in response : 
print ( asset ) 
```



































### Ruby 




























```
require "google/cloud/asset" 

asset_service = Google :: Cloud :: [ Asset ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html) . [ asset_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)
# project_id = 'YOUR_PROJECT_ID' 
formatted_parent = asset_service . [ project_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Paths.html) project : project_id 

content_type = :RESOURCE 
response = asset_service . list_assets ( 
parent : formatted_parent , 
content_type : content_type 
) 

# Do things with the result 
response . page . each do | resource | 
puts resource 
end 
```





























## Additional resources

















### C# 






The following list contains links to more resources related to the
client library for C#:

- [API reference](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Asset.V1/index.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 




























### Go 






The following list contains links to more resources related to the
client library for Go:

- [API reference](https://godoc.org/cloud.google.com/go/asset/apiv1) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 





























### Java 






The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java) 





























### Node.js 






The following list contains links to more resources related to the
client library for Node.js:

- [API reference](/nodejs/docs/reference/asset/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-node/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/googleapis/google-cloud-node) 




























### PHP 






The following list contains links to more resources related to the
client library for PHP:

- [API reference](/php/docs/reference/cloud-asset/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 





























### Python 






The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/cloudasset/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 





























### Ruby 






The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://googleapis.dev/ruby/google-cloud-asset/latest/Google/Cloud/Asset.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-cloud-product` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-product%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)
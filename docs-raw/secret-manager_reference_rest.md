# Secret Manager API

Source: https://berlin.devsitetest.how/secret-manager/docs/reference/rest
Last updated: 2026-11-12

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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

Secret Manager

](https://berlin.devsitetest.how/secret-manager/docs)






- 








[

Reference

](https://berlin.devsitetest.how/secret-manager/docs/apis)












# Secret Manager API 


















Stores sensitive data such as API keys, passwords, and certificates. Provides convenience while improving security.




- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.secrets](#v1.projects.locations.secrets)

- [REST Resource: v1.projects.locations.secrets.versions](#v1.projects.locations.secrets.versions)

- [REST Resource: v1.projects.secrets](#v1.projects.secrets)

- [REST Resource: v1.projects.secrets.versions](#v1.projects.secrets.versions)





## Service: secretmanager.googleapis.com



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://secretmanager.apis-berlin-build0.goog/$discovery/rest?version=v1](https://secretmanager.apis-berlin-build0.goog/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://secretmanager.apis-berlin-build0.goog`





### Regional service endpoint



A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. global 

- `https://secretmanager.apis-berlin-build0.goog` 





## REST Resource: [v1.projects.locations](/secret-manager/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations/get)` | 

`GET /v1/{name=projects/*/locations/*}` 

Gets information about a location. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations/list)` | 

`GET /v1/{name=projects/*}/locations` 

Lists information about the supported locations for this service. | 
|






## REST Resource: [v1.projects.locations.secrets](/secret-manager/docs/reference/rest/v1/projects.locations.secrets)









| 
Methods | 
|



| 

`[addVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/addVersion)` | 

`POST /v1/{parent=projects/*/locations/*/secrets/*}:addVersion` 

Creates a new `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)` containing secret data and attaches it to an existing `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[create](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/create)` | 

`POST /v1/{parent=projects/*/locations/*}/secrets` 

Creates a new `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)` containing no `[SecretVersions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[delete](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/secrets/*}` 

Deletes a `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/get)` | 

`GET /v1/{name=projects/*/locations/*/secrets/*}` 

Gets metadata for a given `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[getIamPolicy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/getIamPolicy)` | 

`GET /v1/{resource=projects/*/locations/*/secrets/*}:getIamPolicy` 

Gets the access control policy for a secret. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/list)` | 

`GET /v1/{parent=projects/*/locations/*}/secrets` 

Lists `[Secrets](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[patch](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/patch)` | 

`PATCH /v1/{secret.name=projects/*/locations/*/secrets/*}` 

Updates metadata of an existing `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[setIamPolicy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/setIamPolicy)` | 

`POST /v1/{resource=projects/*/locations/*/secrets/*}:setIamPolicy` 

Sets the access control policy on the specified secret. | 
|

| 

`[testIamPermissions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/testIamPermissions)` | 

`POST /v1/{resource=projects/*/locations/*/secrets/*}:testIamPermissions` 

Returns permissions that a caller has for the specified secret. | 
|

| 

`[enableManagedRotation](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/enableManagedRotation)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.EnableManagedRotation` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[rotateSecret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/rotateSecret)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.RotateSecret` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.secrets.versions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions)









| 
Methods | 
|



| 

`[access](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/access)` | 

`GET /v1/{name=projects/*/locations/*/secrets/*/versions/*}:access` 

Accesses a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[destroy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/destroy)` | 

`POST /v1/{name=projects/*/locations/*/secrets/*/versions/*}:destroy` 

Destroys a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[disable](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/disable)` | 

`POST /v1/{name=projects/*/locations/*/secrets/*/versions/*}:disable` 

Disables a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[enable](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/enable)` | 

`POST /v1/{name=projects/*/locations/*/secrets/*/versions/*}:enable` 

Enables a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/get)` | 

`GET /v1/{name=projects/*/locations/*/secrets/*/versions/*}` 

Gets metadata for a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/list)` | 

`GET /v1/{parent=projects/*/locations/*/secrets/*}/versions` 

Lists `[SecretVersions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|






## REST Resource: [v1.projects.secrets](/secret-manager/docs/reference/rest/v1/projects.secrets)









| 
Methods | 
|



| 

`[addVersion](/secret-manager/docs/reference/rest/v1/projects.secrets/addVersion)` | 

`POST /v1/{parent=projects/*/secrets/*}:addVersion` 

Creates a new `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)` containing secret data and attaches it to an existing `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[create](/secret-manager/docs/reference/rest/v1/projects.secrets/create)` | 

`POST /v1/{parent=projects/*}/secrets` 

Creates a new `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)` containing no `[SecretVersions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[delete](/secret-manager/docs/reference/rest/v1/projects.secrets/delete)` | 

`DELETE /v1/{name=projects/*/secrets/*}` 

Deletes a `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.secrets/get)` | 

`GET /v1/{name=projects/*/secrets/*}` 

Gets metadata for a given `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[getIamPolicy](/secret-manager/docs/reference/rest/v1/projects.secrets/getIamPolicy)` | 

`GET /v1/{resource=projects/*/secrets/*}:getIamPolicy` 

Gets the access control policy for a secret. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.secrets/list)` | 

`GET /v1/{parent=projects/*}/secrets` 

Lists `[Secrets](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[patch](/secret-manager/docs/reference/rest/v1/projects.secrets/patch)` | 

`PATCH /v1/{secret.name=projects/*/secrets/*}` 

Updates metadata of an existing `[Secret](/secret-manager/docs/reference/rest/v1/projects.locations.secrets#Secret)`. | 
|

| 

`[setIamPolicy](/secret-manager/docs/reference/rest/v1/projects.secrets/setIamPolicy)` | 

`POST /v1/{resource=projects/*/secrets/*}:setIamPolicy` 

Sets the access control policy on the specified secret. | 
|

| 

`[testIamPermissions](/secret-manager/docs/reference/rest/v1/projects.secrets/testIamPermissions)` | 

`POST /v1/{resource=projects/*/secrets/*}:testIamPermissions` 

Returns permissions that a caller has for the specified secret. | 
|

| 

`[enableManagedRotation](/secret-manager/docs/reference/rest/v1/projects.secrets/enableManagedRotation)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.EnableManagedRotation` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[rotateSecret](/secret-manager/docs/reference/rest/v1/projects.secrets/rotateSecret)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.RotateSecret` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.secrets.versions](/secret-manager/docs/reference/rest/v1/projects.secrets.versions)









| 
Methods | 
|



| 

`[access](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/access)` | 

`GET /v1/{name=projects/*/secrets/*/versions/*}:access` 

Accesses a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[destroy](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/destroy)` | 

`POST /v1/{name=projects/*/secrets/*/versions/*}:destroy` 

Destroys a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[disable](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/disable)` | 

`POST /v1/{name=projects/*/secrets/*/versions/*}:disable` 

Disables a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[enable](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/enable)` | 

`POST /v1/{name=projects/*/secrets/*/versions/*}:enable` 

Enables a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/get)` | 

`GET /v1/{name=projects/*/secrets/*/versions/*}` 

Gets metadata for a `[SecretVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list)` | 

`GET /v1/{parent=projects/*/secrets/*}/versions` 

Lists `[SecretVersions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. | 
|
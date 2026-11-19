# Cloud Build in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/build/docs/tpc-differences
Last updated: 2026-11-10

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

Application development

](https://documentation.s3ns.fr/docs/application-development)






- 








[

Cloud Build

](https://documentation.s3ns.fr/build/docs)






- 








[

Guides

](https://documentation.s3ns.fr/build/docs/build-push-docker-image)












# Cloud Build in Cloud de Confiance versus Google Cloud 















Cloud Build is a service that executes your builds on Cloud de Confiance by S3NS, using
source code from a variety of repositories or Cloud Storage, to produce
artifacts such as Docker containers or Java archives.

This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Build.



For more detailed information about Cloud Build, see the
[Cloud Build overview](/build/docs/overview) and the rest of the
Cloud Build documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Cloud Build and
the Google Cloud version.
Some notable differences include the following:






- 
Only the
[default pool](/build/docs/overview#default_pools_and_private_pools) is
available. Private pools aren't available.


- 
You can only create builds directly, using the `CreateBuild` API or
`gcloud builds submit` from the command line. You can't use triggers.


- 
Default Cloud Storage buckets
[aren't fully supported](#observability-differences) for
storing log files.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Build feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Hardware and OS



| 
**Machine types**
| 
Only c3-standard-4 machines are available.
| 

| 
**Storage**
| 
Hyperdisk Balanced is the only available storage option for
Cloud Build. The `diskSizeGb` field is not available.
| 
|


### Integrations



| 
**Provenance**
| 
Cloud Build doesn't support provenance.
| 
|

| 
**Builders**
| 
Cloud Build builders aren't available or supported.
| 
|

| 
**Build notifications**
| 
open-source Cloud Build notifiers don't work without
modification.
| 

| 
**Image types**
| 
Docker is the only artifact type supported for uploading to Artifact Registry.
| 
|

| 
**Configuration**
| 
There is no Terraform provider for managing Cloud Build
resources.
| 
|


### Security and access control



| 
**Secrets**
| 
There is no Secret Manager integration with
Cloud Build.
| 
|

| 
**Customer Managed Encryption Keys (CMEK)**
| 
Cloud Build doesn't support CMEK.
| 
|


### Network



| 
**Service Networking**
| 
Private networking isn't available.
| 
|


### Workflows and tools



| 
**Creating builds**
| 
You can create builds using the Cloud Build API or the Google Cloud CLI
only. Triggers aren't available.
| 
|

| 
**Worker pools**
| 
Only the
[default
pool](/build/docs/overview#default_pools_and_private_pools) is available. You can't create or use private pools.
| 
|

| 
**Scheduled builds**
| 
Scheduled builds aren't available.
| 
|

| 
**Google Cloud CLI**
| 
The only gcloud CLI commands available are those for creating
and managing builds, and `get-default-service-account`.
| 
|

| 
**Cloud de Confiance console**
| 
The only pages available in the Cloud de Confiance console are the Builds page and
the Permissions page. The Dashboard, Repositories, Triggers, and Worker Pool
pages aren't available.
| 
|


### Insights and observability



| 
**Logging**
| 


Unlike in Google Cloud, build logs aren't automatically
stored in a default Cloud de Confiance by S3NS-owned Cloud Storage bucket.
Instead, if you don't specify the `LogsBucket`
option in your build config, Cloud Build uses a user-owned default
Cloud Storage bucket in the same region as your build.



Alternatively, you can specify a user-created Cloud Storage
bucket.



To use
Cloud Storage to store logs, configure your builds to use one of the
following:



- A user-created Cloud Storage bucket

- A user-owned default logs bucket in a project that's in the same region
as the build




`LEGACY_BUCKET` is not available as a value for
`DefaultLogsBucketBehavior` in the build configuration file.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Build
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)
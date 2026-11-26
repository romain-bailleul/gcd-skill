# Storage Transfer Service in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/storage-transfer/docs/tpc-differences
Last updated: 2026-11-26

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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Storage Transfer Service

](https://berlin.devsitetest.how/storage-transfer/docs/overview)












# Storage Transfer Service in Google Cloud Dedicated versus Google Cloud 















Storage Transfer Service enables seamless data movement across object and file
storage systems.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Storage Transfer Service.



For more detailed information about Storage Transfer Service, see the
[Storage Transfer Service overview](/storage-transfer/docs/overview) and the rest of the
Storage Transfer Service documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Storage Transfer Service and
the Google Cloud version.
Some notable differences include the following:






- 
Event-driven transfers and cross-bucket replication are unavailable.


- 
Agentless transfers from Amazon S3 are unavailable. Agents are
required for transfers from S3-compatible sources.


- 
Transfers from Azure Blob Storage, HDFS, and URL lists are unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Storage Transfer Service feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Integrations



| 
**Data sources**
| 


The following sources are unavailable:




- Azure Blob Storage

- Hadoop Distributed File System (HDFS)

- URL lists




Transfers from Amazon S3 and other S3-compatible storage must use transfer
agents. Agentless transfers from Amazon S3 are unavailable.

| 
|

| 
**Organization Policy Service**
| 
Custom organization policy constraints for Storage Transfer Service
resources are unavailable.
| 
|

| 
**VPC Service Controls**
| 
Standalone access levels and perimeter bridges are unavailable. Use
[ingress and
egress rules](/vpc-service-controls/docs/ingress-egress-rules) instead. See
[VPC Service Controls
differences](/vpc-service-controls/docs/tpc-differences).
| 
|


### Workflows and tools



| 
**Event-driven transfers**
| 
Event-driven transfers are unavailable.
| 
|

| 
**Cross-bucket replication**
| 
Cross-bucket replication is unavailable. Use scheduled or one-time
transfers between Cloud Storage buckets instead.
| 
|

| 
**Object filtering**
| 
Filtering source objects by wildcard (glob pattern) or by Amazon S3
storage class is unavailable.
| 
|

| 
**Agents**
| 
Transfer agents must be started with the
`--universe-domain=apis-berlin-build0.goog`
flag so that they contact Google Cloud Dedicated in Germany endpoints.
`gcloud transfer agents install` sets this flag and pulls the
agent image from the Google Cloud Dedicated in Germany registry automatically. If you start the
agent container with `docker run` or `podman run`, pass
this flag explicitly.
| 
|

| 
**Cloud Shell**
| 
Cloud Shell is not available in Google Cloud Dedicated in Germany. You must install and
configure the gcloud CLI on a local machine to access
Google Cloud Dedicated in Germany.
| 
|





## Related guides



The following information might also affect how you use and design for Storage Transfer Service
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)
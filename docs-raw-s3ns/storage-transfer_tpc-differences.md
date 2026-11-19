# Storage Transfer Service in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/storage-transfer/docs/tpc-differences
Last updated: 2026-11-19

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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Storage Transfer Service

](https://documentation.s3ns.fr/storage-transfer/docs/overview)












# Storage Transfer Service in Cloud de Confiance versus Google Cloud 















Storage Transfer Service enables seamless data movement across object and file
storage systems.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Storage Transfer Service.



For more detailed information about Storage Transfer Service, see the
[Storage Transfer Service overview](/storage-transfer/docs/overview) and the rest of the
Storage Transfer Service documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Storage Transfer Service and
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
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Storage Transfer Service feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




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
`--universe-domain=s3nsapis.fr`
flag so that they contact Cloud de Confiance by S3NS endpoints.
`gcloud transfer agents install` sets this flag and pulls the
agent image from the Cloud de Confiance by S3NS registry automatically. If you start the
agent container with `docker run` or `podman run`, pass
this flag explicitly.
| 
|

| 
**Cloud Shell**
| 
Cloud Shell is not available in Cloud de Confiance by S3NS. You must install and
configure the gcloud CLI on a local machine to access
Cloud de Confiance by S3NS.
| 
|





## Related guides



The following information might also affect how you use and design for Storage Transfer Service
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)
# Sources and sinks

Source: https://berlin.devsitetest.how/storage-transfer/docs/sources-and-sinks
Last updated: 2026-11-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage-transfer/docs/overview/tpc-differences) for more details.














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












# Sources and sinks 















Storage Transfer Service supports transfers across cloud object stores, URL lists,
and on-premises or cloud file systems. The following table details the
supported sources, destinations, and transfer types.



| 
Storage system | 
Source | 
Destination | 
Transfer type | 
Notes | 
|




| 
Cloud Storage | 
check_circle | 
check_circle | 
Agentless or agent-based | 


Cloud Storage is a valid sink for transfers from all sources.



Transfers between cloud systems are agentless. Transfers paired with
file systems are agent-based.



To configure Cloud Storage as a source or sink, refer to the
following pages:




- [Configure
access to a source: Cloud Storage](/storage-transfer/docs/source-cloud-storage)

- [Configure
access to a sink: Cloud Storage](/storage-transfer/docs/sink-cloud-storage)


| 
|

| 
Amazon Simple Storage Service (Amazon S3) | 
check_circle | 
| 
Agentless | 


Transfers to Cloud Storage only.



To configure Amazon S3, refer to
[Configure access to
a source: Amazon S3](/storage-transfer/docs/source-amazon-s3).

| 
|

| 
S3-compatible storage | 
check_circle | 
| 
Agent-based | 


Transfers to Cloud Storage only.



To configure S3-compatible storage, refer to
[Configure access to
a source: S3-compatible storage](/storage-transfer/docs/source-s3-compatible).

| 
|

| 
Azure Blob Storage, including Azure Data Lake Storage Gen2 | 
check_circle | 
| 
Agentless | 


Transfers to Cloud Storage only.



To configure Azure storage options, refer to
[Configure access
to a source: Microsoft Azure Storage](/storage-transfer/docs/source-microsoft-azure).
| 
|

| 
Publicly accessible or signed HTTP and HTTPS URLs | 
check_circle | 
| 
Agentless | 


Storage Transfer Service accepts a TSV file specifying a list of URLs to
transfer.



Transfers to Cloud Storage only.



To configure access to a URL list, refer to
[Configure access to a
source: URL list](/storage-transfer/docs/source-url-list). For formatting details, see
[Create a URL list](/storage-transfer/docs/create-url-list).

| 
|

| 
File system | 
check_circle | 
check_circle | 
Agent-based | 


Storage Transfer Service supports transfers:




- From file systems to Cloud Storage

- From Cloud Storage to file systems

- Between two file systems




See [Manage agent
pools](/storage-transfer/docs/on-prem-agent-pools) to configure agents and agent pools.



To configure a file system as a source or sink, refer to the following
pages:




- [Configure access
to a source: file system](/storage-transfer/docs/source-filesystem)

- [Configure access to
a sink: file system](/storage-transfer/docs/sink-filesystem)


| 
|

| 
Hadoop Distributed File System, HDFS | 
check_circle | 
| 
Agent-based | 


Transfers to Cloud Storage only.



To configure a transfer from an HDFS source, refer to
[Transfer from HDFS to
Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/hdfs).

| 
|
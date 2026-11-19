# Data transfer options

Source: https://documentation.s3ns.fr/storage-transfer/docs/transfer-options
Last updated: 2026-11-19

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/storage-transfer/docs/overview/tpc-differences) for more details.














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












# Data transfer options 
















Cloud de Confiance by S3NS offers multiple solutions for transferring your data to or from
Cloud Storage, or between file systems.



| 

Transfer scenario
| 

Recommendation
| 
|

| 

Transferring from another cloud storage provider
| 

Use Storage Transfer Service.
| 
|

| 

Transferring less than 1 TB from on-premises
| 

Use [`gcloud storage`](/sdk/gcloud/reference/storage).
| 
|

| 

Transferring more than 1 TB from on-premises
| 


Use
[Storage Transfer Service](/storage-transfer/docs/create-transfers).

| 
|

| 

Transferring less than 1 TB between Cloud Storage buckets
| 

Use [`gcloud storage`](/sdk/gcloud/reference/storage).
| 
|

| 

Transferring more than 1 TB between Cloud Storage buckets
| 

Use Storage Transfer Service.
| 
|


Use this guidance as a starting point. The specific details of your transfer
scenario will also help you determine which tool is more appropriate.

## Move or back up data from another cloud provider to Cloud Storage

We recommend using
[Storage Transfer Service](/storage-transfer/docs/overview) with self-hosted transfer
agents to move or back up your data from S3-compatible object storage providers
to Cloud Storage.

To get started, see
[Transfer from S3-compatible storage to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/s3-compatible).

## Move data between Cloud Storage buckets

We recommend using Storage Transfer Service to move large amounts of data between
Cloud Storage buckets.

You can alternatively use the Google Cloud CLI to transfer between
Cloud Storage buckets.

To get started, see:

- 

[Transfer between Cloud Storage buckets with Storage Transfer Service](/storage-transfer/docs/cloud-storage-to-cloud-storage).

- 

[Move data from one bucket to another](/storage/docs/moving-buckets#move-buckets-cli)
using the command line (`gcloud storage`).

## Move or back up data from on-premises storage

You can use Storage Transfer Service to move or back up on-premises data. For file
system transfers, you install a small piece of software, called an agent, on a
machine with access to your file system. The agent runs within a Docker or
Podman container and has access to your locally-mounted NFS data, and uploads
the data you specify to Cloud Storage.

To get started, see
[Manage agent pools](/storage-transfer/docs/on-prem-agent-pools).

## Transfer from Cloud to a file system

We recommend using Storage Transfer Service to move data from Cloud Storage to your
file system storage. With this method, you install a small piece of software,
called an agent, in your private data center. The agent runs within a Docker
container and has access to your locally mounted NFS data. We download the data
you specify from Cloud Storage.

To get started, see
[Requirements for file system transfers](/storage-transfer/docs/on-prem-set-up).

For small data sets you can use
[`gcloud storage rsync`](/sdk/gcloud/reference/storage/rsync). Use
`gcloud storage rsync` to transfer data between Cloud Storage and
other cloud storage providers, or between Cloud Storage and your
file system data.
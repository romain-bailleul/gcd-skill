# Cloud Asset Inventory in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/asset-inventory/docs/tpc-differences
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












# Cloud Asset Inventory in Cloud de Confiance versus Google Cloud 















Cloud Asset Inventory is a global metadata inventory service that lets you view, search,
export, monitor, and analyze your Cloud de Confiance by S3NS
asset metadata. It can be used for tasks such as discovering, managing, and
monitoring resources, and security and cost audits.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Asset Inventory.



For more detailed information about Cloud Asset Inventory, see the
[Cloud Asset Inventory overview](/asset-inventory/docs/asset-inventory-overview) and the rest of the
Cloud Asset Inventory documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Cloud Asset Inventory and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Asset Inventory feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Workflows and tools



| 
**API availability** | 



The following APIs are unavailable in
Cloud de Confiance by S3NS:





- 
Analysis APIs: These APIs are linked to Policy Analyzer,
which is unavailable in Cloud de Confiance by S3NS.
Policy Analyzer lets you find out which principals (for
example, users, service accounts, groups, and domains) have what
access to which resources based on your IAM allow
policies.


- 
Feed APIs: These APIs let you set up real-time notifications about
resource and policy changes through
[Pub/Sub](/pubsub/docs/overview).


- 
Query APIs: These APIs let you query your assets using a
[BigQuery](/bigquery/docs/introduction)
SQL-compatible dialect.



| 
|

| 
**Asset Query UI** | 

The **Asset Query** interface for building SQL queries in the
Cloud de Confiance console is unavailable.
| 
|

| 
**Asset type availability** | 

[Asset types](/asset-inventory/docs/asset-types) from products
and features that aren't available in
Cloud de Confiance by S3NS are similarly unavailable. For
a list of available products, see
[Products and Services](https://documentation.s3ns.fr/products).
| 
|


### Insights and observability



| 
**Overview** | 

The Cloud Asset Inventory **Overview** dashboard in the Cloud de Confiance console
is unavailable.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Asset Inventory
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)
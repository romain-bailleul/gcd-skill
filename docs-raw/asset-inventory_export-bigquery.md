# Export asset metadata to BigQuery

Source: https://berlin.devsitetest.how/asset-inventory/docs/export-bigquery
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












# Export asset metadata to BigQuery 















This document shows you how to export an asset snapshot from your organization,
folder, or project to a [BigQuery](/bigquery/what-is-bigquery) table,
and then [run data analysis on your inventory](#additional-examples).
BigQuery provides a SQL-like experience for users to analyze data and
produce meaningful insights without the use of custom scripts.

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

- 

[Create a BigQuery dataset](/bigquery/docs/datasets) to export to,
if you don't have one already.

## Limitations

- 

When exporting BigQuery table data, not all fields are supported by
Cloud Asset Inventory.

- 

Frequently changing asset fields such as `numBytes`, `numLongTermBytes`,
`numPhysicalBytes`, and `numRows` might be exported with a `null` value.

- 

Exporting to BigQuery clustered tables isn't supported.

- 

Appending the export output to an existing table isn't supported unless you
[export to a partitioned table](#partitioned-table). The destination table
must be empty or you must overwrite it. To overwrite it, use the
`--output-bigquery-force` flag with the gcloud CLI, or use
`"force": true` with the REST API.

- 

Google Kubernetes Engine (GKE) resource types, except for
`container.googleapis.com/Cluster` and `container.googleapis.com/NodePool`,
are not supported when exporting to
[separate tables for each resource type](#separate-tables).

- 

Cloud Asset Inventory rejects export requests if a previous request to the same
destination started less than 15 minutes ago and is still running. However, if
an export has taken longer than 15 minutes to complete, it is marked as done
and new export requests to the same destination are permitted.

- 

The `ACCESS_POLICY` content type can only be exported at the
organization level.

- 

If the table you're exporting to already exists and is in the process of being
exported to, a `400` error is returned.

## Casing

Field names use different casing conventions depending on the requested content
type and export settings:

- 

For the `RESOURCE` content type when you export assets to tables per asset
type, there are no spaces between words, and the first letter of each new word
after the first is capitalized. For example,`assetType`.

- 

For all other content types, the field name is lowercase, with spaces replaced
by underscores. For example, `asset_type`.

## BigQuery schemas used for export

Every BigQuery table is defined by a schema that describes the column
names, data types, and other information. Setting the
[content type](/asset-inventory/docs/overview#content_types) for an export
determines the schema for your table:

- 

**Resource or unspecified:** When you set the content type to `RESOURCE` or
don't specify it, and you set the `per-asset-type` flag to `false` or don't
use it, you create a BigQuery table that has the following schema.









**Resource schema**


```
[ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "discovery_document_uri" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "discovery_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "resource_url" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "parent" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "data" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "location" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "resource" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "ancestors" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
] 
```






The `resource.data` column is the resource metadata represented as a JSON
string.

When you set the content type to `RESOURCE` or don't set the content type, and
set the `per-asset-type` flag to `true`, you create
[separate tables for each asset type](#separate-tables). The schema of each
table includes RECORD-type columns mapped to the nested fields in the
`Resource.data` field of that asset type (up to the 15 nested levels that
BigQuery supports). For example tables, see
[**export-assets-examples**](https://console.cloud.berlin-build0.goog/bigquery?project=export-assets-examples)
in the Google Cloud Dedicated console.

- 

**IAM policy:** When you set the content type to `IAM_POLICY`
in the REST API or `iam-policy` in the gcloud CLI, you create a
BigQuery table that has the following schema.









**IAM policy schema**


```
[ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "role" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "members" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "expression" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "location" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "condition" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "bindings" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "service" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "log_type" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "exempted_members" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "audit_log_configs" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "audit_configs" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "etag" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "iam_policy" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "ancestors" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
] 
```






- 

**Organization policy:** When you set the content type to `ORG_POLICY` in the
REST API or `org-policy` in the gcloud CLI, you create a
BigQuery table that has the following schema.









**Organization policy schema**


```
[ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "constraint" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "etag" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "allowed_values" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "denied_values" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "all_values" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "suggested_value" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "inherit_from_parent" , 
"type" : "BOOLEAN" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "list_policy" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "enforced" , 
"type" : "BOOLEAN" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "boolean_policy" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "_present" , 
"type" : "BOOLEAN" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "restore_default" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "org_policy" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "ancestors" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
] 
```






- 

**VPCSC policy:** When you set content type to `ACCESS_POLICY` in the REST API
or `access-policy` in the gcloud CLI, you create a
BigQuery table that has the following schema.









**VPCSC policy schema**


```
[ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "parent" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "scopes" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "etag" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "access_policy" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "ip_subnetworks" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "require_screenlock" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "allowed_encryption_statuses" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "os_type" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "minimum_version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "require_verified_chrome_os" , 
"type" : "BOOLEAN" 
} 
], 
"mode" : "REPEATED" , 
"name" : "os_constraints" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "allowed_device_management_levels" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "require_admin_approval" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "require_corp_owned" , 
"type" : "BOOLEAN" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "device_policy" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "required_access_levels" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "negate" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "members" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "regions" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "network" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "vpc_ip_subnetworks" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "vpc_subnetwork" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "vpc_network_sources" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "conditions" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "combining_function" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "basic" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "expression" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "location" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "expr" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "custom" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "access_level" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "perimeter_type" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "access_levels" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "restricted_services" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "enable_restriction" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "allowed_services" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "vpc_accessible_services" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "access_level" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "resource" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "sources" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "identities" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "identity_type" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "ingress_from" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "service_name" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "method" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "permission" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "method_selectors" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "operations" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "ingress_to" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "ingress_policies" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "identities" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "identity_type" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "access_level" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "resource" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "sources" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "source_restriction" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "egress_from" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "service_name" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "method" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "permission" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "method_selectors" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "operations" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "external_resources" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "egress_to" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "egress_policies" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "status" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "access_levels" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "restricted_services" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "enable_restriction" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "allowed_services" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "vpc_accessible_services" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "access_level" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "resource" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "sources" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "identities" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "identity_type" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "ingress_from" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "service_name" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "method" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "permission" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "method_selectors" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "operations" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "ingress_to" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "ingress_policies" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "identities" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "identity_type" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "access_level" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "resource" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "sources" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "source_restriction" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "egress_from" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "REPEATED" , 
"name" : "resources" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "service_name" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "method" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "permission" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "method_selectors" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "operations" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "external_resources" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "egress_to" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "egress_policies" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "spec" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "use_explicit_dry_run_spec" , 
"type" : "BOOLEAN" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "etag" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "service_perimeter" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "authorization_type" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "authorization_direction" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "orgs" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "authorized_orgs_desc" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "ancestors" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
] 
```






- 

**OSConfig instance inventory:** When you set content type to `OS_INVENTORY`
in the REST API or `os-inventory` in the gcloud CLI, you create a
BigQuery table that has the following schema.









**OS inventory schema**


```
[ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "asset_type" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "hostname" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "long_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "short_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "kernel_version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "kernel_release" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "osconfig_agent_version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "os_info" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "key" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "origin_type" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "create_time" , 
"type" : "TIMESTAMP" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "type" , 
"type" : "INTEGER" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "yum_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "apt_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "zypper_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "googet_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "patch_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "category" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "severity" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "summary" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "zypper_patch" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "categories" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "kb_article_ids" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "support_url" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "more_info_urls" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "revision_number" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "last_deployment_change_time" , 
"type" : "TIMESTAMP" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "wua_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "caption" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "hot_fix_id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "install_time" , 
"type" : "TIMESTAMP" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "qfe_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "cos_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "display_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "display_version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "publisher" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "year" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "month" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "day" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "install_date" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "help_link" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "windows_application" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "installed_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "yum_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "apt_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "zypper_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "googet_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "patch_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "category" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "severity" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "summary" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "zypper_patch" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "title" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "name" , 
"type" : "STRING" 
} 
], 
"mode" : "REPEATED" , 
"name" : "categories" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "kb_article_ids" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "support_url" , 
"type" : "STRING" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "more_info_urls" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "revision_number" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "last_deployment_change_time" , 
"type" : "TIMESTAMP" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "wua_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "caption" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "description" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "hot_fix_id" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "install_time" , 
"type" : "TIMESTAMP" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "qfe_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "package_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "architecture" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "version" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "cos_package" , 
"type" : "RECORD" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "display_name" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "display_version" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "publisher" , 
"type" : "STRING" 
}, 
{ 
"fields" : [ 
{ 
"mode" : "NULLABLE" , 
"name" : "year" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "month" , 
"type" : "INTEGER" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "day" , 
"type" : "INTEGER" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "install_date" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "help_link" , 
"type" : "STRING" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "windows_application" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "available_package" , 
"type" : "RECORD" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "value" , 
"type" : "RECORD" 
} 
], 
"mode" : "REPEATED" , 
"name" : "items" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
], 
"mode" : "NULLABLE" , 
"name" : "os_inventory" , 
"type" : "RECORD" 
}, 
{ 
"mode" : "REPEATED" , 
"name" : "ancestors" , 
"type" : "STRING" 
}, 
{ 
"mode" : "NULLABLE" , 
"name" : "update_time" , 
"type" : "TIMESTAMP" 
} 
] 
```






## Export an asset snapshot







#### gcloud


```
gcloud asset export \ 
-- SCOPE \ 
--billing-project = BILLING_PROJECT_ID \ 
--asset-types = ASSET_TYPE_1 , ASSET_TYPE_2 ,... \ 
--content-type = CONTENT_TYPE \ 
--snapshot-time = " SNAPSHOT_TIME " \ 
--bigquery-table = projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID /tables/ TABLE_NAME \ 
--output-bigquery-force
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


`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: Optional. The project ID that the default Cloud Asset Inventory
service agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The BigQuery table that you're exporting your
metadata to. If it doesn't exist, it's created.

The `--output-bigquery-force` flag overwrites the destination table if it exists.

See the [gcloud CLI reference](/sdk/gcloud/reference/asset/export) for all options.

### Example

Run the following command to export your `resource` metadata as it was on January 30,
2024, in the `my-project` project, to the BigQuery table
`my-table`.


```
gcloud asset export \ 
--project = my-project \ 
--content-type = resource \ 
--snapshot-time = "2024-01-30" \ 
--bigquery-table = projects/my-project/datasets/my-dataset/tables/my-table \ 
--output-bigquery-force
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
"bigqueryDestination" : { 
"dataset" : "projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID " , 
"table" : " TABLE_NAME " , 
"force" : true 
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
of the folder that has the asset metadata you want to export.













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
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: The project ID that the default Cloud Asset Inventory service
agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The BigQuery table that you're exporting your
metadata to. If it doesn't exist, it's created.



The `"force": true` key-value pair overwrites the destination table if it exists.

See the [REST reference](/asset-inventory/docs/reference/rest/v1/TopLevel/exportAssets) for all options.

### Command examples

Run one of the following commands to export your `resource` metadata as it was on
January 30, 2024, in the `my-project` project, to the BigQuery table
`my-table`.




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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"force": true 
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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"force": true 
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
"bigqueryDestination" : { 
"dataset" : "projects/my-project/datasets/my-dataset" , 
"table" : "my-table" , 
"force" : true 
} 
} 
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
// Sample asset-quickstart exports assets to given bigquery table. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"os" 
"strings" 

asset "cloud.google.com/go/asset/apiv1" 
"cloud.google.com/go/asset/apiv1/assetpb" 
) 

func main () { 
ctx := context . Background () 
projectID := os . Getenv ( "GOOGLE_CLOUD_PROJECT" ) 
client , err := asset . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatalf ( "asset.NewClient: %v" , err ) 
} 
defer client . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close) () 
datasetID := strings . Replace ( fmt . Sprintf ( "%s-for-assets" , projectID ), "-" , "_" , - 1 ) 
dataset := fmt . Sprintf ( "projects/%s/datasets/%s" , projectID , datasetID ) 
req := & assetpb . ExportAssetsRequest { 
Parent : fmt . Sprintf ( "projects/%s" , projectID ), 
OutputConfig : & assetpb . OutputConfig { 
Destination : & assetpb . OutputConfig_BigqueryDestination { 
BigqueryDestination : & assetpb . BigQueryDestination { 
Dataset : dataset , 
Table : "test" , 
Force : true , 
}, 
}, 
}, 
} 
op , err := client . ExportAssets ( ctx , req ) 
if err != nil { 
log . Fatalf ( "ExportAssets: %v" , err ) 
} 
resp , err := op . Wait ( ctx ) 
if err != nil { 
log . Fatalf ( "Wait: %v" , err ) 
} 
fmt . Print ( resp ) 
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
// Imports the Google Cloud client library 

import com.google.cloud.[ServiceOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) ; 
import com.google.cloud.asset.v1.[AssetServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) ; 
import com.google.cloud.asset.v1.[BigQueryDestination](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BigQueryDestination.html) ; 
import com.google.cloud.asset.v1.[ContentType](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) ; 
import com.google.cloud.asset.v1.[ExportAssetsRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) ; 
import com.google.cloud.asset.v1.[ExportAssetsRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html).Builder ; 
import com.google.cloud.asset.v1.[ExportAssetsResponse](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsResponse.html) ; 
import com.google.cloud.asset.v1.[OutputConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) ; 
import com.google.cloud.asset.v1.[PartitionSpec](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PartitionSpec.html) ; 
import com.google.cloud.asset.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.concurrent.ExecutionException ; 

public class ExportAssetsBigqueryExample { 

// Use the default project Id. 
private static final [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ ServiceOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html) . getDefaultProjectId (); 

/** 
* Export assets to BigQuery for a project. 

* @param bigqueryDataset which dataset the results will be exported to 
* @param bigqueryTable which table the results will be exported to 
* @param contentType determines the schema for the table 
* @param assetTypes a list of asset types to export. if empty, export all. 
* @param isPerType separate BigQuery tables for each resource type 
*/ 
public static void exportBigQuery ( [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigqueryDataset , [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigqueryTable , 
[ ContentType ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) contentType , [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) [] assetTypes , boolean isPerType ) 
throws IOException , IllegalArgumentException , InterruptedException , ExecutionException { 
try ( [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [ AssetServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) . create ()) { 
[ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) parent = [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html) . of ( projectId ); 
[ OutputConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) outputConfig ; 
// Outputs to per-type BigQuery table. 
if ( isPerType ) { 
outputConfig = 
[ OutputConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) . newBuilder () 
. setBigqueryDestination ( 
[ BigQueryDestination ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BigQueryDestination.html) . newBuilder () 
. setDataset ( bigqueryDataset ) 
. setTable ( bigqueryTable ) 
. setForce ( true ) 
. setSeparateTablesPerAssetType ( true ) 
. setPartitionSpec ( 
[ PartitionSpec ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PartitionSpec.html) . newBuilder () 
. setPartitionKey ( [ PartitionSpec ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PartitionSpec.html) . PartitionKey . READ_TIME ) 
. build ()) 
. build ()) 
. build (); 
} else { 
outputConfig = 
[ OutputConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.OutputConfig.html) . newBuilder () 
. setBigqueryDestination ( 
[ BigQueryDestination ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.BigQueryDestination.html) . newBuilder () 
. setDataset ( bigqueryDataset ) 
. setTable ( bigqueryTable ) 
. setForce ( true ) 
. build ()) 
. build (); 
} 
Builder exportAssetsRequestBuilder = [ ExportAssetsRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) . newBuilder () 
. setParent ( [ parent ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_parent__) . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html#com_google_cloud_asset_v1_ProjectName_toString__) ()). setContentType ( contentType ). setOutputConfig ( outputConfig ); 
if ( assetTypes . length > 0 ) { 
exportAssetsRequestBuilder . addAllAssetTypes ( Arrays . asList ( assetTypes )); 
} 
[ ExportAssetsRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsRequest.html) request = exportAssetsRequestBuilder . build (); 
[ ExportAssetsResponse ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ExportAssetsResponse.html) response = client . exportAssetsAsync ( request ). get (); 
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
variable to `apis-berlin-build0.goog`.




























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const dataSet = 'projects/project_id/datasets/dataset_id'; 
// const table = 'mytable'; 

const { AssetServiceClient } = require ( '[@google-cloud/asset](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html)' ); 
const client = new [ AssetServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/overview.html) (); 

async function exportAssetsBigquery () { 
const projectId = await client . getProjectId (); 
const projectResource = client . [ projectPath ](https://berlin.devsitetest.how/nodejs/docs/reference/asset/latest/asset/v1.assetserviceclient.html) ( projectId ); 
const dataset = dataSet ; 

const request = { 
parent : projectResource , 
outputConfig : { 
bigqueryDestination : { 
dataset : `projects/ ${ projectId } / ${ dataset } ` , 
table : table , 
force : true , 
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

exportAssetsBigquery (); 
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

# TODO project_id = 'Your Google Cloud Project ID' 
# TODO dataset = 'Your BigQuery dataset path' 
# TODO table = 'Your BigQuery table name' 
# TODO content_type ="Content type to export" 

client = asset_v1 . [ AssetServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html) () 
parent = f "projects/ { project_id } " 
output_config = asset_v1 . [ OutputConfig ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.OutputConfig.html) () 
output_config . bigquery_destination . dataset = dataset 
output_config . bigquery_destination . table = table 
output_config . bigquery_destination . force = True 
response = client . [ export_assets ](https://berlin.devsitetest.how/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_export_assets) ( 
request = { 
"parent" : parent , 
"content_type" : content_type , 
"output_config" : output_config , 
} 
) 
print ( response . result ()) 
```





















## Export an asset snapshot to separate tables for each asset type

You can export assets to separate BigQuery tables for each asset
type with the `--per-asset-type` flag in the gcloud CLI, and
`"separateTablesPerAssetType": true` in REST API requests.

In this mode, each table's name is ` TABLE_NAME ` concatenated
with `_` (underscore) and the asset type name. Non-alphanumeric characters are
replaced with `_`.

If exporting to any table fails, the entire export operation fails and returns
the first error. Results of previous successful exports persist.

The following types are packed in a JSON string to overcome a compatibility
issue between [Proto3](https://protobuf.dev/programming-guides/proto3/#json) and
[BigQuery types](/bigquery/docs/reference/standard-sql/data-types).

- 

`google.protobuf.Timestamp`

- 

`google.protobuf.Duration`

- 

`google.protobuf.FieldMask`

- 

`google.protobuf.ListValue`

- 

`google.protobuf.Value`

- 

`google.protobuf.Struct`

- 

`google.api.*`







#### gcloud


```
gcloud asset export \ 
-- SCOPE \ 
--billing-project = BILLING_PROJECT_ID \ 
--asset-types = ASSET_TYPE_1 , ASSET_TYPE_2 ,... \ 
--content-type = CONTENT_TYPE \ 
--snapshot-time = " SNAPSHOT_TIME " \ 
--bigquery-table = projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID /tables/ TABLE_NAME \ 
--per-asset-type \ 
--output-bigquery-force
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


`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: Optional. The project ID that the default Cloud Asset Inventory
service agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The prefix for the BigQuery tables that you're
exporting your metadata to. The full names of the tables are the prefix concatenated with
`_` and the asset type.

The `--output-bigquery-force` flag overwrites the destination table if it exists.

See the [gcloud CLI reference](/sdk/gcloud/reference/asset/export) for all options.

### Example

Run the following command to export your `resource` metadata as it was on January 30,
2024, in the `my-project` project, to multiple BigQuery tables that have
`my-table` as a prefix.


```
gcloud asset export \ 
--project = my-project \ 
--content-type = resource \ 
--snapshot-time = "2024-01-30" \ 
--bigquery-table = projects/my-project/datasets/my-dataset/tables/my-table \ 
--per-asset-type \ 
--output-bigquery-force
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
"bigqueryDestination" : { 
"dataset" : "projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID " , 
"table" : " TABLE_NAME " , 
"force" : true , 
"separateTablesPerAssetType" : true 
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
of the folder that has the asset metadata you want to export.













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
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: The project ID that the default Cloud Asset Inventory service
agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The prefix for the BigQuery tables that you're
exporting your metadata to. The full names of the tables are the prefix concatenated with
`_` and the asset type.



The `"force": true` key-value pair overwrites the destination table if it exists.

### Command examples

Run one of the following commands to export your `resource` metadata as it was on
January 30, 2024, in the `my-project` project, to multiple BigQuery tables
that have `my-table` as a prefix.




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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"force": true, 
"separateTablesPerAssetType": true 
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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"force": true, 
"separateTablesPerAssetType": true 
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






## Export an asset snapshot to a time-unit column partitioned table

You can export assets in a project to
[time-unit column partitioned tables](/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables).
The exported snapshot is stored in a BigQuery table named
` TABLE_NAME ` with daily granularity and two additional
timestamp columns, `readTime` and `requestTime`, one of which you specify as the
partition column with the ` PARTITION_KEY ` value.

To export assets in a project to partitioned tables, make one of the following
requests.







#### gcloud


```
gcloud asset export \ 
-- SCOPE \ 
--billing-project = BILLING_PROJECT_ID \ 
--asset-types = ASSET_TYPE_1 , ASSET_TYPE_2 ,... \ 
--content-type = CONTENT_TYPE \ 
--snapshot-time = " SNAPSHOT_TIME " \ 
--bigquery-table = projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID /tables/ TABLE_NAME \ 
--partition-key = PARTITION_KEY \ 
--output-bigquery-force
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


`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: Optional. The project ID that the default Cloud Asset Inventory
service agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The BigQuery table that you're exporting your
metadata to. If it doesn't exist, it's created.

- 
` PARTITION_KEY `: The
[
partition key column](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#partitionkey) when exporting to BigQuery partitioned tables. Valid
values are `read-time` and `request-time`.

The `--output-bigquery-force` flag overwrites data in the corresponding partition in
the destination table. Data in different partitions remains intact.

If `--output-bigquery-force` isn't specified, exported data is appended to the
corresponding partition.

The export operation fails if a schema update or attempt to append data fails. This includes if
the destination table already exists and doesn't have the schema the export expects.

See the [gcloud CLI reference](/sdk/gcloud/reference/asset/export) for all options.

### Example

Run the following command to export your `resource` metadata as it was on January 30,
2024, in the `my-project` project, to the BigQuery table
`my-table`.


```
gcloud asset export \ 
--project = projects/my-project \ 
--content-type = resource \ 
--snapshot-time = "2024-01-30" \ 
--bigquery-table = projects/my-project/datasets/my-dataset/tables/my-table \ 
--partition-key = my-partition-key \ 
--output-bigquery-force
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
"bigqueryDestination" : { 
"dataset" : "projects/ BIGQUERY_PROJECT_ID /datasets/ DATASET_ID " , 
"table" : " TABLE_NAME " , 
"partitionSpec" : { 
"partitionKey" : " PARTITION_KEY " 
}, 
"force" : true , 
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
of the folder that has the asset metadata you want to export.













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
` ORGANIZATION_ID ` is the ID of the organization that has the asset
metadata you want to export.












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
` BILLING_PROJECT_ID `: The project ID that the default Cloud Asset Inventory service
agent is in that has permissions to manage your BigQuery datasets and tables.
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
` BIGQUERY_PROJECT_ID `: The ID of the project that the
BigQuery table is in that you want to export to.

- ` DATASET_ID `: The ID of the BigQuery dataset.

- 
` TABLE_NAME `: The BigQuery table that you're exporting your
metadata to. If it doesn't exist, it's created.

- 
` PARTITION_KEY `: The
[
partition key column](/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#partitionkey) when exporting to BigQuery partitioned tables. Valid
values are `READ_TIME` and `REQUEST_TIME`.



The `"force": true` key-value pair overwrites data in the corresponding partition in
the destination table. Data in different partitions remains intact.

If `force` isn't set or set to `false`, exported data is appended to the
corresponding partition.

The export operation fails if a schema update or attempt to append data fails. This includes if
the destination table already exists and doesn't have the schema the export expects.

### Command examples

Run one of the following commands to export your `resource` metadata as it was on
January 30, 2024, in the `my-project` project, to the BigQuery table
`my-table`.




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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"partitionSpec": { 
"partitionKey": "my-partition-key" 
}, 
"force": true, 
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
"bigqueryDestination": { 
"dataset": "projects/my-project/datasets/my-dataset", 
"table": "my-table", 
"partitionSpec": { 
"partitionKey": "my-partition-key" 
}, 
"force": true, 
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







## View an asset snapshot in BigQuery



### Console

- 

Go to the **BigQuery Studio** page in the Google Cloud Dedicated console.

[Go to BigQuery Studio](https://console.cloud.berlin-build0.goog/bigquery)

- 

To display the tables and views in the dataset, open the navigation
panel. In the **Resources** section, select your project to expand it,
and then select a dataset.

- 

From the list, select your table.

- 

Select **Details** and note the value in **Number of rows**. You might
need this value to control the starting point for your results using the
gcloud CLI or REST API.

- 

To view a sample set of data, select **Preview**.



### REST

To browse your table's data, call
[`tabledata.list`](/bigquery/docs/reference/rest/v2/tabledata/list). In the
`tableId` parameter, specify the name of your table.

You can configure the following optional parameters to control the output.

- 

`maxResults` is the maximum number of results to return.

- 

`selectedFields` is a comma-separated list of columns to return; if
unspecified, all columns are returned.

- 

`startIndex` is the zero-based index of the starting row to read.

Values are returned wrapped in a JSON object that you must parse, as described
in the [`tabledata.list`](/bigquery/docs/reference/rest/v2/tabledata/list)
reference documentation.



## Query an asset snapshot in BigQuery

After you export your snapshot to BigQuery, you can run queries on your
asset metadata.

By default, BigQuery runs *interactive*, or on-demand, query
jobs, which means that the query is executed as soon as possible. Interactive
queries count towards your
[concurrent rate limit and your daily limit](/bigquery/quota-policy).

Query results are saved to either a
[temporary or permanent table](/bigquery/docs/writing-results#temporary_and_permanent_tables).
You can choose to append or overwrite data in an existing table or to create a
new table, if none exists with the same name.

To run an interactive query that writes the output to a temporary table,
complete the following steps.



### Console

- 

Go to the **BigQuery Studio** page in the Google Cloud Dedicated console.

[Go to BigQuery Studio](https://console.cloud.berlin-build0.goog/bigquery)

- 

Select
** add Compose new query**.

- 

In the **Query editor** text area, enter a valid BigQuery
SQL query.

- 

Optional: To change the data processing location, complete the
following steps.

- 

Select **Edit** > **Query settings**.

- 

Under **Processing location**, select **Auto-select**, and then
choose your data's [location](/bigquery/docs/locations).

- 

To update the query settings, select **Save**.

- 

Select **Run**.



### REST

- 

To start a new job, call the
[`jobs.insert`](/bigquery/docs/reference/rest/v2/jobs/insert) method. In
the [job resource](/bigquery/docs/reference/rest/v2/jobs), set the
following parameters.

- 

In the `configuration` field, set the `query` field to a
[JobConfigurationQuery](/bigquery/docs/reference/rest/v2/Job#JobConfigurationQuery)
that describes the BigQuery query job.

- 

In the [`jobReference`](/bigquery/docs/reference/rest/v2/JobReference)
field, set the `location` field appropriately for your job.

- 

To poll for results, call
[`getQueryResults`](/bigquery/docs/reference/rest/v2/jobs/getQueryResults).
Poll until `jobComplete` equals `true`. You can check for errors and
warnings in the `errors` list.




## Additional SQL query examples

This section provides example SQL queries to analyze your asset metadata after
you've exported it to BigQuery. See standard SQL
[query syntax](/bigquery/docs/reference/standard-sql/query-syntax) for more
information.

### Query available columns directly

To find the quantity of each asset type, run the following query:


```
SELECT asset_type , COUNT ( * ) AS asset_count 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` 
GROUP BY asset_type 
ORDER BY asset_count DESC 
```


### Work with repeated fields

To find Identity and Access Management (IAM) policies that grant access to Gmail
accounts, run the following query. BigQuery uses `UNNEST` to
flatten
[repeated fields](/bigquery/docs/reference/standard-sql/arrays) into a table
that you can query directly:


```
SELECT name , asset_type , bindings . role 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` 
JOIN UNNEST ( iam_policy . bindings ) AS bindings 
JOIN UNNEST ( bindings . members ) AS principals 
WHERE principals like "%@gmail.com" 
```


To find an organization, folder, or project that allows creating an
Cloud SQL instance using a public IP address, run the following query.
This query is useful because allowing public IP addresses with
Cloud SQL instances can introduce vulnerabilities unless
[SSL](/sql/docs/mysql/configure-ssl-instance) or a
[proxy](/sql/docs/mysql/sql-proxy) is configured:


```
SELECT name 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` 
JOIN UNNEST ( org_policy ) AS op 
WHERE 
op . constraint = "constraints/sql.restrictPublicIp" 
AND ( op . boolean_policy IS NULL OR op . boolean_policy . enforced = FALSE ); 
```


To find an organization, folder, or project in the same VPC Service Controls
[service perimeter](/vpc-service-controls/docs/manage-service-perimeters) of a
project, run the following query:


```
SELECT service_perimeter . title , service_perimeter . status . resources 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` 
CROSS JOIN UNNEST ( service_perimeter . status . resources ) as resource 
WHERE resource = "projects/ PROJECT_ID " ; 
```


### Work with JSON strings

To find open firewall rules, run the following query. Learn more about
[JSON functions used in BigQuery](/bigquery/docs/reference/standard-sql/json_functions).


```
CREATE TEMP FUNCTION json2array ( json STRING ) 
RETURNS ARRAY 
LANGUAGE js AS """ 
return JSON.parse(json).map(x=>JSON.stringify(x)); 
""" ; 

SELECT firewall . name , firewall . resource . parent , JSON_EXTRACT ( firewall . resource . data , '$.sourceRanges' ) AS sourceRanges 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` AS firewall 
JOIN UNNEST ( json2array ( JSON_EXTRACT ( firewall . resource . data , '$.sourceRanges' ))) AS source_ranges 
WHERE asset_type = "compute.googleapis.com/Firewall" AND JSON_EXTRACT ( firewall . resource . data , '$.sourceRanges' ) IS NOT NULL AND JSON_EXTRACT_SCALAR ( source_ranges , '$' ) = "0.0.0.0/0" 
```


By
[separating tables for each resource type](/asset-inventory/docs/exporting-to-bigquery#separate_tables),
you can find open firewall rules with an easier and faster query.


```
SELECT firewall . name , firewall . resource . parent , sourceRanges 
FROM ` PROJECT_ID . DATASET_ID . STRUCTURED_INSTANCE_TABLE_NAME ` AS firewall 
JOIN UNNEST ( firewall . resource . data . sourceRanges ) AS sourceRanges 
WHERE sourceRanges = "0.0.0.0/0" ; 
```


### Join tables of different resource types

To join tables of different resource types, run the following query. The
following example shows how to find all subnetworks that have no VM attached.
First, the query finds all subnetworks. Then, from that list, it selects those
subnetworks whose `selfLink` values are not present.


```
CREATE TEMP FUNCTION json2array ( json STRING ) 
RETURNS ARRAY 
LANGUAGE js AS """ 
return JSON.parse(json).map(x=>JSON.stringify(x)); 
""" ; 

SELECT name , JSON_EXTRACT ( subnetwork . resource . data , '$.selfLink' ) AS selflink 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` AS subnetwork 
WHERE asset_type = "compute.googleapis.com/Subnetwork" AND ( JSON_EXTRACT ( subnetwork . resource . data , '$.selfLink' ) NOT IN 
( SELECT DISTINCT JSON_EXTRACT ( network_interfaces , '$.subnetwork' ) 
FROM ` PROJECT_ID . DATASET_ID . TABLE_NAME ` as instance 
JOIN UNNEST ( json2array ( JSON_EXTRACT ( instance . resource . data , '$.networkInterfaces' ))) AS network_interfaces 
WHERE asset_type = "compute.googleapis.com/Instance" 
AND JSON_EXTRACT ( instance . resource . data , '$.networkInterfaces' ) IS NOT NULL 
)) IS NULL 
```


By
[separating tables for each resource type](/asset-inventory/docs/exporting-to-bigquery#separate_tables),
you can find all subnetworks that have no VM attached with an easier and faster
query.


```
SELECT name , subnetwork . resource . data . selfLink 
FROM ` PROJECT_ID . DATASET_ID . STRUCTURED_SUBNETWORK_TABLE_NAME ` AS subnetwork 
WHERE 
( 
subnetwork . resource . data . selfLink 
NOT IN ( 
SELECT DISTINCT networkInterface . subnetwork 
FROM ` PROJECT_ID . DATASET_ID . STRUCTURED_INSTANCE_TABLE_NAME ` as instance 
JOIN 
UNNEST ( instance . resource . data . networkInterfaces ) AS networkInterface 
WHERE 
networkInterface IS NOT NULL 
) 
) IS NULL ; 
```


### Find vulnerable Managed Service for Apache Spark clusters due to [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)


```
CREATE TEMP FUNCTION vulnerable_version ( imageVersion STRING ) 
RETURNS BOOL 
LANGUAGE js AS r """ 
const version_regexp = /(? \d+)(?:\.)(? \d+)(?:\.)?(? \d+)?/g; 
let match = version_regexp.exec(imageVersion); 
if(match.groups.major 
return true; 
} 
if (match.groups.major == 1){ 
if (match.groups.minor 
return true; 
} 
if(match.groups.minor == 3 && match.groups.sub 
return true; 
} 
if(match.groups.minor == 4 && match.groups.sub 
return true; 
} 
if(match.groups.minor == 5 && match.groups.sub 
return true; 
} 
} 
if (match.groups.major == 2 && match.groups.minor == 0 && match.groups.sub 
return true; 
} 
return false; 
""" ; 

SELECT 
c . name , 
c . resource . data . projectId AS project_id , 
c . resource . data . clusterName AS cluster_name , 
c . resource . data . config . softwareConfig . imageVersion AS image_version , 
c . resource . data . status . state AS cluster_state , 
vulnerable_version ( c . resource . data . config . softwareConfig . imageVersion ) AS is_vulnerable 
FROM 
` PROJECT_ID . DATASET_ID . TABLE_NAME_PREFIX _dataproc_googleapis_com_Cluster ` c 
INNER JOIN ` PROJECT_ID . DATASET_ID . TABLE_NAME_PREFIX _cloudresourcemanager_googleapis_com_Project ` p 
ON p . resource . data . projectId = c . resource . data . projectId 
WHERE 
c . resource . data . config . softwareConfig . imageVersion IS NOT NULL 
AND c . resource . data . status . state = "RUNNING" 
AND p . resource . data . lifecycleState = "ACTIVE" ; 
```
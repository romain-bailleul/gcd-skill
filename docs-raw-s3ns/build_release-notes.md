# Cloud Build release notes

Source: https://documentation.s3ns.fr/build/docs/release-notes
Last updated: 2026-11-13

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/build/docs/tpc-differences) for more details.














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

Resources

](https://documentation.s3ns.fr/build/docs/resources)












# Cloud Build release notes 


















This page documents production updates to Cloud Build. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/cloudbuild-release-notes.xml) directly.









## November 16, 2026


Announcement 


Cloud Build is now available in Cloud de Confiance. For more information,
see
[Cloud Build differences in Cloud de Confiance versus Google Cloud](/build/docs/tpc-differences).



## March 04, 2025


Change 


Cloud Build is now available in the `northamerica-south1` region.

For more information, see [Cloud Build locations](/build/docs/locations).



## January 21, 2025


Feature 


You can now map specific build log fields to log entry fields when the build log is sent to Cloud Logging. For more information, see [Map build log fields to log entry fields](/build/docs/securing-builds/store-manage-build-logs#config-structured-logs).



## January 17, 2025


Feature 


You can now use Cloud Build to push Go modules to Artifact Registry. For more information, see [Build and test Go applications](/build/docs/building/build-go).



## September 23, 2024


Change 


Cloud Build is now available in the africa-south1 region.

For more information, see [Cloud Build locations](/build/docs/locations).



## August 19, 2024


Feature 


Cloud Build support for [custom organization policies](/resource-manager/docs/organization-policy/creating-managing-custom-constraints) is now [generally available](https://documentation.s3ns.fr/products/#product-launch-stages).

Custom organization policies let you define constraints for programmatic, fine-grained control over your organization's resources. You can set these policies at the organization, folder, or project level.

To learn more, see [Manage Cloud Build resources with custom constraints](/build/docs/custom-constraints).



## July 09, 2024


Feature 


Cloud Build users can connect to Bitbucket Cloud and Bitbucket Data Center hosts and add repositories with the [Terraform provider for Google Cloud](/build/docs/terraform).

To learn more, see [Connect to a Bitbucket Cloud host](/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#terraform) and [Connect to a Bitbucket Data Center host](/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen#terraform).



## July 02, 2024


Announcement 


Cloud Build is introducing new organization policy constraints.

The default behavior for how Cloud Build uses service accounts in new projects was changed to improve the security posture of our customers going forward. Organizations can opt out of these changes using new [organization policy boolean constraints](/build/docs/cloud-build-service-account-updates#disable-sa).

To learn more about these changes, see [Cloud Build Service Account Change](/build/docs/cloud-build-service-account-updates).



## June 25, 2024


Feature 


Cloud Build support for [Supply-chain Levels for Software Artifacts (SLSA) version 1.0](https://slsa.dev/spec/v1.0/) compliant provenance is now [generally available](https://documentation.s3ns.fr/products/#product-launch-stages) to help you safeguard your automated build pipelines.

Build provenance is verifiable metadata that you can use to audit builds. Cloud Build can generate provenance aligned with the SLSA v1.0 spec when you use the option `requestedVerifyOption` with triggered builds.

Learn how to use [build provenance in Cloud Build](/build/docs/securing-builds/generate-validate-build-provenance).
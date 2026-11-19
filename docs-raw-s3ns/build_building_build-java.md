# Build and test Java applications

Source: https://documentation.s3ns.fr/build/docs/building/build-java
Last updated: 2026-11-10

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

Guides

](https://documentation.s3ns.fr/build/docs/build-push-docker-image)












# Build and test Java applications 














This page explains how to use Cloud Build to build and test
Java-based applications, store built artifacts in a Maven repository in
Artifact Registry, and generate build provenance information.

## Before you begin

- Be familiar with creating Java-based applications.

- Be familiar with [Maven](https://maven.apache.org/maven-features.html) 

- Have your Java project ready.

- Be familiar with [how to write a Cloud Build configuration file](/build/docs/build-config).

- Have a Maven repository in Artifact Registry. If you do not have one, [create a new repository](/artifact-registry/docs/repositories/create-repos).

- To run the `gcloud` commands in this page, install the
[Google Cloud CLI](/sdk).

## Using the `maven` image

You can configure Cloud Build to build Java applications using the
[`maven` image](https://hub.docker.com/_/maven) from Docker Hub.

To execute your tasks in the `maven` image, add a step to your build config with the following fields:

- `name`: Set the value of this field to `maven` or `maven: `, where the
tag represents the version. If you don't specify the image tag, Cloud Build
uses the `latest` image by default.

- `entrypoint`: Setting this field overrides the default entry point of the
image referenced in `name`. Set the value of this field to `mvn` to invoke
`mvn` as the entrypoint of the build step and run `mvn` commands.

- `args`: The `args` field of a build step takes a list of arguments and
passes them to the image referenced by the `name` field.

The following build step specifies the `entrypoint` for the `maven` image
tagged as `3.3-jdk-8` and prints the build tool version:


```
steps : 
- name : maven : 3.3 - jdk - 8 
entrypoint : mvn 
args : [ ' -- version ' ] 
```


## Configuring `Java` builds

- 

In your project root directory, create a build config file named
`cloudbuild.yaml`.

- 

**Run tests**: `maven` provides `maven test`, which downloads dependencies, builds the applications, and runs any tests specified in your source code. The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field.

In your build config file, add `test` to the `args` field to invoke `test`
within `maven`:


```
steps : 
- name : maven : 3.3 - jdk - 8 
entrypoint : mvn 
args : [ ' test ' ] 
```


- 

**Package application**: To package your application into a JAR file
for your `maven` image, specify the `package` command in the `args` field.
The `package` command builds a JAR file in `/workspace/target/`.

The following build step packages your Java application:


```
steps : 
- name : maven : 3.3 - jdk - 8 
entrypoint : mvn 
args : [ ' package ',' - Dmaven . test . skip = true ' ] 
```


- 

**Upload to Artifact Registry**:

In your build config file, use the `mavenArtifacts` field to specify your
application path and your Maven repository in Artifact Registry:


```
artifacts : 
mavenArtifacts : 
- repository : ' https : // location -maven.pkg.dev/ project-id / repository-name ' 
path : ' app - path ' 
artifactId : ' build - artifact ' 
groupId : ' group - id ' 
version : ' version ' 
```


Replace the following values:

- location : the [location](/artifact-registry/docs/repo-locations) for your repository in Artifact Registry.

- project-id : the ID of the Cloud de Confiance by S3NS project that contains your Artifact Registry repository.

- repository-name : the name of your Maven repository in Artifact Registry.

- app-path : the path to your packaged application.

- build-artifact : the name of your package file created from your build step.

- group-id : uniquely identifies your project across all Maven projects, in the format `com.mycompany.app`. For more information, see the [Maven guide to naming conventions](https://maven.apache.org/guides/mini/guide-naming-conventions.html).

- version : the version number for your application, [formatted](https://maven.apache.org/guides/mini/guide-naming-conventions.html) in numbers and dots like `1.0.1`.

- 

**Optional: Enable provenance generation**

Cloud Build can generate verifiable
[Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) build
provenance metadata to help secure your continuous integration pipeline.

To enable provenance generation, add
[`requestedVerifyOption: VERIFIED`](/build/docs/build-config-file-schema#options)
to the `options` section in your config file.

- 

**Start your build**: [manually](/build/docs/running-builds/start-build-manually) or
[using build triggers](/build/docs/automating-builds/create-manage-triggers).

Once your build completes, you can [view repository details](/artifact-registry/docs/repositories/list-repos)
in Artifact Registry.

You can also [view build provenance metadata](/build/docs/securing-builds/generate-validate-build-provenance#view) and [validate provenance](/build/docs/securing-builds/generate-validate-build-provenance#validate_provenance).

## What's next

- Learn how to [view build results](/build/docs/view-build-results).

- Learn how to [safeguard builds](/software-supply-chain-security/docs/safeguard-builds).

- Learn how to [perform blue/green deployments on Compute Engine](/build/docs/deploying-builds/deploy-compute-engine).

- Learn how to [build and containerize Java applications](/build/docs/building/build-containerize-java).

- Learn how to [deploy an application on Cloud Run](/build/docs/deploying-builds/deploy-cloud-run).

- Learn how to [deploy an application on GKE](/build/docs/deploying-builds/deploy-gke).

- Learn how to [troubleshoot build errors](/build/docs/troubleshooting).
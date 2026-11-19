# Overview of Cloud Build

Source: https://documentation.s3ns.fr/build/docs/overview
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












# Overview of Cloud Build 














Cloud Build is a service that executes your builds on Cloud de Confiance by S3NS.

Cloud Build can import source code from a variety of repositories or
Cloud Storage, execute a build to your specifications, and produce
artifacts such as Docker containers.

## Build configuration and build steps

You can write a [build config](/build/docs/build-config) to provide
instructions to Cloud Build on what tasks to perform. You can
configure builds to fetch dependencies, run unit tests, static analyses, and
integration tests, and create artifacts with build tools such as docker, gradle,
maven, bazel, and gulp.

Cloud Build executes your build as a series of build steps, where each
build step is run in a Docker container. Executing build steps is analogous to
executing commands in a script.

You can either use the build steps provided by Cloud Build and the
Cloud Build community, or write your own custom build steps:

- **Custom build steps**: You can [
create your own build steps](/build/docs/create-custom-build-steps) for use in your builds.

Each build step is run with its container attached to a local Docker network
named `cloudbuild`. This allows build steps to communicate with each other and
share data. For more information on the `cloudbuild` network, see
[Cloud Build network](/build/docs/build-config-file-schema#network).

You can use standard [Docker Hub](https://hub.docker.com/) images in
Cloud Build, such as [Ubuntu](https://hub.docker.com/_/ubuntu/) and
[Gradle](https://hub.docker.com/_/gradle/).

## Starting builds

You can [manually start builds](/build/docs/running-builds/start-build-manually)
in Cloud Build using the Google Cloud CLI or the
[Cloud Build API](/build/docs/api/reference/rest/v1/projects.builds/create).

## Viewing build results

You can view your build results using the gcloud CLI, the
[Cloud Build
API](/build/docs/api/reference/rest/v1/projects.builds/list) or use the
**Build History** page in the Cloud Build section in
Cloud de Confiance console, which displays details and logs for every build
Cloud Build executes. For instructions see [Viewing Build
Results](/build/docs/view-build-results).

## How builds work

The following steps describe, in general, the lifecycle of a
Cloud Build build:

- Prepare your application code and any needed assets.

- Create a build config file in YAML or JSON format, which contains
instructions for Cloud Build.

- Submit the build to Cloud Build.

- Cloud Build executes your build based on the build config you
provided.

- If applicable, any built artifacts are pushed to [Artifact Registry](/artifact-registry/docs).

### Docker

Cloud Build uses [Docker](https://docker.com/) 
to execute builds. For each build step, Cloud Build executes a Docker container
as an instance of `docker run`. Currently, Cloud Build is running
Docker engine version 20.10.24.

## Cloud Build interfaces

You can use Cloud Build with the Cloud de Confiance console, `gcloud`
command-line tool, or Cloud Build's REST API.

In the Cloud de Confiance console, you can [view the Cloud Build build
results in the **Build History** page](/build/docs/view-build-results).

You can use the gcloud CLI to [create and manage
builds](/sdk/gcloud/reference/builds). You can run commands to perform tasks
such as [submitting a build](/sdk/gcloud/reference/builds/submit),
[listing builds](/sdk/gcloud/reference/builds/list), and [canceling a
build](/sdk/gcloud/reference/builds/cancel).

You can request builds using the [Cloud Build REST
API](/build/docs/api/reference/rest).

As with other Cloud Platform APIs, you must authorize
access using [OAuth2](/docs/authentication). After you have authorized access,
you can then use the API to start new builds, view build status and details,
list builds per project, and cancel builds that are currently in process.

For more information, see the
[API documentation](/build/docs/api/reference/rest).

## Default pools and private pools

By default, when you run a build on Cloud Build, the build runs in a
secure, hosted environment with access to the public internet. Each build runs on
its own **worker** and is isolated from other workloads. You can customize your
build in multiple ways including increasing the size of the machine type or
allocating more disk space. The default pool has limits on how much you
can customize the environment, particularly around private network access.

## Build security

Cloud Build provides several features to secure your builds including:


- 


**Automated Builds**



An automated build or scripted build defines all build steps in build script
or build configuration, including steps to retrieve source code and steps to
build the code. The only manual command, if any, is the command to run the
build. Cloud Build uses a
[build config](/build/docs/build-config) file to provide build
steps to Cloud Build.



Automated builds provide consistency in the build steps. However, it's also
important to run builds in a consistent, trusted environment.



Although local builds can be useful for debugging purposes, releasing
software from local builds can introduce a lot of security concerns,
inconsistencies and inefficiencies into the build process.




- Allowing local builds provides a way for an attacker with malicious
intent to modify the build process.

- Inconsistencies in developer local environments and developer practices
make it difficult to reproduce builds and diagnose build issues.




In the [requirements](https://slsa.dev/spec/v0.1/requirements)
for the [SLSA](https://slsa.dev) framework, automated builds are a
requirement for SLSA level 1, and using a build service instead of developer
environments for builds is a requirement for SLSA level 2.




- 


**Ephemeral build environment**



Ephemeral environments are temporary environments that are meant to last for
a single build invocation. After the build, the environment is wiped or
deleted. Ephemeral builds ensure that the build service and build steps run in
an ephemeral environment, such as a container or virtual machine (VM). Instead of reusing an
existing build environment, the build service provisions a new environment for
each build and then destroys it after the build process is complete.



Ephemeral environments ensure clean builds since there are no residual files
or environment settings from previous builds that can interfere with the build
process. A non-ephemeral environment provides an opportunity for attackers to
inject malicious files and content. An ephemeral environment also reduces
maintenance overhead and reduces inconsistencies in the build
environment.



[Cloud Build](/build/docs/overview) sets up a new VM
environment for every build and destroys it after the build.






To learn how you can use Cloud Build with other Cloud de Confiance products
and features to safeguard your software supply chain, see
[Software supply chain security](/software-supply-chain-security/docs/overview).

## What's next

- Learn about [Cloud Build differences in Cloud de Confiance versus Google Cloud](/build/docs/tpc-differences).

- Read the [Docker quickstart](/build/docs/quickstart-docker) to
learn how to use Cloud Build to build Docker images.

- Learn how to [build, test, and deploy
artifacts](/build/docs/configuring-builds/build-test-deploy-artifacts)
in Cloud Build.

- Read our resources about [DevOps](https://documentation.s3ns.fr/devops/) and
explore the [DevOps Research and Assessment](https://dora.dev/) research
program.
# Build and test Node.js applications

Source: https://documentation.s3ns.fr/build/docs/building/build-nodejs
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












# Build and test Node.js applications 














This page explains how to use Cloud Build to build and test `Node.js`
applications, store built artifacts in an npm repository in Artifact Registry, and
generate build provenance information.

Cloud Build enables you to use any publicly available container image
to execute your tasks. The public
[`node` image from Docker Hub](https://hub.docker.com/_/node/) 
comes preinstalled with the `npm` tool. You can configure Cloud Build
to build your `Node.js` project with this tool.

## Before you begin

The instructions on this page assume that you are familiar with `Node.js`. In
addition:

- Be familiar with [npm](https://docs.npmjs.com/about-npm).

- Have your `Node.js` project handy, including `package.json` and `test.js`
files.

- Make sure your `package.json` file includes a `start` script and a `test`
script.

- Be familiar with [how to write a Cloud Build configuration file](/build/docs/build-config).

- Have an npm repository in Artifact Registry. If you don't have one, [create a new repository](/artifact-registry/docs/repositories/create-repos).

- To run the `gcloud` commands in this page, install the
[Google Cloud CLI](/sdk).

## Building with `npm`

To execute your tasks in the `node` image from Docker Hub, specify the image URL
in the `name` field in the [Cloud Build config file](/build/docs/build-config-file-schema).
Cloud Build starts the container specified in the `name`
field using the image's default entrypoint. To override the default entrypoint
and define how the build step should be run when it is invoked, add an
`entrypoint` field in your build step. The `node` image in Docker Hub comes
preinstalled with the `npm` tool. Specify the tools in the `entrypoint` field to
invoke them as the entrypoint of your build step.

In the following example build config file:

- The `name` field specifies that the `node` image from Docker Hub is used by
Cloud Build to execute your task. When you're specifying the `node`
image, you can either omit the node version to default to `:latest`, or
specify a [node version](https://hub.docker.com/_/node/) 
to use a specific version. For example, `name: node` will use the latest
version of node, and `name: node:12` will use `node:12`.

- 

The `entrypoint` field specifies that the `npm` tool is used
when the `node` image is invoked.


```
steps:
- name: 'node'
entrypoint: 'npm'
```


## Configuring `Node.js` builds

- 

In your project root directory, create a
config file named `cloudbuild.yaml`.

- 

**Install dependencies**: Before you can build your application, you must
ensure that all of your project's dependencies are installed from `npm`. You
can install dependencies using the `install` command within the `npm` build
step. The `args` field of a build step takes a list of arguments and passes
them to the image referenced by the name field. In your build config file,
add `install` to the `args` field to invoke the `install` command:


```
steps:
- name: 'node'
entrypoint: 'npm'
args: ['install']
```


- 

**Add tests**: If you've defined a `test` script in your `package.json`, you
can configure Cloud Build to run the script by adding `test` to the
`args` field:


```
steps:
- name: 'node'
entrypoint: 'npm'
args: ['install']
- name: 'node'
entrypoint: 'npm'
args: ['test']
```


- 

**Run custom commands**: If your `package.json` contains any custom commands,
you can configure Cloud Build to run that command. In the `args`
field, add `run` as the first argument followed by the name of the custom 
command. The following build config file has arguments to run a custom 
command called `build`:


```
steps:
- name: 'node'
entrypoint: 'npm'
args: ['install']
- name: 'node'
entrypoint: 'npm'
args: ['test']
- name: 'node'
entrypoint: 'npm'
args: ['run', 'build']
```


- 

**Upload to Artifact Registry**:

In your config file, add the `npmPackages` field and specify your npm
repository in Artifact Registry:


```
artifacts : 
npmPackages : 
- repository : ' https : // LOCATION -npm.pkg.dev/ PROJECT-ID / REPOSITORY_NAME ' 
packagePath : ' PACKAGE_PATH ' 
```


Replace the following values:

- LOCATION : the [location](/artifact-registry/docs/repo-locations)
for your repository in Artifact Registry.

- PROJECT_ID : the ID of the Cloud de Confiance by S3NS project that
contains your Artifact Registry repository.

- REPOSITORY_NAME : the name of your npm repository in
Artifact Registry.

- PACKAGE_PATH : the path for the local directory
containing the npm package that you want to upload to Artifact Registry. We
recommend using an absolute path. Your ` PACKAGE_PATH `
value can be `.` to use the current working directory, but the field cannot
be omitted or left empty. This directory must contain a `package.json` file.

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

## Running tests on multiple `node` versions

Sometimes it is necessary to ensure that your project works across multiple
versions of `node`. You can create and configure
[Cloud Build triggers](/build/docs/running-builds/create-manage-triggers)
such that:

- In your build config file, specify the `node` version as a
[substitution variable](/build/docs/configuring-builds/substitute-variable-values).

- Create one trigger for each version of `node` against which you want to build
your application.

- In each of the trigger settings, use the substitution variable value field to
indicate the version of the `node` for that trigger.

The following steps explain how to specify the `node` version using trigger-specific
substitution variables:

- 

In your repository root, add a build config file, which specifies the
`node`version as a substitution variable. In the following example build
config file, `$_NODE_VERSION` is a [user-defined substitution variable](/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions):


```
steps:
- name: 'node:$_NODE_VERSION'
entrypoint: 'npm'
args: ['install']
- name: 'node:$_NODE_VERSION'
entrypoint: 'npm'
args: ['test']
```


- 

For each version of `node` you want to build against, create a build trigger
using the following steps:

- 

Open the **Triggers** page in the Cloud de Confiance console:

[Open Triggers page](https://console.cloud.s3nscloud.fr/cloud-build/triggers)

- 

Select your project from the project selector drop-down menu at the top of
the page.

- 

Click **Open**.

- 

Click **Create trigger**.

On the **Create trigger** page, enter the following settings:

- 

Enter a name for your trigger.

- 

Select the repository event to start your trigger.

- 

Select the repository that contains your source code and build
config file.

- 

Specify the regex for the branch or tag name that will start your
trigger.

- 

**Configuration**: Choose the build config file you created
previously.

- 

Under **Substitution variables**, click **Add variable**.

- Under **Variable**, specify the `node` version variable you used
in your build config file, and under **Value** specify the version
of the `node`. For example, `_NODE_VERSION` and `12`.

- 

Click **Create** to save your build trigger.

You can use these triggers to build your code on the version of `node` you
specified in the trigger.

## What's next

- Learn how to [view build results](/build/docs/view-build-results).

- Learn how to [safeguard builds](/software-supply-chain-security/docs/safeguard-builds).

- Learn how to [build container images](/build/docs/building/build-containers).

- Learn how to [build Go applications](/build/docs/building/build-go).

- Learn how to [perform blue/green deployments on Compute Engine](/build/docs/deploying-builds/deploy-compute-engine).

- Learn how to [troubleshoot build errors](/build/docs/troubleshooting).
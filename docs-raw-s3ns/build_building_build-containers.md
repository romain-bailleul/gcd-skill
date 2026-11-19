# Build container images

Source: https://documentation.s3ns.fr/build/docs/building/build-containers
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












# Build container images 














This page describes how to configure Cloud Build to build and store
Docker images. If you're new to Cloud Build, read the
[quickstarts](/build/docs/quickstarts) and the [build configuration
overview](/build/docs/build-config) first.

Cloud Build provides [pre-built images](https://github.com/GoogleCloudPlatform/cloud-builders) 
that you can reference in a Cloud Build config file to execute your
tasks. These images are supported and maintained by Cloud de Confiance by S3NS. You can use
the [supported, prebuilt Docker image](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker) 
to execute Docker commands and build Docker images.

## Before you begin

The instructions on this page assume that you are familiar with Docker. In
addition:

- Have your application source code along with `Dockerfile` handy.

- Have a Docker repository for storing images in Artifact Registry, or [create a new repository](https://documentation.s3ns.fr/artifact-registry/docs/repositories/create-repos).

- If you want to use the `gcloud` commands in this page, install the [Google Cloud CLI](https://documentation.s3ns.fr/sdk).

- If you want to run the images, [install Docker](https://docs.docker.com/installation/#installation) 

- If you want to sign the images with cosign, follow the instructions in [Authorize service-to-service access](/build/docs/securing-builds/authorize-service-to-service-access)
to create a user-specified service account and grant the permissions
required to generate ID tokens.

## Build with a build config file

To build your Docker image using a build config file:

- In the same directory that contains your application source code,
create a file named `cloudbuild.yaml` or `cloudbuild.json`.

- 

In the build config file:

- Add a `name` field and specify the prebuilt Docker image. The
prebuilt image is stored at `gcr.io/cloud-builders/docker`. In the following
sample config file, the `name` field specifies that the prebuilt Docker
image is used by Cloud Build
to execute the task indicated by the `args` field.

- 

In the `args` field, add the arguments to build the image.



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'build' , '-t' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' , '.' ] 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"build" , 
"-t" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , 
"." 
] 
} 
] 
} 
```



Where:

- ` LOCATION `: the regional or multi-regional location of your Docker repository in Artifact Registry.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Docker repository in Artifact Registry.

- 

` IMAGE_NAME `: the name of your container image.

If your `Dockerfile` and source code are in different directories, add `-f`
and the path to the `Dockerfile` to the list of arguments in the `args` field:



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'build' , '-t' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' , '-f' , ' DOCKERFILE_PATH ' , '.' ] 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"build" , 
"-t" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , ' - f ' , ' DOCKERFILE_PATH ' , "." 
] 
} 
] 
} 
```



Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

- ` DOCKERFILE_PATH `: path to your `Dockerfile`.

- 

Start the build using the build config file:


```
gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY 
```


Where:

- ` CONFIG_FILE_PATH `: the path to the build config file.

- ` SOURCE_DIRECTORY `: the path or URL to the source code.

If you don't specify a ` CONFIG_FILE_PATH ` and ` SOURCE_DIRECTORY ` in the
`gcloud builds submit` command, Cloud Build assumes that the config
file and the source code are in the current working directory.

## Build with a Dockerfile

Cloud Build lets you build a Docker image using just a
`Dockerfile`. You don't require a separate build config file.

To build using a `Dockerfile`, run the following command from the directory
containing your source code and the `Dockerfile`:


```
gcloud builds submit --tag LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME 
```


Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

## Build with Google Cloud's buildpacks

Cloud Build lets you build an image without a Dockerfile or a
build config file. You can do this using
[Google Cloud's buildpacks](/docs/buildpacks/overview).

To build using buildpacks, run the following command from the directory containing
your source code:


```
gcloud builds submit --pack builder= BUILDPACK_BUILDER , \
env= ENVIRONMENT_VARIABLE , \
image= IMAGE_NAME 
```


Where:

- BUILDPACK_BUILDER : the buildpacks builder to use.
If you don't specify a builder, Cloud Build uses
[`gcr.io/buildpacks/builder`](/docs/buildpacks/builders)
by default.

- ENVIRONMENT_VARIABLE : any environment variables for your
build.

- IMAGE : the URL of the image in Artifact Registry.
The image URL must be in the format LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME .

Here are some example commands:

- 

Running a build using the default `gcr.io/buildpacks/builder` to create the
image `us-docker.pkg.dev/gcb-docs-project/containers/gke/hello-app`:


```
gcloud builds submit --pack image=us-docker.pkg.dev/gcb-docs-project/containers/gke/hello-app
```


- 

Passing multiple environment variables to your build using `^--^` as a separator.
For more information about escaping arguments, see [`gcloud topic escaping`](/sdk/gcloud/reference/topic/escaping).


```
gcloud builds submit --pack \
^--^image=gcr.io/my-project/myimage--env=GOOGLE_ENTRYPOINT='java -jar target/myjar.jar',GOOGLE_RUNTIME_VERSION='3.1.301'
```


**Configuring triggers to use buildpacks**: In addition to building using the
command line, you can configure triggers to use buildpacks to build your
image automatically. To learn more, see [Creating and managing build triggers](/build/docs/automating-builds/create-manage-triggers).

## Different ways of storing images in Artifact Registry

You can configure Cloud Build to store a built image in one of the
following ways:

- Use the `images` field to store a Docker
image in Artifact Registry after your build completes.

- Use the `artifacts.oci` field to store an OCI image in Artifact Registry
after your build completes.

- Use the `docker push` command to store a container image in Artifact Registry
as part of your build flow.

The difference between using the `images` field and the Docker `push` command is
that if you use the `images` field, the stored image will be displayed in the
build results. This includes the **Build description** page for a build in the
Cloud de Confiance console, the results of
[`Build.get()`](/build/docs/api/reference/rest/v1/projects.builds/get),
and the results of `gcloud builds list`. However, if you use the
Docker `push` command to store the built image, the image won't be displayed
in the build results.

If you want to store the image as part of your build flow and want to display the
image in the build results, use both the Docker `push` command and the `images`
field in your build config file.

### Store a container image in Artifact Registry after your build completes

- If the target repository does not exist, [create a new repository](/artifact-registry/docs/repositories/create-repos#create).

- In the same directory that contains your application source code and `Dockerfile`,
create a file named `cloudbuild.yaml` or `cloudbuild.json`.

- 

In your build config file, add a build step to build an image and then add
an `images` field specifying the built image. This stores the image in
Artifact Registry. The following snippet shows a build config to build
an image and store it in Artifact Registry:



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'build' , '-t' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' , '.' ] 
images : [ ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' ] 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"build" , 
"-t" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , 
"." 
] 
} 
], 
"images" : [ 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " 
] 
} 
```



Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

- 

Start the build using the build config file:


```
gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY 
```


Where:

- ` CONFIG_FILE_PATH ` is the path to the build config file.

- ` SOURCE_DIRECTORY ` is the path or URL to the source code.

### Store the image in Artifact Registry as part of your build flow

- 

In the same directory that contains your application source code and `Dockerfile`,
create a file named `cloudbuild.yaml` or `cloudbuild.json`.

- 

In your build config file, add a `docker` build step to build an image and
then add another `docker` build step and pass arguments to invoke the
`push` command:



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'build' , '-t' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' , '.' ] 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'push' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' ] 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"build" , 
"-t" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , 
"." 
] 
}, 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"push" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " 
] 
} 
] 
} 
```



Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

- 

Start the build using the build config file:


```
gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY 
```


Where:

- ` CONFIG_FILE_PATH ` is the path to the build config file.

- ` SOURCE_DIRECTORY ` is the path or URL to the source code.

### Store an image as part of your build flow and to display the image in the build results

- In the same directory that contains your application source code and `Dockerfile`,
create a file named `cloudbuild.yaml` or `cloudbuild.json`.

- 

In your build config file, after the step that builds the image, add a step to
invoke the Docker `push` command and then add the `images` field:



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'build' , '-t' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' , '.' ] 
- name : 'gcr.io/cloud-builders/docker' 
args : [ 'push' , ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' ] 
images : [ ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' ] 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"build" , 
"-t" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , 
"." 
] 
}, 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"push" , 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " 
] 
} 
], 
"images" : [ 
" LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " 
] 
} 
```



Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

- 

Start the build using the build config file:


```
gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY 
```


Where:

- ` CONFIG_FILE_PATH ` is the path to the build config file.

- ` SOURCE_DIRECTORY ` is the path or URL to the source code.

### Store an OCI image in Artifact Registry after your build completes

- In the same directory that contains your application source code and `Dockerfile`,
create a file named `cloudbuild.yaml` or `cloudbuild.json`.

- 

In your build config file, add
an `artifacts` field specifying the built OCI image. This configuration
stores the OCI image in Artifact Registry. The following example shows a build
config that builds an OCI image and stores it in Artifact Registry:



### YAML

```
artifacts : 
oci : 
- file : ' OCI_IMAGE_PATH ' 
registryPath : 'https:// LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY ' 
tags : [ "primary_image" ] 
```


### JSON

```
{ 
"artifacts" : { 
"oci" : [ 
{ 
"file" : " OCI_IMAGE_PATH " , 
"registryPath" : "https:// LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY " , 
"tags" : [ "primary_image" ] 
} 
] 
} 
} 
```



Where:

- OCI_IMAGE_PATH is the address of the local directory that contains
the OCI image to upload, for example, `/.pack/layout-repo/my-app`.

- LOCATION is the regional or multi-regional location for your repository.

- PROJECT_ID is your Cloud de Confiance project ID.

- REPOSITORY : is the name of your Artifact Registry repository.

## Sign container images with cosign

If you're storing images in Artifact Registry, you can add another layer of security
by using the
[cosign](https://docs.sigstore.dev/cosign/signing/overview/) tool to
create a record of which service account is used to initiate a build. Backed by
the [OpenID Connect (OIDC)](https://openid.net/connect/) standard,
auditors can use that record to verify that an image was built by a trusted
service account.

The following steps demonstrate how to use your `cloudbuild.yaml` config file
to get an identity token and sign your container image.



### YAML

```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
id : 'tag-and-push' 
script : | 
#!/bin/sh 
set -e 
docker build -t $_IMAGE . 
docker push "$_IMAGE" 
docker inspect $_IMAGE --format "$_IMAGE@{{.Id}}" >image_with_digest 
- name : 'gcr.io/cloud-builders/gcloud' 
id : 'generate-token' 
script : | 
#!/bin/sh 
set -e 
gcloud auth print-identity-token --audiences=sigstore > token 
- name : 'gcr.io/cloud-builders/docker' 
id : 'sign-image' 
script : | 
#!/bin/sh 
set -e 
docker run \ 
--network=cloudbuild \ 
--mount source=home-volume,target=/builder/home \ 
--rm \ 
-e SIGSTORE_NO_CACHE=true \ 
-e HOME=/builder/home \ 
gcr.io/projectsigstore/cosign \ 
sign --identity-token=$(cat token) $(cat image_with_digest) -y 
service_account : '$_SERVICE_ACCOUNT' 
artifacts : 
images : 
- $_IMAGE 
substitutions : 
_IMAGE : ' LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME ' 
_SERVICE_ACCOUNT_ID : ' SERVICE_ACCOUNT_ID ' 
_SERVICE_ACCOUNT : projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID} 
options : 
env : 
- '_IMAGE=$_IMAGE' 
dynamic_substitutions : true 
logging : CLOUD_LOGGING_ONLY 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"id" : "tag-and-push" , 
"script" : "#!/bin/sh set -e \ndocker build -t $_IMAGE . \ndocker push \"$_IMAGE\"" 
}, 
{ 
"name" : "gcr.io/cloud-builders/gcloud" , 
"id" : "generate-token-and-get-digest" , 
"script" : "#!/bin/sh set -e \ngcloud auth print-identity-token --audiences=sigstore > token \ngcloud container images describe \"$_IMAGE\" --format=\"value(image_summary.fully_qualified_digest)\" > image_with_digest" 
}, 
{ 
"name" : "gcr.io/projectsigstore/cosign" , 
"id" : "sign-image" , 
"script" : "#!/busybox/sh cosign sign --identity-token=$(cat token) $(cat image_with_digest) -y" , 
"env" : [ 
"SIGSTORE_NO_CACHE=true" 
] 
} 
], 
"service_account" : "$_SERVICE_ACCOUNT" , 
"artifacts" : { 
"images" : [ 
"$_IMAGE" 
] 
}, 
"substitutions" : { 
"_IMAGE" : " LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME " , 
"_SERVICE_ACCOUNT_ID" : " SERVICE_ACCOUNT_ID " , 
"_SERVICE_ACCOUNT" : "projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID}" 
}, 
"options" : { 
"env" : [ 
"_IMAGE=$_IMAGE" 
], 
"dynamic_substitutions" : true , 
"logging" : "CLOUD_LOGGING_ONLY" 
} 
} 
```


Where:



- 

` LOCATION ` is the regional or multi-regional
[location](/artifact-registry/docs/repositories/repo-locations) of the
repository where the image is stored, for example `us-east1` or `us`.

- 

` PROJECT_ID `: your Cloud de Confiance project ID.

- 

` REPOSITORY ` is the name of the repository where the image
is stored.

- 

` IMAGE_NAME ` is the image's name.

- 

` SERVICE_ACCOUNT_ID ` is the email address of the
user-specified service account you want to run your build. For example, a
service account email address looks like:
`service-account-name@project-id.s3ns.iam.gserviceaccount.com`.

To verify the signature, [install cosign](https://docs.sigstore.dev/cosign/installation/) 
on your local machine, then run the `cosign verify` command:


```
cosign verify \ 
--certificate-identity = SERVICE_ACCOUNT_ID \ 
--certificate-oidc-issuer = https://accounts.google.com \ 
IMAGE 
```


Where:

- ` SERVICE_ACCOUNT_ID ` is the email address of the
trusted service account that you expect to have been used to build the
container image.

- ` IMAGE ` is the full image name including the sha256
image digest.

## Run the Docker image

To verify that the image you built works as expected, you can run it using
Docker.

- 

Configure Docker to use your Artifact Registry credentials when interacting
with Artifact Registry. (You are only required to do this once.) Use the following command to authenticate using the [gcloud credential helper](https://documentation.s3ns.fr/artifact-registry/docs/docker/authentication#gcloud-helper).


```
gcloud auth configure-docker HOSTNAME-LIST 
```


Where HOSTNAME-LIST is a comma-separated list of repository hostnames to add to the credential helper configuration.

For example, to add the regions `us-central1` and `asia-northeast1`, run
the command:


```
gcloud auth configure-docker us-central1-docker.pkg.dev,asia-northeast1-docker.pkg.dev
```


- 

Run the Docker image that you built before:


```
docker run LOCATION -docker.pkg.dev/ PROJECT_ID / REPOSITORY / IMAGE_NAME 
```


Where:

- ` LOCATION `: the regional or multi-regional location for your repository.

- ` PROJECT_ID `: your Cloud de Confiance project ID.

- ` REPOSITORY `: the name of your Artifact Registry repository.

- ` IMAGE_NAME `: the name of your container image.

You will see an output similar to the following:


```
Hello, world! The time is Fri Feb 2 16:09:54 UTC 2018.
```


## What's next

- Learn how to [build Java applications](/build/docs/building/build-containerize-java).

- Learn how to [build Python applications](/build/docs/building/build-containerize-python).

- Learn how to [build Go applications](/build/docs/building/build-containerize-go).

- Learn how to [store build artifacts in Cloud Storage](/build/docs/building/store-build-artifacts).

- Learn how to [store build artifacts in Artifact Registry](/artifact-registry/docs/configure-cloud-build).

- Learn how to [troubleshoot build errors](/build/docs/troubleshooting).
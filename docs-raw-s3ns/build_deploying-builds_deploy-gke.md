# Deploying to GKE

Source: https://documentation.s3ns.fr/build/docs/deploying-builds/deploy-gke
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












# Deploying to GKE 














This page explains how to deploy an application to Kubernetes using
Cloud Build.

Cloud Build provides a [`gke-deploy` builder](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gke-deploy) 
that lets you deploy a containerized application to a
GKE cluster.

`gke-deploy` is a wrapper around `kubectl`, the command-line interface for
Kubernetes. It applies Google's recommended practices for deploying applications
to Kubernetes by:

- 

Updating the application's Kubernetes resource file to use the container
image's digest instead of a tag.

- 

Adding [recommended labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels) to the Kubernetes resource file.

- 

Retrieving credentials for the GKE clusters
to which you're deploying the image.

- 

Waiting for the Kubernetes resource file that was submitted to be ready.

If you want to deploy your applications using `kubectl` directly and don't need
additional functionality, Cloud Build also provides a [`kubectl` builder](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/kubectl) that you can use to deploy your application to a
GKE cluster.

## Before you begin

- 

Create a [GKE cluster](/../../kubernetes-engine/docs/how-to/creating-a-cluster), if you don't have one yet.

- 

Have your containerized application in the form of source code and a
`Dockerfile` ready. Your source code needs to be stored in a repository, such as
Cloud Source Repositories, GitHub, or Bitbucket.

- 

You'll need at least one Kubernetes resource file describing the Kubernetes
resources used to run your application. If you don't have Kubernetes
resource files, use the following steps to generate one for your
application:

- Open the [Kubernetes Engine clusters page](http://console.cloud.s3nscloud.fr/kubernetes/list) in the Cloud de Confiance by S3NS console.

- On the Kubernetes Engine clusters page, click **Deploy**.

- Select your container and click **Continue**. You will see the Configuration
section.

- Under Configuration YAML, click **View YAML** to get a sample Kubernetes
resource file.

### Required IAM permissions

Add the Google Kubernetes Engine Developer role to your account:

- 

In the Cloud de Confiance console, go to the
*settings* Cloud Build **Permissions** page:


[Go to **Permissions**](https://console.cloud.s3nscloud.fr/cloud-build/settings)

- 

Set the status of the **Kubernetes Engine Developer** role to **Enabled**.

## Deploying a prebuilt container image

To deploy a particular version of your application with `gke-deploy`:

- 

Make sure your Kubernetes resource file is referring to the
correct container image tag or digest.

- 

Add the `gke-deploy` step in your [build configuration file](/build/docs/configuring-builds/create-basic-configuration):



### YAML

```
steps : 
... 
# deploy container image to GKE 
- name : "gcr.io/cloud-builders/gke-deploy" 
args : 
- run 
- --filename= KUBERNETES_RESOURCE_FILE 
- --location= CLUSTER_LOCATION 
- --cluster= CLUSTER 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/gke-deploy" , 
"args" : [ 
"run" , 
"--filename= KUBERNETES_RESOURCE_FILE " , 
"--location= CLUSTER_LOCATION " , 
"--cluster= CLUSTER " 
] 
} 
] 
} 
```



Where:

- KUBERNETES_RESOURCE_FILE is the path of your Kubernetes resource
file or the directory path containing your Kubernetes resource files.

- CLUSTER_LOCATION is the region of the cluster.

- CLUSTER is the name of the GKE cluster that the application
will be deployed to.

For more information on available flags, see [`gke-deploy run` flags](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/gke-deploy/cmd/run/run.go).

- 

Start your build:


```
gcloud builds submit -- region = LOCATION -- project = PROJECT -- config BUILD_CONFIG 
```


Where:

- LOCATION is one of the [supported build locations](/build/docs/locations).

- PROJECT is the ID for your project.

- BUILD_CONFIG is the name of your build configuration file.

## Building and deploying a new container image

To build a new container image and deploy the new container image:

- 

Update your Kubernetes resource file with the new container
image using the `--image` attribute:



### YAML

```
steps : 
# build the container image 
- name : "gcr.io/cloud-builders/docker" 
args : [ "build" , "-t" , " LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " , "." ] 
# push container image 
- name : "gcr.io/cloud-builders/docker" 
args : [ "push" , " LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " ] 
# deploy container image to GKE 
- name : "gcr.io/cloud-builders/gke-deploy" 
args : 
- run 
- --filename= KUBERNETES_RESOURCE_FILE 
- --image= LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG 
- --location= CLUSTER_LOCATION 
- --cluster= CLUSTER 
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
" LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " , 
"." 
] 
}, 
{ 
"name" : "gcr.io/cloud-builders/docker" , 
"args" : [ 
"push" , 
" LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " 
] 
}, 
{ 
"name" : "gcr.io/cloud-builders/gke-deploy" , 
"args" : [ 
"run" , 
"--filename= KUBERNETES_RESOURCE_FILE " , 
"--image= LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " , 
"--location= CLUSTER_LOCATION " , 
"--cluster= CLUSTER " 
] 
} 
] 
} 
```



Where:

- LOCATION is one of the [supported build locations](/build/docs/locations).

- PROJECT is the ID for your project.

- IMAGE_NAME is the name that you want for the container
image, usually the application name.

- TAG is the tag of the container image.

- If you are building a new container image with each commit, a good practice
is to use the commit short SHA as a tag. Cloud Build makes this
available as a [default substitution](/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions), `$SHORT_SHA`.

- KUBERNETES_RESOURCE_FILE is the path of your Kubernetes resource
file or the directory path containing your Kubernetes resource files.

- CLUSTER is the name of the GKE cluster that the application
will be deployed to.

- CLUSTER_LOCATION is the region the cluster will be deployed to.

- 

Start your build:


```
gcloud builds submit -- region = LOCATION -- project = PROJECT -- config BUILD_CONFIG 
```


Where:

- LOCATION is one of the [supported build regions](/build/docs/locations).

- PROJECT is the ID for your project.

- BUILD_CONFIG is the name of your build configuration file.

## Automating deployments

You can automate the deployment of your application to GKE by
creating a trigger in Cloud Build. You can configure triggers to
build and deploy images whenever you push changes to your code.

To create a build trigger:

- 

Open the **Triggers** page in the Cloud de Confiance console:

[Open the Triggers page](https://console.cloud.s3nscloud.fr/cloud-build/triggers)

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

Select the repository that contains your source code and build config
file.

- 

Specify the regular expression for the branch or tag name that will
start your trigger.

- 

Choose a **Configuration** for your trigger.

If you choose a Cloud Build configuration file, you can
specify **Substitution variables** by providing a variable name and
the value you want to associate with that variable. In the following
example, the user-defined substitution variable
`_CLOUDSDK_CONTAINER_CLUSTER` specifies the cluster to deploy to,
and the user-defined substitution variable `_CLOUDSDK_COMPUTE_ZONE`
specifies its location. If you want to deploy to a different cluster,
you can use the same build configuration and only need to change
the values of the substitution variables:



### YAML

```
steps : 
... 
# deploy container image to GKE 
- name : "gcr.io/cloud-builders/gke-deploy" 
args : 
- run 
- --filename= KUBERNETES_RESOURCE_FILE 
- --image= LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG 
- --location=${_CLOUDSDK_COMPUTE_ZONE} 
- --cluster=${_CLOUDSDK_CONTAINER_CLUSTER} 
```


### JSON

```
{ 
"steps" : [ 
{ 
"name" : "gcr.io/cloud-builders/gke-deploy" , 
"args" : [ 
"run" , 
"--filename= KUBERNETES_RESOURCE_FILE " , 
"--image= LOCATION -docker.pkg.dev/ PROJECT / REPOSITORY / IMAGE_NAME : TAG " , 
"--location=${_CLOUDSDK_COMPUTE_ZONE}" , 
"--cluster=${_CLOUDSDK_CONTAINER_CLUSTER}" 
] 
} 
] 
} 
```



Where:

- KUBERNETES_RESOURCE_FILE is the path of
your Kubernetes configuration file or the directory path containing
your Kubernetes resource files.

- PROJECT is the ID for your project.

- IMAGE_NAME is the name you want for your
container image, usually the application name.

- TAG is the tag of the container image.

To learn more about how to define substitutions for build configuration files,
see [Using user-defined substitutions](/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions).

- 

Click **Create** to save your build trigger.

When you push code to your repository, Cloud Build will automatically
trigger a build. To learn more about build triggers, see [Creating and managing
build triggers](/build/docs/automating-builds/create-manage-triggers).

## What's next

- Learn how to
[configure automated deployments for your workloads on GKE](/kubernetes-engine/docs/how-to/automated-deployment).

- Learn how to [create a GitOps-style CI/CD pipeline deploying to
GKE with Cloud Build](/../../kubernetes-engine/docs/tutorials/gitops-cloud-build).

- Learn about additional [`gke-deploy` options](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gke-deploy/doc).

- Learn how to [perform blue-green deployments on Compute Engine](/build/docs/deploying-builds/deploy-compute-engine). 

- Learn about additional [Cloud builders](/build/docs/cloud-builders).

- Learn how to [troubleshoot build errors](/build/docs/troubleshooting).
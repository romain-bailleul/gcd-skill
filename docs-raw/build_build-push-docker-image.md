# Quickstart: Build and push a Docker image with Cloud Build

Source: https://berlin.devsitetest.how/build/docs/build-push-docker-image
Last updated: 2026-11-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/build/docs/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Cloud Build

](https://berlin.devsitetest.how/build/docs)






- 








[

Guides

](https://berlin.devsitetest.how/build/docs/build-push-docker-image)


























# Build and push a Docker image with Cloud Build




Learn how to get started with Cloud Build by building a Docker image
and pushing the image to Artifact Registry. Artifact Registry provides a single
location for managing private packages and Docker container images.

You will first build the image using a `Dockerfile`, which is the Docker
configuration file, and then build the same image using the
Cloud Build configuration file.





## Before you begin






















- 





In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.





**Roles required to select or create a project**




- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)












- 


If you're using an existing project for this guide,
[verify that you have
the permissions required to complete this guide](#required-roles). If you created a new
project, then you already have the required permissions.













- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Cloud Build, Compute Engine and Artifact Registry APIs, if any are not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//docs.cloud.google.com/build/docs/build-push-docker-image)














- 


[Install](/sdk/docs/install) the Google Cloud CLI.











- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).






- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```























## Required roles




























































To get the permissions that
you need to build a Docker image and push it to Artifact Registry,

ask your administrator to grant you the
following IAM roles on the Cloud Build service account:













- [Artifact Registry Administrator ](/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)


- [Cloud Build Editor ](/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)


- [Logs Writer ](/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)


- [Storage Bucket Viewer ](/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)


- [Storage Object User ](/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)









For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).














## Prepare source files to build

You'll need some sample source code to package into a container image. In this section,
you'll create a shell script and a `Dockerfile`. A `Dockerfile` is a text
document that contains instructions for Docker to build an image.

- 

Open a terminal window.

- 

Create a new directory named `quickstart-docker` and navigate into it:


```
mkdir quickstart-docker
cd quickstart-docker
```


- 

Create a file named `quickstart.sh` with the following contents:























```
#!/bin/sh 
echo "Hello, world! The time is $( date ) ." 
```



- 

Create a file named `Dockerfile` with the following contents:






















```
FROM alpine 
COPY quickstart.sh /
CMD [ "/quickstart.sh" ] 
```



- 

In the terminal window, run the following command to make `quickstart.sh` executable:


```
chmod +x quickstart.sh
```


## Create a Docker repository in Artifact Registry

- 

Use the
[`gcloud artifacts repositories create`](/sdk/gcloud/reference/artifacts/repositories/create)
command to create a Docker repository named `quickstart-docker-repo` in the
location `us-west2` with the description "Docker repository":


```
gcloud artifacts repositories create quickstart-docker-repo --repository-format = docker \ 
--location = us-west2 --description = "Docker repository" 
```


- 

Verify that your repository was created:


```
gcloud artifacts repositories list
```


The list of displayed repositories should include `quickstart-docker-repo`.

Artifact Registry uses a
[naming convention](/artifact-registry/docs/docker/names) to identify
repositories and images. For example, when you interact with Docker images
stored in Artifact Registry in the `us-west2` region, you use
`us-west2-docker.pkg.dev` as the registry hostname in your commands.

## Build an image using a Dockerfile

Use the [`gcloud builds submit`](/sdk/gcloud/reference/builds/submit) command to
build a Docker image using a `Dockerfile`. You don't require a separate
Cloud Build config file.

- 

Get your Google Cloud Dedicated project ID by running the following command:


```
gcloud config get-value project
```


- 

Run the following command from the directory containing `quickstart.sh` and
`Dockerfile`:


```
gcloud builds submit -- region = us - west2 -- tag us - west2 - docker . pkg . dev / PROJECT_ID / quickstart - docker - repo / quickstart - image: tag1 
```


After the build is complete, the output should be similar to the following:


```
DONE
------------------------------------------------------------------------------------------------------------------------------------
ID CREATE_TIME DURATION SOURCE IMAGES STATUS
545cb89c-f7a4-4652-8f63-579ac974be2e 2020 -11-05T18:16:04+00:00 16S gs://gcb-docs-project_cloudbuild/source/1604600163.528729-b70741b0f2d0449d8635aa22893258fe.tgz us-west2-docker.pkg.dev/gcb-docs-project/quickstart-docker-repo/quickstart-image:tag1 SUCCESS
```


You've just built a Docker image named `quickstart-image` using a `Dockerfile`
and pushed the image to Artifact Registry.

## Build an image using a build config file

In this section you use a Cloud Build config file to build the same
Docker image built in the previous steps. The build config file instructs
Cloud Build to perform tasks based on your specifications.

- 

In the same directory that contains `quickstart.sh` and the `Dockerfile`,
create a file named `cloudbuild.yaml` with the following contents. This file is
your build config file. At build time, Cloud Build automatically
replaces `$PROJECT_ID` with your project ID.























```
steps : 
- name : 'gcr.io/cloud-builders/docker' 
script : | 
docker build -t us-west2-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1 . 
automapSubstitutions : true 
images : 
- 'us-west2-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1' 
```



- 

Start the build by running the following command:


```
gcloud builds submit -- region = us - west2 -- config cloudbuild . yaml 
```


After the build is complete, the output should be similar to the following:


```
DONE
------------------------------------------------------------------------------------------------------------------------------------
ID CREATE_TIME DURATION SOURCE IMAGES STATUS
046ddd31-3670-4771-9336-8919e7098b11 2020 -11-05T18:24:02+00:00 15S gs://gcb-docs-project_cloudbuild/source/1604600641.576884-8153be22c94d438aa86c78abf11403eb.tgz us-west2-docker.pkg.dev/gcb-docs-project/quickstart-docker-repo/quickstart-image:tag1 SUCCESS
```


You've just built `quickstart-image` using the build config file and pushed the
image to Artifact Registry.

## View build details

- 

Open the Cloud Build page in the Google Cloud Dedicated console.

[Open the Cloud Build page](https://console.cloud.berlin-build0.goog/cloud-build)

- 

If necessary, select your project and click **Open**.

You will see the **Build history** page:



- 

If necessary, select `us-west2`in the **Region** drop-down menu to view
builds in that region.

There will be two builds listed, one for each of the builds you executed in
this quickstart.

- 

Click one of the builds.

You will see the **Build details** page.

- 

To view the artifacts of your build, under **Build Summary**, click **Build artifacts**.

You should see output similar to the following:



You can download your build log and view your image details in
Artifact Registry from this page.






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






- 

Open the Artifact Registry page in the Google Cloud Dedicated console.

[Open the Artifact Registry page](https://console.cloud.berlin-build0.goog/artifacts)

- 

Select your project and click **Open**.

- 

Select **quickstart-docker-repo**.

- 

Click **Delete**.

You have now deleted the repository that you created as part of this quickstart.






## What's next



- Learn how to [run a Docker image](/build/docs/building/build-containers#run_the_docker_image).

- Learn how to [create a basic build config
file](/build/docs/configuring-builds/create-basic-configuration).

- Learn how to [deploy using Cloud Build](/build/docs/deploy-containerized-application-cloud-run).

- Learn how to [build Node.js applications](/build/docs/building/build-nodejs).

- Learn how to [build Java applications](/build/docs/building/build-java).

- Learn how to [build Go applications](/build/docs/building/build-go).
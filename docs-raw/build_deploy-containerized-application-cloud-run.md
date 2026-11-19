# Quickstart: Deploy a containerized application to Cloud Run

Source: https://berlin.devsitetest.how/build/docs/deploy-containerized-application-cloud-run
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


























# Deploy a containerized application to Cloud Run using Cloud Build




This page shows you how to use Cloud Build to deploy a containerized application
to Cloud Run.





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



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Cloud Build, Cloud Run, Artifact Registry, and Compute Engine APIs, if any are not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com,compute.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-deploy)














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























## Grant permissions

Cloud Build requires several permissions before it can deploy
an image to Cloud Run. To grant these permissions, do the
following:

- 

Open a terminal window.

- 

Set environment variables to store your project ID and project number.


```
PROJECT_ID = $( gcloud config list --format = 'value(core.project)' ) 
PROJECT_NUMBER = $( gcloud projects describe $PROJECT_ID --format = 'value(projectNumber)' ) 
```


- 

Grant the **Cloud Run Admin** role to your
[Cloud Build service account](/build/docs/cloud-build-service-account).


```
gcloud projects add-iam-policy-binding $PROJECT_ID \ 
--member = serviceAccount: $( gcloud projects describe $PROJECT_ID \ 
--format = "value(projectNumber)" ) -compute@developer.eu0-system.iam.gserviceaccount.com \ 
--role = roles/run.admin \ 
```


- 

Grant the **Storage Object User** role to your
Cloud Build service account.


```
gcloud projects add-iam-policy-binding $PROJECT_ID \ 
--member = serviceAccount: $( gcloud projects describe $PROJECT_ID \ 
--format = "value(projectNumber)" ) -compute@developer.eu0-system.iam.gserviceaccount.com \ 
--role = roles/storage.objectUser \ 
```


- 

Grant the **Service Account User** role to your
Cloud Build service account.


```
gcloud projects add-iam-policy-binding $PROJECT_ID \ 
--member = serviceAccount: $( gcloud projects describe $PROJECT_ID \ 
--format = "value(projectNumber)" ) -compute@developer.eu0-system.iam.gserviceaccount.com \ 
--role = roles/iam.serviceAccountUser
```


## Deploy a prebuilt image

You can configure Cloud Build to deploy a prebuilt image that is stored
in Artifact Registry to Cloud Run.

To deploy a prebuilt image:

- 

Open a terminal window (if not already open).

- 

Create a new directory named `helloworld` and navigate into it:


```
mkdir helloworld
cd helloworld
```


- 

Create a file named `cloudbuild.yaml` with the following contents. This file is
the Cloud Build config file. It contains instructions for Cloud Build
to deploy the image named `us-docker.pkg.dev/cloudrun/container/hello` on the Cloud Run
service named `cloudrunservice`.























```
steps : 
- name : 'gcr.io/cloud-builders/gcloud' 
script : | 
gcloud run deploy cloudrunservice --image us-docker.pkg.dev/cloudrun/container/hello --region us-central1 --platform managed --allow-unauthenticated 
```



- 

Deploy the image by running the following command:


```
gcloud builds submit -- region = us - west2 -- config cloudbuild . yaml 
```


When the build is complete, you will see an output similar to the following:


```
DONE 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

ID CREATE_TIME DURATION SOURCE IMAGES STATUS 
784653b2 - f00e - 4c4b - 9f5f - 96a5f115bef4 2020 - 01 - 23T14:53:13 + 00:00 23S gs://cloudrunqs - project_cloudbuild/source/1579791193 . 217726 - ea20e1c787fb4784b19fb1273d032df2 . tgz - SUCCESS 
```


You've just deployed the image `hello` to Cloud Run.

## Run the deployed image

- 

Open the Cloud Run page in the Google Cloud Dedicated console:

[Open the Cloud Run page](https://console.cloud.berlin-build0.goog/run)

- 

Select your project and click **Open**.

You will see the **Cloud Run Services** page.

- 

In the table, locate the row with the name **cloudrunservice**, and click
**cloudrunservice**.

The **Service details** page for **cloudrunservice** is displayed.

- 

To run the image that you deployed on **cloudrunservice**, click the URL:














## What's next



- [Learn how to build using Cloud Build](https://berlin.devsitetest.how/cloud-build/docs/quickstart-build).

- [Learn how to create a basic build config file](https://berlin.devsitetest.how/cloud-build/docs/configuring-builds/create-basic-configuration).

- [Learn how to view build results](https://berlin.devsitetest.how/cloud-build/docs/view-build-results).

- [Learn about more ways to deploy to Cloud Run](https://berlin.devsitetest.how/cloud-build/docs/deploying-builds/deploy-cloud-run).

- [Learn how to deploy to Google Kubernetes Engine](https://berlin.devsitetest.how/cloud-build/docs/deploying-builds/deploy-gke).

- [Learn more about DevOps resources](https://berlin.devsitetest.how/devops).

- [Explore the DevOps research program](https://www.devops-research.com/research.html).
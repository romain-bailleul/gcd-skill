# Quickstart: Automate builds by using Cloud Build

Source: https://documentation.s3ns.fr/build/docs/automate-builds
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


























# Automate builds by using Cloud Build




This page explains how to use Cloud Build to automate builds.

Cloud Build uses **build triggers** to enable CI/CD automations.
You can configure triggers to listen for incoming events, such as when a
new commit is pushed to a repository or when a pull request is initiated,
and then automatically invoke a build when new events come in.

You will create a trigger and configure that trigger to invoke a build anytime
you push a change to a GitHub repository.





## Before you begin






















- 





In the Cloud de Confiance console, on the project selector page,
select or create a Cloud de Confiance project.





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












[Go to project selector](https://console.cloud.s3nscloud.fr/projectselector2/home/dashboard)












- 


If you're using an existing project for this guide,
[verify that you have
the permissions required to complete this guide](#required-roles). If you created a new
project, then you already have the required permissions.













- 



[Verify that billing is enabled for your Cloud de Confiance project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Cloud Build API, if it is not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.s3nscloud.fr/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-automate)














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























- 

If you don't have one already, create an account on
[GitHub](https://github.com/).


- 

If you have two-factor authentication set up on GitHub,
[create a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to use in place of a GitHub
password with the command line.

## Required roles





















































To get the permissions that
you need to automate builds by using Cloud Build,

ask your administrator to grant you the
following IAM roles on the Cloud Build service account:













- [Cloud Build Editor ](/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)


- [Storage Object User ](/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)


- [Storage Bucket Viewer ](/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)


- [Cloud Build Connection Admin ](/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)









For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).














## Fork and clone a sample GitHub repository

You'll need some sample source code to build. In this section, you'll clone
an existing source repository containing a Hello World example in Go to your
own GitHub user account.

- 

If you don't have one already, create an account on
[GitHub](https://github.com/).


- 

If you have two-factor authentication set up on GitHub,
[create a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to use in place of a GitHub
password with the command line.

- 

Fork the `cloud-build-samples` repository to your own GitHub account:




- 

Go to the Cloud Build
[cloud-build-samples repository](https://github.com/GoogleCloudPlatform/cloud-build-samples).



- 

Click on the **Fork** icon on the top-right corner
of the page.



- 

Click on the GitHub user account you want to fork the repository to.



You will automatically be redirected to the page with your
forked version of the `cloud-build-samples` repository.




- 

Open a terminal in your local environment.



- 

Clone the forked repository by running the following command, where
GITHUB_USERNAME is the username for your GitHub account:


```
git clone https://github.com/ GITHUB_USERNAME /cloud-build-samples.git
```


## Connect Cloud Build to your repository

To build source code on GitHub using triggers, you must first connect
Cloud Build to your GitHub repository. In this section, you'll
connect your `cloud-build-samples` repository to Cloud Build.

- 

In the Cloud de Confiance console navigation menu, click **Cloud Build > Triggers**.

[Open Triggers page](https://console.cloud.s3nscloud.fr/cloud-build/triggers)

- 

Select your project and click **Open**.

- 

Click
**Connect repository** .

- 

Under **Select source**, select
**GitHub (Cloud Build GitHub App)** .

- 

Click **Continue** .

- 

Authenticate your GitHub account.

- 

In the **Select repository** section, select the username of your
**GitHub account** .
If your username doesn't appear in the list:

- 

In the **GitHub account** list, click **+Add**.

You will see a pop-up to install the Cloud Build GitHub app.

- 

Click on your GitHub username.

- 

Click **Only certain repositories** to install the Cloud Build
GitHub app on certain repositories.

- 

On the drop-down menu, select ** GITHUB_USERNAME /cloud-build-samples**,
where GITHUB_USERNAME is the username for your GitHub account.

- 

Click **Install**.

You may be asked to enter the password associated with your GitHub account
before proceeding.

- 

Following the installation of the Cloud Build GitHub app, you
will now be able to see your username in the drop-down menu on the
**GitHub account** field. Select your username.

- 

Under **Repository** , select ** GITHUB_USERNAME /cloud-build-samples**
as your repository.

- 

Click the checkmark to agree to terms and conditions for trigger
connection.

- 

Click **Connect** .

- 

Click **Done** .

You will create a trigger in the next section.

## Create a trigger

- 

Open the **Triggers** page in the Cloud de Confiance console:



[Open Triggers page](https://console.cloud.s3nscloud.fr/cloud-build/triggers)

- 

Select your project from the project selector drop-down menu at the top of
the page.

- 

Click **Open**.

- 

On the **Triggers** page, click **Create trigger** .

- 

On the **Create trigger** page, enter the following settings:




- 

**Name**: Enter `hello-world-trigger` as the name of
your trigger.


- 

**Event**: Select
**Push to a branch** 
as the repository event to invoke your trigger.


- 

**Source** :
Select the `cloud-build-samples` repository as your
source, which contains your source code and your build config file.


- 

**Build Configuration**: Choose
**Cloud Build configuration file** 
as your build config file.


- 

**Cloud Build configuration file location** :
Specify the path to your Cloud Build configuration file as
`quickstart-automate/cloudbuild.yaml`.



- 

Click **Create** 
to save your build trigger.

## Commit a change

In this section, you will commit a change to your cloned `cloud-build-samples`
repository on your own GitHub account.

- 

In your terminal, navigate to the `quickstart-automate` directory:


```
cd cloud-build-samples/quickstart-automate
```


- 

Open the `main.go` file and update the line containing "Hello, world!"
to "Hello, universe!"


```
package main 

import ( 
"fmt" 
) 

func main () { 
fmt . Println ( "Hello, universe!" ) 
} 

```


- 

Review `cloudbuild.yaml` ,
which is the build configuration file used by Cloud Build.
When a build is invoked with a trigger, the build step in this file instructs
Cloud Build to use the
[
`golang` image from Docker Hub](https://hub.docker.com/_/golang)
to build and run the `main.go` file.



```
steps : 
- name : golang 
script : go run quickstart-automate/main.go 

```




- 

Navigate back to the root directory of your repository:


```
` cd ..`
```




- 

Commit your changes to GitHub by running the following commands:


```
` git add quickstart-automate/main.go
git commit -m "update text" 
git push`
```




You may be prompted to enter your credentials when pushing code to your
repository. If prompted, enter your username and password or an
authentication token.

You have now pushed a change to your repository. Your
push will result in an automatic build by your trigger.

## View build details

In this section, you will view the build details associated with your
invoked build after committing a change.

- 

In the Cloud de Confiance console navigation menu, click **Cloud Build > History**.

[Open the Cloud Build page](https://console.cloud.s3nscloud.fr/cloud-build)

- 

Select your project and click **Open**.

You will see the **Build history** page:



- 

In the **Build** 
column, click the name of a build.

- 

On the **Build details** page, click
**Build Artifacts** .

You will see an output similar to the following:



- 

To view the build log, click the download icon and view the downloaded file.

You have successfully invoked a Cloud Build build using a trigger and
viewed the build details.






## Clean up





To avoid incurring charges to your Cloud de Confiance account for
the resources used on this page, follow these steps.






- 

In the Cloud de Confiance console navigation menu, click **Cloud Build > Triggers**.



[Open Triggers page](https://console.cloud.s3nscloud.fr/cloud-build/triggers)

- 

Select your project and click **Open**.


- 

In the `hello-world-trigger` row, click the
Actions menu 
(vertical ellipses) located at the right end of the row.

- 

Select **Delete**.

You have now deleted the trigger associated with your cloned repository.






## What's next



- Learn how to [create a basic build config
file](/cloud-build/docs/configuring-builds/create-basic-configuration).

- Learn how to [create and manage build triggers](/cloud-build/docs/automating-builds/create-manage-triggers).
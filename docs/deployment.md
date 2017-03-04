###  Cloud Endpoint Deployment in Google App Engine App

To deploy out Back End we need use **gcloud** tool. This tool are available
if we have executed requirements.sh manually or using fabric: 
`fab requirements`.

To know more about the installation of gloud take a look to official [docs](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version).

After we need initialize the SDK using `/google-cloud-sdk/bin/gcloud init`
and to do this we need a Googe Account, because the program will
search if we have available projects in [Google Cloud Platform](https://console.cloud.google.com) account.
It will try to link with one of your project to make the next operations that you need.

So, before you do this you will need create a new project in 
Google Cloud Platform console, to do this only need click in `Create Project`
near main manu toolbar and set a cool name, in our case:
IVCheckerBackEnd, so the id of the project will be ivcheckerbackend.

    You are logged in as: [butterflydevsmail@gmail.com].
    
    Pick cloud project to use: 
     [1] ...
     [2] ivchecker-web
     [3] ivcheckerbackend
     [4] ...
     [5] ...
    Please enter numeric choice or text value (must exactly match list 
    item):  3


After we need generate the OpenAPI configuration file. First we generate the specifications of our api in swageer format:
   
    > python lib/endpoints/endpointscfg.py get_openapi_spec main.IVCheckerApi --hostname main-api.endpoints.ivcheckerbackend.appspot.com

And after we upload this file to our linked project with the same gcloud tool:
 
    > gcloud service-management deploy ./ivcheckerv1openapi.json 

    ...
    
    Service Configuration [2017-03-04r0] uploaded for service [main-api.endpoints.ivcheckerbackend.appspot.com]
    
To end we need copy this info in app.yaml in `env_variables`.


After, we only need execute `gcloud app deploy`.
    
When we execute this the app will be deployed, and we will need
choose where we want deploy (we are going to select europe)
and after a while we can see the url to our project developed in
Google App Engine. See this example:
    
    > gcloud app deploy
    You are creating an app for project [ivcheckerbackend].
    WARNING: Creating an App Engine application for a project is irreversible and the region
    cannot be changed. More information about regions is at
    https://cloud.google.com/appengine/docs/locations.
    
    Please choose the region where you want your App Engine application 
    located:
    
    [1] europe-west   (supports standard)
    [2] us-central    (supports standard and flexible)
    [3] us-east1      (supports standard and flexible)
    [4] asia-northeast1 (supports standard and flexible)
    [5] cancel
    Please enter your numeric choice:  1
    
    Creating App Engine application in project [ivcheckerbackend] and region [europe-west]....done.                                                                                 
    You are about to deploy the following services:
    - ivcheckerbackend/default/20170304t001620 (from [/home/juan/Projects/IVCheckerBackEnd/app.yaml])
    Deploying to URL: [http://ivcheckerbackend.appspot.com]
    
    Do you want to continue (Y/n)?  Y   
    
    Beginning deployment of service [default]...
    Some files were skipped. Pass `--verbosity=info` to see which ones.
    You may also view the gcloud log file, found at
    [/home/juan/.config/gcloud/logs/2017.03.04/00.14.02.476100.log].
    
    File upload done.
    
    Updating service [default]...done.                                                                                                                                              
    Deployed service [default] to [http://ivcheckerbackend.appspot.com]
    
    You can stream logs from the command line by running:
      $ gcloud app logs tail -s default
    
    To view your application in the web browser run:
      $ gcloud app browse



*Easy, right?*


    
After in a while we will have **our app working !** 

We can try this in  any browser:


    https://ivcheckerbackend.appspot.com/_ah/api/ivchecker/v1/helloWorld
    
    {
     "content": "Hello World!"
    }
    
    
##### References:

To know more about it:

- [Gcloud command-line tool docs](https://cloud.google.com/sdk/gcloud/)
- [Endpoints frameworks docs](https://cloud.google.com/endpoints/docs/frameworks/python/quickstart-frameworks-python)
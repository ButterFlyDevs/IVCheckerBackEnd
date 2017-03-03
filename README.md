# IVCheckerBackEnd
Back End of IVChecker web and mobile app, builded to 
run in [Google App Engine](https://cloud.google.com/appengine/docs/) using 
[Cloud Endpoints](https://cloud.google.com/endpoints/docs/frameworks/python/about-cloud-endpoints-frameworks) technology with 
[gRPC](http://www.grpc.io/) for communications totally developed
in Python.

#### Requirements:

A lot of requirements will be installed after, but to start you need install 
**fabric** tool, `apt-get install fabric`. 
We use this tool to everything, and of course have installed a Python
interpreter, we use **2.7** version.

To know the list of options of tools execute `fab -l` in 
root project folder, and `fab -d <option>` to know more about
this.

#### Where to start?

The steps are the follow:

 1. Run `fab requirements` in the root folder to install all of them.
 2. Run `fab run` to run in local (`fab kill` to stop).

All features must be tested, to test app, run `fab test`.
 
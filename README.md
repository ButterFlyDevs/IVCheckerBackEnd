# IVCheckerBackEnd
Back End of IVChecker web and mobile app, builded to 
run in Google App Engine using endpoints technology with gRPC
for communications. 

#### Requirements:

A lot of requirements will be installed after but to start you need install 
**fabric** tool, `apt-get install fabric`. 
We use this tool to everything.

To know options execute `fab -l` in root project folder.

#### Where to start?

The steps are the follow:

 1. Run `fab requirements` in the root folder to install all of them.
 2. Run `fab run` to run in local (`fab kill` to stop).

All features must be tested, to test app, run `fab test`.
 
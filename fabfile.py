from fabric.api import local
from fabric.colors import blue, red
import time
######################################################################
#  FABRIC Fabfile.  <http://www.fabfile.org/>
# This is the file to configure Fabric Python Library to admin tasks

# Use:
# fab <command>

# How to know the commands? :
# fab -l

# Info about command:
# fab -d <command>

#######################################################################

# Butterfly Devs  @ Granada 2017


def requirements():
    """
    Run this task to run  provisioning of requirements of the API.
    Example of use: fab requirements
    :return: None
    """

    local('sudo . ./requirements.sh')


def run():
    """
    Run back_end in local host.
    :return:
    """

    local('google_appengine/dev_appserver.py app.yaml &')


def kill():
    """
    Kill all processes that is related with google dev server.
    :return:
    """
    print (red("Killing all processes taht are related with google dev server."))
    local("kill -9 $(ps -aux | grep google | awk '{ print $2}' | head -n -1)")


def restart():
    #TODO review, don't work!

    print (red("Restarting dev server processes."))

    kill()
    time.sleep(5)
    run()


def test():
    """
    Testing all app.
    :return:
    """
    print (blue('Runing IVCheckerBackEnd Test Suite ##'))
    local('pytest test/ -vv -s')

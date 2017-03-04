#!/usr/bin/env bash

#####################
# Requirements file #
#####################

# Butterfly Devs  @ Granada 2017

# You can run directly this file (. ./requirements.sh) in the root dir of the project or using our preferred
# tool of automation, Fabric (http://www.fabfile.org/ - apt-get install fabric) run:

echo -e "\033[35m \n\t    ### IVChecker BackEnd Project \033[35m ### \033[0m"
echo -e "\033[34m \t      Butterfly Devs @ Granada 2017 \033[34m  \033[0m"
echo -e "\033[35m \n\t    Thank you for your contribution! \n \033[0m"

echo -e "It will be installed: UnZIP, Curl, Google App Engine SDK v.1.9.50 , pytest and python requirements for GAE app. \n"


read -p "Are you sure? [y/n]: " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo -e "\n\033[34m 1. Installing unzip \033[0m\n"
    sudo apt-get install -y unzip

    echo -e "\n\033[34m 2. Installing curl \033[0m\n"
    sudo apt-get install -y curl

    # Control will enter here if google_appengine directory doesn't exist.
    if [ ! -d "google_appengine" ];
    then

        # Version of 23 January  2017  (In other projects we used 1.9.30)
        echo -e "\n\033[34m 3. Downloading Google App Engine SDK v.1.9.50 \033[0m\n"
        curl -O https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.50.zip

        echo -e "\n\033[34m 4. Unzip SDK \033[0m\n"
        unzip google_appengine_1.9.50.zip

        echo -e "\n\033[34m 5. Deleting .zip \033[0m\n"
        rm google_appengine_1.9.50.zip

    fi


    echo -e "\n\033[34m 6. Installing Python pip \033[0m\n"
    sudo apt-get install python-pip
    echo 'Version of pip installed:'
    pip --version

    echo -e "\n\033[34m Upgrading pip \033[0m\n"
    pip install --upgrade pip

    echo 'Version of pip updated:'
    pip --version

    echo -e "\n\033[34m 7. Installing pytest \033[0m\n"
    sudo pip install -U pytest
    pytest --version

    echo -e "\n\033[34m 8. Installing GAE python dependencies from requirements.txt \033[0m\n"
    sudo pip install -r requirements.txt -t lib/

    echo -e "\n\033[34m 9. Dowloading Google Cloud SDK v.146.0.0 \033[0m\n"
    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-146.0.0-linux-x86_64.tar.gz

    echo -e "\n\033[34m Extract files from Google Cloud SDK \033[0m\n"
    unzip google-cloud-sdk-146.0.0-linux-x86_64.tar.gz

    echo -e "\n\033[34m Installing Google Cloud SDK \033[0m\n"
    ./google-cloud-sdk/install.sh

    echo -e "\n\033[34m Deleting .tar.gz file \033[0m\n"
    rm google-cloud-sdk-146.0.0-linux-x86_64.tar.gz



    echo -e "\n\033[34m Done! \033[0m\n"




else

    echo -e "\n\033[34m :( \033[0m\n"

fi





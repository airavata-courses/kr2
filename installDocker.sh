#!/bin/bash

#update your packages
sudo apt-get upgrade -y
sudo apt update

#install pre-requisites
sudo apt install apt-transport-https ca-certificates curl software-properties-common

#add the GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#add docker repository to apt sources
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt update

#sudo apt-cache policy docker-ce

sudo apt install docker-ce

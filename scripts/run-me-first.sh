#!/bin/bash

## Update, and prep system for Docker

sudo apt-get update --yes
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package list again and install dependant packages for our solution
sudo apt-get update --yes
sudo apt install --yes software-properties-common unzip apt-transport-https ca-certificates curl gnupg lsb-release docker-ce docker-ce-cli containerd.io terraform

## Install the AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o ~/"awscliv2.zip"
cd ~/
unzip awscliv2.zip
sudo ./aws/install
rm -rf awscliv2.zip aws


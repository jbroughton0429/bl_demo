#!/bin/bash

# Simple Bash script to Deploy Terraform Environment to AWS

cd ../global/buckets/
terraform init
terraform apply -auto-approve 

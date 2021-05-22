# BL Demo


## Purpose

This is the sample coding challenge project for BL. This document describes the challenge, process and solution in order to properly execute the challenge presented by the team at BL.

## Scope

This solution will cover the following scenarios:
* Terraform to create an AWS bucket
    * Upload content to this bucket
* Create a tool to enumerate the data in the bucket
* Use Docker to run the tool
* Health Monitoring - Future

## Build out Infrastructure

### Variables
*This one needs Work - I've got to move my TF data into vars*

**vars.tf**

Line 4: Bucket Region
Line 10: Name of your TF State Bucket
Line 16: Name of your Files Bucket

**main.tf**

Line 2: AWS Region
Line 5: TF State Bucket
Line 19: Files Bucket


  1. Make sure that your AWS environment is setup first
    ```sh
    $ aws configure
    ```
  2. Make your necessary changes (above) for Terraform Variables.

  3. Execute deploy.sh
    ```sh
    $./deploy.sh
    ```

## Staging Script Execution (Pre Docker)

The steps to execute these scripts are as follow:

**NOTE**: This is reproducable on *Ubuntu 20.04*

1. Inside of scripts folder execute: 
```
./run-me-first.sh
```
2. Setup your AWS credentials
```
aws configure
```
3. Run your Terraform
```
../terraform/scripts/deploy.sh
```
4. Build your test files
```
python3 upload.py
```

## Build and Deploy Docker Images

1. Slip into the docker folder and build out your docker image

```
docker build --pull --rm -f Dockerfile -t jtest:demo .
```

2. Run the Docker Image

```
 docker-compose up
```

3. Pull your files
Your Volumes 'should' be located in: docker_mydata
You can verify this with: *docker volume ls*
If this is indeed the name of your docker volumn, declared in your compose file. Than you will need to locate your
location for this by doing the following:

```
docker volume inspect docker_mydata
```

Navigate to the "MountPoint" described in the results. In this example it is:
*/var/lib/docker/volumes/docker_mydata/_data*
You will be presented with 3 files:
* filecount.txt - A total count of files in the S3 Bucket
* filelist.txt - A list of files inside of the S3 bucket
* list.py - The script that was executed

## Clean Up

1. Delete your test files and clear your bucket data
From inside of your *scripts* directory, execute the below command. This will delete your test files on your
local machine and purge your bucket data.
```
python3 purge.py
```

2. Remove your Terraform Buckets
Navigate to: */terraform/scripts/* folder. From here you will want to destroy your s3 Buckets that was created at the beginning
of this execercise.
```
./destroy.sh
```

# Notes - Further information
As you can see in Step's 6 and 7, I was preparing for more steps moving forward
1) Moving this solution into a dockerized, always-on daemonized solution via docker-compose
2) Using the 'filecount.txt' to check the number of files (should be >= our initial load) towards a health monitor with healthz or other
   docker health monitoring solutions


# References
Insert References Here
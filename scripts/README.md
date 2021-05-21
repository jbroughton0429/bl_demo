# Scripts

This directory is the meat and potatos of your test/demo scenario

In no particular order, a brief overview of the following scripts are as follows:

* run-me-first.sh - This stages your current running environment for your AWS, docker, terraform, etc
* upload.py - This will create dummy files, and upload them to AWS
* purge.py - This cleans up your local filesystem of dummy files, and also deletes the files created in AWS
* list.py - This is the python script necessary for Dockerfile 

## Variables

1. It's imperrative that you have AWS configured on your local machine prior to executing these scripts (outside of run-me-first.sh). Once
'run-me-first.sh' has been execute, the variables for AWS credentials should be populated with:

```
aws configure
```

2. Buckets are var'd out the same across each script as: __bucket = s3.Bucket('put_your_bucket_here')__  
Make sure you replace this with the bucket name that you wish to use

3. Upload.py
This creates a directory called 'playground' (var = directory). with 5x test files prefixed: jungle-gym. **Note** If you change this variable file, you will need to change the directory variable in purge.py as well.

## Execution

The steps to execute these scripts are as follow:

This is reproducable on __Ubuntu 20.04__

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
**Insert steps here on Docker - blah blah yadda yadda**

x. Delete your test files and clear your bucket data
```
python3 purge.py
```


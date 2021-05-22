# Terraform

This directory is meant for building out the AWS Bucket and packer image

- AWS Backend - AWS Credentials are picked up from the AWS Pkg
- Buckets: Terraform State stored in bucket, 1x bucket

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

# Building your Environment

1. Make sure that your AWS environment is setup first
    ```sh
    $ aws configure
    ```
2. Make your necessary changes (above) for Terraform Variables. 
3. Modify the deploy.sh and destroy.sh files to add/remove the comment string if you are going to automate the creation of the bucket. *Note that Currently the bucket creation and destruction is commented out*
4. Execute deploy.sh
    ```sh
    $./deploy.sh
    ```
    This will build out your environment (), and if you uncommented the Buckets, build out your Buckets. 
    
**Please remember that you will need to uncomment the buckets for the first round, in order for TF-State to be built.**
    ```
   
   

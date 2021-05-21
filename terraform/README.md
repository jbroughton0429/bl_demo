# Terraform

This directory is meant for building out the AWS Bucket and packer image

- AWS Backend - AWS Credentials are picked up from the AWS Pkg
- Buckets: Terraform State stored in bucket, 1x bucket
- VM using the provided AMI's from Packer
- Security Groups built with only SSH access
- Machines:
--T2 Micro with GP2, 30GB disks, Keys to access are generated from /scripts/keygen.sh, populated to /keys

### Variables
*This one needs Work - I've got to move my TF data into vars*

Buckets - [Bucket Data Path](/global/buckets/)
Inside of vars.tf you will need to modify lines: 4,10,16,22 for your respective environments

Line 4: Bucket Region
Line 10: Name of your TF State Bucket
Line 16: Name of your Legacy Bucket
Line 22: Name of your Bucket

DevOps (Console) - [Console Data Path](/Devops/)
Inside of main.tf you will need to modify lines: 3, 8, 10, 48

Line 3: AWS Region
Line 8: TF State Bucket
Line 10: Bucket Region

# Specific Image Information

### Console (DevOps) Image
The purpose of this image is to run a test python script that itterates over 'ls' in a bucket and reports the number of files in a bucket, to the health monitor.

The TF-State is stored in the bucket. This means that from this Console machine, we can manage the current state of the buckets. We 'could' in theory, modify the state of this running machine (firewall rules, network changes, etc) but it would be best to do this from your origional machine that build the packer image.

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
   
   

#!/usr/bin/env python3

import boto3
import sys

## Quick check of keys and access. Will error if 
## Credentials are missing

sts = boto3.client('sts')
try:
    sts.get_caller_identity()
    print("Valid Credentials")
except boto3.exceptions.NoCredentialsError:
    print("Credentials are Invalid/Missing.")


s3 = boto3.resource('s3')
bucket = s3.Bucket('jaysons-files-bucket')


# Print out a list of filenames, to file
# TODO: We will use Docker Bind mounts to link this to the localhost so that the localhost can view these files

def list_files(bucket):
    sys.stdout = open("filelist.txt", "w")
    for obj in bucket.objects.all():
        print(obj.key)
sys.stdout.close()



# Print out a count of files from the bucket
# TODO: This will be used for checking file health, we know 5 files (from upload.py) should always exist at any given time

def count_files(bucket):
    sys.stdout = open("filecount.txt", "w")
    count_obj = 0

    for i in bucket.objects.all():
        count_obj += 1

    print(count_obj)
    sys.stdout.close()


list_files(bucket)
count_files(bucket)

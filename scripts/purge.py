#!/usr/bin/env python3

# Maintenance Script: DELETE
#
# This Script will do the following items:
#
# * Delete the items in the bucket
# * Delete the temp files and folder on your file system
# * Call you a cab to the pub

import shutil
import boto3

#TODO: Add testing

# Call S3 Resources and define my vars
s3 = boto3.resource('s3')

# Bucket Name
bucket = s3.Bucket('jaysons-files-bucket')

# Local Directory for file storage
directory = "playground"

# Remove my files from the local directory
shutil.rmtree(directory, ignore_errors=True)

# Purge files from bucket with the directory prefix
def remote_del_files():

    session = boto3.Session()
    for obj in bucket.objects.filter(Prefix=directory):
        s3.Object(bucket.name, obj.key).delete()

remote_del_files()


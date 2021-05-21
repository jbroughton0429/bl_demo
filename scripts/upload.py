#!/usr/bin/env python3

#
# Core Script: Create Files
#
# This script builds/creates your temporary files used for testing purposes
# We use mkstemp to write a bunch of temp files to the filesystem and then
# move these files over to a bucket.

# When you are done playing around, be sure you run it's companion script
# <clean-up.py> which will delete these folders/temp-files.

import os
import boto3

from tempfile import mkstemp

# Quickly double-check that your creds are loaded..if not, fail

# TODO: something appears to be borked here. NoCredentialsError is
# a valid exception, and this is the error that returns. However
# I receive an attribute error that boto3.exceptions has no attribute
# NoCredentialsError.

sts = boto3.client('sts')
try:
    sts.get_caller_identity()
    print("Valid Credentials")
except boto3.exceptions.NoCredentialsError:
    print("Credentials are Invalid/Missing.")


# Call S3 Resources and define my vars

s3 = boto3.resource('s3')
bucket = s3.Bucket('jaysons-files-bucket')

# Declare your Directory dict types. This way we can add multiple folders and 
# Sub-types later on if necessary.  dir1, dir2, dir2
directory = {
	"dir1":"playground"
}

# Create directory on this filesystem if it does not exist
# Yes I'm using backported tempfile in Ubuntu. Should probably 
# update that at some point.

if not os.path.exists(directory["dir1"]):
        os.mkdir(directory["dir1"]);

def temp_files():
    '''
    Creates Temporary files on this Filesystem
    '''
    for i in range(5):
        fd, path = mkstemp(prefix='jungle_gym-', suffix='.txt', dir=directory["dir1"])
        with os.fdopen(fd, 'w') as fp:
            fp.write('Monkey Bars!\n')


## Upload temp files, inside of directory to bucket
def upload_files(path):

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
               bucket.put_object (Key=full_path, Body=data)
        for obj in bucket.objects.all():
            names = [bucket.name,obj.key]

temp_files()
upload_files(directory["dir1"])

## Print data in bucket - Testing

#for bucket in bucket.objects.all():
#    print(bucket)


#!/usr/bin/env python3

import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('jaysons-files-bucket')

for bucket in bucket.objects.all():
    print(bucket)

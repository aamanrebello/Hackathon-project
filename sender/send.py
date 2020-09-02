#!/usr/bin/env python
import boto3
s3 = boto3.resource("s3")
bucket_name = "aamanrebellohack"
object_name = "readings.txt"
try:
 response = s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'))
 print(response)
except Exception as error:
 print(error)

# NOTE: Above function essentially sends a file (which will always be called readings.txt) to
# an S3 bucket called aamanrebellohack.

# This is what was created for the purposes of the hackathon, although naturally there is a need
# to scale up the code with modules and functions if we wish to implement this idea on a larger scale.
# There may be more than one buckets and the file may not always be called readings.txt 

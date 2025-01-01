import boto3
import logging
from botocore.exceptions import ClientError

my_bucket_name= 'eunorht-fg-34i9j3f9j39rfji8jf4i'  # Bucket name must be unique
my_region = CreateBucketConfiguration={
     'LocationConstraint': 'eu-north-1'
 }
file_name ='buckets_list'
t = 'w'
s3_client=boto3.client('s3')



def create_bucket(s3_client, bucket_name, region=None):
    try:
        if region is None:  
           # s3_client=boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name) # Bucket (string) – [REQUIRED]
        else:
            # s3_client=boto3.client('s3')
             location = {'LocationConstraint': region} # eu-east-1 = location by default 
             s3_client.create_bucket(Bucket=bucket_name,
                                     CreateBucketConfiguration=region)

    except ClientError as e:
        logging.error(e)
        return False
    return True


def writeBucketsToFile(s3_client,file_name, t ):
    try:
        with open(file_name, t) as o:
            response = s3_client.list_buckets()
            for i in response['Buckets']:
                o.write(i['Name']+'\n')
        print(f"Bucket names have been written to {file_name}")
    except FileNotFoundError as ef:
        print(f"Error::::: {ef} ")



#create_bucket(my_bucket_name, my_region)

writeBucketsToFile(s3_client, file_name, t)

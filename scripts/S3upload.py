import boto3
from pathlib import Path

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = Path(file_name).name 

    s3_client = boto3.client('s3',region_name='ap-south-1')
    s3_client.upload_file(file_name, bucket, object_name)

if __name__ == "__main__":
    bucket = 'retailsbucketpro'
    file_path = Path('../data/processed_sales_data.csv').resolve()
    upload_to_s3(str(file_path), bucket)

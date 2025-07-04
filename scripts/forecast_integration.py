import boto3

def create_forecast_dataset(dataset_name):
    client = boto3.client('forecast')
    response = client.create_dataset(DatasetName=dataset_name, Domain="RETAIL")
    return response

def create_dataset_import_job(dataset_arn, data_source):
    client = boto3.client('forecast')
    response = client.create_dataset_import_job(
        DatasetImportJobName='retail_sales_import',
        DatasetArn=dataset_arn,
        DataSource={
            'S3Config': {
                'Path': data_source,
                'RoleArn': 'arn:aws:iam::YOUR_ACCOUNT_ID:role/forecast-role'
            }
        }
    )
    return response

if __name__ == "__main__":
    dataset_response = create_forecast_dataset('retail_sales')
    dataset_arn = dataset_response['DatasetArn']
    data_source = 's3://your-bucket/processed_sales_data.csv'
    import_job_response = create_dataset_import_job(dataset_arn, data_source)
    print(import_job_response)

import boto3
import sagemaker
from sagemaker import get_execution_role

def train_model(bucket, data_path):
    sagemaker_session = sagemaker.Session()
    role = get_execution_role()

   
    container = sagemaker.image_uris.retrieve('forecasting-deepar', boto3.Session().region_name)


    estimator = sagemaker.estimator.Estimator(
        image_uri=container,
        role=role,
        instance_count=1,
        instance_type='ml.m4.xlarge',
        output_path=f's3://{bucket}/output',
        sagemaker_session=sagemaker_session
    )

   
    estimator.set_hyperparameters(
        time_freq='D',  
        context_length=7,
        prediction_length=7,
        epochs=100,
        mini_batch_size=32
    )

    estimator.fit({'train': data_path})

if __name__ == "__main__":
    bucket = 'retailsbucketpro'
    data_path = f's3://{bucket}/data/processed_sales_data.csv'
    train_model(bucket, data_path)

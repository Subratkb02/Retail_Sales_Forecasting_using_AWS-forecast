import boto3
import sagemaker
from sagemaker import get_execution_role
import os

def get_sagemaker_role():
    """Get the SageMaker execution role, with fallback for local development."""
    try:
        # Try to get execution role if running in SageMaker environment
        return get_execution_role()
    except ValueError:
        # Fallback for local development - use environment variable or default
        role_arn = os.environ.get('SAGEMAKER_ROLE_ARN')
        if role_arn:
            return role_arn
        else:
            # You need to replace this with your actual SageMaker execution role ARN
            # Create a role in IAM with SageMaker permissions and replace the ARN below
            return "arn:aws:iam::767828725519:role/SageMakerExecutionRole"

def train_model(bucket, data_path):
    sagemaker_session = sagemaker.Session()
    role = get_sagemaker_role()

   
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

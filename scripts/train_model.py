import boto3
import sagemaker
from sagemaker import get_execution_role
import os


def get_sagemaker_role():
    """Get the SageMaker execution role, with fallback for local development."""
    try:
        return get_execution_role()
    except ValueError:
        role_arn = os.environ.get('SAGEMAKER_ROLE_ARN')
        if role_arn:
            return role_arn
        else:
            return "arn:aws:iam::767828725519:role/Sagemaker_Retail"


def train_model(bucket, data_path):
    sagemaker_session = sagemaker.Session()
    role = get_sagemaker_role()

    # Retrieve the container image for the DeepAR algorithm
    container = sagemaker.image_uris.retrieve('forecasting-deepar', boto3.Session().region_name)

    # Create an Estimator object
    estimator = sagemaker.estimator.Estimator(
        image_uri=container,
        role=role,
        instance_count=1,
        instance_type='ml.m4.xlarge',
        output_path=f's3://{bucket}/output',
        sagemaker_session=sagemaker_session
    )

    # Set hyperparameters for the model training
    estimator.set_hyperparameters(
        time_freq='D',  # Daily frequency
        context_length=7,
        prediction_length=7,
        epochs=100,
        mini_batch_size=32
    )

    # Start the training job
    estimator.fit({'train': data_path})


if __name__ == "__main__":
    bucket = 'retailsbucketpro'
    data_path = f's3://{bucket}/data/processed_sales_data.csv'
    train_model(bucket, data_path)
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

def deploy_model(bucket):
    sagemaker_session = sagemaker.Session()
    role = get_sagemaker_role()

   
    model = sagemaker.model.Model(
        image_uri=sagemaker.image_uris.retrieve('forecasting-deepar', boto3.Session().region_name),
        model_data=f's3://{bucket}/output/model.tar.gz',
        role=role,
        sagemaker_session=sagemaker_session
    )
    predictor = model.deploy(initial_instance_count=1, instance_type='ml.t2.medium')

    return predictor

if __name__ == "__main__":
    bucket = 'retailsbucketpro'
    predictor = deploy_model(bucket)
    predictor.delete_endpoint()

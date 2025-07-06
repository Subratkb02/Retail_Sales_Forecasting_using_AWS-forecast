# SageMaker Setup Guide

## Issue Resolution

The error you encountered occurs because `get_execution_role()` only works when running inside a SageMaker environment (SageMaker Studio, SageMaker notebooks, or SageMaker training jobs). When running locally, your AWS identity is a user, not a role.

## Solution

The code has been updated to use `get_sagemaker_role()` function which provides fallback logic for local development.

## Setup Instructions

### Option 1: Create a SageMaker Execution Role (Recommended)

1. Go to AWS IAM Console
2. Create a new role with the following:
   - Trust entity: SageMaker service
   - Permissions: 
     - `AmazonSageMakerFullAccess`
     - `AmazonS3FullAccess` (or a more restrictive policy for your S3 bucket)
3. Copy the ARN of the created role
4. Replace the default ARN in both `train_model.py` and `deploy_model.py` files:
   ```python
   return "arn:aws:iam::767828725519:role/YourSageMakerExecutionRole"
   ```

### Option 2: Use Environment Variable

Set the environment variable `SAGEMAKER_ROLE_ARN` with your role ARN:

**Windows (PowerShell):**
```powershell
$env:SAGEMAKER_ROLE_ARN="arn:aws:iam::767828725519:role/YourSageMakerExecutionRole"
```

**Windows (Command Prompt):**
```cmd
set SAGEMAKER_ROLE_ARN=arn:aws:iam::767828725519:role/YourSageMakerExecutionRole
```

**Linux/Mac:**
```bash
export SAGEMAKER_ROLE_ARN="arn:aws:iam::767828725519:role/YourSageMakerExecutionRole"
```

### Required IAM Permissions

Your SageMaker execution role should have permissions to:
- Access S3 buckets (read/write)
- Create and manage SageMaker training jobs
- Create and manage SageMaker endpoints
- Access to container images in ECR

## Running the Code

After setting up the role, you can run the training script:

```bash
python scripts/train_model.py
```

## Notes

- The fallback mechanism will work in both local development and SageMaker environments
- Make sure your AWS credentials are configured properly (`aws configure`)
- The role ARN format: `arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME`

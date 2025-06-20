# Terraform Infrastructure for mdepew-agent

This directory contains Terraform configurations that set up the complete infrastructure for the mdepew-agent application on Google Cloud Platform. The infrastructure is designed to support a CI/CD pipeline with staging and production environments.

## Overview

The Terraform configuration in this directory provisions the following resources:

- **Service Accounts**: Creates dedicated service accounts for Cloud Build and Cloud Run
- **API Enablement**: Enables necessary Google Cloud APIs across all projects
- **Storage Resources**: Creates GCS buckets and Artifact Registry repositories
- **IAM Permissions**: Sets up appropriate IAM roles and permissions
- **CI/CD Pipelines**: Configures Cloud Build triggers for PR checks and deployments
- **Logging & Monitoring**: Sets up log sinks and BigQuery datasets for telemetry and feedback

## Project Structure

The infrastructure is split across multiple Google Cloud projects:

- **CICD Runner Project**: Hosts the CI/CD pipeline components (Cloud Build)
- **Staging Project**: Hosts the staging environment
- **Production Project**: Hosts the production environment

## Key Components

### Service Accounts

- **CICD Runner SA**: Service account for running Cloud Build pipelines
- **Cloud Run App SA**: Service account for the application running in Cloud Run

### Storage Resources

- **Artifact Registry**: Docker repository for storing container images
- **GCS Buckets**: 
  - Load test results bucket
  - Logs data buckets for each environment

### CI/CD Pipeline

Three Cloud Build triggers are configured:

1. **PR Checks**: Triggered on pull requests to the main branch
2. **CD Pipeline**: Triggered on pushes to the main branch, deploys to staging
3. **Deploy to Production**: Manual trigger with approval required for production deployment

### Logging & Monitoring

- **BigQuery Datasets**: Separate datasets for telemetry and feedback data
- **Log Sinks**: Configured to export logs to BigQuery for analysis

## Configuration

The infrastructure is configured through variables defined in the `vars/env.tfvars` file:

- `project_name`: Base name used for resource naming
- `prod_project_id`: Google Cloud project ID for production
- `staging_project_id`: Google Cloud project ID for staging
- `cicd_runner_project_id`: Google Cloud project ID for CI/CD
- `host_connection_name`: Name of the GitHub connection in Cloud Build
- `repository_name`: GitHub repository name
- `region`: Google Cloud region for resource deployment

## Usage

### Prerequisites

- Terraform v1.0+
- Google Cloud SDK
- Appropriate permissions on the Google Cloud projects

### Deployment Steps

1. Initialize Terraform:
   ```
   terraform init
   ```

2. Plan the deployment:
   ```
   terraform plan -var-file=vars/env.tfvars
   ```

3. Apply the configuration:
   ```
   terraform apply -var-file=vars/env.tfvars
   ```

### Important Notes

- Before running Terraform, ensure that the GitHub connection is properly set up in Cloud Build
- The host_connection_name variable in env.tfvars must match the name of your GitHub connection
- The repository_name variable should be in the format "owner/repo"
- Make sure all required APIs are enabled in your projects before running Terraform

## Troubleshooting

Common issues:
- **Resource not found errors**: Ensure all required APIs are enabled
- **Permission denied errors**: Check IAM permissions for the account running Terraform
- **GitHub connection errors**: Verify the GitHub connection is properly set up in Cloud Build

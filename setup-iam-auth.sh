#!/bin/bash

PROJECT_ID="nicer-garlic-app"
SERVICE_ACCOUNT="garlic-api-sa"

# 1. Create service account
gcloud iam service-accounts create $SERVICE_ACCOUNT \
  --display-name="Garlic API Service Account" \
  --project=$PROJECT_ID

# 2. Grant Cloud SQL IAM permissions
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"

# 3. Create database user for IAM authentication
gcloud sql users create $SERVICE_ACCOUNT@$PROJECT_ID.iam \
  --instance=dev-nicergarlic-pg \
  --type=cloud_iam_service_account \
  --project=$PROJECT_ID

# 4. Grant database permissions (connect to database and run)
echo "Connect to your database and run:"
echo "GRANT CONNECT ON DATABASE garlicp2 TO \"$SERVICE_ACCOUNT@$PROJECT_ID.iam\";"
echo "GRANT USAGE ON SCHEMA public TO \"$SERVICE_ACCOUNT@$PROJECT_ID.iam\";"
echo "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO \"$SERVICE_ACCOUNT@$PROJECT_ID.iam\";"
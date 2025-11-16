#!/bin/bash

# Authorize Cloud Run IP ranges for Cloud SQL access
gcloud sql instances patch dev-nicergarlic-pg \
  --authorized-networks=0.0.0.0/0 \
  --project=nicer-garlic-app

echo "Authorized all IP ranges for Cloud SQL access"
echo "Note: This allows all IPs. For production, use specific Cloud Run IP ranges."
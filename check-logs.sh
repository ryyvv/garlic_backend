#!/bin/bash

# Check Cloud Run logs for errors
gcloud logging read 'resource.type="cloud_run_revision" AND resource.labels.service_name="garlic-backend" AND severity>=ERROR' \
  --limit=10 \
  --project=nicer-garlic-app \
  --format="table(timestamp,severity,textPayload)"

echo ""
echo "=== Recent application logs ==="
gcloud logging read 'resource.type="cloud_run_revision" AND resource.labels.service_name="garlic-backend"' \
  --limit=20 \
  --project=nicer-garlic-app \
  --format="table(timestamp,severity,textPayload)"
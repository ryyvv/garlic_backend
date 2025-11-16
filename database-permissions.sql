-- Run these commands in PostgreSQL after connecting with:
-- gcloud sql connect dev-nicergarlic-pg --user=postgres --project=nicer-garlic-app

GRANT CONNECT ON DATABASE garlicp2 TO "garlic-api-sa@nicer-garlic-app.iam";
GRANT USAGE ON SCHEMA public TO "garlic-api-sa@nicer-garlic-app.iam";
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO "garlic-api-sa@nicer-garlic-app.iam";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO "garlic-api-sa@nicer-garlic-app.iam";

-- Grant permissions on future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO "garlic-api-sa@nicer-garlic-app.iam";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO "garlic-api-sa@nicer-garlic-app.iam";
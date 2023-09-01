/api-lambda-python
|-- .gitignore
|-- README.md
|-- package.json (or requirements.txt for Python)
|-- serverless.yml (or template.yaml for AWS SAM)
|
|-- /src
|   |-- /lambda
|   |   |-- /auth
|   |   |   |-- handler.py (User Authentication & Authorization)
|   |   |-- /items
|   |   |   |-- create.py
|   |   |   |-- read.py
|   |   |   |-- update.py
|   |   |   |-- delete.py
|   |   |-- /files
|   |   |   |-- upload.py
|   |   |   |-- delete.py
|   |   |-- /notifications
|   |   |   |-- send.py
|   |   |   |-- retrieve.py
|   |   |-- /search
|   |   |   |-- handler.py (Search Functionality)
|   |   |-- /logs
|   |   |   |-- activity.py (User Activity Logs)
|   |   |   |-- search.py (Search Logs)
|   |
|   |-- /shared
|   |   |-- utils.py
|   |   |-- database.py
|   |   |-- s3_helper.py (For S3 interactions)
|   |   |-- cognito_helper.py (For Cognito interactions)
|
|-- /tests
|   |-- /unit
|   |   |-- test_auth.py
|   |   |-- test_items.py
|   |   |-- test_files.py
|   |   |-- test_notifications.py
|   |   |-- test_search.py
|   |   |-- test_logs.py
|   |
|   |-- /integration
|       |-- test_api_endpoints.py
|
|-- /docs
|   |-- DOCUMENTATION.md (API Documentation)

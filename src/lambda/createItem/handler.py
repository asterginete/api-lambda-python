import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'YourDynamoDBTableName'
table = dynamodb.Table(table_name)

def create_item(item):
    try:
        response = table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Item created successfully')
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Error: {e.response['Error']['Message']}")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Unexpected error: {str(e)}")
        }

def lambda_handler(event, context):
    # Extract the body from the event
    body = json.loads(event['body'])
    
    # Call the create_item function
    return create_item(body)

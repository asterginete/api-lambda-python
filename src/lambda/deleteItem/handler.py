import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'YourDynamoDBTableName'
table = dynamodb.Table(table_name)

def delete_item(key):
    try:
        table.delete_item(Key=key)
        return {
            'statusCode': 200,
            'body': json.dumps('Item deleted successfully')
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
    # Extract the primary key from the pathParameters
    key = event['pathParameters']
    
    # Convert string numbers to integers if your primary key is of type number
    # for k, v in key.items():
    #     if v.isdigit():
    #         key[k] = int(v)
    
    # Call the delete_item function
    return delete_item(key)

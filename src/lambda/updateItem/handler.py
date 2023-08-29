import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'YourDynamoDBTableName'
table = dynamodb.Table(table_name)

def update_item(key, update):
    try:
        update_expression = "SET " + ", ".join([f"{k}=:{k}" for k in update.keys()])
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues={f":{k}": v for k, v in update.items()},
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Item updated successfully')
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
    
    # Extract the update data from the body
    update_data = json.loads(event['body'])
    
    # Call the update_item function
    return update_item(key, update_data)

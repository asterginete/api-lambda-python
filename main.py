import boto3
import json

dynamodb = boto3.resource('dynamodb')
table_name = 'ItemTable'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    http_method = event['httpMethod']
    body = json.loads(event['body']) if event['body'] else {}
    path_parameters = event['pathParameters']

    if http_method == 'POST':
        return create_item(body)
    elif http_method == 'GET':
        return read_item(path_parameters)
    elif http_method == 'PUT':
        return update_item(path_parameters, body)
    elif http_method == 'DELETE':
        return delete_item(path_parameters)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }


def create_item(item):
    response = table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps('Item created successfully')
    }

def read_item(key):
    response = table.get_item(Key=key)
    item = response.get('Item', {})
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def update_item(key, update):
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

def delete_item(key):
    table.delete_item(Key=key)
    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
    }

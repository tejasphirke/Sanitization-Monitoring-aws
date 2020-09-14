import json
import boto3
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('sanitizerAppDB')
def lambda_handler(event, context):
    # TODO implement
    table.put_item(Item=event)
    return {
        "code": 200,
        "message": "Registeration Successful"
    }

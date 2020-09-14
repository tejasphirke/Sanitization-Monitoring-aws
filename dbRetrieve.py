import json
import boto3
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('sanitizerAppDB')

def lambda_handler(event, context):
    # TODO implement
    name=event['Name']
    print("Name")
    print(name)
    resp = table.get_item(Key={"Name":name})
    return resp['Item']

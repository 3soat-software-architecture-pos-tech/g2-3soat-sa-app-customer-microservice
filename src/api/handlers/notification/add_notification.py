import json
import boto3

from datetime import datetime

def handler(event, context):
    print(event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Notifications')
    record = json.loads(event['Records'][0]['body'])

    try:
        new_record = {
            "id": str(record['id']),
            "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
            "customer_id": str(record['customer_id']),
            "status_order": record['statusOrder']
        }

        response = table.put_item(Item=new_record)

        return {
            "statusCode": 200,
            "message": response
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "message": e
        }
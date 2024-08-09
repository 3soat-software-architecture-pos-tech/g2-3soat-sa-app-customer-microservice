import boto3
from boto3.dynamodb.conditions import Attr

def handler(event, context):
    try:
        customer_id_value = event['pathParameters']['id']
        
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('Notifications')

        response = table.scan(
            FilterExpression=Attr('customer_id').eq(customer_id_value)
        )

        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "content": items
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "message": e
        }
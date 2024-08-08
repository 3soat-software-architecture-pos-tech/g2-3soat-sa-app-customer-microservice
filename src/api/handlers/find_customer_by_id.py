import json
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.find_customer_by_id import FindCustomerByIdUseCase

def handler(event, context):
    customer_id = event['pathParameters']['id']
    repository = DynamoDBCustomerRepository()
    use_case = FindCustomerByIdUseCase(repository)
    customer = use_case.execute(customer_id)
    if customer:
        return {
            'statusCode': 200,
            'body': json.dumps(customer.dict())
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Customer not found'})
        }

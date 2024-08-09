import json
from src.core.entities.customer import Customer
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.update_customer import UpdateCustomerUseCase

def handler(event, context):
    customer_id = event['pathParameters']['id']
    data = json.loads(event['body'])
    customer = Customer(id=customer_id, **data)
    repository = DynamoDBCustomerRepository()
    use_case = UpdateCustomerUseCase(repository)
    use_case.execute(customer)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Customer updated successfully'})
    }

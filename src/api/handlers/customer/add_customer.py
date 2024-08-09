import json
from src.core.entities.customer import Customer
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.add_customer import AddCustomerUseCase

def handler(event, context):
    data = json.loads(event['body'])
    customer = Customer(**data)
    repository = DynamoDBCustomerRepository()
    use_case = AddCustomerUseCase(repository)
    use_case.execute(customer)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Customer added successfully'})
    }

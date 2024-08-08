import json
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.delete_customer import DeleteCustomerUseCase

def handler(event, context):
    customer_id = event['pathParameters']['id']
    repository = DynamoDBCustomerRepository()
    use_case = DeleteCustomerUseCase(repository)
    use_case.execute(customer_id)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Customer deleted successfully'})
    }

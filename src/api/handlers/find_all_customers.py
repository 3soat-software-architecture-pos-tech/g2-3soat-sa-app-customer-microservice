import json
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.find_all_customers import FindAllCustomersUseCase

def handler(event, context):
    repository = DynamoDBCustomerRepository()
    use_case = FindAllCustomersUseCase(repository)
    customers = use_case.execute()
    return {
        'statusCode': 200,
        'body': json.dumps([customer.dict() for customer in customers])
    }

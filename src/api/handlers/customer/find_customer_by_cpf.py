import json
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.use_cases.find_customer_by_cpf import FindCustomerByCpfUseCase

def handler(event, context):
    cpf = event['pathParameters']['cpf']
    repository = DynamoDBCustomerRepository()
    use_case = FindCustomerByCpfUseCase(repository)
    customer = use_case.execute(cpf)
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

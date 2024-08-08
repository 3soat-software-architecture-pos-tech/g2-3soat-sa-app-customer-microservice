import boto3
from boto3.dynamodb.conditions import Key
from typing import List
from src.core.entities.customer import Customer
from src.core.interfaces.customer_repository import CustomerRepository

class DynamoDBCustomerRepository(CustomerRepository):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('Customers')

    def add(self, customer: Customer) -> None:
        self.table.put_item(Item=customer.dict())

    def find_all(self) -> List[Customer]:
        response = self.table.scan()
        return [Customer(**item) for item in response['Items']]

    def find_by_id(self, customer_id: str) -> Customer:
        response = self.table.get_item(Key={'id': customer_id})
        return Customer(**response['Item']) if 'Item' in response else None

    def find_by_cpf(self, cpf: str) -> Customer:
        response = self.table.query(
            IndexName='CpfIndex',
            KeyConditionExpression=Key('cpf').eq(cpf)
        )
        return Customer(**response['Items'][0]) if response['Items'] else None

    def delete_by_id(self, customer_id: str) -> None:
        self.table.delete_item(Key={'id': customer_id})

    def update_by_id(self, customer: Customer) -> None:
        self.table.put_item(Item=customer.dict())

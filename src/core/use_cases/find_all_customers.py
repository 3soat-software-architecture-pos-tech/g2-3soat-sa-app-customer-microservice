from typing import List
from src.core.entities.customer import Customer
from src.core.interfaces.customer_repository import CustomerRepository

class FindAllCustomersUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self) -> List[Customer]:
        return self.repository.find_all()

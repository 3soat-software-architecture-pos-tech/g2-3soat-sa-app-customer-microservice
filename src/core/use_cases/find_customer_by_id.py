from src.core.entities.customer import Customer
from src.core.interfaces.customer_repository import CustomerRepository

class FindCustomerByIdUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: str) -> Customer:
        return self.repository.find_by_id(customer_id)

from src.core.entities.customer import Customer
from src.core.interfaces.customer_repository import CustomerRepository

class AddCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer: Customer):
        self.repository.add(customer)

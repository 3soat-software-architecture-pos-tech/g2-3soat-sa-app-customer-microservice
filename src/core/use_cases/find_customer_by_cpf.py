from src.core.entities.customer import Customer
from src.core.interfaces.customer_repository import CustomerRepository

class FindCustomerByCpfUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, cpf: str) -> Customer:
        return self.repository.find_by_cpf(cpf)

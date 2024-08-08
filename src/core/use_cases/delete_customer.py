from src.core.interfaces.customer_repository import CustomerRepository

class DeleteCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: str):
        self.repository.delete_by_id(customer_id)

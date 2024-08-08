from abc import ABC, abstractmethod
from typing import List
from src.core.entities.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def add(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def find_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Customer:
        pass

    @abstractmethod
    def delete_by_id(self, customer_id: str) -> None:
        pass

    @abstractmethod
    def update_by_id(self, customer: Customer) -> None:
        pass

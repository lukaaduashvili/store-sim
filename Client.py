from abc import abstractmethod
from typing import List

from Item import Item


class ClientInterface:
    @abstractmethod
    def get_client_products(self) -> List[Item]:
        pass

    @abstractmethod
    def add_item_to_basket(self, item: Item) -> None:
        pass

    @abstractmethod
    def remove_item_from_basket(self, item: Item) -> None:
        pass


class StoreClient(ClientInterface):
    def __init__(self) -> None:
        self._products: List[Item] = []

    def get_client_products(self) -> List[Item]:
        return self._products

    def add_item_to_basket(self, item: Item) -> None:
        self._products.append(item)

    def remove_item_from_basket(self, item: Item) -> None:
        self._products.remove(item)

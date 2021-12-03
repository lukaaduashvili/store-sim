from abc import abstractmethod
from typing import List

from Item import Item


class Receipt:
    @abstractmethod
    def add_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass


class ClerkReceipt(Receipt):
    all_items: dict[str, int] = dict()
    totalSum: int = 0

    def add_item(self, item: Item) -> None:
        if item.name in self.all_items:
            self.all_items[item.name] = self.all_items[item.name] + item.amount
        else:
            self.all_items.update({item.name: item.amount})
        self.totalSum += item.price * item.amount

    def to_string(self) -> str:
        final_receipt: str = ""
        final_receipt += "Name      | Units |\n"
        final_receipt += "----------|-------|\n"
        for item in self.all_items:
            amount: int = self.all_items[item]
            final_receipt += "{:10s}|  {:3d}  |\n".format(item, amount)
        final_receipt += f"\nTotal Revenue: {self.totalSum}"
        return final_receipt


class ClientReceipt(Receipt):
    items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def to_string(self) -> str:
        final_receipt: str = ""
        final_receipt += "Name      | Units | Price | Total |\n"
        final_receipt += "----------|-------|-------|-------|\n"
        for item in self.items:
            final_receipt += "{:10s}|  {:3d}  |  {:3d}  |  {:3d}  |\n".format(
                item.name, item.amount, item.price, item.price * item.amount
            )
        return final_receipt

from abc import abstractmethod
from typing import List

from Discount import StoreDiscount
from Item import Item


class Receipt:
    @abstractmethod
    def add_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass

    @abstractmethod
    def get_client_items(self) -> List[Item]:
        pass

    def change_price(self, item: Item, price: float) -> None:
        pass


class ClerkReceipt(Receipt):
    def __init__(self) -> None:
        self.all_items: dict[str, int] = dict()
        self.total_sum: float = 0

    def add_item(self, item: Item) -> None:
        if item.name in self.all_items:
            self.all_items[item.name] = self.all_items[item.name] + item.amount
        else:
            self.all_items.update({item.name: item.amount})
        self.total_sum += item.price * item.amount

    def change_price(self, item: Item, price: float) -> None:
        self.total_sum -= item.price * item.amount
        self.total_sum += item.amount * item.price

    def to_string(self) -> str:
        final_receipt: str = ""
        final_receipt += "Name      | Units |\n"
        final_receipt += "----------|-------|\n"
        for item in self.all_items:
            amount: int = self.all_items[item]
            final_receipt += "{:10s}|  {:3d}  |\n".format(item, amount)
        final_receipt += f"\nTotal Revenue: {self.total_sum}"
        return final_receipt

    def get_client_items(self) -> List[Item]:
        pass


class ClientReceipt(Receipt):
    def __init__(self, disc: StoreDiscount) -> None:
        self.discount: StoreDiscount = disc
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def to_string(self) -> str:
        final_receipt: str = ""
        final_receipt += "Name      |  Units  |  Price  |  Total  |\n"
        final_receipt += "----------|---------|---------|---------|\n"
        total_price: float = 0
        for item in self.items:
            final_receipt += "{:10s}|  {:3d}    |   {:3.2f}  |   {:3.2f}  |\n".format(
                item.name, item.amount, item.price, item.price * item.amount
            )
            total_price += item.price * item.amount
        final_receipt += f"Sum: {total_price}"
        return final_receipt

    def get_client_items(self) -> List[Item]:
        return self.items

    def change_price(self, item: Item, price: float) -> None:
        self.items.remove(item)
        new_item: Item = Item()
        new_item.price = price
        new_item.name = item.name
        new_item.amount = item.amount
        self.items.append(new_item)

    def apply_discount(self) -> None:
        disc: List[List[Item]] = self.discount.get_bundle_items()
        prices: List[float] = self.discount.get_bundle_discount()
        for i in range(len(disc)):
            cnt: int = 0
            for item in disc[i]:
                if item in self.get_client_items():
                    cnt += 1
                if cnt == len(disc[i]):
                    print("here")
                    self.discount_items(prices[i], i)
                    break

    def discount_items(self, percent: float, bundle_num: int) -> None:
        for item in self.discount.get_bundle_items()[bundle_num]:
            self.change_price(item, item.price * percent)

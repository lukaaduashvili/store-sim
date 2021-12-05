from typing import List

import Client
import Discount
from observerInterfaces import Observer, Subject
from Receipt import ClerkReceipt, ClientReceipt


class Clerk(Subject):
    _managers: List[Observer] = []
    clerk_receipt: ClerkReceipt = ClerkReceipt()
    _num_receipt: int = 0

    def attach(self, observer: Observer) -> None:
        self._managers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._managers.remove(observer)

    def notify(self, num: int) -> None:
        for observer in self._managers:
            observer.update(self, num)

    def print_x_report(self) -> None:
        print(self.clerk_receipt.to_string())

    def close_cashier(self) -> None:
        self.print_x_report()
        self._num_receipt = 0
        self.clerk_receipt = ClerkReceipt()

    @staticmethod
    def payment_prompt() -> None:
        payment: str = input("Pay with cash or card?")
        if payment == "card":
            print("Customer paid with card")
        else:
            print("Customer paid with cash")

    def process_client(
        self, client: Client.StoreClient, discount: Discount.StoreDiscount
    ) -> None:
        self._num_receipt += 1
        client_receipt: ClientReceipt = ClientReceipt(discount)

        for item in client.get_client_products():
            client_receipt.add_item(item)
        client_receipt.apply_discount()

        for item in client_receipt.get_client_items():
            self.clerk_receipt.add_item(item)
        print(client_receipt.to_string())
        self.payment_prompt()

        if self._num_receipt == 5:
            self.notify(20)
        elif self._num_receipt == 10:
            self.notify(100)

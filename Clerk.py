from typing import List

import Client
import Discount
from observerInterfaces import Observer, Subject
from Receipt import ClerkReceipt, ClientReceipt

X_REPORT_NUM: int = 20
Z_REPORT_NUM: int = 100


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
    def payment_prompt() -> str:
        payment: str = input("Pay with cash or card?")
        if payment == "card":
            return "Customer paid with card"
        return "Customer paid with cash"

    def process_client(
        self, client: Client.StoreClient, discount: Discount.StoreDiscount
    ) -> str:
        self._num_receipt += 1
        client_receipt: ClientReceipt = ClientReceipt(discount)

        for item in client.get_client_products():
            client_receipt.add_item(item)
        client_receipt.apply_discount()

        for item in client_receipt.get_client_items():
            self.clerk_receipt.add_item(item)
        print(client_receipt.to_string())

        if self._num_receipt == X_REPORT_NUM:
            self.notify(self._num_receipt)
        elif self._num_receipt == Z_REPORT_NUM:
            self.notify(self._num_receipt)

        print(self.payment_prompt())
        return self.payment_prompt()

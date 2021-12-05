from __future__ import annotations

from typing import List

from Singleton import Singleton


class ProductDB(metaclass=Singleton):
    Apple: dict[str, str] = {"Name": "Apple", "Price": "3.99"}
    Beer: dict[str, str] = {"Name": "Beer", "Price": "5.50"}
    Milk: dict[str, str] = {"Name": "Milk", "Price": "3.99"}
    Cheese: dict[str, str] = {"Name": "Cheese", "Price": "8.99"}
    Bread: dict[str, str] = {"Name": "Bread", "Price": "2.99"}

    productDb: List[dict[str, str]] = [Apple, Beer, Milk, Cheese, Bread]

    def get_item_price(self, name: str) -> float:
        for item in self.productDb:
            if item["Name"] == name:
                return float(item["Price"])
        return -1

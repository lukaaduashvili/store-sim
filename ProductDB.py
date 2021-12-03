from __future__ import annotations

from typing import List

from Singleton import Singleton


class ProductDB(metaclass=Singleton):
    Apple: dict[str, str] = {"Name": "Apple", "Price": "5"}
    Beer: dict[str, str] = {"Name": "Beer", "Price": "10"}
    productDb: List[dict[str, str]] = [Apple, Beer]

    def get_item_price(self, name: str) -> int:
        for item in self.productDb:
            if item["Name"] == name:
                return int(item["Price"])
        return -1

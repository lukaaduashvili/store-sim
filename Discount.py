from abc import abstractmethod
from typing import List

from Item import Item


class DiscountInterface:
    @abstractmethod
    def add_bundle(self, percent: float) -> None:
        pass

    @abstractmethod
    def add_bundle_items(self, item: Item, bundle_id: int) -> None:
        pass


class StoreDiscount(DiscountInterface):
    _bundleItems: List[List[Item]] = []
    _bundleDiscountPrice: List[float] = []

    def add_bundle(self, percent: float) -> None:
        lst: List[Item] = []
        self._bundleItems.append(lst)
        self._bundleDiscountPrice.append(percent)

    def add_bundle_items(self, item: Item, bundle_id: int) -> None:
        self._bundleItems[bundle_id].append(item)

    def get_bundle_items(self) -> List[List[Item]]:
        return self._bundleItems

    def get_bundle_discount(self) -> List[float]:
        return self._bundleDiscountPrice

from _pytest import monkeypatch

from Clerk import Clerk
from Client import StoreClient
from Discount import StoreDiscount
from Item import FourPackFactory, Item, SingleItemFactory, SixPackFactory
from ProductDB import ProductDB


def test_item() -> None:
    item: Item = Item()
    item.name = "Dog"
    item.amount = 1
    item.price = 3.99
    assert item.name == "Dog"
    assert item.amount == 1
    assert item.price == 3.99


def test_item_db() -> None:
    product_db: ProductDB = ProductDB()
    assert product_db.get_item_price("Apple") == 3.99
    assert product_db.get_item_price("Ixvis tolma") == -1


def test_one_item_factory() -> None:
    one_factory: SingleItemFactory = SingleItemFactory()
    item: Item = one_factory.create_product("Apple")
    assert item.name == "Apple"
    assert item.price == 3.99
    assert item.amount == 1


def test_four_item_factory() -> None:
    four_factory: FourPackFactory = FourPackFactory()
    item: Item = four_factory.create_product("Apple")
    assert item.name == "Apple"
    assert item.price == 3.99
    assert item.amount == 4


def test_six_item_factory() -> None:
    six_factory: SixPackFactory = SixPackFactory()
    item: Item = six_factory.create_product("Apple")
    assert item.name == "Apple"
    assert item.price == 3.99
    assert item.amount == 6


def test_client() -> None:
    client: StoreClient = StoreClient()
    six_factory: SixPackFactory = SixPackFactory()
    item: Item = six_factory.create_product("Apple")
    client.add_item_to_basket(item)
    assert len(client.get_client_products()) == 1
    client.remove_item_from_basket(item)
    assert len(client.get_client_products()) == 0
    one_factory: SingleItemFactory = SingleItemFactory()
    item2: Item = one_factory.create_product("Apple")
    client.add_item_to_basket(item2)
    assert client.get_client_products()[0].amount == 1


def get_store_discount() -> StoreDiscount:
    discount: StoreDiscount = StoreDiscount()
    discount.add_bundle(0.88)
    one_factory: SingleItemFactory = SingleItemFactory()
    item1: Item = one_factory.create_product("Apple")
    item2: Item = one_factory.create_product("Cheese")
    discount.add_bundle_items(item1, 0)
    discount.add_bundle_items(item2, 0)
    return discount


def test_discount() -> None:
    discount: StoreDiscount = get_store_discount()
    assert discount.get_bundle_discount()[0] == 0.88
    assert len(discount.get_bundle_items()[0]) == 2


def test_clerk() -> None:
    clerk: Clerk = Clerk()
    client: StoreClient = StoreClient()
    six_factory: SixPackFactory = SixPackFactory()
    item: Item = six_factory.create_product("Apple")
    client.add_item_to_basket(item)
    discount: StoreDiscount = get_store_discount()
    clerk.process_client(client, discount)

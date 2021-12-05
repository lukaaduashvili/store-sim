from random import randint

from Clerk import Clerk
from Client import StoreClient
from Discount import StoreDiscount
from Item import FourPackFactory, Item, SingleItemFactory, SixPackFactory
from Manager import Manager
from ProductDB import ProductDB


class Simulation:
    def __init__(self, num_sim: int) -> None:
        self.clerk: Clerk = Clerk()
        self.manager: Manager = Manager()
        self.discount: StoreDiscount = StoreDiscount()
        self.product_data: ProductDB = ProductDB()
        self.oneFactory: SingleItemFactory = SingleItemFactory()
        self.fourFactory: FourPackFactory = FourPackFactory()
        self.sixFactory: SixPackFactory = SixPackFactory()
        self.num_sim: int = num_sim

        self.clerk.attach(self.manager)

        self.discount.add_bundle(0.75)
        self.discount.add_bundle_items(self.oneFactory.create_product("Apple"), 0)
        self.discount.add_bundle_items(self.oneFactory.create_product("Beer"), 0)

        self.discount.add_bundle(0.9)
        self.discount.add_bundle_items(self.oneFactory.create_product("Cheese"), 1)
        self.discount.add_bundle_items(self.oneFactory.create_product("Bread"), 1)

    def begin(self) -> None:
        for i in range(self.num_sim):
            client: StoreClient = StoreClient()
            for j in range(randint(3, 10)):
                client.add_item_to_basket(self.choose_random_item())
            self.clerk.process_client(client, self.discount)

    def choose_random_item(self) -> Item:
        pack: int = randint(0, 100)
        product = randint(0, 4)
        p_name: str = ""
        if product == 0:
            p_name = "Apple"
        elif product == 1:
            p_name = "Beer"
        elif product == 2:
            p_name = "Milk"
        elif product == 3:
            p_name = "Cheese"
        elif product == 4:
            p_name = "Bread"

        item: Item = Item()

        if pack < 60:
            item = self.oneFactory.create_product(p_name)
        elif 60 <= pack < 85:
            item = self.fourFactory.create_product(p_name)
        else:
            item = self.sixFactory.create_product(p_name)

        return item

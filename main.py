import Item
import Receipt
from ProductDB import ProductDB

if __name__ == "__main__":
    pDb = ProductDB()
    oneItemFactory = Item.SingleItemFactory()
    fourItemFactory = Item.FourPackFactory()
    receipt: Receipt = Receipt.ClientReceipt()
    receiptF: Receipt = Receipt.ClerkReceipt()

    receipt.add_item(oneItemFactory.create_product("Apple"))
    receiptF.add_item(oneItemFactory.create_product("Apple"))

    receipt.add_item(oneItemFactory.create_product("Beer"))
    receiptF.add_item(oneItemFactory.create_product("Beer"))

    receipt.add_item(fourItemFactory.create_product("Beer"))
    receiptF.add_item(fourItemFactory.create_product("Beer"))

    print(receipt.to_string())
    print(receiptF.to_string())

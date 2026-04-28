class Shopping_Cart:
    def __init__(self, item):
        self.cart = {item: 1}
    def add_item(self, product):
        if product in self.cart:
            self.cart[product] += 1
        else:
            self.cart[product] = 1
    def get_contents(self):
        for item in self.cart:
            return item
    def add_cart(self, cart2):
        for item in cart2.get_contents():
            if item in self.cart:
                self.cart[item] += 1
            else:
                self.cart[item] = 1
        return self.cart
    
cart1 = Shopping_Cart("Bananas")
cart1.add_item("Bread")
cart1.add_item("Bread")
cart1.add_item("Meat")
cart1.add_item("Pasta")
cart1.add_item("Pasta")
cart1.add_item("Sauce")

cart2 = Shopping_Cart("Apples")
cart2.add_item("Avocado")
cart2.add_item("Bananas")
cart2.add_item("Meat")
cart2.add_item("Pasta")
cart2.add_item("Bread")
cart2.add_item("Beans")

print(cart2.get_contents())
print(cart1.get_contents())

#print(cart1.add_cart(cart2))
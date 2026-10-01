class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "qty": quantity})
        print(f"Added: {name} x{quantity} - Rs.{price * quantity}")
    
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"Removed: {name}")
                return
        print(f"{name} not found in cart!")
    
    def show_cart(self):
        if not self.items:
            print("Cart is empty!")
            return
        
        print("\n--- Your Shopping Cart ---")
        total = 0
        for item in self.items:
            item_total = item["price"] * item["qty"]
            total += item_total
            print(f"{item['name']} x{item['qty']} = Rs.{item_total}")
        print(f"Total: Rs.{total}")
        print("--------------------------")

# Example
cart = ShoppingCart()
cart.add_item("Rice 5kg", 1200)
cart.add_item("Milk", 250, 2)
cart.add_item("Bread", 180)
cart.show_cart()
cart.remove_item("Bread")
cart.show_cart()

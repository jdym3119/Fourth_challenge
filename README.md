# Fourth_challenge

### Figure: Attached Files

The first part of the challenge is located in the attached files.

### Restaurant:
Below you will find the second part of the challenge.

```python
class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def calculate_total_price(self, quantity=1):
        return self._price * quantity
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size
    
    def calculate_total_price(self, quantity=1):
        discount = 0.1 if any(isinstance(item["item"], MainCourse) for item in order.items.values()) else 0
        return (self.get_price() * quantity) * (1 - discount)

class Appetizer(MenuItem):
    def __init__(self, name, price, servings):
        super().__init__(name, price)
        self._servings = servings

class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self._ingredients = ingredients

class Order:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, quantity=1):
        if item.get_name() in self.items:
            self.items[item.get_name()]["quantity"] += quantity
        else:
            self.items[item.get_name()] = {"item": item, "quantity": quantity}
    
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]["quantity"]:
                del self.items[item_name]
            else:
                self.items[item_name]["quantity"] -= quantity
        else:
            print(f"'{item_name}' no está en el pedido.")
    
    def calculate_total_bill(self):
        total_bill = 0
        for item_info in self.items.values():
            item = item_info["item"]
            quantity = item_info["quantity"]
            total_bill += item.calculate_total_price(quantity)
        total_bill -= self.calculate_discount()
        return total_bill
    
    def calculate_discount(self):
        if len(self.items) > 3:
            return self.calculate_total_bill() * 0.05
        else:
            return 0

class Payment:
    def __init__(self):
        pass
    
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class Card(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self._number = number
        self._cvv = cvv
    
    def pay(self, amount):
        print(f"Paying {amount} with card {self._number[-4:]}")

class Cash(Payment):
    def __init__(self, amount_given):
        super().__init__()
        self._amount_given = amount_given
    
    def pay(self, amount):
        if self._amount_given >= amount:
            print(f"Payment made in cash. Change: {self._amount_given - amount}")
        else:
            print(f"Insufficient funds. {amount - self._amount_given} short for payment.")

order = Order()
beverage1 = Beverage("Coffee", 1.50, "Small")
beverage2 = Beverage("Tea", 1.50, "Small")
beverage3 = Beverage("Soft drinks", 2.00, "Small")
beverage4 = Beverage("Fruit juice", 2.50, "Small")
beverage5 = Beverage("Water", 1.00, "Small")
beverage6 = Beverage("Sparkling water", 1.50, "Small")
appetizer1 = Appetizer("Potato soup Colombian style", 6.99, 1)
appetizer2 = Appetizer("Fried squid with spicy tomato sauce", 9.99, 1)
main_course1 = MainCourse("Brazilian Steak", 24.99, ["Beef", "Potatoes", "Vegetables"])
main_course2 = MainCourse("Grilled Fish", 18.50, ["Fish", "Rice", "Vegetables"])
main_course3 = MainCourse("Roast Chicken", 16.99, ["Chicken", "Mashed Potatoes", "Green Beans"])

payment1 = Card("1234567890123456", 123)
payment2 = Cash(100)

order.add_item(beverage1)
order.add_item(beverage2)
order.add_item(main_course1)

print(order.calculate_total_bill())
payment1.pay(order.calculate_total_bill())
payment2.pay(order.calculate_total_bill())

```

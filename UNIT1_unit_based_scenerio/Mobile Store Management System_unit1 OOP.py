class Mobile:
    def __init__(self, model_name, brand, price):
        self.model_name = model_name
        self.brand = brand
        self.price = price
        self.category = self.categorize_price()

    def categorize_price(self):
        if self.price >= 50000:
            return "Flagship"
        elif 20000 <= self.price < 50000:
            return "Mid-Range"
        else:
            return "Budget"

    def display(self):
        print(f"Brand: {self.brand:<10} | Model: {self.model_name:<15} | Price: ₹{self.price:<8} | Category: {self.category}")


class MobileStore:
    def __init__(self, store_name):
        self.store_name = store_name
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all_mobiles(self):
        print(f"\n--- {self.store_name} Inventory ---")
        for mobile in self.mobiles:
            mobile.display()


# Execution
store = MobileStore("Smart Tech Store")
store.add_mobile(Mobile("Galaxy S24", "Samsung", 79999))
store.add_mobile(Mobile("Nord CE 4", "OnePlus", 24999))
store.add_mobile(Mobile("Redmi 13C", "Xiaomi", 10999))

store.display_all_mobiles()
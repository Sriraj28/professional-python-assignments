def cash(price): return price
def discount(price): return price * 0.9

def pay(price, strategy=cash):
    return strategy(price)

print(pay(100, cash))      # 100
print(pay(100, discount))  # 90.0
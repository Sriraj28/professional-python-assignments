from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount= float):
        """"All subclasses must implement this method"""
        pass

class UPI(PaymentGateway):
    def pay(self, amount= float):
        print(f"paid {amount} using UPI")

class Card(PaymentGateway):
    def pay(self, amount= float):
        print(f"paid {amount} using Card")

payment = UPI()
payment.pay(500)
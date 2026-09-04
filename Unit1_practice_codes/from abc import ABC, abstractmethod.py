from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float):
        """All subclasses MUST implement this method"""
        pass

class UPI(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paid ₹{amount} using UPI PIN")

class Card(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paid ₹{amount} using Card OTP")

# gateway = PaymentGateway() # Raises TypeError: Can't instantiate abstract class
payment = UPI()
payment.pay(500)

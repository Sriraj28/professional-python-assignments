from abc import ABC, abstractmethod

# 1. Define the PaymentStrategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# 2. Implement Concrete Payment Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount: float) -> None:
        masked_card = f"**** **** **** {self.card_number[-4:]}"
        print(f"Paid ${amount:.2f} using Credit Card ({masked_card})")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using PayPal account ({self.email})")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        masked_wallet = f"{self.wallet_address[:6]}...{self.wallet_address[-4:]}"
        print(f"Paid ${amount:.2f} using Bitcoin Wallet ({masked_wallet})")


# 3. Create PaymentProcessor Context Class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy

    # 4. Allow switching strategies at runtime
    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        if not self._strategy:
            print("Error: No payment method selected!")
            return
        self._strategy.pay(amount)


# Execution / Demonstration
if __name__ == "__main__":
    processor = PaymentProcessor()

    # Credit Card Transaction
    processor.set_strategy(CreditCardPayment("1234567890123456", "John Doe"))
    processor.process_payment(150.00)

    # PayPal Transaction
    processor.set_strategy(PayPalPayment("user@example.com"))
    processor.process_payment(75.50)

    # Bitcoin Transaction
    processor.set_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    processor.process_payment(300.25)
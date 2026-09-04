class BankAccount:
    def __init__(self, owner: str, balance: float ):
        self.owner = owner     #public var
        self._account_type = "Saving"  #protected _var
        self.__balance = balance  #private __var

    #getter
    def get_balance(self):
        return self.__balance

    #setter with validation
    def deposite(self, amount= float):
        if amount > 0:
            self.__balance += amount 
        else:
            print("invalid depsoit amount")

acc = BankAccount("Sriraj", 10000.0)
print(acc.get_balance())

print(acc._BankAccount__balance)

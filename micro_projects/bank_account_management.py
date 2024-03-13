class BankAccount:
    def __init__(
        self,
        account_number: str,
        balance: float = 0
    ):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(
        self,
        amount: float
    ):
        """
        Method to deposit money into the account.
        """
        self.amount = amount
        self.balance += amount

    def withdraw(
        self,
        amount: float
    ):
        """
        Method to withdraw money from the account.
        """
        self.amount = amount
        self.balance -= amount

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """

        print(f"Your balance is: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(
        self,
        account_number: str,
        balance: float = 0,
        interest_rate: float = 0
    ):
        """
        Constructor method to initialize
        the account number, balance, and interest rate.
        """

        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest

    def __repr__(self) -> str:
        saving_balance = f"This savings account balance is: {float(self.balance)}"

        return saving_balance


if __name__ == "__main__":
    bank_account = BankAccount("123456789", 1000)
    bank_account.deposit(500)
    bank_account.withdraw(200)
    bank_account.get_balance()
    saving_account = SavingsAccount("987654321", 2000, 5)
    saving_account.deposit(1000)
    saving_account.calculate_interest()
    print(saving_account)

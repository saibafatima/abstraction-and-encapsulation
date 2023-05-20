# Q4. How can we achieve data abstraction?

definition = "Data abstraction in programming refers to the practice of hiding the internal details and complexity of data objects and providing a simplified and consistent interface for accessing and manipulating the data. This helps in managing complexity, improving code maintainability, and reducing dependencies on the implementation details"

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        # Perform validation or additional logic if needed
        self._balance += amount

    def withdraw(self, amount):
        # Perform validation or additional logic if needed
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Creating an instance of BankAccount
my_account = BankAccount("1234567890", 1000)

# Using the public methods to interact with the account
print("Account number:", my_account.get_account_number())
print("Balance:", my_account.get_balance())

my_account.deposit(500)
print("Balance after deposit:", my_account.get_balance())

my_account.withdraw(200)
print("Balance after withdrawal:", my_account.get_balance())

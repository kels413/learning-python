"""
**Problem: Bank Account Management**

Create a simple program that models a bank account using object-oriented programming in Python.
The `BankAccount` class should have the following attributes and methods:

Attributes:
- `account_number`: A unique identifier for each bank account.
- `account_holder`: The name of the account holder.
- `balance`: The current balance in the account.

Methods:
- `__init__(self, account_number, account_holder, balance)`: Initializes a new bank account
with the given account number, account holder name, and initial balance.
- `deposit(self, amount)`: Deposits the specified amount into the account.
- `withdraw(self, amount)`: Withdraws the specified amount from the account. Ensure that the
 withdrawal amount does not exceed the current balance.
- `get_balance(self)`: Returns the current balance of the account.
"""
import sys
import re

print("Welcome to CS Free Bank")


class User:

    def __init__(self, first_name, last_name, phone_number, email, gender, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
        self.password = password


def receive_input():
    email_trial = 0
    key1 = "@"
    key2 = ".com"

    first_name = input("please Enter your first name ")
    first_name = first_name.title()

    # if any(char.isdigit() for char in first_name):
    digit_in_first_name = re.search("\d", first_name)
    if digit_in_first_name:
        raise ValueError("Name cannot contain digit! ")

    last_name = input("please Enter your last name ")
    last_name = last_name.title()

    digit_in_last_name = re.search("\d", last_name)

    if digit_in_last_name:
        raise ValueError("Last name cannot contain digits!")

    phone_number = input("please input your phone Number ")
    if not phone_number.isdigit():
        raise TypeError("Number must be digit! ")

    email = input("please input your email ")
    check_email_white_space = re.search("\s", email)

    while check_email_white_space:
        email = input("please input your email ")
        print("Email cannot contain white space")
        email_trial += 1
        if email_trial == 3:
            print("because of security reasons! Try again Later")
            sys.exit(1)

    gender = input("please input your gender ")
    password = input("please input your password ")

    user_instance = User(first_name, last_name, phone_number, email, gender, password)

    return user_instance


def display_detail(user):
    print(f"first Name: {user.first_name}")
    print(f"last Name: {user.last_name}")
    print(f"Phone Number: {user.phone_number}")
    print(f"Email: {user.email}")
    print(f"Gender: {user.gender}")
    print(f"Password: {user.password}")


try:
    new_user = receive_input()
    display_detail(new_user)
except ValueError as ve:
    print(f"ValueError ! {ve}")
except TypeError as te:
    print(f"TypeError! {te}")
except Exception as e:
    print(f"An Unexpected Error occurred ! {e}")


class Bank:

    # Init Method
    def __init__(self, account_holder, account_number, balance):

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # deposit Method
    def deposit(self, amount):
        try:
            if isinstance(amount, (int, float)):
                if amount < 10:
                    print("sorry you cannot deposit less than 10$")

                else:
                    print(f"\n{self.account_holder} deposited {amount}$")
                    self.small_under()
                    self.balance += amount
                    return self.balance

            else:
                raise TypeError("Invalid type amount")

        except TypeError as e:
            print(f"Error! {e}")
            self.small_under()

    # Withdrawal Method

    def withdraw(self, amount):

        try:

            if isinstance(amount, (int, float)):
                if amount > self.balance:
                    print("sorry! Insufficient Funds 🤦")

                elif amount < 10:
                    print("sorry you cannot withdraw less than 10$ ")

                elif self.balance - amount < 10:
                    print("10$ meant to be left in the account for maintenance")

                else:
                    print(f"\n{self.account_holder} withdrew {amount}$")
                    self.small_under()
                    self.balance -= amount
                    return self.balance

            else:
                raise TypeError("Invalid input type")

        except TypeError as e:
            self.small_under()
            print(f"Error! {e}")

    def get_balance(self):
        return f"\nCurrent balance {self.balance}$"
        self.small_under()

    def display(self):
        print(f"Account Holder {self.account_holder}\nAccount Number {self.account_number}\nAccount balance {self.balance}")

    def small_under(self):
        print("_" * 80)


kelvin = Bank("kelvin okoye", "2260605690", 100)


# calling methods
# kelvin.small_under()
# kelvin.display()
# kelvin.deposit(30)
# kelvin.deposit("42e")
# kelvin.display()
# kelvin.withdraw(10)
# kelvin.display()
# kelvin.withdraw("423")
# kelvin.small_under()
# print(kelvin.get_balance())

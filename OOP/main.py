# #problem in python
# # """"
# # 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# # Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# # Make a method called describe_restaurant() that prints these two pieces of
# # information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# # Make an instance called restaurant from your class.
# # Print the two attributes individually, and then call both methods.
# #
# # Three Restaurants: Start with your class from Exercise 9-1. Create three
# # different instances from the class, and call describe_restaurant() for each
# # instance.
# # 9-3. Users: Make a class called User. Create two attributes called first_name
# # and last_name, and then create several other attributes that are typically stored
# # in a user profile. Make a method called describe_user() that prints a summary
# # of the user’s information. Make another method called greet_user() that prints
# # a personalized greeting to the user.
# # Create several instances representing different users, and call both methods
# # for each us
# # """
# #
# #
# # # def printLines():
# # #     print()
# # #     for i in range(0,15):
# # #         print("_", end=" ")
# # # print()
# #
#
# class Users:
#     def __init__(self, first_name, last_name, age):
#
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempt = 0
#
#     def describe_user(self):
#         print(f"hello my fist name is {self.first_name}, my last name is {self.last_name} I am {self.age} years old")
#
#     def increament_login_attempt(self):
#         self.login_attempt += 1
#
#     def reset_login_attemp(self):
#         self.login_attempt = 0
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"The name of our restaurant is {self.restaurant_name} and we use {self.cuisine_type} to bring our meal to the world")
#
#
#     def open_restaurant(self):
#
#         print("Hello welcome to our restaurant")
#         print()
#
#     def set_number_served(self, no_served):
#         self.number_served = no_served
#         return no_served
#
#     def read_number_served(self):
#         print(f"we have served {self.number_served} people food")
#
#     def increment_number_served(self, increase_served):
#         self.number_served += increase_served
#
# #
# # restaurant1 = Restaurant("crunchies", "ukpaka")
# # restaurant1.open_restaurant()
# # restaurant1.set_number_served(5)
# # restaurant1.increment_number_served(20)
# # restaurant1.read_number_served()
# #
# # restaurant1.describe_restaurant()
# #
#
#
# user1 = Users("kelly", "okoye", 19,)
# user1.describe_user()
# user1.increament_login_attempt()
# user1.increament_login_attempt()
# user1.increament_login_attempt()
# user1.increament_login_attempt()
# user1.reset_login_attemp()
#
# print(user1.login_attempt)
#

#
# class Add:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#         self.sum = 0
#
#     # def set_Numbers(self, num1, num2):
#     #     self.a = num1
#     #     self.b = num2
#
#     def calc_Numbers(self):
#         self.sum = self.a + self.b
#         return self.sum
#
#     def print_numbers(self):
#         print(f"sum of {self.a} and {self.b} is equal to {self.sum}")
#
#
# numbers = Add(2,2)

# numbers.set_Numbers(2,2)
#
# numbers.calc_Numbers()
#
# numbers.print_numbers()
#

############################################################################################
# single inheritance
#parent classiifii
# class Car:
#     def __init__(self, okechukwu):
#         self.school = 5
#         self.book = "kelly"
#         self.okechukwu = okechukwu
#
#
#     def speedRate(self):
#         print("this is a very high speed car")
#
#     def cost(self):
#         print("but it is very costly")
#
# #subclass
# class ElectricCar(Car):
#
#     def __init__(self, name, okechuwu):
#         super().__init__(okechuwu)
#         self.name = name
#
#     def display_name(self):
#         print(f"name is {self.book}")
#         print(f"second name is {self.okechukwu}")
#     def speedRate(self):
#         super().speedRate()
#         print("it's a lie oo am not that fast")
# carBMW = ElectricCar("kelly", "oke")
# carBMW.display_name()
# print(carBMW.school)


#################################################################################################################

#  multiple inheritance

# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def display(self):
#         return f"car year is {self.year} model is {self.model}"
#
#
# class MercedisCar(Car):
#     def __init__(self, model, year, auto_drive):
#         super().__init__(model, year)
#         self.auto_drive = auto_drive
#
#     def display(self):
#         return f"{super().display()}"
#
#     def display_auto_drive(self):
#         try:
#             if type(self.auto_drive) == bool:
#                 return "Car is Self_drive" if self.auto_drive else "Car is manual"
#             else:
#                 print("only boolean value accepted")
#
#         except Exception as e:
#             return e
#
# class Toyota(MercedisCar):
#     pass
#
#
# BMW = Toyota(2023, "A4", True)
# result = BMW.display()
# result2 = BMW.display_auto_drive()
# print(result, result2)
#
# class Human:
#     def __init__(self):
#         print("I love JESUS")
#         print("Its the JESUS from the human __init__")
#
#     def toCook(self):
#         print("I am cooking")
#
# class wuman:
#     def __init__(self):
#         print("I love JESUS")
#         print("it is the jesus from the wuman __init__")
#
#     # def printName(self):
#     #     return f"this is my name {self.name}"
#     #
#     # def toCook(self):
#     #     print("I am cooking")
#
#
# class man(Human, wuman):
#     def __init__(self):
#       wuman.__init__(self)
#
#
#
# #
# #
# # class man(Human, wuman):
# #     def __init__(self):
# #         wuman.__init__(self)
#
# man1 = man()
# man1.toCook()
#
#
#


import sys

# print("Python version")
print(sys.version)
# print("Version info.")
print(sys.version_info)

import random

# password Generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D',
                     'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X',
                     'Y', 'Z']


# print(letters)
# print(letters_random)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
           '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';',
           ':', ',', '.', '<', '>', '/', '?']


print("Welcome to the PyPassword Generator!")
no_letters = int(input("how many letters would you like in your password?: "))
# no_numbers = int(input("how many numbers would you like ? "))
# no_symbols = int(input("how many symbols would you like ? "))


for i in range(no_letters):
    letters_random = random.randint(1, len(letters))
    random_letters = letters[letters_random]

    print(random_letters, end=" ")
print()
print()

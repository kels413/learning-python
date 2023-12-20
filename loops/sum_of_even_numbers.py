target = int(input("please Enter a Number: "))
total = 0
for i in range(2, target + 1, 2):
    total += i

print(total)


# or you can also use this
#
# for i in range(target + 1):
#     if i % 2 == 0:
#         total += i
# print(total)

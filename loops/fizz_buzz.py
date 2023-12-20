# any number divisible by 3 print Fizz
# any number divisible by 5 print BUZZ
# number divisible by both print FIZZBUZZ


number = range(1, 101)

for i in number:

    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)

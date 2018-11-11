import random

numbers = [x+1 for x in range(20)]
random.shuffle(numbers)

for number in numbers:
    answer = input(str(number))
    if number%3 == 0 and number%5 == 0:
        number = "fizzbuzz"
    elif number%5 == 0:
        number = "buzz"
    elif number%3 == 0:
        number = "fizz"
    else:
        number = str(number)
    if number == answer:
        continue
    else:
        print("wrong")
        break

def is_neat(number):
    divisor = 0
    text = str(number)
    for i in range(len(text)):
        divisor += int(text[i])
    if number % divisor == 0:
        return True
    else:
        return False

for number in range(101,1001):
    print(number,is_neat(number))

def function(values):
    (text, integer, decimal, boolean) = values
    print(text)
    if boolean == True:
        return integer*decimal

text = input("Just type something, anything: ")

while True:
    number = input("Type an integer: ")
    try:
        number = int(number)
        break
    except ValueError:
        print("An INTEGER you monkey")

while True:
    decimal = input("Type a decimal: ")
    try:
        decimal = float(decimal)
        break
    except ValueError:
        print("That was not a decimal you uneducated chip...")

values = (text, number, decimal, True)
print(function(values))

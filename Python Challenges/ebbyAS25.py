values = []

while True:
    value = int(input("Enter a value(e to exit): "))
    if value == "e": break
    else: values.append(value)

for value in values:
    bar = ''
    for i in range(value):
        bar += "*"
    print(bar)

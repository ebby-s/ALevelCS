attempts = 0
while True:
    MyNumber = input("Please enter a number: ")
    try:
        attempts = attempts + 1
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \n asked for a number...")

print(valid_number)
print("seriously? %d attempts?"% attempts)

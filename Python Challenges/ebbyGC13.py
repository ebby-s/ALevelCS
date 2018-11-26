def totalISBN(isbn):
    total = 0
    value = 13
    for num in isbn:
        if value%2 != 0:
            total += int(num)
        else:
            total += 3*int(num)
        value -= 1
    return total

def validate(isbn):
    if totalISBN(isbn)%10 == 0: return True
    else: return False

isbn = input("Enter ISBN: ")
if validate(isbn) == True: print("ISBN number is valid.")
else: print("ISBN is invalid.")

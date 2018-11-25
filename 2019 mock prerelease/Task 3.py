def LeftToInt(phrase,n):
    return int(phrase[0,n])

def Hash(isbn):
    address = LeftToInt(isbn,3)
    return address

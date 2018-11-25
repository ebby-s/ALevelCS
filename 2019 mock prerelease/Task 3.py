def LeftToInt(phrase,n):
    return int(phrase[0,n])

def Hash(isbn):
    address = LeftToInt(isbn,3)
    return address

class BookRecord:
    def __init__(self):
        self.isbn = None
        self.title = None
        self.loan = None

dummyRecord = BookRecord()
dummyRecord.isbn = "0000000000"


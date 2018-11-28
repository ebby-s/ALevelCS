import pickle

def LeftToInt(phrase,n):
    return int(phrase[0:n])

def Hash(isbn):
    address = LeftToInt(isbn,3)
    return address

class BookRecord:
    def __init__(self):
        self.isbn = None
        self.title = None
        self.loan = None
    def __str__(self):
        return "{0} {1} {2}".format(self.isbn,self.title,self.loan)

dummyRecord = BookRecord()
dummyRecord.isbn = "0000000000"

bookFile = open("BookFile.txt","wb")
for i in range(1,1001):
    pickle.dump(dummyRecord,bookFile)
bookFile.close()


newBook = BookRecord()

bookFile = open("Bookfile.txt","ab")
for i in range(5):
    newBook.isbn = input("Enter ISBN: ")
    newBook.title = input("Enter title: ")
    address = Hash(newBook.isbn)
    bookFile.seek(address)
    pickle.dump(newBook,bookFile)
bookFile.close()


bookFile = open("BookFile.txt","rb")
for i in range(1000):
    record = pickle.load(bookFile)
    if record.isbn != "0000000000": print(str(record))
bookFile.close()

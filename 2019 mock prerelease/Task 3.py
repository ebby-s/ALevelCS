import pickle

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
    def __str__(self):
        return "{0} {1} {2}".format(self.isbm,self.title,self.loan)

dummyRecord = BookRecord()
dummyRecord.isbn = "0000000000"

bookFile = open("BookFile.txt","wb")
for i in range(1,1001):
    pickle.dump(dummyRecord,bookFile)
bookFile.close()

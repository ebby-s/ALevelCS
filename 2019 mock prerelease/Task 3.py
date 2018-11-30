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

def open_file(file,mode):
    try: return open(file,mode)
    except: return False

def write_file(file,data,address):
    content = open(file).readlines()
    content[address] = data
    new_file = open(file,"wb")
    for line in content:
        new_file.write(line)

dummyRecord = BookRecord()
dummyRecord.isbn = "0000000000"

bookFile = open("BookFile.txt","wb")
for i in range(1,1001):
    pickle.dump(dummyRecord,bookFile)
bookFile.close()


newBook = BookRecord()

bookFile = open_file("Bookfile.txt","ab")
for i in range(5):
    newBook.isbn = input("Enter ISBN: ")
    newBook.title = input("Enter title: ")
    address = Hash(newBook.isbn)

    address_found = False
    file_full = False
    next_address = address
    while not address_found and not file_full:
        try: if pickle.load(bookFile).isbn != "0000000000": next_address += 1
        except EOFError: next_address = 0
        elif next_address == address: file_full = True
        else: address_found = True
    
    bookFile.seek(next_address)
    write_file("bookFile.txt",pickle.dumps(newBook),next_address)
bookFile.close()


bookFile = open_file("BookFile.txt","rb")
for i in range(1001):
    record = pickle.load(bookFile)
    if record.isbn != "0000000000": print(str(record))
bookFile.close()

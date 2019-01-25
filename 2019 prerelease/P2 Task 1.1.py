def is_int(char):
    try:
        char = int(char)
        return True
    except: return False

def yes(text):
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    name = str(input("Enter Student ID: "))
    email = str(input("Enter email address: "))
    return name+"#"+email

def valid(text):
    [name,email] = text.split("#")
    check = []
    for char in name: check.append(is_int(char))
    if check == [False,False,True,True,True,True]:
        return True
    else: return False

def prnt_list(array):
    array.insert(0,"Name#Email")
    for record in array:
        [name,email] = record.split("#")
        print("{0:>20} {1:>20}".format(name,email))

StudentList = []

while yes("Would you like to input another record?"):
    record = input_record()
    if valid(record): StudentList.append(record)
    else: print("Invalid information")


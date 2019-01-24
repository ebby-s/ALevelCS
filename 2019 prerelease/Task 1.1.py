def is_int(char):
    try:
        char = int(char)
        return True
    except: return False

def yes():
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    name = str(input("Enter name: "))
    email = str(input("Enter email: "))
    return name+"#"+email

def valid(text):
    [name,email] = text.split("#")
    

StudentFile = open("Student File.txt","w")

while yes("Would you like to input a record?"):
    record = input_record()
    if valid(record): file.wite(record)
    else: print("Invalid information")

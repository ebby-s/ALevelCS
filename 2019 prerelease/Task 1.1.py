def is_int(char):
    try:
        char = int(char)
        return True
    except: return False

def yes(text):
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    name = str(input("Enter name: "))
    email = str(input("Enter email: "))
    return name+"#"+email

def valid(text):
    [name,email] = text.split("#")
    check = []
    for char in name: check.append(is_int(char))
    if check == [False,False,True,True,True,True]:
        return True
    else: return False
    
StudentFile = open("Student File.txt","w")

while yes("Would you like to input a record?"):
    record = input_record()
    if valid(record): StudentFile.write(record)
    else: print("Invalid information")

StudentFile.close()

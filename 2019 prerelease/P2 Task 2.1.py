def is_int(char):
    try:
        char = int(char)
        return True
    except: return False

def yes(text):
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    student_id = str(input("Enter Student ID: "))
    email = str(input("Enter email address: "))
    return student_id+"#"+email

def valid(text):
    [student_id,email] = text.split("#")
    check = []
    for char in student_id: check.append(is_int(char))
    if check == [False,False,True,True,True,True]:
        return True
    else: return False
    
StudentFile = open("Student File.txt","w")

while yes("Would you like to input another record?"):
    record = input_record()
    if valid(record): StudentFile.write(record)
    else: print("Invalid information")

StudentFile.close()

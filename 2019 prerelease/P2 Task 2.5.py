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
    dob = str(input("Enter date of birth: "))
    return [student_id,email,dob]

def valid(text):
    [student_id,email,dob] = text
    check = []
    for char in student_id: check.append(is_int(char))
    if check == [False,False,True,True,True,True]:
        return True
    else: return False
    
StudentFile = open("Student File.txt","w")

while yes("Would you like to input another record?"):
    record = input_record()
    if valid(record):
        for elem in record:
            StuderntFile.write(elem)
    else: print("Invalid information")

StudentFile.close()

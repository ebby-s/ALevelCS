def yes(text):
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    name = str(input("Enter name: "))
    email = str(input("Enter email address: "))
    return name+"#"+email

def print_list(array):
    array.insert(0,"Name#Email")
    for record in array:
        [name,email] = record.split("#")
        print("{0:>20} {1:>20}".format(name,email))

StudentList = []

while yes("Would you like to input another record?"):
    record = input_record()
    StudentList.append(record)

print_list(StudentList)


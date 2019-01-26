def yes(text):
    if input(text) in ["Y","y","yes"]: return True
    else: return False

def input_record():
    name = str(input("Enter name: "))
    email = str(input("Enter email address: "))
    dob = str(input("Enter date of birth: "))
    return [name,email,dob]

def print_list(array):
    array.insert(0,["Name","Email","DoB"])
    for record in array:
        if record == [0,0,0]: continue
        [name,email,dob] = record
        print("{0:>20} {1:>20} {2:>10}".format(name,email,dob))

def basic_search(target,array):
    for record in array:
        [name,email,dob] = record
        if name == target: return email
    return "Name not found"

def search(target,array):
    results = []
    for record in array:
        [name,email,dob] = record
        if target in name: results.append(record)
    return results

StudentList = []

while yes("Would you like to input another record?"):
    record = input_record()
    StudentList.append(record)

print_list(StudentList)

search_term = input("Enter a name or part of a name to search: ")
print_list(search(search_term,StudentList))

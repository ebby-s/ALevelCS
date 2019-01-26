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
        if record == "#": continue
        [name,email] = record.split("#")
        print("{0:>20} {1:>20}".format(name,email))

def basic_search(target,array):
    for record in array:
        [name,email] = record.split("#")
        if name == target: return email
    return "Name not found"

def search(target,array):
    results = []
    for record in array:
        [name,email] = record.split("#")
        if target in name: results.append(record)
    return results

StudentList = []

while yes("Would you like to input another record?"):
    record = input_record()
    StudentList.append(record)

print_list(StudentList)

search_term = input("Enter a name or part of a name to search: ")
print_list(search(search_term,StudentList))

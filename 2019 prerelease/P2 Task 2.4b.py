def print_list(array):
    array.insert(0,"Name#Email#DoB")
    for record in array:
        if record == "##": continue
        [name,email,dob] = record.split("#")
        print("{0:>20} {1:>20} {2:>10}".format(name,email,dob))

def basic_search(target,array):
    for record in array:
        [name,email,dob] = record.split("#")
        if name == target: return email
    return "Name not found"

def search(target,array):
    results = []
    for record in array:
        [name,email,dob] = record.split("#")
        if target in name: results.append(record)
    return results

StudentFile = open("Student File.txt")
search_term = str(input("Enter part of name to search: "))

print_list(search(search_term,StudentFile.readlines()))

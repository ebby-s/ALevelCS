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

def arrange(file):
    lines = file.readlines()
    result = []
    for x,elem in enumerate(lines):
        result[x//3].insert(x%3,elem)
    return result

StudentFile = open("Student File.txt")
search_term = str(input("Enter part of name to search: "))

print_list(search(search_term,arrange(StudentFile)))

def basic_search(target,array):
    for record in array:
        [name,email] = record.split("#")
        if name == target: return email
    return "Name not found"

StudentFile = open("Student File.txt")
search_term = str(input("Enter name to search: "))

print(basic_search(search_term,StudentFile.readlines()))

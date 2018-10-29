prefixes = "JKLMNOPQ"
suffix = "uack"

for letter in prefixes:
    print(letter + suffix)

def count_letters(string,letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)

def count_letters2(string,letter):
    count = -1
    pos = 0
    check_pos = 0
    while pos != -1:
        pos = string.find(letter,check_pos)
        check_pos = pos + 1
        count += 1
    print(count)



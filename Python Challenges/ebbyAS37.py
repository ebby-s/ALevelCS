consonants = list("bcdfghjklmnpqrstvwxyz")
text = input("Enter text: ")

converted = ''
for char in list(text):
    if char in consonants: converted += char+"o"+char
    else: converted += char
print(converted)

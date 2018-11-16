text = open("words.txt")
original = (" ").join(text.readlines())

sorted_words = sorted(original.split(" "))

output = open("sorted words.txt","w")

for word in sorted_words:
    output.write(word)

output.close()

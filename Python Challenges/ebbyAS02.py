def search(word,letter):
    found = False
    positions = []
    for i in range (0,len(word),1):
        if word[i] == letter:
            found = True
            positions.append(i)
    return {"found":found,"positions":positions}

word = ["a","a","e","i","u"]
test = search(word,"a")
print(test["found"])
print(test["positions"])

word = "aaeiu"
wlen = len(word)

while True:
    cletter = input("Enter a letter to search: ")
    for i in range (0,wlen,1):
        if word[i] == cletter:
            print(i)
        else:
            "Do nothing"

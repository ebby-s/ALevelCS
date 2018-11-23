wordfile = open("wordlist.txt")
words = wordfile.readlines()

prev_word = None
while True:
    if prev_word = None:
        prev_word = input("Enter a word: ")
        continue

    word = input("Enter a word: ")
    if word not in words or word[0] != prev_word[-1]:
        print("You lose")
        break

    prev_word = word
        

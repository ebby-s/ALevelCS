def letters(word):
    counts = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz': counts[letter] = 0
    for char in word:
        if char in counts.keys():
            counts[char] += 1
    return counts

wordfile = open("wordlist.txt")
words = wordfile.readlines()
for i in range(len(words)): words[i] = words[i].replace("\n","")

anagrams = {}
for word in words:
    anagrams[word] = []
    for compare in words:
        if letters(word) == letters(compare) and word != compare:
            anagrams[word].append(compare)

print(anagrams)

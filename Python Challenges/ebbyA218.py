end = 0

def CheckWord(word):
    check = ((2*word + 0.25)**0.5)-0.5
    if check%1 == 0:
        return check
    else:
        return False

def AddWord(word):
    alphabet = ['"',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    wordsum = 0
    for i in range(len(word)):
        wordsum += alphabet.index(word[i])
    return wordsum

WordList = []
while True:
    with open('p042_words.txt') as f:
        for line in f:
            line = line.strip()
            WordList = line
            WordList = WordList.split('","')
    break

for i in range(len(WordList)):
    end += 1

print(end)

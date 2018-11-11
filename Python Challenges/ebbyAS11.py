import random

WordList = []
while True:
    with open('WordList.txt') as f:
        for line in f:
            line = line.strip()
            WordList.append(line)
    break

def pass_gen(words,punc):
    punc = ";:.,/?\!@#$%^&*()-"
    passcode = ''
    while len(passcode) < 8:
        choice1 = random.choice(words)
        choice2 = random.choice(list(punc))
        passcode += random.choice([choice1,choice2])
    return passcode


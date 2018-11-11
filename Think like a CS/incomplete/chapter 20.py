letters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
phrase = str(input("Enter string: "))

for char in list(phrase):
    if char.lower() in letters:
        letters[char] += 1

for i in letters.keys():
    if letters[i] != 0:
        print(i, letters[i])

word_list = []
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 0

for i in word_count.keys():
    if word_count[i] != 0:
        print(i, word_count[i])

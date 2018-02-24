vowels = ["a","e","i","o","u"]
inword = str(input("Enter a word: "))
vowel_count = 0
for i in range(len(inword)):
    if inword[i] in vowels:
        vowel_count += 1
print(vowel_count)

letters = list('abcdefghijklmnopqrstuvwxyz')
count = {}
for letter in letters:
    count[letter] = 0
text = input("Enter text: ")

for char in list(text):
    if char in letters:
        count[char] += 1

sorted_counts = sorted(count.items(), key=lambda kv: kv[1])

print(sorted_counts[0:3],sorted_counts[23:26])

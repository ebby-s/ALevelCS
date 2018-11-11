file = open("file.txt")
lines = file.readlines()
reversed_file = open("reversed.txt","w")
for line in reversed(lines):
    reversed_file.write(line)
reversed_file.close()

for line in lines:
    if "snake" in line:
        print(line)

numbered = []
for i,line in enumerate(lines):
    i = str(i)
    while len(i) < 4:
        i = "0"+i
    numbered.append(i+line)

undo_numbers = []
for line in lines:
    line = line[4:]
    undo_numbers.append(line)

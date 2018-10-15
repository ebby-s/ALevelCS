'''
OPENFILE "MONSTER-FILE" FOR READ
Array ← []
REPEAT
    READFILE "MONSTER-FILE", FileMonster
        FileMonster ← FileMonster.split(',')
        Array ← FileMonster
        OUTPUT  FileMonster 
UNTIL EOF("MONSTER-FILE")  
'''

List = []
f = open('Monsters.txt','r')
for line in f:
    line = f.readline()
    if line != "":
        t1 = line.split(",")
        List.append(t1[1])
loop = True
while loop==True:
    choice=int(input("\n This is the menu, Choose a number: \n 1. Show contents \n 2. Search \n 3. Exit \n \n : "))
    if choice == 1:
        f = open('Monsters.txt','r')
        for line in f:
            print(line)
    elif choice == 2:
        f = open('Monsters.txt','r')
        IsFound = False
        ThisMonster = str(input("Enter monster: "))
        for line in f:
            FileMonster = line.split(",")
            if ThisMonster in FileMonster:
                IsFound = True
                print("Monster found")
        if IsFound == False:
            print('"Error 404: Monster not found"')
    elif choice == 3:
        loop = False

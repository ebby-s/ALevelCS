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

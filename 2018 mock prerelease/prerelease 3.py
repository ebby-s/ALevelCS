import random
valid = False
loop = True
ccard = []
List = []
var2val = {0:"Name: ",1:"Origin: ",2:"Description: ",3:"Attack: ",4:"Magical Force: ",5:"Magical Defence: ",6:"Defence: ",7:"Intelligence: ",8:"Health: ",9:"Experience: "}
sep = ','

f = open('Monsters.txt','r')
for line in f:
    line = f.readline()
    List.append(line)
for i in range(0,10):
    ccard.append(input("Enter "+var2val[i]))
for i in range(3,10):
    while int(ccard[i]) > 30 or int(ccard[i]) < 0:
        tnval = int(input("Invalid value detected.\nEnter new value for "+ var2val[i]))
        ccard[i] = str(tnval)
ccard = sep.join(ccard)
while loop==True:
    choice=int(input("\n This is the menu, Choose a number: \n 1. Compare card to random known card \n 2. Add card to list of known cards \n 3. Exit \n \n : "))
    if choice == 1:
        f = open('Monsters.txt','r')
        mrand = random.randint(0,len(List))
        print(List[mrand])
        print(ccard)
    elif choice == 2:
        for i in range(2):
            w = open('Monsters.txt','a+')
            w.write("\n"+ccard)
    elif choice == 3:
        loop = False

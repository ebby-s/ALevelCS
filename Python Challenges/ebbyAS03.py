inword = str(input("Enter a phrase: "))
inlist = []
for i in range(len(inword)):
    inlist.append(inword[i])
output = ''
for i in range(len(inlist),0,-1):
    output += inlist[i-1]
print(output)

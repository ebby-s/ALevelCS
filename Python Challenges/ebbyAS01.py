num = 0
nlist = [1,6,9,3,5,11]

for i in range(0,len(nlist)-1,1):
    if nlist[i] > nlist[i+1]:
        num = nlist[i]
        nlist[i]=nlist[i+1]
        nlist[i+1] = num

print(nlist)

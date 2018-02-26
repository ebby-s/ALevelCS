nlist = [1,6,9,3,5,11]

for j in range(len(nlist)):
    for i in range(j):
        if nlist[i] > nlist[i+1]:
            num = nlist[i]
            nlist[i]=nlist[i+1]
            nlist[i+1] = num

print(nlist)

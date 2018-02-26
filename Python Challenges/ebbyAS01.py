import datetime
def sort(nlist):
    done = 1
    while done != 0:
        done = 0
        for i in range(len(nlist)-1):
            if nlist[i] > nlist[i+1]:
                done += 1
                num = nlist[i]
                nlist[i]=nlist[i+1]
                nlist[i+1] = num
    return nlist

start_time = datetime.datetime.now()
nlist = sort([4,1,7,3,9,4,2,6,7])
print(datetime.datetime.now()-start_time)
print(nlist)

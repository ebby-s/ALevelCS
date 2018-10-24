import datetime
unsorted = [6,3,11,4,97,23,10,45,37,26,2,7,3]

def bubble_sort(nlist):
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
nlist = bubble_sort(unsorted)
print(datetime.datetime.now()-start_time)
print(nlist)

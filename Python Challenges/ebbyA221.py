def RemoveDuplicate(inlist):
    outlist = []
    for i in range(len(inlist)):
        if inlist[i] not in outlist:
            outlist.append(inlist[i])
    return outlist

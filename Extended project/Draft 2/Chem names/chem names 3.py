chains = ["0","meth","eth","prop","but","pent","hex","hept","oct"]
suffixes = ["oic acid","enitrile","one","ol","al","cyclo","ene"]
prefixes = ['methyl','ethyl','propyl','fluoro','chloro','bromo','iodo','hydroxy']
numprefixes = ["0","mono","di","tri","tetra"]
lists = [chains,suffixes,prefixes,numprefixes]

def Type(inword):
    try:
        pos = int(inword)
        return True
    except ValueError:
        return False

def Groups(inword,lists):
    found = []
    outword = inword
    for i in lists:
        for j in i:
            if j in inword:
                found.append(j)
                outword = outword.replace(j,str(found.index(j)))
                inword = inword.replace(j,"")
    return {"groups":found,"pos":outword}

def GroupPos(inword,info):
    groups = info["groups"]
    pos = info["pos"]
    endpos = pos
    grouppositions = []
    for i,j in enumerate(pos):
        if j == "-" and Type(pos[i-1]) and pos[i-1] != "0":
            grouppos = [pos[i-1],groups[int(pos[i+1])]]
            grouppositions.append(grouppos)
            endpos = endpos.replace(pos[i-1:i+2],"")
    for i in endpos:
        if Type(i):
            main = groups[int(i)]
    return {"groups":grouppositions,"main":main}

while True:
    inword = input("Enter name: ")
    info = Groups(inword,lists)
    if "-" not in inword:
        final = {"groups":[['1',info["groups"][1]]],"main":info["groups"][0]}
    else:
        final = GroupPos(inword,info)
    print(final)

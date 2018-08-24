import turtle
import drawing_module

scale = [43.3,25]
wn = turtle.Screen()
pen = turtle.Turtle()
pen.penup()
pen.ht()
pen.speed(100)

chains = ["0","meth","eth","prop","but","pent","hex","hept","oct"]
suffixes = ["oic acid","enitrile","one","ol","al","ene"]
prefixes = ['methyl','ethyl','propyl','fluoro','chloro','bromo','iodo','hydroxy']
numprefixes = ["0","mono","di","tri","tetra"]
lists = [chains,suffixes,prefixes,numprefixes]

def Overlap(a,b):
    for i in a:
        if i in b:
            return True
    return False

def Type(inword):
    try:
        pos = int(inword)
        return True
    except ValueError:
        return False

def Groups(inword,lists):
    found = []
    ints = []
    outword = inword
    for i in lists:
        for j in i:
            if j in inword:
                found.append(j)
                outword = outword.replace(j,str(found.index(j)))
                inword = inword.replace(j,"")
    for i in inword:
        if Type(i):
            ints.append(int(i))
    return {"groups":found,"pos":ints,"ref":outword}

def GroupPos(inword,info):
    groups = info["groups"]
    pos = info["ref"]
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

def AltGroupPos(inword,info):
    groups = info["groups"]
    pos = info["pos"]
    ref = info["ref"]
    alts = []
    altgrouppositions = []
    for i in groups:
        if i in numprefixes:
            alts.append(i)
    for i in alts:
        for j,k in enumerate(ref):
            if k == str(groups.index(i)) and Type(ref[j+1]):
                group = groups[int(ref[j+1])]
                positions = []
                for l in range(numprefixes.index(i)):
                    altgrouppositions.append([ref[j-2*l-2],group])
    return altgrouppositions

def Draw(startpos,angle,length):
    startpos[1] += 8
    pen.setpos(startpos)
    pen.seth(angle)
    pen.pendown()
    pen.left(30)
    for i in range(length-1):
        pen.forward(50)
        if i%2 == 0:
            pen.right(120)
        pen.left(60)
    pen.penup()


inword = "2,3-dichloro, 4-bromo pent-1-ene"
info = Groups(inword,lists)
if "-" not in inword:
    final = {"groups":[['1',info["groups"][1]]],"main":info["groups"][0]}
else:
    final = GroupPos(inword,info)

if Overlap(numprefixes,info["groups"]):
    final2 = AltGroupPos(inword,info)
    final["groups"] = final["groups"] + final2

for i in final["groups"]:
    if i[1] in numprefixes:
        final["groups"].remove(i)

print(final)
Draw([0,0],0,chains.index(final["main"]))

for i in final["groups"]:
    if int(i[0])%2 == 0:
        direct = 60
        side = 25
    else:
        direct = 240
        side = 0
    if i in prefixes[0:2]:
        length = prefixes.index(i)+2
    else:
        length = 2
    if i[1] != "ene":
        Draw([(int(i[0])-1)*43.3,side],direct,length)
    else:
        print([(int(i[0])-1)*43.3+10,side-6],direct-240)
        Draw([(int(i[0])-1)*43.3+10,side-6],direct-240,2)
        
    if i[1] == "chloro":
        drawing_module.c(30,[(int(i[0])-1)*43.3,side+drawing_module.function(direct,180,"")*75],"black",1)
        drawing_module.l(17,[(int(i[0])-1)*43.3+5,side+drawing_module.function(direct,180,"")*75],"black",1)
    if i[1] == "bromo":
        drawing_module.B(17,[(int(i[0])-1)*43.3-10,side+drawing_module.function(direct,180,"")*75],"black",1)
        drawing_module.r(20,[(int(i[0])-1)*43.3+5,side+drawing_module.function(direct,180,"")*75],"black",1)


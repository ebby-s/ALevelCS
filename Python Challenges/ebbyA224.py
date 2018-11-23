def function(order):
    return 2*order - 1

def oblique(array):
    new_array = [[] for x in range(function(max([len(array),len(array[0])])))]
    for y,row in enumerate(array):
        for x,element in enumerate(row):
            new_array[x+y].append(element)
    return new_array

def de_oblique(array):
    new_array = [[] for x in range(function(max([len(array),len(array[0])])))]
    for y,row in enumerate(array):
        for x,element in enumerate(row):
            new_array[x].append(element)
    return new_array

obliqued = oblique([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
print(obliqued)
print(de_oblique(obliqued))

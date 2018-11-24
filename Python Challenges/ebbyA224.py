

def oblique(array):
    new_array = [[] for x in range(len(array)+len(array[0])-1)]
    for y,row in enumerate(array):
        for x,element in enumerate(row):
            new_array[x+y].append(element)
    return new_array

def de_oblique(array):
    height = max([len(x) for x in array])
    width = len(array)+1 - height
    new_array = [[] for x in range(height)]
    for y,row in enumerate(array):
        for x,element in enumerate(row):
            if y<width: new_array[x].append(element)
            else: new_array[x+1+y-width].append(element)
    return new_array

obliqued = oblique([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
print(obliqued)
print(de_oblique(obliqued))


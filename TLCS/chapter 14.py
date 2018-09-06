xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]

def merge(xs,ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi == len(xs):
            result.extend(ys[yi:])
            return(result)

        if yi == len(ys):
            result.extend(ys[yi:])
            return(result)
        
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
        
print(merge(xs,ys))

def is_float(test):
    try:
        test = float(test)
        return True
    except: return False

test = [[1,2,3,4],
        [5,6,61,8],
        [9,10,11,12]]

def max_array(array):
    max_coords = [0,0]
    for y,row in enumerate(array):
        for x,element in enumerate(row):
            if array[y][x] > array[max_coords[1]][max_coords[0]]:
                max_coords = [x,y]
    return max_coords

print(max_array(test))

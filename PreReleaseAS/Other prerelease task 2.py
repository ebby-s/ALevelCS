""" So I'm making two different ways to solve the question, one with functions and one with an object. """

def create_array(x,y,value=0):         # Creates an array, for 2D arrays, x != 1, example: create_array(3,5)
    try:
        x = int(x)
        y = int(y)
        if x < 0 or y < 0:
            print("Negative values for initialisation of array")
            return
    except ValueError:
        print("Non-int values for initialisation of array")
        return
        
    if x == 1:
        return [ value for i in range(y)]
    else:
        return [ [ value for j in range(x)] for i in range(y)]

def fill_with_value(array,value):   # Fills array with a single value, example: fill_with_value(create_array(3,5),7)
    if type(array[0]) == type([]):
        for row in range(len(array)):
            for field in range(len(array[row])):
                array[row][field] = value
    else:
        for field in range(len(array)):
            array[field] = value

def fill_order(array,start,end):  # Fills the array with values in ascending or descending order, example: fill_order(create_array(3,5),2,11)
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        print("Non-int values for range of numbers to add to array")

def fill_with_function(array,function,argument=None):  # Fills the array with the values output by a function, example: fill_with_function(create_array(3,5),fibonacci,12)
    values = function(argument)
    
    
def fibonacci(order):    # Outputs values of the fibonacci sequence, example: fibonacci(12)
    x = 1
    y = 0
    output = []
    for i in range(order):
        if i%2 == 0:
            x += y
            output.append(x)
        else:
            y += x
            output.append(y)
    return output


class array:

    def __init__(self,x,y=None):   # Can be initialised with or without values, example with values: array([[1,2,3],[4,5,6],[7,8,9]]), example without values: array(3,5)
        """An array"""
        if y == None:
            self.data = x
        else:
            self.data = [ [ 0 for j in range(x)] for i in range(y)]

    def show(self):                    # Prints the array
        for row in self.data:
            print(row)

    def set_value(self,x,y,value):       # Sets a single value in the array
        self.data[y][x] = value

    def set_row(self,y,values):              # Sets a row of values
        for i,value in enumerate(values):
            self.data[y][i] = value

    def set_col(self,x,values):             # Sets a column of values
        for i,value in enumerate(values):
            self.data[i][x] = value

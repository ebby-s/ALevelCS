def fill_array():                                      # Creates an array filled with a single value
    value = input("Enter value to repeat: ")
    while True:
        try:
            xlength = int(input("Enter xlength of array: "))
            ylength = int(input("Enter ylength of array: "))
            if xlength > 0 or ylength > 0:
                break
            else:
                print("Length has to be positive")
        except:
            print("Length has to be an integer")
    
    return [[value for y in range(ylength)] for x in range(xlength)]

def order_array():                          # Creates an array with an incrementing or decrementing set of values
    while True:
        try:
            value = int(input("Enter starting value: "))
            direction = int(input("Enter direction(+1 or -1): "))
            xlength = int(input("Enter xlength of array: "))
            ylength = int(input("Enter ylength of array: "))
            if xlength <= 0 or ylength <= 0:
                print("Length has to be positive")
            elif abs(direction) != 1:
                print("Direction has to be +1 or -1")
            else:
                break
        except:
            print("Invalid value entered")
    
    return [[value + direction*y + direction*ylength*x for y in range(ylength)] for x in range(xlength)]

def function_array(function,argument):                    # Creates an array with the output of a function
    return function(argument)

def average(array,xindex_range,yindex_range):
    total = 0
    count = 0
    for i in xindex_range:
        for j in yindex_range:
            total += array[i][j]
            count += 1
    
    return total/count


def fibonacci(order):                          # Outputs fibonacci numbers
    x = 1
    y = 0
    output = []
    for i in range(int(order)):
        if i%2 == 0:
            x += y
            output.append(x)
        else:
            y += x
            output.append(y)
    return output


'''
done = False
choices = [fill_array,order_array]
functions = [fibonacci]
while not done:
    while True:
        print("""---------------------------------------
Main menu
You can create an array with:
1. A single value repeated
2. An incrementing or decrementing set of values
3. The output from a function

4. Exit
""")
        try:
            choice = int(input("Choice: "))
            if 0 < choice < 5:
                break
            else:
                print("Invalid choice")
        except:
            print("Invalid input, must be int")

    if choice not in [3,4]:
        print(choices[choice-1]())
    elif choice == 3:
        print("""Choose a function:
1. Fibonacci
""")
        while True:
            try:
                function_choice = int(input("Choice: "))
                if 0 < function_choice < 2:
                    break
                else:
                    print("Invalid choice")
            except:
                print("Invalid input, must be int")
        argument = input("Enter an argument: ")
        print(function_array(functions[function_choice-1],argument))
        
    elif choice == 4:
        exit()
'''

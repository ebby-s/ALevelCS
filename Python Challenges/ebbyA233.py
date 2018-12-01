def mult3(num):
    if num != 0: return 3 + mult3(num-1)
    else: return 0

def rec_sum(num):
    if num != 0: return num + rec_sum(num-1)
    else: return 0

def pascal(order):
    if order == 1: return [1]
    else:
        line = [1]
        prev_line = pascal(order-1)
        for i in range(len(prev_line)-1):
            line.append(prev_line[i] + prev_line[i+1])
        line += [1]
    return line

def pascal_fib(original,order=None):
    fib = 0
    if order == None: order = original
    if order == 1: line = [1]
    else:
        line = [1]
        prev_line,fib = pascal_fib(original,order-1)
        for i in range(len(prev_line)-1):
            line.append(prev_line[i] + prev_line[i+1])
        line += [1]
    try: fib += line[original-order]
    except: '''do nothing'''
    return line,fib

def sieve(values,n=0):
    prime = values[n]
    for value in values:
        if value%prime == 0 and prime != value:
            values.remove(value)
    if n+2 > len(values): return values
    else: return sieve(values,n+1)

def fibonacci(order):
    if order in [1,2]: return 1
    return fibonacci(order-1) + fibonacci(order-2)

def find_index(value,current=1):
    if fibonacci(current) == value: return current
    if fibonacci(current) > value: return -1
    else: return find_index(value,current+1)

def find_power(fib):
    n = find_index(fib)
    return 2*n+1






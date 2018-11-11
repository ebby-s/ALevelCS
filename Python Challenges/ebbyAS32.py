import random

def visit(floors):
    order = [i+1 for i in range(floors)]
    random.shuffle(order)
    return order
    

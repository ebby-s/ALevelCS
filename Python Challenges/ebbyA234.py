import operator

def bitwise(op,byte1,byte2):
    operators = {"AND":operator.and_,"OR":operator.or_,"XOR":operator.xor}
    return operators[op](byte1,byte2)

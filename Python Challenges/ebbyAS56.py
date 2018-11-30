import random

def complement(original):
    complement = bin(256+original)[-8:].replace('-','').replace('b','')
    while len(complement) < 8:
        complement = "0"+complement
    return complement

def game():
    question = random.randint(-125,-1)
    ans = complement(question)
    user_ans = str(input("Enter {0} in two's complement form: ".format(question)))
    if ans == user_ans: return True
    else:
        print(ans)
        return False

while True:
    if not game(): break

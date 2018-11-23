import random

def calc_parity(mode,byte):
    if mode == 0: return int(str(byte).count("1")%2)
    else: return int((str(byte).count("1")+1)%2)

def game(mode):
    question = ''
    for i in range(7):
        question += str(random.choice([0,1]))
    ans = calc_parity(mode,question)
    user_ans = int(input("Parity bit for {0}: ".format(question)))
    if user_ans == ans: return True
    else: return ans

parity = int(input("Choose a parity(0=even,1=odd): "))
while True:
    print(game(parity))

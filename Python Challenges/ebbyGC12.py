import time

def time(turns,period):
    for i in range(1,turns+1):
        if i%1 == 0:
            print("player 1's turn")
        else:
            print("player 2's turn")
        time.sleep(period)

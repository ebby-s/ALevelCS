import random

def share_diagonal(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy

def col_clashes(bs, c):
    for i in range(c):
          if share_diagonal(i, bs[i], c, bs[c]): return True
    return False

def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col): return True
    return False

def main(n):
    bd = list(range(n))
    found = False
    while not found:
        random.shuffle(bd)
        if not has_clashes(bd):
            print("Found solution {0}.".format(bd))
            found = True

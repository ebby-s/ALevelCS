



def checker(n,m):
    board = [[x for x in range(m)] for y in range(n)]
    for i in range(len(board)):
        if i%2 == 0:
            start = 0
        else:
            start = 1
        for j in range(len(board[i])):
            if (start+board[i][j])%2 == 0:
                board[i][j] = "."
            else:
                board[i][j] = "*"
    for row in board:
        print(row)

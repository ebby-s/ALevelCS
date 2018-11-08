def pyramid(size):
    total = 0
    for i in range(size):
        total += 1
        out = ''
        for j in range(total):
            out += "x"
        print(out)


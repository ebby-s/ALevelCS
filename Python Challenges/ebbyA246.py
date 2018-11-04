limits = [1,111]

while True:
    mid = int((limits[0]+limits[1])/2)
    current = input("Is "+str(mid)+" your number? ")
    if current == "=":
        break
    elif current == "<":
        limits[1] = mid
    elif current == ">":
        limits[0] = mid

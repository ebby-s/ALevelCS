def readposint():
    try:
        val = int(input("Enter a posiive integer: "))
        if val < 0:
            print("Not positive")
            val = readposint()
    except ValueError:
        print("Not an integer")
        val = readposint()
    return val

readposint()

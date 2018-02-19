import sys
directions = ["N","E","S","W"]
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

def turn_clockwise(direction):
    for i in range(0,4,1):
        if i ==3:
            i = -1
        if direction == directions[i] and i != 3:
            return directions[i+1]

def day_name (day):
    if day >=0 and day <=6:
        return days[day]

def day_num (day):
    for i in range(0,7,1):
        if day == days[i]:
            return i

def day_add (day,delta):
    delta = delta % 7
    if delta < 0:
        delta = 7 - delta
    for i in range(0,7,1):
        if i == 6:
            i = -1
        if day == days[i]:
            if i+delta>6:
                i=i-7
            return(days[i+delta])

def to_secs (hour, minute, second):
    second = second + 60*minute
    second = second + 3600*hour
    second = int(second)
    return second

def hours_in (hour, minute, second):
    minute = minute/60
    second = second/3600
    hour += minute+second
    hour = int(hour)
    return hour

def compare (a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    elif a<b:
        return -1

def hypotenuse (a,b):
    t = a**2
    t += b**2
    t = t**0.5
    return t

def slope (x1,y1,x2,y2):
    y = y1-y2
    x = x1-x2
    m = y/x
    return m

def intercept (x1,y1,x2,y2):
    y = y1-y2
    x = x1-x2
    m = y/x
    c = y1-x1*m
    return c

def is_factor (f,n):
    if n%f == 0:
        return True
    else:
        return False

def is_multiple (m,n):
    if m%n == 0:
        return True
    else:
        return False

def f2c(t):
    t -= 32
    t = t*5/9
    t = round(t)
    return t

def c2f(t):
    t = t*9/5
    t += 32
    t = round(t)
    return t
    
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)
test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)
test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
test(day_num("Halloween") == None)
test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433,0,0) == 8758)
test(compare(5, 4) == 1)
test(compare(7, 7) == 0)
test(compare(2, 3) == -1)
test(compare(42, 1) == 1)
test(hypotenuse(3, 4) == 5.0)
test(hypotenuse(12, 5) == 13.0)
test(hypotenuse(24, 7) == 25.0)
test(hypotenuse(9, 12) == 15.0)
test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)
test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)
test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))
test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))
test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)
test(c2f(0) == 32)
test(c2f(100) == 212)
test(c2f(-40) == -40)
test(c2f(12) == 54)
test(c2f(18) == 64)
test(c2f(-48) == -54)

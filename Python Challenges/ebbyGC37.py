a = ("All")
b= ("work")
c= ("and")
d= ("no")
e= ("play")
f= ("makes")
g= ("Jack")
h= ("a")
i= ("dull")
j= ("boy")
print (a, b, c, d, e, f, g, h, i, j)

print (6*(1-2))
#print (6*(1-2))

bruce = 6
print (bruce + 4)

p = float(input("initial investment"))
r = float(input("annual interest rate as a decimal"))
n = float(input("number of times interest is compounded per year"))
t = float(input("number of years"))

b = 1+( r/n)
c = n*t
d = b**c
a = p*d
print (a)

r = 5100 % 24
t = 14 + r
rt = t % 24

if rt > 12:
    rt = rt - 12
    print (rt, 'PM')
else:
    print (rt, "AM")

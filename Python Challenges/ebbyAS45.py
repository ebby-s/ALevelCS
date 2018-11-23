def calc_space(width,height,depth):
    return width*height*depth/8

while True:
    height = int(input("Height in pixels: "))
    width = int(input("Width in pixels: "))
    depth = int(input("Color depth: "))
    print(calc_space(height,width,depth)," bytes")

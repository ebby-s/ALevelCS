import chapter15

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
        
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

    def flip(self):
        self.width,self.height = self.height,self.width

    def contains(self,other):
        return self.corner.x < other.x < (self.corner.x+self.width) and self.corner.y > other.y > (self.corner.y-self.height)

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

def detect_collision(rect1,rect2):
    corners = [rect1.corner]
    corners.append(Point(rect1.corner.x+rect1.width,rect1.corner.y))
    corners.append(Point(rect1.corner.x,rect1.corner.y-rect1.height))
    corners.append(Point(rect1.corner.x+rect1.width,rect1.corner.y-rect1.height))
    for i in corners:
        if rect2.contains(i):
            return True
    return False

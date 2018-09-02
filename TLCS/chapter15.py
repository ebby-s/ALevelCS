def distance(p,q):
    dx = p.x - q.x
    dy = p.y - q.y
    result = (dx**2 + dy**2)**0.5
    return result

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect_x(self):
        return Point(self.x,-self.y)

    def slope_from_origin(self):
        if self.x == 0:
            return 999999999999999999999999999999999999999999999999999
        return self.y/self.x

    def get_line_to(target,self):
        if self.x-target.x == 0:
            return 999999999999999999999999999999999999999999999999999
        m = (self.y - target.y)/(self.x-target.x)
        c = self.y - m*self.x
        return [m,c]

class SMS_store:

    def __init__(self):
        """Create an place to store messages"""
        self.messages = []
        

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        self.messages.append([False,from_number, time_arrived, text_of_SMS])

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        result = []
        for i in self.messages:
            if not i[0]:
                result.append(i)
        return result

    def get_message(self,i):
        if i >= len(self.messages):
            return
        self.messages[i][0] = True
        return self.messages[i][1:]

    def delete(self,i):
        self.messages.remove[i]

    def clear():
        self.messages = []







class Rural:
    """A rural settlement"""
    
    def __init__(self,NameR,Science,Art):
        self._Name=NameR
        self._Status="Hamlet"
        self._Population=1
        self._Culture=2
        self._Science=Science/20
        self._Art=Art

    def Grow(self):
        self._Population += self._Science
        self._Culture += self._Art

    def Status(self):
        return {'Name':self._Name,'Status':self._Status,'Population':self._Population,'Culture':self._Culture}

class Urban:
    """An urban settlement"""

    def __init__(self,NameU,Science,Art):
        self._Name=NameU
        self._Status="Town"
        self._Population=2
        self._Culture=1
        self._Science=Science
        self._Art=Art/20

    def Grow(self):
        self._Population += self._Science
        self._Culture += self._Art

    def Status(self):
        return {'Name':self._Name,'Status':self._Status,'Population':self._Population,'Culture':self._Culture}

def CreateRural():
    Name=input("Enter a Name: ") 
    NewRural=Rural(Name,5,5)
    print(NewRural.Status())
    global Art
    global Science
    Art =+ 1
    Science =+ 1

def CreateUrban():
    Name=input("Enter a Name: ") 
    NewUrban=Urban(Name,5,5)
    print(NewUrban.Status())
    global Art
    global Science
    Art =+ 1
    Science =+ 1

def PassDay():
    NewRural.Grow()
    NewUrban.Grow()

CreateRural()
CreateUrban()
print (Art,Science)
PassDay()

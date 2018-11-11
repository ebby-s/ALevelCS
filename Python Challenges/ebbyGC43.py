
def dvt(x=None,v=None,t=None):
    if x == None:
        return v*t
    elif v == None:
        return x/t
    elif t == None:
        return x/v

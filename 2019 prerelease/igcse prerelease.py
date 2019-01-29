class item:
    def __init__(self,number=None,desc="",price=None):
        self.number = number
        self.bids = []
        self.desc = desc
        self.res_price = price
        self.total = None
    def __int__(self):
        return int(self.number)
    def __str__(self):
        return str(self.desc)
    def bid(self,amount,id_number):
        if len(self.bids) == 0:
            self.bids.append([id_number,amount])
            return True
        elif self.bids[-1][1] < amount:
            self.bids.append([id_number,amount])
            return True
        else: return False
    def sold_check(self):
        if len(self.bids) == 0: return False
        elif self.res_price <= self.bids[-1][1]:
            self.total = 1.1*self.bids[-1][1]
            return True
        else: return False
    def highest_bid(self):
        if len(self.bids) == 0: return 0
        else: return self.bids[-1][1]

def print_table(layout,text):
    for row in text:
        print()

def find_sold(items):
    sold = []
    unsold = []
    for item in items:
        if item.sold_check(): sold.append(item)
        else: unsold.append(item)
    return [sold,unsold]

items = []

layout = "{0:>2} {1:>13} {2:>25} {3:>5}"






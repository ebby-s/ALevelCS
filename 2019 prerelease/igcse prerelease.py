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

def find_sold(items):
    sold = []
    unsold = []
    for item in items:
        if item.sold_check(): sold.append(item)
        else: unsold.append(item)
    return [sold,unsold]

def main_menu():
    print("__________________")
    print("Menu")
    print()
    print("1. Show items")
    print("2. Bid on item")
    print("3. Quit")
    try: return int(input(" : "))
    except:
        print("Invalid choice")
        return main_menu()

def show_items(items):
    layout = "{0:>3} {1:>15} {2:>25} {3:>12}"
    print(layout.format(" ","Item number","Description","Highest bid"))
    for i,item in enumerate(items):
        print(layout.format(i,int(item),str(item),item.highest_bid()))

def take_bids(items):
    try: item = int(input("Choose an item: "))

def step1(items):
    while True:
        choice = main_menu()
        if choice == 1: show_items(items)
        elif choice == 2:
            
            

items = []








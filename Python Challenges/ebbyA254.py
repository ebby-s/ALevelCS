class CarRecord:
    def __init__(self,ID=None,Reg=None,DateOfReg=None,EngSize=None,Price=None):
        self.VehicleID = ID
        self.Registration = Reg
        self.DateOfRegistration = DateOfReg
        self.EngineSize = EngSize
        self.PurchasePrice = Price

cars = [CarRecord() for x in range(10)]



class Taxi:
    def __init__(self):
        self.registration = None
        self.charge = None
    def fare(self,time):
        return self.charge * time

class Car(Taxi):
    pass
    

class Minibus(Taxi):
    def __init__(self):
        self.registration = None
        self.charge = None
        self.booking_charge = None
        self.max_passengers = None
    def fare(self,time):
        return self.booking_charge + self.charge*time

def between(self,t1,t2):
    if t1.to_seconds() <= self.to_seconds() < t2.to_seconds():
        return True
    return False

def __gt__(self,target):
    if self.to_seconds() > target.to_seconds():
        return True
    return False

def increment(self,seconds):
    seconds += self.to_seconds()
    self.hours = int(seconds/3600)
    seconds = seconds%3600
    self.minutes = int(seconds/60)
    self.seconds = seconds%60


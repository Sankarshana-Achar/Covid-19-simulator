class Person:
    def __init__(self):
        self.id=None
        self.age=0
        self.closest=[]
        self.contacts = int(0)
        self.status="Healthy"
        self.limit = int(0)
        self.days = int(0)
        self.lat=None
        self.long=None
        self.closest10 = []
        self.district = None
        self.houseId = None

    def setValues(self,id_,age_,lat_,long_,hh__,dd__):
        self.id=id_
        self.age=age_
        self.lat=lat_
        self.long=long_
        self.houseId = hh__
        self.district = dd__

    def setStatus(self,status):
        self.status = status

    def isHealthy(self):
        if self.status is "Healthy":
            return True
        return False

    def getStatus(self):
        return self.status

    def setLimit(self,lim):
        self.limit=lim
        self.days = 0

    def isInfected(self):
        if self.status is "Symptamatic":
            return True
        if self.status is "Asymptamatic":
            return True
        return False

    def isAsymptamatic(self):
        if self.status is "Asymptamatic":
            return True
        return False

    def getID(self):
        return self.id

    def increment(self):
        self.days = self.days + 1

    def reachedLimit(self):
        if (self.days >= self.limit):
            return True
        return False

    def getDistrict(self):
        return self.district

    def clear(self):
        self.status = "Healthy"
        self.limit = int(0)
        self.days = int(0)
from Person import Person as person
from DataPool import DataPool as DataPool
import numpy as np
import math as math
import copy as copy
import random
import threading
from File_handler import File_handler as Writer


class Simulator:
    # ---- Constructor ----#
    def __init__(self, people, days):
        self.writer = Writer("writeData")
        self.n = 1000
        self.dataPool = DataPool(int(people))
        self.dists = 1
        self.distAsymp = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distSymp = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]*self.dists
        self.distAdmitted = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distCured = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distRecovered = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distICU = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distVen = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distDead = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distIntInfect = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distNonintInfect = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.pr = person()
        self.people = []
        self.curedKid = []
        self.curedYoung = []
        self.curedAdult = []
        self.recoveredKid = []
        self.recoveredYoung = []
        self.recoveredAdult = []
        self.intInfectKid = []
        self.intInfectYoung = []
        self.intInfectAdult = []
        self.nonintInfectKid = []
        self.nonintInfectYoung = []
        self.nonintInfectAdult = []
        self.asympKid = []
        self.asympYoung = []
        self.asympAdult = []
        self.admittedKid = []
        self.admittedYoung = []
        self.admittedAdult = []
        self.ICUKid = []
        self.ICUYoung = []
        self.ICUAdult = []
        self.VenKid = []
        self.VenYoung = []
        self.VenAdult = []
        self.deadKid = []
        self.deadYoung = []
        self.deadAdult = []
        self.sympYoung = []
        self.sympKid = []
        self.sympAdult = []
        self.dayAdult = 1
        self.toICU = 0.11  # increased for now
        self.toVen = 0.88
        self.records = int(people)
        self.toDie = 0.11
        self.asympKidNum = []
        self.asympYoungNum = []
        self.asympAdultNum = []
        self.admittedKidNum = []
        self.admittedYoungNum = []
        self.admittedAdultNum = []
        self.ICUKidNum = []
        self.ICUYoungNum = []
        self.ICUAdultNum = []
        self.VenKidNum = []
        self.VenYoungNum = []
        self.VenAdultNum = []
        self.sympYoungNum = []
        self.sympKidNum = []
        self.sympAdultNum = []
        self.deadYoungNum = []
        self.deadKidNum = []
        self.deadAdultNum = []
        self.curedYoungNum = []
        self.curedKidNum = []
        self.recoveredAdultNum = []
        self.recoveredYoungNum = []
        self.recoveredKidNum = []
        self.intInfectKidNum = []
        self.intInfectYoungNum = []
        self.intInfectAdultNum = []
        self.nonintInfectKidNum = []
        self.nonintInfectYoungNum = []
        self.nonintInfectAdultNum = []
        self.curedAdultNum = []
        self.asympNum = []
        self.sympNum = []
        self.admittedNum = []
        self.venNum = []
        self.ICUNum = []
        self.deadNum = []
        self.curedNum = []
        self.recoveredNum = []
        self.intInfectNum = []
        self.nonintInfectNum = []
        self.days = int(days)
        self.determiner = [[2.774, 0.899], [2.883, 0.856], [2.599, 0.844]]
        self.immune_days = 0
        self.mask_dist_percent = 0
        self.close_circle = 0


    # ---- Constructor declared ----#

    # ---- Function to count Intervention-Infected patient ----#

    def intInfect(self, id):
        if self.people[id].age < 5:
            self.intInfectKid.append(id)
        elif  self.people[id].age > 59:
            self.intInfectAdult.append(id)
        else:
            self.intInfectYoung.append(id)

    # ---- Completed function definition of intInfect() ----#

    # ---- Function to count Non-Intervention-Infected patient ----#

    def nonintInfect(self, id):
        if self.people[id].age < 5:
            self.nonintInfectKid.append(id)
        elif self.people[id].age > 59:
            self.nonintInfectAdult.append(id)
        else:
            self.nonintInfectYoung.append(id)

    # ---- Completed function definition of nonintInfect() ----#

    # ---- Function to Recover the patient ----#

    def recovered(self, id):
        if self.people[id].age < 5:
            self.recoveredKid.append(id)
        elif self.people[id].age > 59:
            self.recoveredAdult.append(id)
        else:
            self.recoveredYoung.append(id)

    # ---- Completed function definition of recovered() ----#


    # ---- Function to Cure the patient ----#

    def cured(self, id):
        if self.people[id].age < 5:
            self.curedKid.append(id)
        elif self.people[id].age > 59:
            self.curedAdult.append(id)
        else:
            self.curedYoung.append(id)

    # ---- Completed function definition of cured() ----#

    # ---- Function to Admit the patient ----#

    def admit(self, id):
        if self.people[id].age < 5:
            self.admittedKid.append(id)
        elif self.people[id].age > 59:
            self.admittedAdult.append(id)
        else:
            self.admittedYoung.append(id)  # May Erase

    # ---- Completed function definition of admit() ----#

    # ---- Function get the patient to have Symmptomatic covid-19 ----#

    def symp(self, id):
        if self.people[id].age < 5:
            self.sympKid.append(id)
        elif self.people[id].age > 59:
            self.sympAdult.append(id)
        else:
            self.sympYoung.append(id)

    # ---- Completed function definition of symp() ----#

    # ---- Function get the patient to have Asymptomatic covid-19 ----#

    def asymp(self, id):
        if self.people[id].age < 5:
            self.asympKid.append(id)
        elif self.people[id].age > 59:
            self.asympAdult.append(id)
        else:
            self.asympYoung.append(id)

    # ---- Completed function definition of asymp() ----#

    # ---- Function to get the patient into the ventilator----#

    def ven(self, id):
        if self.people[id].age < 5:
            self.VenKid.append(id)
        elif self.people[id].age > 59:
            self.VenAdult.append(id)
        else:
            self.VenYoung.append(id)

    # ---- Completed function definition of ven() ----#

    # ---- Function to get the patient into the ICU----#

    def ICU(self, id):
        if self.people[id].age < 5:
            self.ICUKid.append(id)
        elif self.people[id].age > 59:
            self.ICUAdult.append(id)
        else:
            self.ICUYoung.append(id)

    # ---- Completed function definition of ICU() ----#

    # ---- This function returns the location of the required element ----#

    def exists(self, lis, val):
        for i in range(len(lis)):
            if lis[i] is val:
                return True
        return False

    # ---- Completed Function definition of constructor ----#

    # ---- Function to set the number of contacts for everyone ----#

    def setcontacts(self, id):
        # if self.people[id].age < 5:
        #     val = 0
        # elif self.people[id].age > 59:
        #     val = 2
        # else:
        #     val = 1
        # print(type(self.people[id]), self.people[id])
        numlist = self.dataPool.getNum(self.people[id])/10
        # print("Contact: " + str(numlist))
        while (True):
            self.people[id].contacts = int(numlist)  # MODIFIED
            if self.people[id].contacts is not None:
                break

    # ---- This function sets the closest[] to the person whose id is passed ----#

    def setclosest(self, id):
        lat1 = 15
        lat2 = 20
        long1 = 77
        long2 = 82
        farthest = math.hypot(lat2 - lat1, long1 - long2)
        size = len(self.people)
        for i in range(id, size):
            if len(self.people[id].closest) >= self.people[id].contacts:
                return
            if len(self.people[i].closest) >= self.people[i].contacts:
                continue
            if id != i:
                dist = math.hypot(self.people[id].lat - self.people[i].lat, self.people[id].long - self.people[i].long)
                meet = random.choices([1, 0], weights=(1 - (dist / farthest), dist / farthest), k=1)
                if meet[0] is 1:
                    if not self.exists(self.people[id].closest, i):
                        self.people[id].closest.append(i)
                        self.people[i].closest.append(id)
        # self.writer.log(" The closest of "+str(id)+" is "+str(self.people[id].closest))

    # ---- Completed function definition of setClosest() ----#

    # ---- This function gets the person to meet up with all the people who have come in contact ----#
    def coronaSpree(self, id):
        size = len(self.people[id].closest)
        weight = []
        j = int(0)
        if self.people[id].isInfected():
            if self.presentday <= 68:
                size = size * 0.41
                self.close_circle = 0.85
                self.mask_dist_percent = 0
            elif (self.presentday <= 129) and (self.presentday > 68):
                size = size * 0.54
                self.close_circle = 0.8
            elif (self.presentday <= 142) and (self.presentday > 129):
                size = size * 0.67
                self.close_circle = 0.75
            else:
                size = size * 1
                self.close_circle = 0.63

            for i in range(int(size)):  # MODIFIED Might need numerical correction
                if i < self.close_circle * (int(size)):
                    chance = random.randint(3, 10)
                    j = int(i)
                    if id > self.people[id].closest[j]:
                        continue
                    if not self.people[self.people[id].closest[j]].isHealthy():  # MODIFIED
                        continue
                    per = self.people[id].closest[j]
                else:
                    rand = random.randint(0, len(self.people) - 1)
                    chance = random.randint(1, 5)
                    if id > rand:
                        continue
                    if self.exists(self.people[id].closest, rand):
                        i = i - 1
                        continue
                    if not self.people[rand].isHealthy():  # MODIFIED
                        continue
                    else:
                        per = rand

                mask = 0
                mask = random.choices([1, 0], weights=(self.mask_dist_percent, 100 - self.mask_dist_percent), k=1)
                if mask[0] == 1:
                    mask_effectiveness = 14.3  # mask effectiveness in percent
                    chance = chance * ((100 - mask_effectiveness) / 100)

                    distancing_effectiveness = 10.2  # distancing effectiveness in percent
                    chance = chance * ((100 - distancing_effectiveness) / 100)

                st = random.choices([1, 0], weights=(chance, 100 - chance), k=1)  # chance that corona has spread
                if st[0] is 1:  # If corona has spread through intervention or not
                    if int(mask[0]) > 0:
                        self.intInfect(per)
                    else:
                        self.nonintInfect(per)

                if st[0] is 1:  # If corona has spread
                    if (self.people[per].age < 5):
                        chance = 0.8
                    elif (self.people[per].age > 59):
                        chance = 0.8
                    else:
                        chance = 0.8

                else:  # If corona has not spread
                    continue

                st = random.choices([1, 0], weights=(chance, 1 - chance), k=1)  # Odds that the affected is asymptomatic
                if st[0] is 1:  # if asymptomatic
                    self.people[per].setStatus("Asymptamatic")
                    lim = 5 + int(14)
                    # if self.people[per].age < 5:  # incubation period
                    #     lim = lim + int(3)
                    # elif self.people[per].age > 59:
                    #     lim = lim + int(5)
                    # else:
                    #     lim = lim + int(14)
                    self.people[per].setLimit(lim)
                    self.asymp(per)

                else:  # if symptomatic
                    self.people[per].setStatus("Symptamatic")
                    lim = 5 + int(5)
                    # if self.people[per].age < 5:  # incubation period
                    #     lim = lim + int(3)
                    # elif self.people[per].age > 59:
                    #     lim = lim + int(5)
                    # else:
                    #     lim = lim + int(14)
                    self.people[per].setLimit(lim)
                    self.symp(per)
                    return

    # ---- Completed function definition of coronaSpree() ----#

    # ---- Funtion that updates status once the limit is reached ----#

    def update(self):
        size = len(self.sympKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.sympKid[i]].reachedLimit():
                self.people[self.sympKid[i]].setLimit(14)
                self.people[self.sympKid[i]].setStatus("Admitted")
                self.admit(self.sympKid[i])
                l = self.sympKid.pop(i)
                size = size - 1

        size = len(self.sympYoung)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.sympYoung[i]].reachedLimit():
                self.people[self.sympYoung[i]].setLimit(14)
                self.people[self.sympYoung[i]].setStatus("Admitted")
                self.admit(self.sympYoung[i])
                l = self.sympYoung.pop(i)
                size = size - 1

        size = len(self.sympAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.sympAdult[i]].reachedLimit():
                self.people[self.sympAdult[i]].setLimit(14)
                self.people[self.sympAdult[i]].setStatus("Admitted")
                self.admit(self.sympAdult[i])
                l = self.sympAdult.pop(i)
                size = size - 1

        size = len(self.asympKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.asympKid[i]].reachedLimit():
                self.people[self.asympKid[i]].setLimit(self.immune_days)
                self.people[self.asympKid[i]].setStatus("Cured")
                self.cured(self.asympKid[i])
                self.recovered(self.asympKid[i])
                l = self.asympKid.pop(i)
                size = size - 1

        size = len(self.asympYoung)

        for i in range(size):
            if i >= size:
                break
            if self.people[self.asympYoung[i]].reachedLimit():
                self.people[self.asympYoung[i]].setLimit(self.immune_days)
                self.people[self.asympYoung[i]].setStatus("Cured")
                self.cured(self.asympYoung[i])
                self.recovered(self.asympYoung[i])
                l = self.asympYoung.pop(i)
                size = size - 1

        size = len(self.asympAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.asympAdult[i]].reachedLimit():
                self.people[self.asympAdult[i]].setLimit(self.immune_days)
                self.people[self.asympAdult[i]].setStatus("Cured")
                self.cured(self.asympAdult[i])
                self.recovered(self.asympAdult[i])
                l = self.asympAdult.pop(i)
                size = size - 1

        size = len(self.admittedKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.admittedKid[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toICU, 1 - self.toICU), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(7, 8, 9)
                    lim = int(lim_)
                    self.people[self.admittedKid[i]].setStatus("ICU")
                    self.people[self.admittedKid[i]].setLimit(lim)
                    self.ICU(self.admittedKid[i])
                    l = self.admittedKid.pop(i)
                    size = size - 1
                else:
                    self.people[self.admittedKid[i]].setLimit(self.immune_days)
                    self.people[self.admittedKid[i]].setStatus("Cured")
                    self.cured(self.admittedKid[i])
                    self.recovered(self.admittedKid[i])
                    l = self.admittedKid.pop(i)
                    size = size - 1

        size = len(self.admittedYoung)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.admittedYoung[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toICU, 1 - self.toICU), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(7, 8, 9)
                    lim = int(lim_)
                    self.people[self.admittedYoung[i]].setStatus("ICU")
                    self.people[self.admittedYoung[i]].setLimit(lim)
                    self.ICU(self.admittedYoung[i])
                    l = self.admittedYoung.pop(i)
                    size = size - 1
                else:
                    self.people[self.admittedYoung[i]].setLimit(self.immune_days)
                    self.people[self.admittedYoung[i]].setStatus("Cured")
                    self.cured(self.admittedYoung[i])
                    self.recovered(self.admittedYoung[i])
                    l = self.admittedYoung.pop(i)
                    size = size - 1

        size = len(self.admittedAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.admittedAdult[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toICU, 1 - self.toICU), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(7, 8, 9)
                    lim = int(lim_)
                    self.people[self.admittedAdult[i]].setStatus("ICU")
                    self.people[self.admittedAdult[i]].setLimit(lim)
                    self.ICU(self.admittedAdult[i])
                    l = self.admittedAdult.pop(i)
                    size = size - 1
                else:
                    self.people[self.admittedAdult[i]].setLimit(self.immune_days)
                    self.people[self.admittedAdult[i]].setStatus("Cured")
                    self.cured(self.admittedAdult[i])
                    self.recovered(self.admittedAdult[i])
                    l = self.admittedAdult.pop(i)
                    size = size - 1

        size = len(self.ICUKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.ICUKid[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toVen, 1 - self.toVen), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(5, 7, 12)
                    lim = int(lim_)
                    self.people[self.ICUKid[i]].setLimit(lim)
                    self.people[self.ICUKid[i]].setStatus("Ventilator")
                    self.ven(self.ICUKid[i])
                    l = self.ICUKid.pop(i)
                    size = size - 1
                else:
                    self.people[self.ICUKid[i]].setLimit(self.immune_days)
                    self.people[self.ICUKid[i]].setStatus("Cured")
                    self.cured(self.ICUKid[i])
                    self.recovered(self.ICUKid[i])
                    l = self.ICUKid.pop(i)
                    size = size - 1

        size = len(self.ICUYoung)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.ICUYoung[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toVen, 1 - self.toVen), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(5, 7, 12)
                    lim = int(lim_)
                    self.people[self.ICUYoung[i]].setLimit(lim)
                    self.people[self.ICUYoung[i]].setStatus("Ventilator")
                    self.ven(self.ICUYoung[i])
                    l = self.ICUYoung.pop(i)
                    size = size - 1
                else:
                    self.people[self.ICUYoung[i]].setLimit(self.immune_days)
                    self.people[self.ICUYoung[i]].setStatus("Cured")
                    self.cured(self.ICUYoung[i])
                    self.recovered(self.ICUYoung[i])
                    l = self.ICUYoung.pop(i)
                    size = size - 1

        size = len(self.ICUAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.ICUAdult[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toVen, 1 - self.toVen), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(5, 7, 12)
                    lim = int(lim_)
                    self.people[self.ICUAdult[i]].setLimit(lim)
                    self.people[self.ICUAdult[i]].setStatus("Ventilator")
                    self.ven(self.ICUAdult[i])
                    l = self.ICUAdult.pop(i)
                    size = size - 1
                else:
                    self.people[self.ICUAdult[i]].setLimit(self.immune_days)
                    self.people[self.ICUAdult[i]].setStatus("Cured")
                    self.cured(self.ICUAdult[i])
                    self.recovered(self.ICUAdult[i])
                    l = self.ICUAdult.pop(i)
                    size = size - 1

        size = len(self.VenAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.VenAdult[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toDie, 1 - self.toDie), k=1)
                if st[0] == 1:
                    lim_ = random.triangular(5, 7, 12)
                    lim = int(lim_)
                    self.people[self.VenAdult[i]].setLimit(lim)
                    self.people[self.VenAdult[i]].setStatus("Dead")
                    self.deadAdult.append(self.VenAdult[i])
                    l = self.VenAdult.pop(i)
                    size = size - 1
                else:
                    self.people[self.VenAdult[i]].setLimit(self.immune_days)
                    self.people[self.VenAdult[i]].setStatus("Cured")
                    self.cured(self.VenAdult[i])
                    self.recovered(self.VenAdult[i])
                    l = self.VenAdult.pop(i)
                    size = size - 1

        size = len(self.VenKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.VenKid[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toDie, 1 - self.toDie), k=1)
                if st[0] == 1:
                    lim = int(-1)
                    self.people[self.VenKid[i]].setLimit(lim)
                    self.people[self.VenKid[i]].setStatus("Dead")
                    self.deadKid.append(self.VenKid[i])
                    l = self.VenKid.pop(i)
                    size = size - 1
                else:
                    self.people[self.VenKid[i]].setLimit(self.immune_days)
                    self.people[self.VenKid[i]].setStatus("Cured")
                    self.cured(self.VenKid[i])
                    self.recovered(self.VenKid[i])
                    l = self.VenKid.pop(i)
                    size = size - 1

        size = len(self.VenYoung)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.VenYoung[i]].reachedLimit():
                st = random.choices([1, 0], weights=(self.toDie, 1 - self.toDie), k=1)
                if st[0] == 1:
                    lim = int(-1)
                    self.people[self.VenYoung[i]].setLimit(lim)
                    self.people[self.VenYoung[i]].setStatus("Dead")
                    self.deadYoung.append(self.VenYoung[i])
                    l = self.VenYoung.pop(i)
                    size = size - 1
                else:
                    self.people[self.VenYoung[i]].setLimit(self.immune_days)
                    self.people[self.VenYoung[i]].setStatus("Cured")
                    self.cured(self.VenYoung[i])
                    self.recovered(self.VenYoung[i])
                    l = self.VenYoung.pop(i)
                    size = size - 1

        size = len(self.curedKid)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.curedKid[i]].reachedLimit():
                self.people[self.curedKid[i]].setStatus("Healthy")
                l = self.curedKid.pop(i)
                size = size - 1

        size = len(self.curedYoung)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.curedYoung[i]].reachedLimit():
                self.people[self.curedYoung[i]].setStatus("Healthy")
                l = self.curedYoung.pop(i)
                size = size - 1

        size = len(self.curedAdult)
        for i in range(size):
            if i >= size:
                break
            if self.people[self.curedAdult[i]].reachedLimit():
                self.people[self.curedAdult[i]].setStatus("Healthy")
                l = self.curedAdult.pop(i)
                size = size - 1


    # ---- Complted funtion definition of update() ----#

    # ---- Set daily records ----#
    #[[[kid],[young],[adult],[total]],[[kid],[young],[adult],[total]]]
    #            district1                     district2
    #array[dist][0].append(tempKid)
    def record(self):

        kid = [0]*self.dists
        young =  [0]*self.dists
        adult =  [0]*self.dists

        if len(self.asympKid) is 0:
            self.asympKidNum.append(0)
        else:
            self.asympKidNum.append(len(self.asympKid))
            for i in range(len(self.asympKid)):
                # if(self.people[self.asympKid[i]].getDistrict()==1):
                #     print(" 681 : here ")
                kid[self.people[self.asympKid[i]].getDistrict()] =  kid[self.people[self.asympKid[i]].getDistrict()] + 1

        if len(self.asympYoung) is 0:
            self.asympYoungNum.append(0)
        else:
            self.asympYoungNum.append(len(self.asympYoung))
            for i in range(len(self.asympYoung)):
                young[self.people[self.asympYoung[i]].getDistrict()] = young[self.people[self.asympYoung[i]].getDistrict()] + 1

        if len(self.asympAdult) is 0:
            self.asympAdultNum.append(0)
        else:
            self.asympAdultNum.append(len(self.asympAdult))
            for i in range(len(self.asympAdult)):
                adult[self.people[self.asympAdult[i]].getDistrict()] = adult[self.people[self.asympAdult[i]].getDistrict()] + 1
        #self.distAsymp = [[[], [], [], []]] * self.dists


        for i in range(self.dists):
            self.distAsymp[i][0].append(kid[i])
            self.distAsymp[i][1].append(young[i])
            self.distAsymp[i][2].append(adult[i])
            self.distAsymp[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        young =  [0]*self.dists
        adult =  [0]*self.dists
        total = [0]*self.dists

        if (len(self.sympKid) is 0):
            self.sympKidNum.append(0)
        else:
            self.sympKidNum.append(len(self.sympKid))
            for i in range(len(self.sympKid)):
                kid[self.people[self.sympKid[i]].getDistrict()] = kid[self.people[self.sympKid[i]].getDistrict()] + 1

        if len(self.sympYoung) is 0:
            self.sympYoungNum.append(0)
        else:
            self.sympYoungNum.append(len(self.sympYoung))
            for i in range(len(self.sympYoung)):
                young[self.people[self.sympYoung[i]].getDistrict()] = young[self.people[self.sympYoung[i]].getDistrict()] + 1

        if len(self.sympAdult) is 0:
            self.sympAdultNum.append(0)
        else:
            self.sympAdultNum.append(len(self.sympAdult))
            for i in range(len(self.sympAdult)):
                adult[self.people[self.sympAdult[i]].getDistrict()] = adult[self.people[self.sympAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distSymp[i][0].append(kid[i])
            self.distSymp[i][1].append(young[i])
            self.distSymp[i][2].append(adult[i])
            self.distSymp[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        young =  [0]*self.dists
        adult =  [0]*self.dists
        total = [0]*self.dists

        if (len(self.admittedKid) is 0):
            self.admittedKidNum.append(0)
        else:
            self.admittedKidNum.append(len(self.admittedKid))
            for i in range(len(self.admittedKid)):
                kid[self.people[self.admittedKid[i]].getDistrict()] = young[self.people[self.admittedKid[i]].getDistrict()] + 1

        if len(self.admittedYoung) is 0:
            self.admittedYoungNum.append(0)
        else:
            self.admittedYoungNum.append(len(self.admittedYoung))
            for i in range(len(self.admittedYoung)):
                young[self.people[self.admittedYoung[i]].getDistrict()] = young[self.people[self.admittedYoung[i]].getDistrict()] + 1

        if len(self.admittedAdult) is 0:
            self.admittedAdultNum.append(0)
        else:
            self.admittedAdultNum.append(len(self.admittedAdult))
            for i in range(len(self.admittedAdult)):
                adult[self.people[self.admittedAdult[i]].getDistrict()] = adult[self.people[self.admittedAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distAdmitted[i][0].append(kid[i])
            self.distAdmitted[i][1].append(young[i])
            self.distAdmitted[i][2].append(adult[i])
            self.distAdmitted[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        young =  [0]*self.dists
        adult =  [0]*self.dists
        total = [0]*self.dists

        if len(self.ICUKid) is 0:
            self.ICUKidNum.append(0)
        else:
            self.ICUKidNum.append(len(self.ICUKid))
            for i in range(len(self.ICUKid)):
                kid[self.people[self.ICUKid[i]].getDistrict()] = kid[self.people[self.ICUKid[i]].getDistrict()] + 1

        if len(self.ICUYoung) is 0:
            self.ICUYoungNum.append(0)
        else:
            self.ICUYoungNum.append(len(self.ICUYoung))
            for i in range(len(self.ICUYoung)):
                young[self.people[self.ICUYoung[i]].getDistrict()] = young[self.people[self.ICUYoung[i]].getDistrict()] + 1

        if len(self.ICUAdult) is 0:
            self.ICUAdultNum.append(0)
        else:
            self.ICUAdultNum.append(len(self.ICUAdult))
            for i in range(len(self.ICUAdult)):
                adult[self.people[self.ICUAdult[i]].getDistrict()] = adult[self.people[self.ICUAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distICU[i][0].append(kid[i])
            self.distICU[i][1].append(young[i])
            self.distICU[i][2].append(adult[i])
            self.distICU[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        young =  [0]*self.dists
        adult =  [0]*self.dists
        total = [0]*self.dists

        if len(self.VenKid) is 0:
            self.VenKidNum.append(0)
        else:
            self.VenKidNum.append(len(self.VenKid))
            for i in range(len(self.VenKid)):
                kid[self.people[self.VenKid[i]].getDistrict()] = kid[self.people[self.VenKid[i]].getDistrict()] + 1

        if len(self.VenYoung) is 0:
            self.VenYoungNum.append(0)
        else:
            self.VenYoungNum.append(len(self.VenYoung))
            for i in range(len(self.VenYoung)):
                young[self.people[self.VenYoung[i]].getDistrict()] = young[self.people[self.VenYoung[i]].getDistrict()] + 1

        if len(self.VenAdult) is 0:
            self.VenAdultNum.append(0)
        else:
            self.VenAdultNum.append(len(self.VenAdult))
            for i in range(len(self.VenAdult)):
                adult[self.people[self.VenAdult[i]].getDistrict()] = adult[self.people[self.VenAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distVen[i][0].append(kid[i])
            self.distVen[i][1].append(young[i])
            self.distVen[i][2].append(adult[i])
            self.distVen[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        adult = [0]*self.dists
        young = [0]*self.dists
        total = [0]*self.dists

        if len(self.deadKid) is 0:
            self.deadKidNum.append(0)
        else:
            self.deadKidNum.append(len(self.deadKid))
            for i in range(len(self.deadKid)):
                kid[self.people[self.deadKid[i]].getDistrict()] = kid[self.people[self.deadKid[i]].getDistrict()] + 1

        if len(self.deadYoung) is 0:
            self.deadYoungNum.append(0)
        else:
            self.deadYoungNum.append(len(self.deadYoung))
            for i in range(len(self.deadYoung)):
                young[self.people[self.deadYoung[i]].getDistrict()] = young[self.people[self.deadYoung[i]].getDistrict()] + 1

        if len(self.deadAdult) is 0:
            self.deadAdultNum.append(0)
        else:
            self.deadAdultNum.append(len(self.deadAdult))
            for i in range(len(self.deadAdult)):
                adult[self.people[self.deadAdult[i]].getDistrict()] = adult[self.people[self.deadAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distDead[i][0].append(kid[i])
            self.distDead[i][1].append(young[i])
            self.distDead[i][2].append(adult[i])
            self.distDead[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0]*self.dists
        adult = [0]*self.dists
        young = [0]*self.dists
        total = [0]*self.dists

        if len(self.curedKid) is 0:
            self.curedKidNum.append(0)
        else:
            self.curedKidNum.append(len(self.curedKid))
            for i in range(len(self.curedKid)):
                kid[self.people[self.curedKid[i]].getDistrict()] = kid[self.people[self.curedKid[i]].getDistrict()] + 1

        if len(self.curedYoung) is 0:
            self.curedYoungNum.append(0)
        else:
            self.curedYoungNum.append(len(self.curedYoung))
            for i in range(len(self.curedYoung)):
                young[self.people[self.curedYoung[i]].getDistrict()] = young[self.people[self.curedYoung[i]].getDistrict()] + 1

        if len(self.curedAdult) is 0:
            self.curedAdultNum.append(0)
        else:
            self.curedAdultNum.append(len(self.curedAdult))
            for i in range(len(self.curedAdult)):
                adult[self.people[self.curedAdult[i]].getDistrict()] = adult[self.people[self.curedAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distCured[i][0].append(kid[i])
            self.distCured[i][1].append(young[i])
            self.distCured[i][2].append(adult[i])
            self.distCured[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0] * self.dists
        adult = [0] * self.dists
        young = [0] * self.dists
        total = [0] * self.dists

        if len(self.recoveredKid) is 0:
            self.recoveredKidNum.append(0)
        else:
            self.recoveredKidNum.append(len(self.recoveredKid))
            for i in range(len(self.recoveredKid)):
                kid[self.people[self.recoveredKid[i]].getDistrict()] = kid[self.people[self.recoveredKid[i]].getDistrict()] + 1

        if len(self.recoveredYoung) is 0:
            self.recoveredYoungNum.append(0)
        else:
            self.recoveredYoungNum.append(len(self.recoveredYoung))
            for i in range(len(self.recoveredYoung)):
                young[self.people[self.recoveredYoung[i]].getDistrict()] = young[self.people[self.recoveredYoung[i]].getDistrict()] + 1

        if len(self.recoveredAdult) is 0:
            self.recoveredAdultNum.append(0)
        else:
            self.recoveredAdultNum.append(len(self.recoveredAdult))
            for i in range(len(self.recoveredAdult)):
                adult[self.people[self.recoveredAdult[i]].getDistrict()] = adult[self.people[self.recoveredAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distRecovered[i][0].append(kid[i])
            self.distRecovered[i][1].append(young[i])
            self.distRecovered[i][2].append(adult[i])
            self.distRecovered[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0] * self.dists
        adult = [0] * self.dists
        young = [0] * self.dists
        total = [0] * self.dists

        if len(self.intInfectKid) is 0:
            self.intInfectKidNum.append(0)
        else:
            self.intInfectKidNum.append(len(self.intInfectKid))
            for i in range(len(self.intinfectKid)):
                kid[self.people[self.intInfectKid[i]].getDistrict()] = kid[self.people[self.intInfectKid[i]].getDistrict()] + 1

        if len(self.intInfectYoung) is 0:
            self.intInfectYoungNum.append(0)
        else:
            self.intInfectYoungNum.append(len(self.intInfectYoung))
            for i in range(len(self.intInfectYoung)):
                young[self.people[self.intInfectYoung[i]].getDistrict()] = young[self.people[self.intInfectYoung[i]].getDistrict()] + 1


        if len(self.intInfectAdult) is 0:
            self.intInfectAdultNum.append(0)
        else:
            self.intInfectAdultNum.append(len(self.intInfectAdult))
            for i in range(len(self.intinfectAdult)):
                adult[self.people[self.intInfectAdult[i]].getDistrict()] = adult[self.people[self.intInfectAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distIntInfect[i][0].append(kid[i])
            self.distIntInfect[i][1].append(young[i])
            self.distIntInfect[i][2].append(adult[i])
            self.distIntInfect[i][3].append(kid[i] + young[i] + adult[i])

        kid = [0] * self.dists
        adult = [0] * self.dists
        young = [0] * self.dists
        total = [0] * self.dists

        if len(self.nonintInfectKid) is 0:
            self.nonintInfectKidNum.append(0)
        else:
            self.nonintInfectKidNum.append(len(self.nonintInfectKid))
            for i in range(len(self.nonintInfectKid)):
                kid[self.people[self.nonintInfectKid[i]].getDistrict()] = kid[self.people[self.nonintInfectKid[i]].getDistrict()] + 1

        if len(self.nonintInfectYoung) is 0:
            self.nonintInfectYoungNum.append(0)
        else:
            self.nonintInfectYoungNum.append(len(self.nonintInfectYoung))
            for i in range(len(self.nonintInfectYoung)):
                young[self.people[self.nonintInfectYoung[i]].getDistrict()] = young[self.people[self.nonintInfectYoung[i]].getDistrict()] + 1

        if len(self.nonintInfectAdult) is 0:
            self.nonintInfectAdultNum.append(0)
        else:
            self.nonintInfectAdultNum.append(len(self.nonintInfectAdult))
            for i in range(len(self.nonintInfectAdult)):
                adult[self.people[self.nonintInfectAdult[i]].getDistrict()] = adult[self.people[self.nonintInfectAdult[i]].getDistrict()] + 1

        for i in range(self.dists):
            self.distNonintInfect[i][0].append(kid[i])
            self.distNonintInfect[i][1].append(young[i])
            self.distNonintInfect[i][2].append(adult[i])
            self.distNonintInfect[i][3].append(kid[i] + young[i] + adult[i])

        self.asympNum.append(len(self.asympKid) + len(self.asympYoung) + len(self.asympAdult))
        self.sympNum.append(len(self.sympKid) + len(self.sympYoung) + len(self.sympAdult))
        self.admittedNum.append(len(self.admittedKid) + len(self.admittedYoung) + len(self.admittedAdult))
        self.ICUNum.append(len(self.ICUKid) + len(self.ICUYoung) + len(self.ICUAdult))
        self.venNum.append(len(self.VenKid) + len(self.VenYoung) + len(self.VenAdult))
        self.deadNum.append(len(self.deadKid) + len(self.deadYoung) + len(self.deadAdult))
        self.curedNum.append(len(self.curedKid) + len(self.curedYoung) + len(self.curedAdult))
        self.recoveredNum.append(len(self.recoveredKid) + len(self.recoveredYoung) + len(self.recoveredAdult))
        self.intInfectNum.append(len(self.intInfectKid) + len(self.intInfectYoung) + len(self.intInfectAdult))
        self.nonintInfectNum.append(len(self.nonintInfectKid) + len(self.nonintInfectYoung) + len(self.nonintInfectAdult))

    # ---- Completed function definition of record() ---#

    # ---- Increment the number of days ----#

    def anotherDay(self):
        for i in range(len(self.asympKid)):
            self.people[self.asympKid[i]].increment()
            # print("Simulator/anotherday : Incremented " + self.asympKid[i].days)

        for i in range(len(self.asympYoung)):
            self.people[self.asympYoung[i]].increment()
            # print("Simulator/anotherday : Incremented " + self.asympYoung[i].days)

        for i in range(len(self.asympAdult)):
            self.people[self.asympAdult[i]].increment()
        #  print("Simulator/anotherday : Incremented " + str(self.people[self.asympAdult[i]].days))

        for i in range(len(self.sympKid)):
            self.people[self.sympKid[i]].increment()

        for i in range(len(self.sympYoung)):
            self.people[self.sympYoung[i]].increment()

        for i in range(len(self.sympAdult)):
            self.people[self.sympAdult[i]].increment()

        for i in range(len(self.admittedKid)):
            self.people[self.admittedKid[i]].increment()

        for i in range(len(self.admittedYoung)):
            self.people[self.admittedYoung[i]].increment()

        for i in range(len(self.admittedAdult)):
            self.people[self.admittedAdult[i]].increment()

        for i in range(len(self.ICUKid)):
            self.people[self.ICUKid[i]].increment()

        for i in range(len(self.ICUYoung)):
            self.people[self.ICUYoung[i]].increment()

        for i in range(len(self.ICUAdult)):
            self.people[self.ICUAdult[i]].increment()

        for i in range(len(self.VenKid)):
            self.people[self.VenKid[i]].increment()

        for i in range(len(self.VenYoung)):
            self.people[self.VenYoung[i]].increment()

        for i in range(len(self.VenAdult)):
            self.people[self.VenAdult[i]].increment()

        for i in range(len(self.deadAdult)):
            self.people[self.deadAdult[i]].increment()

        for i in range(len(self.deadYoung)):
            self.people[self.deadYoung[i]].increment()

        for i in range(len(self.deadKid)):
            self.people[self.deadKid[i]].increment()

        for i in range(len(self.curedAdult)):
            self.people[self.curedAdult[i]].increment()

        for i in range(len(self.curedYoung)):
            self.people[self.curedYoung[i]].increment()

        for i in range(len(self.curedKid)):
            self.people[self.curedKid[i]].increment()

        self.update()

    # ---- Completed function definition of anotherDay() ----#

    def firstQuarter(self):
        lim = int(len(self.people) / 4)
        self.writer.log("From first " +str(lim))
        for i in range(lim):
            self.setclosest(i)

    def secondQuarter(self):
        lim1 = int(len(self.people)/ 4)
        lim2 = int(len(self.people) / 2)
        self.writer.log("From second " + str(lim1)+ " : "+str(lim2))
        for i in range(lim1, lim2):
            self.setclosest(i)

    def thirdQuarter(self):
        lim1 = int(len(self.people) / 2)
        lim2 = int((3*len(self.people)) / 4)
        self.writer.log("From third " + str(lim1) + " : " + str(lim2))
        for i in range(lim1, lim2):
            self.setclosest(i)

    def fourthQuarter(self):
        lim = int(3 *len(self.people) / 4)
        self.writer.log("From fourth " + str(lim) + " : " + str(len(self.people)))
        for i in range(lim, len(self.people)):
            self.setclosest(i)

    def clear(self):
        self.distAsymp = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distSymp = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distAdmitted = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distCured = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distRecovered = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distICU = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distVen = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distDead = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distIntInfect = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.distNonintInfect = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.pr = person()
        self.curedKid = []
        self.curedYoung = []
        self.curedAdult = []
        self.recoveredKid = []
        self.recoveredYoung = []
        self.recoveredAdult = []
        self.intInfectKid = []
        self.intInfectYoung = []
        self.intInfectAdult = []
        self.nonintInfectKid = []
        self.nonintInfectYoung = []
        self.nonintInfectAdult = []
        self.asympKid = []
        self.asympYoung = []
        self.asympAdult = []
        self.admittedKid = []
        self.admittedYoung = []
        self.admittedAdult = []
        self.ICUKid = []
        self.ICUYoung = []
        self.ICUAdult = []
        self.VenKid = []
        self.VenYoung = []
        self.VenAdult = []
        self.deadKid = []
        self.deadYoung = []
        self.deadAdult = []
        self.sympYoung = []
        self.sympKid = []
        self.sympAdult = []
        self.asympKidNum = []
        self.asympYoungNum = []
        self.asympAdultNum = []
        self.admittedKidNum = []
        self.admittedYoungNum = []
        self.admittedAdultNum = []
        self.ICUKidNum = []
        self.ICUYoungNum = []
        self.ICUAdultNum = []
        self.VenKidNum = []
        self.VenYoungNum = []
        self.VenAdultNum = []
        self.sympYoungNum = []
        self.sympKidNum = []
        self.sympAdultNum = []
        self.deadYoungNum = []
        self.deadKidNum = []
        self.deadAdultNum = []
        self.curedYoungNum = []
        self.curedKidNum = []
        self.recoveredAdultNum = []
        self.recoveredYoungNum = []
        self.recoveredKidNum = []
        self.intInfectKidNum = []
        self.intInfectYoungNum = []
        self.intInfectAdultNum = []
        self.nonintInfectKidNum = []
        self.nonintInfectYoungNum = []
        self.nonintInfectAdultNum = []
        self.curedAdultNum = []
        self.asympNum = []
        self.sympNum = []
        self.admittedNum = []
        self.venNum = []
        self.ICUNum = []
        self.deadNum = []
        self.curedNum = []
        self.recoveredNum = []
        self.intInfectNum = []
        self.nonintInfectNum = []
        for per in self.people:
            self.mask_dist_percent = 0
            self.immune_days = 0
            self.close_circle = 0
            per.clear()



    # ---- Pretty much the most important function. It performs the simulation ----#
    def simulate(self):

        # ---- Bringing in the data of the people. It would be stored in people[] ---- #

        self.people = self.dataPool.getPeople()
        self.writer.log("Simulator/sim            : " + str(len(self.people)) + " people included in the simulation ")

        # ---- Data had been brought in ----

        # ---- Finding the closest people to each person, and storing their ids in closest[] ----
        m = 0
        counter = 1
        for i in range(len(self.people)):
            self.setcontacts(i)
            m = m+1
            if(m >= 25000):
                print("Finish setting the closest of "+str(m*counter)+" people")
                m = 0
                counter = counter+1

        t1 = threading.Thread(target=self.firstQuarter, args=())
        t2 = threading.Thread(target=self.secondQuarter, args=())
        t3 = threading.Thread(target=self.thirdQuarter, args=())
        t4 = threading.Thread(target=self.fourthQuarter, args=())
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

        self.writer.log("Simulator/sim            : Proximate people of each person set successfully")
        # ---- Closest people of each person had been set ---- #

        self.writer.log("\nSimulator/sim            : Starting simulator")
        for case in range(6):
            if case is 0:
                # print("Woah")
                self.mask_dist_percent = 100
                self.immune_days = 90
            elif case is 1:
                self.mask_dist_percent = 75
                self.immune_days = 90
            elif case is 2:
                self.mask_dist_percent = 50
                self.immune_days = 90
            elif case is 3:
                self.mask_dist_percent = 100
                self.immune_days = 180
            elif case is 4:
                self.mask_dist_percent = 75
                self.immune_days = 180
            elif case is 5:
                self.mask_dist_percent = 50
                self.immune_days = 180
            self.writer.log("\tRunnning case "+str(case+1))
            print("\tRunnning case "+str(case+1))
            self.asymp(0)  # Just one person is infected initially
            self.people[0].setStatus("Asymptamatic")
            self.people[0].setLimit(14)
            dist_mark = self.dataPool.dist_mark
            left = len(dist_mark)
            self.writer.log("We introduce one new carrier in each district every week.")
            for day in range(self.days):
                flag =True
                print("Simulating day: " + str(int(day)))
                if (day % 7 == 0) and (day < 300):
                    for i in range(len(dist_mark)):
                        if dist_mark[i] == dist_mark[-1]:
                            if(len(dist_mark)!=1):
                                break
                        if(left==1):
                            end = len(self.people)-1
                        # else:
                        #     end = dist_mark[i+1]-1
                        while (flag):
                            left = left -1
                            ran = random.randint(dist_mark[i],end)
                            if (self.people[ran].isHealthy()):
                                self.asymp(ran)
                                self.people[ran].setStatus("Asymptamatic")
                                self.people[ran].setLimit(14)
                                print("\t\tIntroduced new carrier on day : " + str(day))
                                flag = False
                for i in range(len(self.people)):
                    self.presentday = int(day)
                    self.coronaSpree(i)
                self.anotherDay()
                self.record()
            self.writer.createRecords(self, case)
            self.clear()
        self.writer.log("\nSimulator/sim            : Completed the simulation of " + str(len(self.people)) + " people over " + str(self.days+1) + " days.")

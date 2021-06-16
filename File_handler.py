import pandas as pd
import numpy as np
import Person as person
import Simulator as sim
import os as os
import linecache as line

class File_handler:
    def __init__(self,type):
        self.data = []
        self.record = ""
        self.base = "/home/sp_anbu/Narasimma/July28_Rangareddy/Data/"
        self.begin = 20
        self.dists = []
        self.districts = os.listdir('/home/sp_anbu/Narasimma/July28_Rangareddy/Data/Districts')
        self.houseRecords = []
        self.peopleRecords = []
        self.dist_mark = []

        for dist in self.districts:
            self.dists.append(dist)
            print("Dist : " + str(dist))

        if type.isnumeric() and type != str(-1):
            j=1
            if (os.path.isdir(self.base + "Result")):
                j = int(1)
                while (os.path.isdir(self.base + str("Result" + str(j)))):
                    j = j + 1
            j=j-1
            if(j==0):
                j=""
            self.base = self.base + str("Result" + str(j))
            self.console = self.base + "/" + "console.txt"
            district = int(-1)
            start = 0
            limit = int(type)
            lim = limit
            self.log("FileHandler/Constructor : Scanning " + (str(len(self.districts))) + " districts " + str(
                self.districts))
            self.log("FileHandler/Constructor : Need to access " + type + " people from each districts")

            for dist in self.districts:
                district = district + 1
                self.house = open("/home/sp_anbu/Narasimma/July28_Rangareddy/Data/Districts/" + dist + "/households.txt", "r")
                self.people = open("/home/sp_anbu/Narasimma/July28_Rangareddy/Data/Districts/" + dist +"/people.txt", "r")
                self.house.readline()
                self.people.readline()

                if(type != str(-1)):
                    for i in range(start,limit):
                        self.houseRecords.append(self.house.readline().split("\t"))
                        self.houseRecords[i].append(str(district))
                        # print(str(dist))

                    for i in range(start,limit):
                        self.peopleRecords.append(self.people.readline().split("\t"))
                        if i == start:
                            self.dist_mark.append(i)
                    self.log("\tCompleted extracting district info of : " + str(self.districts[district]))
                    start = limit
                    limit = limit + lim
        else:

            if(type != "writeData"):
                j = 1
                if (os.path.isdir(self.base + "Result")):
                    j = int(1)
                    while (os.path.isdir(self.base + str("Result" + str(j)))):
                        j = j + 1
                j = j - 1
                if (j == 0):
                    j = ""
                self.base = self.base + str("Result" + str(j))
                self.console = self.base + "/" + "console.txt"
                district = -1
                self.log("FileHandler/Constructor : Scanning " + (str(len(self.districts))) + " districts " + str(
                    self.districts))
                self.log("FileHandler/Constructor : Need to access everyone from each districts")
                ppl = 0

                for dist in self.districts:
                    start = 0
                    district = district + 1
                    self.house = open("/home/sp_anbu/Narasimma/July28_Rangareddy/Data/Districts/" + dist + "/households.txt", "r")
                    self.people = open("/home/sp_anbu/Narasimma/July28_Rangareddy/Data/Districts/" + dist + "/people.txt", "r")
                    self.house.readline()
                    self.people.readline()
                    def is_eof(f):
                        cur = f.tell()
                        f.seek(0,os.SEEK_END)
                        end = f.tell()
                        f.seek(cur,os.SEEK_SET)
                        return cur==end
                    i = 0
                    while(not is_eof(self.house)):
                        self.houseRecords.append(self.house.readline().split("\t"))
                        self.houseRecords[i].append(str(district))
                        if(i%10000 == 0):
                            self.log("File_handler/Constructor : "+str(i))
                        # print(i)
                        i=i+1
                    i=0
                    while(not is_eof(self.people)):
                        self.peopleRecords.append(self.people.readline().split("\t"))
                        # print(i)
                        if start==0:
                            self.dist_mark.append(ppl)
                            start = 1
                        i=i+1
                        ppl = ppl+1
                    self.log("\tCompleted extracting district info of : " + str(self.districts[district]) + " with " + str(i) + " people")

                self.log("File_Handler/Constructor : Data accessed successfully")

        if type == "writeData":
            self.base = "/home/sp_anbu/Narasimma/July28_Rangareddy/Data/"
            j=""
            if (os.path.isdir(self.base + "Result")):
                j = int(1)
                while (os.path.isdir(self.base + str("Result" + str(j)))):
                    j = j + 1
            os.mkdir(self.base + str("Result" + str(j)),0o777)
            self.base = self.base + str("Result" + str(j)) +"/"
            self.console = self.base + "/" + "console.txt"
            open(self.console,"a")
            print("File_Handler/Constructor : data recorder created successfully")

    def getDistricts(self):
        return self.districts

    def getHouseHolds(self):
        return self.houseRecords

    def getPeople(self):
        return self.peopleRecords

   # def getValues(self,id):
   #     pr = person.Person()
   #     pr.setValues(id,self.df[id][2],self.df[id][8],self.df[id][9])  # id,age,lat,long
   #     return pr

    def getMark(self):
        return self.dist_mark

    def size(self):
        return self.df.size-1

    def getDistrictData(self):
        i = 0
        for i in range(self.begin):
            self.dataFile.readline()
        x = self.dataFile.readline().split("*")
        while(x!=['', '\n']):
            self.data.append(x)
        return self.data

    def createRecords(self,sim,case_):
        case = "Case_" + str(case_+1) + "/"
        os.mkdir(self.base + case,0o777)
        os.mkdir(self.base + case + "OverAll",0o777)
        overall = str("OverAll")

        f = open(self.base + case + overall + "/SymptamaticKids.txt", "w+")
        f.write(str(sim.sympKidNum))
        f = open(self.base + case + overall + "/Symptamaticyoungpeople.txt", "w+")
        f.write(str(sim.sympYoungNum))
        f = open(self.base + case + overall + "/SymptamaticAdults.txt", "w+")
        f.write(str(sim.sympAdultNum))
        f = open(self.base + case + overall + "/OverallSymptamatic.txt", "w+")
        f.write(str(sim.sympNum))

        f = open(self.base + case + overall + "/AsymptamaticKids.txt", "w+")
        f.write(str(sim.asympKidNum))
        f = open(self.base + case + overall + "/Asymptamaticyoungpeople.txt", "w+")
        f.write(str(sim.asympYoungNum))
        f = open(self.base + case + overall + "/AsymptamaticAdults.txt", "w+")
        f.write(str(sim.asympAdultNum))
        f = open(self.base + case + overall + "/OverallAsymptamatic.txt", "w+")
        f.write(str(sim.asympNum))

        f = open(self.base + case + overall + "/AdmittedKids.txt", "w+")
        f.write(str(sim.admittedKidNum))
        f = open(self.base + case + overall + "/Admittedyoungpeople.txt", "w+")
        f.write(str(sim.admittedYoungNum))
        f = open(self.base + case + overall + "/AdmittedAdults.txt", "w+")
        f.write(str(sim.admittedAdultNum))
        f = open(self.base + case + overall + "/OverallAdmitted.txt", "w+")
        f.write(str(sim.admittedNum))

        f = open(self.base + case + overall + "/ICUedKids.txt", "w+")
        f.write(str(sim.ICUKidNum))
        f = open(self.base + case + overall + "/ICUedyoungpeople.txt", "w+")
        f.write(str(sim.ICUYoungNum))
        f = open(self.base + case + overall + "/ICUedAdults.txt", "w+")
        f.write(str(sim.ICUAdultNum))
        f = open(self.base + case + overall + "/OverallICUed.txt", "w+")
        f.write(str(sim.ICUNum))

        f = open(self.base + case + overall + "/VentillatoredKids.txt", "w+")
        f.write(str(sim.VenKidNum))
        f = open(self.base + case + overall + "/Ventillatoredyoungpeople.txt", "w+")
        f.write(str(sim.VenYoungNum))
        f = open(self.base + case + overall + "/VentillatoredAdults.txt", "w+")
        f.write(str(sim.VenAdultNum))
        f = open(self.base + case + overall + "/OverallVentillatored.txt", "w+")
        f.write(str(sim.venNum))

        f = open(self.base + case + overall + "/DeathofKids.txt", "w+")
        f.write(str(sim.deadKidNum))
        f = open(self.base + case + overall + "/Deathofyoungpeople.txt", "w+")
        f.write(str(sim.deadYoungNum))
        f = open(self.base + case + overall + "/DeathofAdults.txt", "w+")
        f.write(str(sim.deadAdultNum))
        f = open(self.base + case + overall + "/OverallDeath.txt", "w+")
        f.write(str(sim.deadNum))

        f = open(self.base + case + overall + "/ImmuneKids.txt", "w+")
        f.write(str(sim.curedKidNum))
        f = open(self.base + case + overall + "/Immuneyoungpeople.txt", "w+")
        f.write(str(sim.curedYoungNum))
        f = open(self.base + case + overall + "/ImmuneAdults.txt", "w+")
        f.write(str(sim.curedAdultNum))
        f = open(self.base + case + overall + "/OverallImmune.txt", "w+")
        f.write(str(sim.curedNum))

        f = open(self.base + case + overall + "/RecoveredKids.txt", "w+")
        f.write(str(sim.recoveredKidNum))
        f = open(self.base + case + overall + "/Recoveredyoungpeople.txt", "w+")
        f.write(str(sim.recoveredYoungNum))
        f = open(self.base + case + overall + "/RecoveredAdults.txt", "w+")
        f.write(str(sim.recoveredAdultNum))
        f = open(self.base + case + overall + "/OverallRecovered.txt", "w+")
        f.write(str(sim.recoveredNum))

        f = open(self.base + case + overall + "/IntInfectedKids.txt", "w+")
        f.write(str(sim.intInfectKidNum))
        f = open(self.base + case + overall + "/IntInfectedyoungpeople.txt", "w+")
        f.write(str(sim.intInfectYoungNum))
        f = open(self.base + case + overall + "/IntInfectedAdults.txt", "w+")
        f.write(str(sim.intInfectAdultNum))
        f = open(self.base + case + overall + "/OverallIntInfected.txt", "w+")
        f.write(str(sim.intInfectNum))

        f = open(self.base + case + overall + "/NonIntInfectedKids.txt", "w+")
        f.write(str(sim.nonintInfectKidNum))
        f = open(self.base + case + overall + "/NonIntInfectedyoungpeople.txt", "w+")
        f.write(str(sim.nonintInfectYoungNum))
        f = open(self.base + case + overall + "/NonIntInfectedAdults.txt", "w+")
        f.write(str(sim.nonintInfectAdultNum))
        f = open(self.base + case + overall + "/OverallNonIntInfected.txt", "w+")
        f.write(str(sim.nonintInfectNum))

        for i in range(len(self.dists)):
            os.mkdir(self.base + case + str(self.dists[i]),0o777)
            death_base = self.base + case
            tempBase = self.base + case + str(self.dists[i])
            f = open(tempBase + "/SymptamaticKids.txt", "w+")
            f.write(str(sim.distSymp[i][0]))
            f = open(tempBase + "/Symptamaticyoungpeople.txt", "w+")
            f.write(str(sim.distSymp[i][1]))
            f = open(tempBase + "/SymptamaticAdults.txt", "w+")
            f.write(str(sim.distSymp[i][2]))
            f = open(tempBase + "/OverallSymptamatic.txt", "w+")
            f.write(str(sim.distSymp[i][3]))

            f = open(tempBase + "/AsymptamaticKids.txt", "w+")
            f.write(str(sim.distAsymp[i][0]))
            f = open(tempBase + "/Asymptamaticyoungpeople.txt", "w+")
            f.write(str(sim.distAsymp[i][1]))
            f = open(tempBase + "/AsymptamaticAdults.txt", "w+")
            f.write(str(sim.distAsymp[i][2]))
            f = open(tempBase + "/OverallAsymptamatic.txt", "w+")
            f.write(str(sim.distAsymp[i][3]))

            f = open(tempBase + "/AdmittedKids.txt", "w+")
            f.write(str(sim.distAdmitted[i][0]))
            f = open(tempBase + "/Admittedyoungpeople.txt", "w+")
            f.write(str(sim.distAdmitted[i][1]))
            f = open(tempBase + "/AdmittedAdults.txt", "w+")
            f.write(str(sim.distAdmitted[i][2]))
            f = open(tempBase + "/OverallAdmitted.txt", "w+")
            f.write(str(sim.distAdmitted[i][3]))

            f = open(tempBase + "/ICUedKids.txt", "w+")
            f.write(str(sim.distICU[i][0]))
            f = open(tempBase + "/ICUedyoungpeople.txt", "w+")
            f.write(str(sim.distICU[i][1]))
            f = open(tempBase + "/ICUedAdults.txt", "w+")
            f.write(str(sim.distICU[i][2]))
            f = open(tempBase + "/OverallICUed.txt", "w+")
            f.write(str(sim.distICU[i][3]))

            f = open(tempBase + "/VentillatoredKids.txt", "w+")
            f.write(str(sim.distVen[i][0]))
            f = open(tempBase + "/Ventillatoredyoungpeople.txt", "w+")
            f.write(str(sim.distVen[i][1]))
            f = open(tempBase + "/VentillatoredAdults.txt", "w+")
            f.write(str(sim.distVen[i][2]))
            f = open(tempBase + "/OverallVentillatored.txt", "w+")
            f.write(str(sim.distVen[i][3]))

            f = open(tempBase + "/DeathofKids.txt", "w+")
            f.write(str(sim.distDead[i][0]))
            f = open(tempBase + "/Deathofyoungpeople.txt", "w+")
            f.write(str(sim.distDead[i][1]))
            f = open(tempBase + "/DeathofAdults.txt", "w+")
            f.write(str(sim.distDead[i][2]))
            f = open(tempBase + "/OverallDeath.txt", "w+")
            f.write(str(sim.distDead[i][3]))

            f = open(tempBase + "/ImmuneKids.txt", "w+")
            f.write(str(sim.distCured[i][0]))
            f = open(tempBase + "/Immuneyoungpeople.txt", "w+")
            f.write(str(sim.distCured[i][1]))
            f = open(tempBase + "/ImmuneAdults.txt", "w+")
            f.write(str(sim.distCured[i][2]))
            f = open(tempBase + "/OverallImmune.txt", "w+")
            f.write(str(sim.distCured[i][3]))

            f = open(tempBase + "/RecoveredKids.txt", "w+")
            f.write(str(sim.distRecovered[i][0]))
            f = open(tempBase + "/Recoveredyoungpeople.txt", "w+")
            f.write(str(sim.distRecovered[i][1]))
            f = open(tempBase + "/RecoveredAdults.txt", "w+")
            f.write(str(sim.distRecovered[i][2]))
            f = open(tempBase + "/OverallRecovered.txt", "w+")
            f.write(str(sim.distRecovered[i][3]))

            f = open(tempBase + "/IntInfectedKids.txt", "w+")
            f.write(str(sim.distIntInfect[i][0]))
            f = open(tempBase + "/IntInfectedyoungpeople.txt", "w+")
            f.write(str(sim.distIntInfect[i][1]))
            f = open(tempBase + "/IntInfectedAdults.txt", "w+")
            f.write(str(sim.distIntInfect[i][2]))
            f = open(tempBase + "/OverallIntInfected.txt", "w+")
            f.write(str(sim.distIntInfect[i][3]))

            f = open(tempBase + "/NonIntInfectedKids.txt", "w+")
            f.write(str(sim.distNonintInfect[i][0]))
            f = open(tempBase + "/NonIntInfectedyoungpeople.txt", "w+")
            f.write(str(sim.distNonintInfect[i][1]))
            f = open(tempBase + "/NonIntInfectedAdults.txt", "w+")
            f.write(str(sim.distNonintInfect[i][2]))
            f = open(tempBase + "/OverallNonIntInfected.txt", "w+")
            f.write(str(sim.distNonintInfect[i][3]))

            f = open(death_base + "/DeathRecords.txt","w+")
            age = [0]*120
            for person in sim.people:
                if(person.getStatus()=="Dead"):
                    if(int(person.age) < 120):
                        age[int(person.age)] = age[int(person.age)]+1
            f.write(str(age))
            self.log("\t\tFileHandler/createRecords : Records created for case " + str(case_))

    def log(self,st):
        # print(st)
        f = open(self.console , "a")
        f.writelines(st + "\n")











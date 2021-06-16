from File_handler import File_handler as Files
from Person import Person as Per
import math as math
import numpy as np
import pandas as pd


# import scipy.stats

class DataPool:
    def __init__(self, num):
        global df_people, df_house
        self.skipped = 0
        ppl = 0
        files = Files(str(num))
        self.districts = files.getDistricts()
        self.people = []
        self.houseRecord = []
        self.peopleRecord = []
        self.houseRecord = files.getHouseHolds()
        self.peopleRecord = files.getPeople()
        size = len(self.houseRecord) - 1
        for i in range(size):
            while (i <= size) and (self.houseRecord[i] == ['\n']):
                size = size - 1
                self.houseRecord.pop(i)
            if (i > size):
                break
            self.houseRecord[i][0] = float(self.houseRecord[i][0])
            self.houseRecord[i][4] = float(self.houseRecord[i][4])
            self.houseRecord[i][5] = float(self.houseRecord[i][5])
        self.houseRecord.sort(key=lambda x: x[1])

        size = len(self.peopleRecord) - 1
        for i in range(size):
            while (i <= size) and (self.peopleRecord[i] == ['\n']):
                size = size - 1
                self.peopleRecord.pop(i)
            if (i > size):
                break
            str.rstrip(self.peopleRecord[i][7])
            self.peopleRecord[i][2] = float(self.peopleRecord[i][2])
            self.peopleRecord[i][7] = float(self.peopleRecord[i][7])
            self.peopleRecord[i][1] = float(self.peopleRecord[i][1])
        self.peopleRecord.sort(key=lambda x: int(x[1]))

        houseLen = len(self.houseRecord)
        peopleLen = len(self.peopleRecord)
        # PeopleRecord : id, hh_id, age, sex ,race, hh_rel, school_id, work_id
        # houseRecord : hh_id, admin_code, hh_race, hh_income, latitude, longitude, district
        current = self.houseRecord[0][0]
        per = 0
        j = 0
        print("In data pool")
        # print(self.houseRecord[0])
        df_people = pd.DataFrame(self.peopleRecord,
                                 columns=['per_id', 'hh_id', 'age', 'sex', 'race', 'hh_rel', 'school_id', 'work_id'])
        df_house = pd.DataFrame(self.houseRecord, columns=['hh_id', 'admin_code', 'hh_race', 'hh_income', 'lat', 'lon','dist_id'])
        df_people.dropna()
        df_house.dropna()
        df_per = df_people.merge(df_house, on='hh_id')
        df_per1 = pd.DataFrame(df_per, columns=['per_id','age','lat','lon','hh_id','dist_id'])
        dict = {'per_id':float,'age':int,'lat':float,'lon':float,'hh_id':float,'dist_id':str}
        df_per1 = df_per1.astype(dict)
        peopleDict = df_per1.to_dict("records")

        print("Valid: " + str(len(peopleDict)) + " Total People: " + str(len(self.peopleRecord)) + " Houses: " + str(len(self.houseRecord)))
        files.log("Valid: " + str(len(peopleDict)) + " Total People: " + str(len(self.peopleRecord)) + " Houses: " + str(len(self.houseRecord)))
        #print(self.peopleRecord[0].age)

        for i in range(len(peopleDict)):

            per = Per()
            per.setValues(peopleDict[i]["per_id"],peopleDict[i]["age"],peopleDict[i]["lat"],peopleDict[i]["lon"],peopleDict[i]["hh_id"],int(peopleDict[i]["dist_id"]))
            self.people.append(per)
        self.dist_mark = files.getMark()
        files.log("\nDataPool/Constructor    : Including a total of " + str(len(self.people)) + " in the simulation")
        files.log("DataPool/Constructor    : Skipped " + str(self.skipped) + " due to unavailable and/or invalid data")

    def getPeople(self):
        return self.people

    def getNum(self, per):
        # print("Per distr: " + str(self.districts[0]))
        if (str(self.districts[0]) == "28532"):
            if (per.age < 5):
                return np.random.gamma(3.6, 1.1, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 1.1, 2)[1]
                # return int(er.pdf(5,1.07,2)[1])
            else:
                return np.random.gamma(5.11, 0.78, 2)[1]

        elif (str(self.districts[0]) == "28533"):
            if (per.age < 5):
                return np.random.gamma(3.53, 2.27, 2)[1]
                # return int(er,pdf(4,2.01,2)[1])
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 2.35, 2)[1]
                # return int(er.pdf(5,2.28,2)[1])
            else:
                return np.random.gamma(5.11, 1.67, 2)[1]

        elif (str(self.districts[0]) == "28534"):
            if (per.age < 5):
                return np.random.gamma(3.13, 3.18, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 3.03, 2)[1]
                # return int(er.pdf(5,2.95,2)[1])
            else:
                return np.random.gamma(5.11, 2.16, 2)[1]

        elif (str(self.districts[0]) == "28535"):
            if (per.age < 5):
                return np.random.gamma(4.32, 1.51, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 1.76, 2)[1]
                # return int(er.pdf(5,1.72,2)[1])
            else:
                return np.random.gamma(5.11, 1.26, 2)[1]

        elif (str(self.districts[0]) == "28536"):
            if (per.age < 5):
                return np.random.gamma(2.54, 144, 2)[1]
                # return int(er.pdf(3,122,2)[1])
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.14, 129, 2)[1]
            else:
                return np.random.gamma(3.3, 7.62, 2)[1]

        elif (str(self.districts[0]) == "28537"):
            if (per.age < 5):
                return np.random.gamma(3.21, 3.21, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 3.12, 2)[1]
                # return int(er.pdf(5,3.03,2)[1])
            else:
                return np.random.gamma(5.11, 2.22, 2)[1]

        elif (str(self.districts[0]) == "28538"):
            if (per.age < 5):
                return np.random.gamma(2.67, 2.14, 2)[1]
                # return int(er.pdf(3,1.9,2)[1])
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 1.8, 2)[1]
                # return int(er.pdf(5,1.75,2)[1])
            else:
                return np.random.beta(4.77, 10.5, 2)[1]

        elif (str(self.districts[0]) == "28539"):
            if (per.age < 5):
                return np.random.gamma(3.99, 1.31, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 1.46, 2)[1]
                # return int(er.pdf(5,1.42,2)[1])
            else:
                return np.random.beta(4.92, 10.8, 2)[1]

        elif (str(self.districts[0]) == "28540"):
            if (per.age < 5):
                return np.random.gamma(3.27, 2.16, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 2.12, 2)[1]
                # return int(er.pdf(5,2.06,2)[1])
            else:
                return np.random.beta(5.42, 12.1, 2)[1]

        elif (str(self.districts[0]) == "28541"):
            if (per.age < 5):
                return np.random.gamma(3.19, 2.14, 2)[1]
            elif (per.age < 60) and (per.age >= 5):
                return np.random.gamma(4.86, 2.06, 2)[1]
                # return int(er.pdf(5,2,2)[1])
            else:
                return np.random.beta(4.75, 10, 2)[1]

        else:
            return 10

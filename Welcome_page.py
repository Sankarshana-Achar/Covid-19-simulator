from Simulator import Simulator as Sim
import GraphGenerator as graph
import os as os
from DataPool import DataPool as Data
from File_handler import File_handler as fileMaintainer

if __name__ == '__main__':
    print("Welcome to COVID-19 simulator!")
    people = input("How many people would you like in the simulation? ")
    days = input("Over how many days would you like to simulate? ")
    sim = Sim(people,days)
    sim.simulate()

    while True:
        num = int(input("Which graph would you like to check? \n Press ( 1 ) for asymptamatic \n Press ( 2 ) for symptamatic \n Press ( 3 ) for hospitalised \n Press ( 4 ) for ICU-ed \n Press ( 5 ) for ventilator cases \n Press ( 6 ) for death \n Press ( 7 ) for immune \n Press ( 8 ) for recovered \n Press ( 9 ) to exit"))
        if num is 9:
            break
        age = int(input(
            "Press ( 1 ) for checking the trend among kids \n Press ( 2 ) for checking the trend among the youth \n Press ( 3 ) for checking the trend among the adults \n Press ( 4 ) to check overall trend "))

        if num is 1:
            if age is 1:
                graph.generate(sim, sim.asympKidNum)
            if age is 2:
                graph.generate(sim, sim.asympYoungNum)
            if age is 3:
                graph.generate(sim, sim.asympAdultNum)
            if age is 4:
                graph.generate(sim,sim.asympNum)

        if num is 2:
            if age is 1:
                graph.generate(sim, sim.sympKidNum)
            if age is 2:
                graph.generate(sim, sim.sympYoungNum)
            if age is 3:
                graph.generate(sim, sim.sympAdultNum)
            if age is 4:
                graph.generate(sim,sim.sympNum)

        if num is 3:
            if age is 1:
                graph.generate(sim, sim.admittedKidNum)
            if age is 2:
                graph.generate(sim, sim.admittedYoungNum)
            if age is 3:
                graph.generate(sim, sim.admittedAdultNum)
            if age is 4:
                graph.generate(sim,sim.admittedNum)

        if num is 4:
            if age is 1:
                graph.generate(sim, sim.ICUKidNum)
            if age is 2:
                graph.generate(sim, sim.ICUYoungNum)
            if age is 3:
                graph.generate(sim, sim.ICUAdultNum)
            if age is 4:
                graph.generate(sim,sim.ICUNum)


        if num is 5:
            if age is 1:
                graph.generate(sim, sim.VenKidNum)
            if age is 2:
                graph.generate(sim, sim.VenYoungNum)
            if age is 3:
                graph.generate(sim, sim.VenAdultNum)
            if age is 4:
                graph.generate(sim,sim.venNum)

        if num is 6:
            if age is 1:
                graph.generate(sim, sim.deadKidNum)
            if age is 2:
                graph.generate(sim, sim.deadYoungNum)
            if age is 3:
                graph.generate(sim, sim.deadAdultNum)
            if age is 4:
                graph.generate(sim,sim.deadNum)

        if num is 7:
            if age is 1:
                graph.generate(sim, sim.curedKidNum)
            if age is 2:
                graph.generate(sim, sim.curedYoungNum)
            if age is 3:
                graph.generate(sim, sim.curedAdultNum)
            if age is 4:
                graph.generate(sim,sim.curedNum)

        if num is 8:
            if age is 1:
                graph.generate(sim, sim.recoveredKidNum)
            if age is 2:
                graph.generate(sim, sim.recoveredYoungNum)
            if age is 3:
                graph.generate(sim, sim.recoveredAdultNum)
            if age is 4:
                graph.generate(sim,sim.recoveredNum)

    print("Thanks for using our simulator !")
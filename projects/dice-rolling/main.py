import math
from random import random

class diceSimulation():
    def __init__(self,diceCount):
        self.diceCount = diceCount
        self.rollDices()
    def rollDices(self):
        self.dices = []
        for i in range(0,self.diceCount):
            self.dices.append(int(math.ceil(random()*6)))
        self.printDices()
    def printDices(self):
        for dice in self.dices:
            self.result = ''
            for i in range(0,dice):
                self.result += '*'
            print(self.result,dice)
        self.again(input("Tekrar atmak ister misiniz?(y/n): "))
    def again(self,guess):
        if guess == "y":
            self.rollDices()
        elif guess == "n":
            print("Zar atma oyunu sona erdi.")

        

diceSimulation(int(input("Kaç adet zar kullanacaksınız: ")))
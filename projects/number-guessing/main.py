
from random import random

import math

class guessNumber():
    def __init__(self,option):
        self.option = option
        self.count = 0
        self.numberGenerator()
        self.guess()
    def numberGenerator(self):
        match self.option:
            case 1:
                self.num = int(math.ceil(random()*1000))
            case 2:
                self.num = int(math.ceil(random()*100))
            case 3:
                self.num = int(math.ceil(random()*10))
        return self.num
    def guess(self):
        self.guessNumber = int(input("Tahmin giriniz: "))
        self.count += 1
        self.guessControl()
    def guessControl(self):
        if self.guessNumber == self.num:
            print(f"Tebrikler {self.count}. tahmininizde doğru bildiniz.")
        elif self.guessNumber > self.num:
            print("Aşağı")
            self.guess()
        elif self.guessNumber < self.num:
            print("Yukarı")
            self.guess()

print("Seçenekler: \n 1- Zor (1-1000 aralığı) \n 2- Orta (1-100 aralığı) \n 3- Kolay (1-10 aralığı)")
guessNumber(int(input("")))
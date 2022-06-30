import math


import math
from random import random

class guessTheWord():
    def __init__(self):
        self.wrongCounter = 0
        self.initWords()
        self.choiceWord()
        self.guessLetter()
    def initWords(self):
        self.words = words = ["ekmek","proje"]
    def choiceWord(self):
        self.choosenWord = self.words[int((random()*len(self.words)))]
        self.replacingWord = self.choosenWord
    def guessLetter(self):
        if self.wrongCounter < 10:
            if self.replacingWord:
                self.letterGuess = input("Harf tahmini giriniz: ")
                self.checkGuess()
            else:
                print(f'{self.choosenWord} kelimesi tahmin edildi.')
        else:
            print(f'10 adet yanlış tahmin yapıldı. {self.choosenWord} kelimesi bilinemedi.')
    def checkGuess(self):
        print(self.replacingWord.count(self.letterGuess))
        if self.replacingWord.count(self.letterGuess):
            print(f'Girdiğiniz harf {self.replacingWord.count(self.letterGuess)} adet mevcuttur.')
            self.replacingWord = self.replacingWord.replace(self.letterGuess,'')
            self.guessLetter()
        else:
            print('Yanlış tahmin yaptınız.')
            self.wrongCounter += 1
            self.guessLetter()

guessTheWord()
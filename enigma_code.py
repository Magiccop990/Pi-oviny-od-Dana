import time, random

numbers = [1, 0]
number = str("")
let = list()
codex = {}
num_list = list()

class Decodex():
    def __init__(self):
        self.number = number
        self.numbers = numbers
        self.let = let
        self.codex = codex
        self.key = 0
        self.let_index = 0
        self.num_list = num_list

    def RandomNum(self):
        self.rand_num = random.choice(self.numbers)

    def Number(self):
        for i in range(6):
            control.RandomNum()
            self.number += str(self.rand_num)
            if self.number in self.num_list:
                self.number = str("")
                control.Number()

    def GetCodex(self):
        control.GetLet()
        self.number = str("")
        self.let_index = 0
        self.num_list = []
        for i in range(len(self.let)):
            control.Number()
            self.num_list.append(self.number)
            self.key = self.let[self.let_index]
            self.codex[self.key] = self.number
            self.let_index += 1
            self.number = str("")
        print("Codex succssesfuly created...")

    def Code(self):
        self.text = str(input("Please enter message: "))
        self.result = self.text
        self.let_index = 0
        for i in range(len(self.let)):
            self.key = self.let[self.let_index]
            self.number = self.codex[self.key]
            self.result = self.result.replace(self.key, " " + self.number)
            self.let_index += 1
            self.number = str("")
        print("Result: " + self.result)

    def Decode(self):
        self.let_index = 0
        self.text = self.result
        for i in range(len(self.let)):
            self.number = self.codex[self.let[self.let_index]]
            self.key = control.search_by_val(self.number)
            self.text = self.text.replace(" " + self.number, self.key)
            self.let_index += 1
        print(self.text)

    def search_by_val(self, val):
        for keys in self.codex:
            if val == self.codex[keys]:
                return keys

    def GetLet(self):
        self.letters = open("letter.txt", "r")
        self.letter = self.letters.read()
        self.alphabet = self.letter.split("\n")
        self.let = self.alphabet
        self.letters.close()

    def Main(self):
        self.command = str(input(">> "))
        if self.command == "/code":
            control.Code()
            control.Main()

        elif self.command == "/decode":
            control.Decode()
            control.Main()

        elif self.command == "/getcodex":
            control.GetCodex()
            control.Main()

        elif self.command == "/getlet":
            control.GetLet()
            print(self.let)
            control.Main()

        elif self.command == "/exit":
            exit()

        elif self.command == "/help":
            print("Avaible commands: /code /decode /exit /help /getcodex /getlet /searchbyval")
            control.Main()

        elif self.command == "/searchbyval":
            try:
                self.useless = int(input("Enter a number: "))
            except:
                raise TypeError
                print("Please enter a valid number")
            else:
                self.useless = control.search_by_val(self.useless)
                print(self.useless)
                control.Main()

        else:
            print("There is no command named " + self.command)
            control.Main()

control = Decodex()
control.GetCodex()
control.Main()

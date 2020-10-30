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
        self.safe_decode = False

    def RandomNum(self):
        self.rand_num = random.choice(self.numbers)

    def Number(self):
        for i in range(6):
            panel.RandomNum()
            self.number += str(self.rand_num)
            if self.number in self.num_list:
                self.number = str("")
                panel.Number()

    def NewCodex(self):
        panel.GetLet()
        self.number = str("")
        self.let_index = 0
        self.num_list = []
        for i in range(len(self.let)):
            panel.Number()
            self.num_list.append(self.number)
            self.key = self.let[self.let_index]
            self.codex[self.key] = self.number
            self.let_index += 1
            self.number = str("")
        print("Codex succssesfuly created...")

    def Code(self):
        self.safe_decode = True
        self.let_index = 0
        for i in range(len(self.let)):
            self.key = self.let[self.let_index]
            self.number = self.codex[self.key]
            self.result = self.result.replace(self.key, " " + self.number)
            self.let_index += 1
            self.number = str("")
        print("Result: " + self.result)

    def Decode(self):
        if self.safe_decode == True:
            self.let_index = 0
            self.text = self.result
            for i in range(len(self.let)):
                self.number = self.codex[self.let[self.let_index]]
                self.key = panel.search_by_val(self.number)
                self.text = self.text.replace(" " + self.number, self.key)
                self.let_index += 1
            print("Message: " + self.text)
            self.safe_decode = False
        else:
            print("You need to code a message first.")

    def search_by_val(self, val):
        for keys in self.codex:
            if val == self.codex[keys]:
                return keys

    def GetLet(self):
        try:
            self.letters_file = open("letter.txt", "r")
        except:
            self.letters_file_create = open("letter.txt", "w")
            self.letters_file_create.write("")
            print("File has been created, but you need to download the file from https://github.com/Streamer272/Pi-oviny-od-Dana/blob/master/letter.txt")
            self.letters_file_create.close()
            exit()
        else:
            self.letter = self.letters_file.read()
            self.alphabet = self.letter.split("\n")
            self.let = self.alphabet
            self.letters_file.close()

    def SaveCodex(self):
        self.codex_file = open("codex.txt", "w")
        self.let_index = 0
        for i in range(len(self.let)):
            self.number = self.codex[self.let[self.let_index]]
            self.key = panel.search_by_val(self.number)
            self.codex_file.write(self.key + ";" + self.number + "\n")
            self.let_index += 1
        self.codex_file.close()
        print("Codex save succssesful...")

    def ReadCodex(self):
        self.object = []
        self.codex = {}
        self.codex_read = open("codex.txt", "r")
        for i in range(len(self.let)):
            self.object = self.codex_read.readline().replace("\n", "")
            self.object = self.object.split(";")
            self.codex[str(self.object[0])] = str(self.object[1])
            self.object = str("")
        print("Codex read succssesful...")
        self.codex_read.close()

    def Main(self):
        self.command = str(input(">> "))
        if self.command[0] == "/":
            if "/code" in self.command:
                if self.command == "/code":
                    self.text = str(input("Please enter message: "))
                    self.result = self.text
                    panel.Code()
                    panel.Main()
                elif "/code" in self.command:
                    self.text = self.command.replace("/code ", "")
                    self.result = self.text
                    panel.Code()
                    panel.Main()

            elif "/decode" in self.command:
                if self.command == "/decode":
                    panel.Decode()
                    panel.Main()
                elif "/decode" in self.command:
                    self.result = self.command.replace("/decode", "")
                    for letter in self.let:
                        if letter in self.result:
                            print("Please enter only 1 and 0.")
                            panel.Main()
                    self.safe_decode = True
                    panel.Decode()
                    panel.Main()

            elif "/newcodex" in self.command:
                panel.NewCodex()
                panel.Main()

            elif "/print" in self.command:
                self.object = str("")
                self.object = self.command.replace("/print ", "")
                if self.object == "codex":
                    print(self.codex)
                    panel.Main()
                elif self.object == "letters":
                    panel.GetLet()
                    print(self.let)
                    panel.Main()
                else:
                    print("You need to enter a keyword.")
                    self.object = str("")
                    panel.Main()

            elif "/getkey" in self.command:
                self.object = str("")
                if self.command == "/getkey":
                    try:
                        self.object = str(input("Enter a number: "))
                    except:
                        print("Please enter a valid number")
                    else:
                        print("Letter: " + panel.search_by_val(self.object))
                        panel.Main()
                elif "/getkey" in self.command:
                    self.object = str(self.command.replace("/getkey ", ""))
                    print("Letter: " + panel.search_by_val(self.object))
                    self.object = str("")
                    panel.Main()

            elif "/getvalue" in self.command:
                self.object = str("")
                if "/getvalue" == self.command:
                    self.object = str(input("Please enter 1 letter: "))
                    try:
                        print("Letter: " + self.codex[self.object])
                    except:
                        print("You can enter only one letter.")
                    else:
                        panel.Main()
                if "/getvalue" in self.command:
                    self.object = self.command.replace("/getvalue ", "")
                    try:
                        print("Letter: " + self.codex[self.object])
                    except:
                        print("You can enter only one letter.")
                    else:
                        self.object = str("")
                        panel.Main()

            elif self.command == "/help":
                print("Avaible commands: /code /decode /newcodex /print /getkey /getvalue /help /exit /savecodex /getcodex")
                panel.Main()

            elif "/exit" in self.command:
                exit()

            elif "/getcodex" in self.command:
                panel.ReadCodex()
                panel.Main()

            elif "/savecodex" in self.command:
                panel.SaveCodex()
                panel.Main()

            else:
                print("There is no command named " + self.command)
                panel.Main()

        else:
            print("Please enter a valid command, to get command list type: /help")
            panel.Main()

panel = Decodex()
panel.NewCodex()

if __name__ == "__main__":
    panel.Main()

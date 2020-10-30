import time, random, os

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
        self.safe_codex = False
        #commands
        self.code = "/code"
        self.decode = "/decode"
        self.newcodex = "/newcodex"
        self.print = "/print"
        self.getkey = "/getkey"
        self.getvalue = "/getvalue"
        self.help = "/help"
        self.exit = "/exit"
        self.getcodex = "/getcodex"
        self.savecodex = "/savecodex"
        self.command_list = [self.code, self.decode, self.newcodex, self.print, self.getkey, self.getvalue, self.help, self.exit, self.getcodex, self.savecodex]
        self.text_output = str(self.command_list).replace(",", "")
        self.text_output = self.text_output.replace("[", "")
        self.text_output = self.text_output.replace("]", "")

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
        self.safe_codex = True
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
            print("\nWe cant fint 'letter.txt', you should consider downloading 'letter.txt' from https://github.com/Streamer272/Pi-oviny-od-Dana/blob/master/letter.txt\n")
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
        panel.GetLet()
        self.safe_codex = True
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
            if self.code in self.command:
                if self.safe_codex == True:
                    if self.command == self.code:
                        self.text = str(input("Please enter message: "))
                        self.result = self.text
                        panel.Code()
                        panel.Main()
                    elif self.code in self.command:
                        self.text = self.command.replace(self.code + " ", "")
                        self.result = self.text
                        panel.Code()
                        panel.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    panel.Main()

            elif self.decode in self.command:
                if self.safe_codex == True:
                    if self.command == self.decode:
                        panel.Decode()
                        panel.Main()
                    elif self.decode in self.command:
                        self.result = self.command.replace(self.decode, "")
                        for letter in self.let:
                            if letter in self.result:
                                print("Please enter only 1 and 0.")
                                panel.Main()
                        self.safe_decode = True
                        panel.Decode()
                        panel.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    panel.Main()

            elif self.newcodex in self.command:
                panel.NewCodex()
                panel.Main()

            elif self.print in self.command:
                self.object = str("")
                self.object = self.command.replace(self.print + " ", "")
                if self.object == "codex":
                    if self.safe_codex == True:
                        print(self.codex)
                        panel.Main()
                    else:
                        print("Codex has not been definied. Please definy the codex")
                        panel.Main()
                elif self.object == "letters":
                    panel.GetLet()
                    print(self.let)
                    panel.Main()
                elif self.object == "keywords":
                    print("Avable keywords: codex, letters")
                    panel.Main()
                else:
                    print("You need to enter a keyword. To get keywords please type: /print keywords")
                    self.object = str("")
                    panel.Main()

            elif self.getkey in self.command:
                if self.safe_codex == True:
                    self.object = str("")
                    if self.command == self.getkey:
                        try:
                            self.object = str(input("Enter a number: "))
                        except:
                            print("Please enter a valid number")
                        else:
                            print("Letter: " + panel.search_by_val(self.object))
                            panel.Main()
                    elif self.getkey in self.command:
                        self.object = str(self.command.replace(self.getkey + " ", ""))
                        print("Letter: " + panel.search_by_val(self.object))
                        self.object = str("")
                        panel.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    panel.Main()

            elif self.getvalue in self.command:
                if self.safe_codex == True:
                    self.object = str("")
                    if self.getvalue == self.command:
                        self.object = str(input("Please enter 1 letter: "))
                        try:
                            print("Letter: " + self.codex[self.object])
                        except:
                            print("You can enter only one letter.")
                        else:
                            panel.Main()
                    if self.getvalue in self.command:
                        self.object = self.command.replace(self.getvalue + " ", "")
                        try:
                            print("Letter: " + self.codex[self.object])
                        except:
                            print("You can enter only one letter.")
                        else:
                            self.object = str("")
                            panel.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    panel.Main()

            elif self.command == self.help:
                print("Avaible commands: " + self.text_output)
                panel.Main()

            elif self.exit in self.command:
                exit()

            elif self.getcodex in self.command:
                panel.ReadCodex()
                panel.Main()

            elif self.savecodex in self.command:
                panel.SaveCodex()
                panel.Main()

            else:
                print("There is no command named " + self.command)
                panel.Main()

        else:
            print("Please enter a valid command, to get command list type: /help")
            panel.Main()

panel = Decodex()

if __name__ == "__main__":
    panel.Main()

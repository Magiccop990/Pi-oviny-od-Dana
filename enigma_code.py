#variables
import random, socket

#variables
symbols = [1, 0]
number = str("")
let = list()
codex = {}
num_list = list()
let_index = 0
key = ""
result = ""
text = ""
letter = ""
alphabet = ""
letters_file = ""
codex_file = ""
obj = ""
codex_read = ""


#code, decode class
class Decodex():
    def __init__(self):
        global number, symbols, let, codex, num_list, let_index, key, result, text, letter, alphabet, letters_file, codex_file, obj, codex_read
        self.number = number
        self.symbols = symbols
        self.let = let
        self.codex = codex
        self.key = 0
        self.let_index = 0
        self.num_list = num_list
        self.safe_decode = False
        self.safe_codex = False

    def RandomNum(self):
        rand_num = random.choice(self.symbols)
        return rand_num

    def Number(self):
        for i in range(6):
            rand_num = panel.RandomNum()
            self.number += str(rand_num)
            if self.number in self.num_list:
                self.number = str("")
                panel.Number()
        return self.number

    def NewCodex(self):
        self.let = panel.GetLet()
        self.safe_codex = True
        self.number = str("")
        self.let_index = 0
        self.num_list = []
        for i in range(len(self.let)):
            number_to_codex = panel.Number()
            self.num_list.append(number_to_codex)
            self.key = self.let[self.let_index]
            self.codex[self.key] = self.number
            self.let_index += 1
            self.number = str("")
        print("Codex succssesfuly created...")
        return codex

    def Code(self, to_code):
        self.result = to_code
        self.let_index = 0
        for i in range(len(self.let)):
            self.key = self.let[self.let_index]
            self.number = self.codex[self.key]
            self.result = self.result.replace(self.key, " " + self.number)
            self.let_index += 1
            self.number = str("")
        return self.result

    def Decode(self, to_decode):
        panel.GetLet()
        self.result = to_decode
        self.let_index = 0
        self.text = self.result
        for i in range(len(self.let)):
            self.number = self.codex[self.let[self.let_index]]
            self.key = panel.search_by_val(self.number)
            self.text = self.text.replace(" " + self.number, self.key)
            self.let_index += 1
        return self.text

    def search_by_val(self, val):
        for keys in self.codex:
            if val == self.codex[keys]:
                return keys

    def GetLet(self):
        try:
            self.letters_file = open("letter.txt", "r")
        except:
            print("\nWe cant fint 'letter.txt', you should consider downloading 'letter.txt' from https://github.com/Streamer272/Main_Repository/blob/ENIGMA/letter.txt\n")
            exit()
        else:
            self.letter = self.letters_file.read()
            self.alphabet = self.letter.split("\n")
            self.let = self.alphabet
            self.letters_file.close()
        return self.let

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
        self.let = panel.GetLet()
        self.safe_codex = True
        self.obj = []
        self.codex = {}
        self.codex_read = open("codex.txt", "r")
        for i in range(len(self.let)):
            self.obj = self.codex_read.readline().replace("\n", "")
            self.obj = self.obj.split(";")
            self.codex[str(self.obj[0])] = str(self.obj[1])
            self.obj = str("")
        print("Codex read succssesful...")
        self.codex_read.close()
        return codex

    def TesCod(self):
        return self.safe_codex

    def SafDec(self, value):
        if value == True:
            self.safe_decode = True
        else:
            self.safe_decode = False

    def GetCod(self):
        return self.codex



#terminal + commands
class CommandLine():
    def __init__(self):
        #commands
        self.code_command = 0
        self.decode_command = 1
        self.newcodex_command = 2
        self.getkey_command = 3
        self.getvalue_command = 4
        self.help_command = 5
        self.exit_command = 6
        self.getcodex_command = 7
        self.savecodex_command = 8
        self.frequency_command = 9
        self.server_command = 10
        self.client_command = 11
        self.command_list = ["/code", "/decode", "/newcodex", 
        "/getkey", "/getvalue", "/help", 
        "/exit", "/getcodex", "/savecodex", "/frequency", 
        "/server", "/client"]
        
    #making variables global
    def GetVariables(self):
        global codex, obj
        self.obj = obj

    def Main(self):
        global let, codex, result, obj, msg
        terminal.GetVariables()
        self.let = panel.GetLet()
        self.command = str(input(">> "))
        if self.command[0] == "/":
            if "/rename" in self.command:
                self.obj = self.command.split(" ")
                old_name = self.obj[1]
                new_name = self.obj[2]
                index_number = self.command_list.index(old_name)
                self.command_list[index_number] = new_name
                print(old_name + " is now called " + new_name)
                terminal.Main()

            elif self.command_list[self.code_command] in self.command:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    if self.command == self.command_list[self.code_command]:
                        msg_to_code = str(input("Please enter message: "))
                        self.result = panel.Code(msg_to_code)
                        print("Result: " + self.result)
                        terminal.Main()
                    elif self.command_list[self.code_command] in self.command:
                        msg_to_code = self.command.replace(self.command_list[self.code_command] + " ", "")
                        self.result = panel.Code(msg_to_code)
                        print("Result: " + self.result)
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command_list[self.decode_command] in self.command:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    if self.command == self.command_list[self.decode_command]:
                        msg = panel.Decode(self.result)
                        print("Message: " + msg)
                        terminal.Main()
                    elif self.command_list[self.decode_command] in self.command:
                        self.result = self.command.replace(self.command_list[self.decode_command], "")
                        for letter in self.let:
                            if letter in self.result:
                                print("Please enter only 1 and 0.")
                                terminal.Main()
                        panel.SafDec(True)
                        msg = panel.Decode(self.result)
                        print("Message: " + msg)
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command_list[self.newcodex_command] in self.command:
                codex = panel.NewCodex()
                terminal.Main()

            elif self.command_list[self.getkey_command] in self.command:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    self.obj = str("")
                    if self.command == self.command_list[self.getkey_command]:
                        try:
                            self.obj = str(input("Enter a number: "))
                        except:
                            print("Please enter a valid number")
                        else:
                            print("Letter: " + panel.search_by_val(self.obj))
                            terminal.Main()
                    elif self.command_list[self.getkey_command] in self.command:
                        self.obj = str(self.command.replace(self.command_list[self.getkey_command] + " ", ""))
                        print("Letter: " + panel.search_by_val(self.obj))
                        self.obj = str("")
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command_list[self.getvalue_command] in self.command:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    self.obj = str("")
                    if self.command_list[self.getvalue_command] == self.command:
                        self.obj = str(input("Please enter 1 letter: "))
                        try:
                            print("Letter: " + self.codex[self.obj])
                        except:
                            print("You can enter only one letter.")
                        else:
                            terminal.Main()
                    if self.command_list[self.getvalue_command] in self.command:
                        self.obj = str(self.command.replace(self.command_list[self.getvalue_command] + " ", ""))
                        try:
                            print("Letter: " + self.codex[self.obj])
                        except:
                            print("You can enter only one letter.")
                        else:
                            self.obj = str("")
                            terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command == self.command_list[self.help_command] or self.command == "/":
                self.text_output = str(self.command_list).replace(",", "")
                self.text_output = self.text_output.replace("[", "")
                self.text_output = self.text_output.replace("]", "")
                print("Avaible commands: " + self.text_output)
                terminal.Main()

            elif self.command_list[self.exit_command] in self.command:
                print("Closing...")
                exit()

            elif self.command_list[self.getcodex_command] in self.command:
                self.codex = panel.ReadCodex()
                terminal.Main()

            elif self.command_list[self.savecodex_command] in self.command:
                panel.SaveCodex()
                terminal.Main()

            elif self.command == self.command_list[self.client_command]:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    recieve = cisco.Client()
                    msg = panel.Decode(recieve)
                    print("Message: " + msg)
                    terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command == self.command_list[self.server_command]:
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    msg_to_code = str(input("Please enter message: "))
                    msg_to_send = panel.Code(msg_to_code)
                    cisco.Server(msg_to_send)
                    terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.command_list[self.frequency_command] in self.command:
                if self.command_list[self.frequency_command] == self.command:
                    frequency = int(input("Enter new frequency: "))
                    print("The frequency is now: " + frequency)
                    terminal.Main()
                elif self.command_list[self.frequency_command] in self.command:
                    frequency = self.command.replace(self.command + " ", "")
                    print("The frequency is now: " + frequency)
                    terminal.Main()

            else:
                print("There is no command named " + self.command)
                terminal.Main()

        else:
            if self.command == "codex":
                safe_codex = panel.TesCod()
                if safe_codex == True:
                    self.codex = panel.GetCod()
                    print(self.codex)
                    terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()
            elif self.command == "let" or self.command == "letters":
                self.let = panel.GetLet()
                print(self.let)
                terminal.Main()
            elif self.command == "keywords":
                print("Avable keywords: codex, letters")
                terminal.Main()
            else:
                print("Please enter a valid command, to get command list type: /help or /")
                terminal.Main()



#cisco, local usage
class Online():
    def __init__(self):
        global msg, frequency
        frequency = 1234

    def Server(self, message):
        print("Server running...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), int(frequency)))
        s.listen(5)
        clientsocket, adress = s.accept()
        print("Client recieved the message...")
        clientsocket.send(bytes(message, "utf-8"))
        clientsocket.close()

    def Client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), int(frequency)))
        full_msg = ""
        while True:
            msg = s.recv(8)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")
        return full_msg

    def Main(self):
        self.input = str(input(">> "))


#def classes
panel = Decodex()
terminal = CommandLine()
cisco = Online()


#if not imported start process
if __name__ == "__main__":
    terminal.Main()

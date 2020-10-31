#variables
import time, random, os, socket

#variables
symbols = [1, 0]
number = str("")
let = list()
codex = {}
num_list = list()
let_index = 0
key = ""
result = ""
safe_decode = False
text = ""
letter = ""
alphabet = ""
letters_file = ""
codex_file = ""
safe_codex = False
obj = ""
codex_read = ""


#code, decode class
class Decodex():
    def __init__(self):
        global number, symbols, let, codex, num_list, let_index, key, result, safe_decode, text, letter, alphabet, letters_file, codex_file, safe_codex, obj, codex_read
        self.number = number
        self.symbols = symbols
        self.let = let
        self.codex = codex
        self.key = 0
        self.let_index = 0
        self.num_list = num_list
        self.safe_decode = False
        self.safe_codex = False
        #making variables global
        number = self.number
        symbols = self.symbols
        let = self.let
        codex = self.codex
        key = self.key
        let_index = self.let_index
        num_list = self.num_list
        safe_decode = self.safe_decode
        safe_codex = self.safe_codex

    def RandomNum(self):
        self.rand_num = random.choice(self.symbols)
        rand_num = self.rand_num

    def Number(self):
        for i in range(6):
            panel.RandomNum()
            self.number += str(self.rand_num)
            if self.number in self.num_list:
                self.number = str("")
                panel.Number()
        #making variables global
        number = self.number

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
        #making variables global
        safe_codex = self.safe_codex
        number = self.number
        let_index = self.let_index
        num_list = self.num_list
        key = self.key
        codex = self.codex

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
        #making variables global
        safe_codex = self.safe_codex
        let_index = self.let_index
        key = self.key
        number = self.number
        result = self.result

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
        #making variables global
        safe_decode = self.safe_decode
        let_index = self.let_index
        text = self.text
        result = self.result
        number = self.number
        key = self.key

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
        #making variables global
        letter = self.letter
        alphabet = self.alphabet
        let = self.let
        letters_file = self.letters_file

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
        #making variables global
        codex_file = self.codex_file
        let_index = self.let_index
        number = self.number
        key = self.key
        codex_file = self.codex_file

    def ReadCodex(self):
        panel.GetLet()
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
        #making variables global
        safe_codex = self.safe_codex
        obj = self.obj
        codex = self.codex
        codex_read = self.codex_read


#terminal + commands
class CommandLine():
    def __init__(self):
        #commands
        self.code_command= "/code"
        self.decode_command = "/decode"
        self.newcodex_command = "/newcodex"
        self.print_command = "/print"
        self.getkey_command = "/getkey"
        self.getvalue_command = "/getvalue"
        self.help_command = "/help"
        self.exit_command = "/exit"
        self.getcodex_command = "/getcodex"
        self.savecodex_command = "/savecodex"
        self.frequency_command = "/frequency"
        self.server_command = "/server"
        self.client_command = "/client"
        self.command_list = [self.code_command, self.decode_command, self.newcodex_command, self.print_command, self.getkey_command, self.getvalue_command, self.help_command, self.exit_command, self.getcodex_command, self.savecodex_command, self.frequency_command , self.client_command , self.server_command]
        self.text_output = str(self.command_list).replace(",", "")
        self.text_output = self.text_output.replace("[", "")
        self.text_output = self.text_output.replace("]", "")

    #making variables global
    def GetVariables(self):
        global number, symbols, let, codex, num_list, let_index, key, result, safe_decode, text, letter, alphabet, letters_file, codex_file, safe_codex, obj, codex_read
        self.number = number
        self.symbols = symbols
        self.let = let
        self.codex = codex
        self.num_list = num_list
        self.let_index = let_index
        self.key = key
        self.result = result
        self.safe_decode = safe_decode
        self.text = text
        self.letter = letter
        self.alphabet = alphabet
        self.letters_file = letters_file
        self.codex_file = codex_file
        self.safe_codex = safe_codex
        self.obj = obj
        self.codex_read = codex_read

    def Main(self):
        terminal.GetVariables()
        panel.GetLet()
        self.command = str(input(">> "))
        if self.command[0] == "/":
            if "/rename" in self.command:
                pass

            elif self.code_command in self.command:
                if self.safe_codex == True:
                    if self.command == self.code:
                        self.text = str(input("Please enter message: "))
                        self.result = self.text
                        panel.Code()
                        terminal.Main()
                    elif self.code_command in self.command:
                        self.text = self.command.replace(self.code_command + " ", "")
                        self.result = self.text
                        panel.Code()
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.decode_command in self.command:
                if self.safe_codex == True:
                    if self.command == self.decode_command:
                        panel.Decode()
                        terminal.Main()
                    elif self.decode_command in self.command:
                        self.result = self.command.replace(self.decode_command, "")
                        for letter in self.let:
                            if letter in self.result:
                                print("Please enter only 1 and 0.")
                                terminal.Main()
                        self.safe_decode = True
                        panel.Decode()
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.newcodex_command in self.command:
                panel.NewCodex()
                terminal.Main()

            elif self.print_command in self.command:
                self.obj = str("")
                self.obj = self.command.replace(self.print_command + " ", "")
                if self.obj == "codex":
                    if self.safe_codex == True:
                        print(self.codex)
                        terminal.Main()
                    else:
                        print("Codex has not been definied. Please definy the codex")
                        terminal.Main()
                elif self.obj == "letters":
                    panel.GetLet()
                    print(self.let)
                    terminal.Main()
                elif self.obj == "keywords":
                    print("Avable keywords: codex, letters")
                    terminal.Main()
                else:
                    print("You need to enter a keyword. To get keywords please type: /print keywords")
                    self.obj = str("")
                    terminal.Main()

            elif self.getkey_command in self.command:
                if self.safe_codex == True:
                    self.obj = str("")
                    if self.command == self.getkey_command:
                        try:
                            self.obj = str(input("Enter a number: "))
                        except:
                            print("Please enter a valid number")
                        else:
                            print("Letter: " + panel.search_by_val(self.obj))
                            terminal.Main()
                    elif self.getkey_command in self.command:
                        self.obj = str(self.command.replace(self.getkey_command + " ", ""))
                        print("Letter: " + panel.search_by_val(self.obj))
                        self.obj = str("")
                        terminal.Main()
                else:
                    print("Codex has not been definied. Please definy the codex")
                    terminal.Main()

            elif self.getvalue_command in self.command:
                if self.safe_codex == True:
                    self.obj = str("")
                    if self.getvalue_command == self.command:
                        self.obj = str(input("Please enter 1 letter: "))
                        try:
                            print("Letter: " + self.codex[self.obj])
                        except:
                            print("You can enter only one letter.")
                        else:
                            terminal.Main()
                    if self.getvalue_command in self.command:
                        self.obj = self.command.replace(self.getvalue_command + " ", "")
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

            elif self.command == self.help_command:
                print("Avaible commands: " + self.text_output)
                terminal.Main()

            elif self.exit_command in self.command:
                exit()

            elif self.getcodex_command in self.command:
                panel.ReadCodex()
                terminal.Main()

            elif self.savecodex_command in self.command:
                panel.SaveCodex()
                terminal.Main()

            if self.command == self.client_command:
                cisco.Client()
                terminal.Main()

            elif self.command == self.server_command:
                cisco.Server()
                terminal.Main()

            elif self.command == self.frequency_command:
                self.frequency = int(input("Enter new frequency: "))
                terminal.Main()

            else:
                print("There is no command named " + self.command)
                terminal.Main()

        else:
            print("Please enter a valid command, to get command list type: /help")
            terminal.Main()


#cisco, local usage
class Online():
    def __init__(self):
        self.frequency = 1234
    def Server(self):
        print("Server running...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.frequency))
        s.listen(5)
        clientsocket, adress = s.accept()
        print("Client successesfuly connected...")
        msg = str(input("Please enter message: "))
        clientsocket.send(bytes(msg, "utf-8"))
        clientsocket.close()

    def Client(self):
        print("Client running...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), self.frequency))
        print("Successesfuly connecter to server...")
        full_msg = ""
        while True:
            msg = s.recv(8)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")
        print("Message: " + full_msg)

    def Main(self):
        self.input = str(input(">> "))


#def classes
panel = Decodex()
terminal = CommandLine()
cisco = Online()


#if not imported start process
if __name__ == "__main__":
    terminal.Main()

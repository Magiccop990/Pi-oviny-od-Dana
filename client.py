import socket, threading, time

class Online():
    def __init__(self):
        self.frequency = 10000
        self.decode_format = "utf-8"
        self.DISCONNECT_MSG = "!d"
        self.ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
        self.IP_PORT = (self.ip, self.frequency)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recieve = True
        self.thread_run = True
        self.yes = False  #lol

    def Connect(self):
        try:
            self.client.connect(self.IP_PORT)
        except:
            print("The server isn't available...")
            exit()
        else:
            pass

    def rcv(self):
        while self.recieve:
            if self.thread_run:
                self.recieve_msg = self.client.recv(2048).decode(self.decode_format)
                if len(self.recieve_msg) == 0:
                    pass
                else:
                    self.recieve_msg = self.recieve_msg.replace("[", "")
                    self.recieve_msg = self.recieve_msg.replace("]", "")
                    self.recieve_msg = self.recieve_msg.replace("'", "")
                    if self.nickname in self.recieve_msg:
                        time.sleep(1)
                    elif self.recieve_msg != "[]":
                        print(f"{self.recieve_msg}")
                        time.sleep(1)
                    else:
                        time.sleep(1)
            else:
                break

    def send(self, msg):
        self.message_for_server = msg.encode(self.decode_format)
        self.client.send(self.message_for_server)
        return self.message_for_server

    def start(self):
        cisco.Connect()
        self.nickname = str(input("Nickname: "))
        cisco.send(self.nickname)
        self.recieve_thread = threading.Thread(target=cisco.rcv)  
        self.main_thread = threading.Thread(target=cisco.main)
        self.main_thread.start()
        cisco.send("")
        self.recieve_thread.start()

    def main(self):
        while True:
            if self.thread_run:
                self.to_send = str(input(""))
                if self.to_send == self.DISCONNECT_MSG:
                    cisco.send("!disconnect")
                    self.thread_run = False
                    time.sleep(0.5)
                    exit()
                else:
                    self.message_for_server = cisco.send(self.to_send)
            else:
                break

cisco = Online()

if __name__ == "__main__":
    cisco.start()

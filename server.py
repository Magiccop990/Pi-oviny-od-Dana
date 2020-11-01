import socket, threading, time


class Server():
    def __init__(self):
        self.frequency = 1234  #frequency
        self.ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
        self.name = socket.gethostname()  #pc name
        print(self.ip + " + " + self.name)
        self.IP_PORT = (self.ip, self.frequency)  #server describtiom
        self.FORMAT = "utf-8"
        self.DISCONNECT_MSG = "!disconnect"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket type
        self.server.bind(self.IP_PORT)  #bind the server describtion to IP_PORT
        self.msg_for1 = []
        self.msg_for2 = []
        self.connected1 = False
        self.connected2 = False
        self.stop = False
        self.exit_ = True

    def SendToClient1(self):
        while True:
            if len(self.msg_for1) != 0:
                if self.connected1 == True:
                    self.client1.send(str(self.msg_for1).encode(self.FORMAT))
                    self.msg_for1 = []
                else:
                    time.sleep(1)

    def SendToClient2(self):
        while True:
            if len(self.msg_for2) != 0:
                if self.connected2 == True:
                    self.client2.send(str(self.msg_for2).encode(self.FORMAT))
                    self.msg_for2 = []
                else:
                    time.sleep(1)

    def handle_client1(self):
        while self.connected1:
            self.msg = self.client1.recv(1024).decode(self.FORMAT)
            self.msg_for2.append(self.msg)
            if self.msg == self.DISCONNECT_MSG:
                self.connected1 = False
                print(f"{self.IP_PORT} disconnected...")
                self.msg_for2.append("One member disconnected...")
                break
            print(f"{self.IP_PORT} {self.msg}")
        self.client1.close()

    def handle_client2(self):
        while self.connected2:
            self.msg = self.client2.recv(1024).decode(self.FORMAT)
            self.msg_for1.append(self.msg)
            if self.msg == self.DISCONNECT_MSG:
                self.connected2 = False
                print(f"{self.IP_PORT} disconnected...")
                self.msg_for1.append("One member disconnected...")
                break
            print(f"{self.IP_PORT} {self.msg}")
        self.client1.close()

    def Exit(self):
        while True:
            if self.exit_ == True:
                time.sleep(10)
                if self.connected1 == False and self.connected2 == False:
                    print("Everyone left, it's so dark here...")
                else:
                    pass
            else:
                break
    
    def client1_start(self):
        self.client1, self.IP_PORT1 = self.server.accept()
        print(f"New client {self.IP_PORT1}")
        self.connected1 = True
        self.message_send_thread1.start()
        s.handle_client1()

    def client2_start(self):
        self.client2, self.IP_PORT2 = self.server.accept()
        print(f"New client {self.IP_PORT2}")
        self.connected2 = True
        self.message_send_thread2.start()
        s.handle_client2()

    def Threads(self):
        self.destroy = threading.Thread(target=s.Exit)
        self.thread1 = threading.Thread(target=s.client1_start)
        self.thread2 = threading.Thread(target=s.client2_start)
        self.message_send_thread1 = threading.Thread(target=s.SendToClient2)
        self.message_send_thread2 = threading.Thread(target=s.SendToClient1)

    def main(self):
        s.Threads()
        self.server.listen()
        self.thread1.start()
        self.thread2.start()
        self.destroy.start()

s = Server()

if __name__ == "__main__":
    print("Server is running...")
    s.main()

import socket, threading, time  #we need all these modules

#main class
class Server():
    def __init__(self):
        self.frequency = 10000  #frequency
        self.ip = "0.0.0.0"# - "95.103.201.58" / "192.168.1.21"
        self.name = socket.gethostname()  #pc name
        self.IP_PORT = (self.ip, self.frequency)  #server describtiom
        self.decode_format = "utf-8"  #encode format
        self.DISCONNECT_MSG = "!disconnect"  #disconnect msg
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket type
        self.server.bind(self.IP_PORT)  #bind the server describtion to IP_PORT
        self.exit_protocol = False  #if True program will close
        self.connections = {}  #all clients that connecter to server
        self.from_nick = ""
        self.msg_rcv_bol = False  #to be able to watch message sending

    #handle every client, every client will run on this code
    def handle(self, client, client_ip):
        nickname = client.recv(1024).decode(self.decode_format)
        print(f"Welcome {nickname}")  #welcome on server
        connected = True
        while connected:
            if self.exit_protocol:
                break
            self.msg = client.recv(1024).decode(self.decode_format)  #recieve message
            self.from_nick = nickname
            print(f"{nickname}: {self.msg}")  #print message
            self.msg_rcv_bol = True
            cisco.Send()  #send message to all clients
            if self.msg == self.DISCONNECT_MSG:  #if message == disconnect message: break
                connected = False
                print(f"{nickname} disconnected...")
                self.connections[client] = False  #TypeError: 'socket' object cannot be interpreted as an integer
        client.close()

    #watch if anyone send message, if not, start countdown(30 s), when finished, print "It's so dark here, everyone left..."
    def Watcher(self):
        num = 0
        while True:
            if self.exit_protocol:
                break
            if num == 30:
                print("It's so dark here, everyone left...")
                num = 0
            elif self.msg_rcv_bol == True:
                self.msg_rcv_bol = False
                num = 0
            elif self.msg_rcv_bol == False:
                num += 1
                time.sleep(1)

    #send message to every client
    def Send(self):
        for conns in self.connections:
            if self.connections[conns] == True:
                conns.send(self.from_nick.encode(self.decode_format) + ": ".encode(self.decode_format) + self.msg.encode(self.decode_format))  #send message
            else:
                pass

    #client connections accept
    def Main(self):
        self.server.listen(5)  #the server can hold up to 5 clients
        watch = threading.Thread(target=cisco.Watcher)  #watcher thread
        watch.start()  #watcher start
        while True:
            if self.exit_protocol:
                break
            connection, IP_PORT = self.server.accept()  #new connection accept
            self.connections[connection] = True  #list gets connection
            client_thread = threading.Thread(target=cisco.handle, args=(connection, IP_PORT))  #start that more time than one
            client_thread.start()  #start that thread

cisco = Server()

#dufam ze toto vies co robi
if __name__ == "__main__":
    print("Server is running...")
    cisco.Main()

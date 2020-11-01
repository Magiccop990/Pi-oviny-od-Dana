import socket, threading, time

class Online():
    def __init__(self):
        self.frequency = 1234
        self.FORMAT = "utf-8"
        self.DISCONNECT_MSG = "!d"
        self.ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
        self.IP_PORT = (self.ip, self.frequency)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rcv = True

    def Connect(self):
        try:
            self.client.connect(self.IP_PORT)
        except:
            print("The server isn't available...")
            exit()
        else:
            pass

    def rcv(self):
        while self.rcv:
            self.rcv_msg = self.client.recv(2048).decode(self.FORMAT)
            self.rcv_msg = self.rcv_msg.replace("[", "")
            self.rcv_msg = self.rcv_msg.replace("]", "")
            self.rcv_msg = self.rcv_msg.replace("'", "")
            print(f"Friend: {self.rcv_msg}")
            time.sleep(1)

    def send(self, msg):
        self.message_for_server = self.msg.encode(FORMAT)
        self.client.send(self.message_for_server)

    def main(self):
        cisco.Connect()
        self.rcv_thread = threading.Thread(target=cisco.rcv)
        self.rcv_thread.start()
        while True:
            self.to_send = str(input(""))
            if self.to_send == self.DISCONNECT_MSG:
                cisco.send("!disconnect")
                break
            else:
                cisco.send(self.to_send)

cisco = Online()

if __name__ == "__main__":
    cisco.main()

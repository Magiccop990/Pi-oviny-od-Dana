import socket, threading

frequency = 5050  #frequency
FORMAT = "utf-8"
DISCONNECT_MSG = "!disconnect"
ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
IP_PORT = (ip, frequency)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(IP_PORT)

def rcv():
    print(client.recv(2048).decode(FORMAT))

def send(msg):
    message_for_server = msg.encode(FORMAT)
    client.send(message_for_server)
    thread = threading.Thread(target=rcv)
    thread.start()

while True:
    to_send = str(input(":"))
    if to_send == "!disconnect":
        send(to_send)
        break
    else:
        send(to_send)

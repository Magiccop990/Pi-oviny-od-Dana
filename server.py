import socket, threading

frequency = 5050  #frequency
ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
name = socket.gethostname()  #pc name
print(ip + " + " + name)
IP_PORT = (ip, frequency)  #server describtiom
FORMAT = "utf-8"
DISCONNECT_MSG = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket type
server.bind(IP_PORT)  #bind the server describtion to IP_PORT

def handle_client1():
    client1, IP_PORT1 = server.accept()  #new connection accept
    print(f"New client {IP_PORT1}")
    connected = True
    while connected:
        msg = client1.recv(1024).decode(FORMAT)  #recieve message
        if msg == DISCONNECT_MSG:
            connected = False
            print(f"{IP_PORT} disconnected...")
            break
        print(f"{IP_PORT}: {msg}")
        client1.send("msg delivered".encode(FORMAT))
    client1.close()

def handle_client2():
    client2, IP_PORT2 = server.accept()  #new connection accept
    print(f"Welcome {IP_PORT2}")
    connected = True
    while connected:
        msg = client2.recv(1024).decode(FORMAT)  #recieve message
        print(f"{IP_PORT}: {msg}")
        if msg == DISCONNECT_MSG:
            connected = False
            print(f"{IP_PORT} disconnected...")
        client2.send("msg delivered".encode(FORMAT))
    client2.close()

def start():
    server.listen()
    thread1 = threading.Thread(target=handle_client1)  #start that more time than one
    thread2 = threading.Thread(target=handle_client2)  #yes
    thread1.start()  #start that thread
    thread2.start()  #start that thread

print("Server is running...")
start()

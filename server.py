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

def handle_client(client, IP_PORT):
    print(f"Welcome {client}")
    connected = True
    while connected:
        msg = client.recv(1024).decode(FORMAT)  #recieve message
        print(f"{IP_PORT}: {msg}")
        if msg == DISCONNECT_MSG:
            connected = False
            print(f"{IP_PORT} disconnected...")
        client.send("msg delivered".encode(FORMAT))
    client.close()

def start():
    server.listen()
    while True:
        connection, IP_PORT = server.accept()  #new connection accept
        thread = threading.Thread(target=handle_client, args=(connection, IP_PORT))  #start that more time than one
        thread.start()  #start that thread

print("Server is running...")
start()

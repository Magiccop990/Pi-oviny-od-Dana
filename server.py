import socket, threading, time

frequency = 5050  #frequency
ip = "192.168.1.21"# - "95.103.201.58" / "192.168.1.21"
name = socket.gethostname()  #pc name
print(ip + " + " + name)
IP_PORT = (ip, frequency)  #server describtiom
FORMAT = "utf-8"
DISCONNECT_MSG = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket type
server.bind(IP_PORT)  #bind the server describtion to IP_PORT
msg_for1 = []
msg_for2 = []
connected1 = False
connected2 = False
stop = False

def SendToClient1():
    global msg_for1, client1, connected1, stop
    stop_thread = threading.Thread(target=wait)
    stop_thread.start()
    while True:
        global msg_for1, client1, connected1, stop
        if stop == False:
            time.sleep(1)
            if connected1 == True:
                client1.send(str(msg_for1).encode(FORMAT))
                msg_for1 = []
                break
        else:
            stop = False
            break

def wait():
    global stop
    time.sleep(60)
    stop = True

def handle_client1():
    global msg_for1, msg_for2, client2, client1, connected1, connected2
    client1, IP_PORT1 = server.accept()  #new connection accept
    print(f"New client {IP_PORT1}")
    connected1 = True
    while connected1:
        msg = client1.recv(1024).decode(FORMAT)  #recieve message from client 1
        message_send_thread1 = threading.Thread(target=SendToClient2)
        message_send_thread1.start()
        msg_for2.append(msg)
        if msg == DISCONNECT_MSG:
            connected1 = False
            print(f"{IP_PORT} disconnected...")
            msg_for2.append("One member disconnected...")
            break
        print(f"{IP_PORT}: {msg}")
    client1.close()

def SendToClient2():
    global msg_for2, client2, connected2, stop
    stop_thread = threading.Thread(target=wait)
    stop_thread.start()
    while True:
        global msg_for2, client2, connected2, stop
        if stop == False:
            time.sleep(1)
            if connected2 == True:
                client2.send(str(msg_for2).encode(FORMAT))
                msg_for2 = []
                break
        else:
            stop = False
            break

def handle_client2():
    global msg_for2, msg_for1, client1, client2, connected2, connected1
    client2, IP_PORT2 = server.accept()  #new connection accept
    print(f"New client {IP_PORT2}")
    connected2 = True
    while connected2:
        msg = client2.recv(1024).decode(FORMAT)  #recieve message from client 2
        message_send_thread2 = threading.Thread(target=SendToClient1)
        message_send_thread2.start()
        msg_for1.append(msg)
        if msg == DISCONNECT_MSG:
            connected2 = False
            print(f"{IP_PORT} disconnected...")
            msg_for1.append("One member disconnected...")
            break
        print(f"{IP_PORT}: {msg}")
    client1.close()

def Exit():
    global connected1, connected2
    if connected1 == False and connected2 == False:
        print("Everyone left, closing...")
        exit()
    else:
        time.sleep(1)
        pass

def start():
    server.listen()
    thread1 = threading.Thread(target=handle_client1)  #start that more time than one
    thread2 = threading.Thread(target=handle_client2)  #yes
    thread1.start()  #start that thread
    thread2.start()  #start that thread
    destroy = threading.Thread(target=Exit)
    destroy.start()

print("Server is running...")
start()

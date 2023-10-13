import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
# preparing for getting request from client and setting maximum que
s.listen(5)

while True:
    # establishing connection between client and server
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("welcome to the server!","utf-8"))
    clientsocket.close()

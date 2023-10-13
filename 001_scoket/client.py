import socket

# creating socket by socket.socket(family={address family}, type={socket type}, proto={protocol number}, fileno=None)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting remote socket by connect(({IPaddress},{port number}))
s.connect((socket.gethostname(),1234))

full_msg = ''
while True:
    # recieving data ranging buffer size from socket 
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)

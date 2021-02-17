# based on https://docs.python.org/3/library/socket.html
# Echo client program

import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print('Received', repr(data))
    
    s.sendall(b'Hello susi')
    data = s.recv(1024)
    print('Received', repr(data))
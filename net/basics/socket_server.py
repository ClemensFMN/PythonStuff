# based on https://docs.python.org/3/library/socket.html
# Echo server program

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
            # we prepare to receive a large number of bytes to receive
            # if fewer bytes were sent, then the method returns fewer anyway...
        while True:
            data = conn.recv(1024)
            print('Received. ', len(data))
            print('Received', data)
            if len(data) == 0:
                print("nothing more received")
                break
            conn.sendall(data.upper())

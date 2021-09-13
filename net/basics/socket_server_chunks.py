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
            # different to the other server, we prepare to receive fewer bytes
        buf = b''
        while True:
            data = conn.recv(4)
            print('Received. ', len(data))
            while(len(data) != 0):
                buf = buf + data
                print('Buffer: ', buf)
                data = conn.recv(3)
                print('Received: ', len(data))
            print('done')
            conn.sendall(buf.upper())

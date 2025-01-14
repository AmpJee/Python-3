import socket

HOST = '127.0.0.1'    # The remote host
PORT = 80         # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'GET / HTTP/1.1\r\nHost: test.net\r\n\r\n')
    s.sendall(b'Hi from client')
    data = s.recv(1024)
print('Received from server: ', repr(data))
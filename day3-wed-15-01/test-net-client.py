import socket
import threading

HOST = '127.0.0.1'
PORT = 21002

def send_message_function(client_socket):
    while True:
        message = input("Enter a message: ")
        client_socket.send((message + "\n").encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    send_thread = threading.Thread(target=send_message_function, args=(s,), daemon=True)
    send_thread.start()

    while True:
        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break
        if message_received:
            print("Received message: ", message_received)
            if message_received == "exit\n":
                break
        else:
            break

s.close()
print("Client finished")
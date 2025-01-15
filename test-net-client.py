import socket

HOST = '127.0.0.1'
PORT = 21002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message = input("Enter a message: ")
        s.send((message+"\n").encode())

        if message == "exit":
            break
        print("Message sent to server, waiting for response")

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
        else:
            break
s.close()
print("Client finished")
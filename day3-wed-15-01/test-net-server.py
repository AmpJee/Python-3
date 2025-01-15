import socket
import sys
import threading

HOST = '0.0.0.0'
PORT = 21002
s = None
clients = []

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())


def handle_client(client_socket):
    while True:
        message_received = ""
        while True:
            data = client_socket.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                client_socket.close()
                clients.remove(client_socket)
                return
        if message_received:
            print("Received message: ", message_received)
            broadcast_message(message_received, client_socket)
    client_socket.close()
    clients.remove(client_socket)
    print("Client disconnected")


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except OSError as msg:
        s = None
        print(f"Error creating socket: {msg}")
        exit(1)

    try:
        s.bind((HOST, PORT))
        s.listen()
        print("Socket bound and listening")
    except OSError as msg:
        print("Error binding/listening!")
        s.close()
        exit(1)

    while True:
        try:
            conn, addr = s.accept()
            print(f"Connected to {addr}")
            clients.append(conn)
            client_thread = threading.Thread(target=handle_client, args=(conn,), daemon=True)
            client_thread.start()
        except KeyboardInterrupt:
            print("Server interrupted")
            break

    s.close()
    print("Server finished")


if __name__ == "__main__":
    main()
import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode("utf-8")

        if not message:
            break

        print(f"Client: {message}")

        # Send response back to the client
        response = input("Enter your response: ")
        client_socket.sendall(response.encode("utf-8"))

    print("Client disconnected.")
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  
    PORT = 12345       

    start_server(HOST, PORT)

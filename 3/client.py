import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print("Connected to server.")

    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        print(f"Server: {response}")

    client_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  
    PORT = 12345       

    start_client(HOST, PORT)

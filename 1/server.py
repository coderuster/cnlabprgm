import socket

def receive_file(save_as,server_port):

    server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('0.0.0.0', server_port))

    server_socket.listen(1)

    print("Server is listening on port: ", server_port)

    clien_socket, client_address = server_socket.accept()

    file_data= clien_socket.recv(4096);

    with open(save_as, 'wb') as file:
        file.write(file_data)

    print("File has been received and saved as: ", save_as)
    
    clien_socket.close()

    server_socket.close()

if __name__ == "__main__":
    receive_file("received_file.txt", 8000)

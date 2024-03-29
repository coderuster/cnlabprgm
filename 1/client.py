import socket

def send_file(file_path,server_ip,server_port):

    with open (file_path, 'rb') as file:
        file_data= file.read()

    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((server_ip, server_port))
    
    sock.sendall(file_data)

    sock.close()

    print("File has been sent to the server")

if __name__ == "__main__":
    send_file("test.txt", "127.0.0.1",8000) 

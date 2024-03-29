import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', 8000))

    server.listen(1)
    client,client_address= server.accept()
    while True:
        try:    
            data= client.recv(1024)
            client.send(data)
        except ConnectionResetError as e:
            print(e)
            break
    server.close()


if __name__ == '__main__':
    main()

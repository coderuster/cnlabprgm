import socket

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(1)
    client,add=server.accept()
    while(True):
        data=client.recv(1024)
        f_name=data.decode()
        try:
            print(f_name)
            with open("test.txt",'rb') as f:
                data=f.read()
                client.send(data)
        except:
            client.send('File not found'.encode())

if __name__=='__main__':
    main()


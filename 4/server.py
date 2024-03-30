import socket
import os

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(1)
    client,add=server.accept()
    while(True):
        data=client.recv(1024)
        f_name=data.decode()
        try:
            if not os.path.exists(f_name):
                continue
            with open(f_name,'rb') as f:
                while True:
                        chunk = f.read(1024)
                        if not chunk:
                            break
                        client.sendall(chunk)
        except:
            client.send('File not found'.encode())

if __name__=='__main__':
    main()


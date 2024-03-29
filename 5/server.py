import socket

ups={
    'google.com':'8.8.8.8',
    'facebook.com':'69.69.69.69',
}

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(1)
    client,add=server.accept()
    while(True):
        data=client.recv(1024)
        if(not data):
            break
        f_name=data.decode()
        try:
            client.send(ups[f_name].encode())
        except:
            client.send('Dns not found'.encode())
    server.close()

if __name__=='__main__':
    main()

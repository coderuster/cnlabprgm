import socket

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',12345))
    while True:
        f_name=input('Enter the URL: ')
        if(f_name=='exit'):
            break
        client.send(f_name.encode())
        data=client.recv(1024)
        print("IP Address: ",data.decode())
    client.close()


if __name__=="__main__":
    main()


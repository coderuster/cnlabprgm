import socket

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',12345))
    while True:
        f_name=input('Enter the file name: ')
        if(f_name=='exit'):
            break
        client.send(f_name.encode())
        data=client.recv(1024)
        with open("received.txt",'wb') as f:
            f.write(data)
    client.close()

if __name__=='__main__':
    main()
    

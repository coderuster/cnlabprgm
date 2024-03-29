import socket

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',8000))
    while(True):
        cmd=input('Enter a command: ').strip();
        if(cmd.lower()=='exit'):
            client.close()
            break
        else:
            client.send(cmd.encode())
            data=client.recv(1024)
            print(data.decode())

if __name__ == '__main__':
    main()

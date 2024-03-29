import socket
import subprocess

def execute_arp(ip):
    try:
        result = subprocess.run(['arp', '-a',ip], capture_output=True, text=True)

        if result.returncode == 0:
            return result.stdout
        else:
            return "Error executing arp -a command."

    except Exception as e:
        print(f"An error occurred: {e}")
    return "Error executing arp -a command."

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
            client.send(execute_arp(f_name).encode())
        except:
            client.send('Error'.encode())
    server.close()

if __name__=='__main__':
    main()

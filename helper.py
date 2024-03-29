import os

def get_cmd(name,number):
    return f"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/coderuster/cnlabprgm/main/{number}/{name}' -OutFile '{name}'"

def main():
    number=input("Enter the experiment number: ").strip()
    cmd1=get_cmd("server.py",number)
    cmd2=get_cmd("client.py",number)
    os.system(cmd1)
    os.system(cmd2)

if __name__=="__main__":
    main()

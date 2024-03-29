import subprocess

def get_cmd(name,number):
    return f"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/coderuster/cnlabprgm/main/{number}/{name}' -OutFile '{name}'"

def run_powershell(cmd): 
    process = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    if process.returncode == 0:
      output = process.stdout.decode()
      print(f"List of Chrome processes:\n{output}")
    else:
      error = process.stderr.decode()
      print(f"Error: {error}")


def main():
    number=input("Enter the experiment number: ").strip()
    cmd1=get_cmd("server.py",number)
    cmd2=get_cmd("client.py",number)
    run_powershell(cmd1)
    run_powershell(cmd2)

if __name__=="__main__":
    main()

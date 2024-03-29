import requests

def get_cmd(name,number):
    return f"https://raw.githubusercontent.com/coderuster/cnlabprgm/main/{number}/{name}"

def run_command(cmd):
  try:
      data=requests.get(cmd)
      return data.text
  except Exception as e:
    print(f"Error: {e}")
    return "ERROR"

def main():
    number=input("Enter the experiment number: ").strip()
    files=["server.py","client.py"]
    for f in files:
        cmd1=get_cmd(f,number)
        content=run_command(cmd1)
        with open(f,"w") as file:
            file.write(content)
if __name__=="__main__":
    main()


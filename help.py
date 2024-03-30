import urllib.request
import json

def get_files(repo_url, folder_path):
    api_url = f"{repo_url.rstrip('/')}/contents/{folder_path}"
    ret=[]
    with urllib.request.urlopen(api_url) as response:
        if response.getcode() == 200:
            contents = json.loads(response.read())
            
            for item in contents:
                if item["type"] == "file":
                    filename = item["name"]
                    ret.append(filename)
        else:
            print(f"Failed to fetch folder contents. Status code: {response.getcode()}")
    return ret

repo_url = "https://api.github.com/repos/coderuster/cnlabprgm/"
folder_path = "1"

print_file_names_from_folder(repo_url, folder_path)

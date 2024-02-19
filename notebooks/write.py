import requests


token = "{PUT YOUR TOKEN HERE}"
file_content = "'Hello World!'"
my_repo = 'tfluhr'
repo_name = "Digital_Signage_Builder"
slideshow_name = input("Give your slideshow a name: ")
#file_path = f"sites/{slideshow_name}/test.html"
file_path = f"{slideshow_name}.txt"



def upload_file_to_repo(my_repo, repo_name, file_path, file_content, token):
    url = f"https://api.github.com/repos/{my_repo}/{repo_name}/contents/sites/{slideshow_name}/{file_path}"
    #url = f"https://api.github.com/repos/{my_repo}/{repo_name}/contents/{file_path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "tfluhr",
        "content-type": "text/plain"
    }
    data = {
        "message": "Upload file",
        "content": file_content
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        print("File uploaded successfully!")
    except requests.HTTPError as e:
        print(f"Error uploading file: {e}")


upload_file_to_repo(my_repo, repo_name, file_path, slideshow_name, token)


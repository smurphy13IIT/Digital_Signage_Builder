import requests
import base64

token = "{PUT TOKEN HERE}"
file_content = "Hello World!"
my_repo = 'tfluhr'
repo_name = "Digital_Signage_Builder"
slideshow_name = input("Give your slideshow a name: ")
#file_path = f"sites/{slideshow_name}/test.html"
file_path = f"{slideshow_name}.txt"

def write_string_to_file(my_repo, repo_name, file_path, slideshow_name, token, file_content):
    url = f"https://api.github.com/repos/{my_repo}/{repo_name}/contents/sites/{slideshow_name}/{file_path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Encode file content as base64
    content_bytes = file_content.encode('utf-8')
    content_base64 = base64.b64encode(content_bytes).decode('utf-8')

    print(content_base64)

    data = {
        "message": "Write string to file",
        "content": content_base64
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        print("String written to file successfully!")
    except requests.HTTPError as e:
        print(f"Error writing string to file: {e}")

write_string_to_file(my_repo, repo_name, file_path, slideshow_name, token, file_content)

#if __name__ == "__main__":
#    owner = "your_username"
#    repo_name = "your_repository"
#    file_path = "path/to/your/file.txt"  # Path in the repository where you want to write the file
#    file_content = "Hello, World!"  # Content to write to the file
    # Replace 'your_access_token' with your GitHub personal access token
#    token = "your_access_token"
#    write_string_to_file(owner, repo_name, file_path, file_content, token)

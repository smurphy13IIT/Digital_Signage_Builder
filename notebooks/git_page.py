import requests

#https://github.com/smurphy13IIT/Digital_Signage_Builder.git
owner = "TybaltAurelius"
repo_name = "Digital_Signage_Builder"

# Replace 'your_access_token' with your GitHub personal access token
token = "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"
#fork_repository(owner, repo_name, token)

def build_page(owner, repo_name, token):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/pages"
    headers = {
        "Authorization": f"bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = '''{
        "source" : {
            "branch" : "master",
            "path" : "/"
        }
    }'''
    response = requests.post(url, headers=headers, data=data)
    print(response)
    print(response.json())

build_page(owner, repo_name, token)

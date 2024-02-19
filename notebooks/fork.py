import requests

#https://github.com/smurphy13IIT/Digital_Signage_Builder.git
owner = "smurphy13IIT"
repo_name = "Digital_Signage_Builder"
# Replace 'your_access_token' with your GitHub personal access token
token = "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"
#fork_repository(owner, repo_name, token)

def fork_repository(owner, repo_name, token):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/forks"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, headers=headers)
    print(response)

fork_repository(owner, repo_name, token)

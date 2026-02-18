import os
from github import Github

# Secret se token utha raha hai
token = os.getenv("MY_GITHUB_TOKEN")
g = Github(token)

# Testing ke liye
repo_name = "facebook/react"
repo = g.get_repo(repo_name)

print(f"Audit Report for: {repo_name}")
print(f"Stars: {repo.stargazers_count}")
print(f"Is Protected: {repo.get_branch('main').protected}")


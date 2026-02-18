import os
from github import Github
from github import Auth

# Secret se token utha raha hai
token = os.getenv("MY_GITHUB_TOKEN")

if not token:
    print("❌ Error: Token nahi mila! Secret name check karein.")
    exit(1) # Stop the script

try:
    # Naya tareeka (Modern way to connect)
    auth = Auth.Token(token)
    g = Github(auth=auth)

    user = g.get_user()
    print(f"✅ Success! Connected as: {user.login}")
    
    # Testing check
    repo = g.get_repo("facebook/react")
    print(f"Repo: {repo.full_name} | Stars: {repo.stargazers_count}")

except Exception as e:
    print(f"❌ Connection Error: {e}")
  

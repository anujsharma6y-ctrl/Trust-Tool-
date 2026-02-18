import os
from github import Github, Auth

# Token lene ki koshish
token = os.getenv("MY_GITHUB_TOKEN")

# Agar token khali hai toh saaf-saaf error print karein
if not token or len(token) == 0:
    print("❌ ERROR: Secret 'MY_GITHUB_TOKEN' nahi mila. Settings check karein!")
    exit(1)

try:
    auth = Auth.Token(token)
    g = Github(auth=auth)
    
    # Testing repo (Aap apni repo ka naam bhi daal sakte hain)
    repo = g.get_repo("facebook/react")
    
    # Simple HTML Page Generator
    html_content = f"<h1>Trust Center Live!</h1><p>Repo: {repo.full_name}</p><p>Stars: {repo.stargazers_count}</p>"
    
    with open("index.html", "w") as f:
        f.write(html_content)
        
    print("✅ Success! Website file ready.")

except Exception as e:
    print(f"❌ Connection Error: {e}")
    exit(1)
    

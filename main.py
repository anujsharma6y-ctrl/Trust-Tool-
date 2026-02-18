import os

token = os.getenv("MY_GITHUB_TOKEN")

if not token:
    print("❌ Secret abhi bhi nahi mil raha. Please check GitHub Settings!")
else:
    # Token ki sirf pehli 4 digits dikhayega (poora nahi dikhana chahiye!)
    print(f"✅ Secret mil gaya! Token starts with: {token[:4]}...")
    

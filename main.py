import os
from github import Github, Auth

# 1. Secret se token utha raha hai
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# 2. Data ikattha karein (Example ke liye Facebook React repo)
repo = g.get_repo("facebook/react") 
stars = repo.stargazers_count
is_protected = repo.get_branch("main").protected

# 3. HTML (Website) ka Design taiyaar karein
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Trust Center</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans">
    <div class="max-w-4xl mx-auto py-20 px-4">
        <div class="bg-white shadow-xl rounded-2xl overflow-hidden border border-slate-200">
            <div class="bg-indigo-600 p-8 text-white text-center">
                <h1 class="text-3xl font-bold italic">🛡️ TrustShield</h1>
                <p class="opacity-90 mt-2">Real-time Security Transparency</p>
            </div>
            
            <div class="p-8">
                <div class="flex justify-between items-center border-b pb-6 mb-6">
                    <div>
                        <h2 class="text-xl font-semibold">{repo.full_name}</h2>
                        <p class="text-slate-500 text-sm">Automated Security Audit</p>
                    </div>
                    <span class="bg-green-100 text-green-700 px-4 py-1 rounded-full text-sm font-bold border border-green-200">
                        LIVE STATUS
                    </span>
                </div>

                <div class="grid md:grid-cols-2 gap-6">
                    <div class="border rounded-xl p-5 bg-slate-50">
                        <p class="text-slate-500 text-xs uppercase tracking-wider font-bold mb-2">Code Integrity</p>
                        <h3 class="text-lg font-medium">Main Branch Protection</h3>
                        <p class="mt-2 text-2xl font-bold {'text-green-600' if is_protected else 'text-red-500'}">
                            {'SECURE ✅' if is_protected else 'RISKY ❌'}
                        </p>
                    </div>

                    <div class="border rounded-xl p-5 bg-slate-50">
                        <p class="text-slate-500 text-xs uppercase tracking-wider font-bold mb-2">Community Trust</p>
                        <h3 class="text-lg font-medium">GitHub Stars</h3>
                        <p class="mt-2 text-2xl font-bold text-indigo-600 font-mono">
                            {stars:,}
                        </p>
                    </div>
                </div>

                <div class="mt-10 text-center">
                    <p class="text-xs text-slate-400 font-mono tracking-tighter">
                        Last Audit: {os.popen('date').read()}
                    </p>
                    <p class="mt-4 text-slate-400 text-sm italic">Verified by MyTrustTool Engine</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# 4. index.html file create karein
with open("index.html", "w") as f:
    f.write(html_template)

print("✅ Website file (index.html) successfully ban gayi hai!")

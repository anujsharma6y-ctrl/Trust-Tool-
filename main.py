import os
from github import Github, Auth

# Token connection
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# Data Fetching (Aap 'facebook/react' ki jagah apni repo ka naam bhi daal sakte hain)
repo_name = "Trust Tool"
repo = g.get_repo(repo_name)
stars = repo.stargazers_count
is_protected = repo.get_branch("main").protected

# Professional HTML Template
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TrustShield | Security Center</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white font-sans min-h-screen flex items-center justify-center p-6">
    <div class="max-w-2xl w-full bg-gray-800 rounded-3xl shadow-2xl overflow-hidden border border-gray-700">
        <div class="bg-gradient-to-r from-blue-600 to-indigo-600 p-8 text-center">
            <h1 class="text-4xl font-extrabold tracking-tight">🛡️ TrustShield</h1>
            <p class="text-blue-100 mt-2 opacity-80 uppercase text-xs tracking-[0.2em] font-semibold">Security Audit Live</p>
        </div>

        <div class="p-8">
            <div class="flex items-center justify-between mb-8">
                <div>
                    <h2 class="text-2xl font-bold">{repo_name}</h2>
                    <p class="text-gray-400 text-sm">Automated Transparency Report</p>
                </div>
                <div class="animate-pulse flex items-center space-x-2 bg-green-900/30 border border-green-500/50 px-3 py-1 rounded-full">
                    <div class="w-2 h-2 bg-green-500 rounded-full"></div>
                    <span class="text-green-400 text-[10px] font-bold uppercase">System Active</span>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-gray-700/50 p-6 rounded-2xl border border-gray-600 hover:border-blue-500 transition-colors">
                    <p class="text-gray-400 text-[10px] font-bold uppercase tracking-wider mb-2">Integrity</p>
                    <p class="text-sm font-medium">Branch Protection</p>
                    <p class="text-2xl font-black mt-1 {'text-green-400' if is_protected else 'text-red-400'}">
                        {'SECURE ✅' if is_protected else 'RISKY ❌'}
                    </p>
                </div>

                <div class="bg-gray-700/50 p-6 rounded-2xl border border-gray-600 hover:border-indigo-500 transition-colors">
                    <p class="text-gray-400 text-[10px] font-bold uppercase tracking-wider mb-2">Popularity</p>
                    <p class="text-sm font-medium">GitHub Stars</p>
                    <p class="text-2xl font-black mt-1 text-indigo-400">{stars:,}</p>
                </div>
            </div>

            <div class="mt-10 pt-6 border-t border-gray-700 text-center">
                <p class="text-gray-500 text-[10px] font-mono tracking-widest">
                    Last Audit: {os.popen('date -u').read().strip()} UTC
                </p>
                <p class="text-gray-400 text-xs mt-4 italic opacity-60 font-serif font-semibold">Verified by MyTrustTool V1.0</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("🚀 Dashboard updated to Professional UI!")

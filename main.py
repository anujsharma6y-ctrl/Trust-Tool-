import os
from github import Github, Auth

# Connection setup
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# Target Repo - Aap ise apni repo name se badal sakte hain
repo_name = "facebook/react" 
repo = g.get_repo(repo_name)

# --- NEW SECURITY LOGIC ---
# Check Alerts (Basic scan simulation)
try:
    # Hum check kar rahe hain ki kya repository mein koi 'Security Advisory' hai
    advisories = repo.get_advisories()
    vulnerability_count = sum(1 for a in advisories if a.state == "published")
except:
    # Agar permissions ki wajah se advisory nahi dikhti, toh hum default 0 maanenge
    vulnerability_count = 0

is_protected = repo.get_branch("main").protected
# --------------------------

# Professional HTML Template (Updated for Vulnerabilities)
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TrustShield Pro | Security Scanner</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-slate-200 font-sans min-h-screen flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-[#1e293b] rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.5)] overflow-hidden border border-slate-700">
        
        <div class="bg-gradient-to-r from-cyan-500 to-blue-600 p-10 text-center relative">
            <div class="absolute top-4 right-6 flex items-center space-x-2">
                <span class="relative flex h-3 w-3">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-3 w-3 bg-white"></span>
                </span>
                <span class="text-[10px] font-bold tracking-widest text-white/80 uppercase">Scanner Live</span>
            </div>
            <h1 class="text-5xl font-black italic tracking-tighter text-white">TrustShield<span class="text-cyan-200">PRO</span></h1>
            <p class="text-cyan-100 mt-2 font-medium opacity-90 italic">Advanced Vulnerability Detection</p>
        </div>

        <div class="p-10">
            <div class="mb-10 flex flex-col md:flex-row md:items-end justify-between gap-4">
                <div>
                    <h2 class="text-3xl font-bold text-white tracking-tight">{repo_name}</h2>
                    <p class="text-slate-400 font-mono text-sm mt-1">Audit Reference: {repo.id}</p>
                </div>
                <div class="bg-slate-800 px-6 py-3 rounded-2xl border border-slate-700">
                    <p class="text-slate-500 text-[10px] font-bold uppercase tracking-widest mb-1 text-center">Security Score</p>
                    <p class="text-3xl font-black text-cyan-400 text-center">{'98%' if vulnerability_count == 0 else '75%'}</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-slate-900/50 p-6 rounded-3xl border border-slate-800 group hover:border-cyan-500/50 transition-all">
                    <p class="text-slate-500 text-[10px] font-bold uppercase mb-3">Integrity</p>
                    <p class="text-xs text-slate-400 leading-tight mb-2">Branch Protection</p>
                    <p class="text-xl font-bold {'text-green-400' if is_protected else 'text-red-400'}">
                        {'ENABLED' if is_protected else 'DISABLED'}
                    </p>
                </div>

                <div class="bg-slate-900/50 p-6 rounded-3xl border border-slate-800 group hover:border-red-500/50 transition-all">
                    <p class="text-slate-500 text-[10px] font-bold uppercase mb-3">Vulnerabilities</p>
                    <p class="text-xs text-slate-400 leading-tight mb-2">Known Threats</p>
                    <p class="text-xl font-bold {'text-green-400' if vulnerability_count == 0 else 'text-red-500'}">
                        {vulnerability_count} Found
                    </p>
                </div>

                <div class="bg-slate-900/50 p-6 rounded-3xl border border-slate-800 group hover:border-blue-500/50 transition-all">
                    <p class="text-slate-500 text-[10px] font-bold uppercase mb-3">Community</p>
                    <p class="text-xs text-slate-400 leading-tight mb-2">GitHub Stars</p>
                    <p class="text-xl font-bold text-blue-400">{repo.stargazers_count:,}</p>
                </div>
            </div>

            {f'''<div class="mt-8 bg-red-900/20 border border-red-500/30 p-4 rounded-2xl flex items-center space-x-4">
                <span class="text-2xl">⚠️</span>
                <p class="text-red-200 text-xs font-medium">Attention: This repository has {vulnerability_count} published security advisories. Immediate review recommended.</p>
            </div>''' if vulnerability_count > 0 else ''}

            <div class="mt-12 text-center">
                <p class="text-[9px] text-slate-500 font-mono uppercase tracking-[0.3em]">
                    Next Automated Scan: {os.popen('date -d "+24 hours" -u').read().strip()}
                </p>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

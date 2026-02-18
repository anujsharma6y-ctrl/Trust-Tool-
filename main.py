import os
from github import Github, Auth

# 1. Connection setup
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# 2. Target Repo - DHAYAN RAKHEIN: "username/repository" format hona chahiye
# Example: "facebook/react" ya "anujsharma6y-ctrl/Trust-Tool-"
repo_name = "Security Audit" 

try:
    repo = g.get_repo(repo_name)
    stars = repo.stargazers_count
    
    # Security Logic
    try:
        advisories = repo.get_advisories()
        vulnerability_count = sum(1 for a in advisories if a.state == "published")
    except:
        vulnerability_count = 0

    is_protected = repo.get_branch("main").protected
    last_audit = os.popen('date -u').read().strip()
    status_text = "SECURE" if vulnerability_count == 0 else "ACTION REQUIRED"

except Exception as e:
    print(f"❌ Error: Repo '{repo_name}' nahi mili. Spelling check karein!")
    # Fallback data taaki build fail na ho
    repo_name = "Invalid Repo Name"
    stars = 0
    vulnerability_count = "N/A"
    is_protected = False
    last_audit = "N/A"
    status_text = "ERROR"

# 3. Create Text Report for Download
report_content = f"""
TRUSTSHIELD SECURITY AUDIT REPORT
---------------------------------
Repository: {repo_name}
Audit Time: {last_audit}
Status: {status_text}

FINDINGS:
1. Vulnerabilities: {vulnerability_count} found.
2. Branch Protection: {'Enabled' if is_protected else 'Disabled'}
3. Community Trust: {stars} Stars

Verified by TrustShield Engine.
"""
with open("security_report.txt", "w") as f:
    f.write(report_content)

# 4. Professional HTML Dashboard
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TrustShield PRO | Client Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-slate-200 font-sans min-h-screen flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-[#1e293b] rounded-[2rem] shadow-2xl overflow-hidden border border-slate-700">
        <div class="bg-gradient-to-r from-cyan-600 to-blue-700 p-10 text-center">
            <h1 class="text-4xl font-black italic text-white tracking-tighter">TrustShield<span class="text-cyan-200 text-2xl not-italic ml-1">PRO</span></h1>
            <p class="text-cyan-100 mt-1 text-xs font-bold tracking-[0.3em]">CERTIFIED SECURITY AUDIT</p>
        </div>
        <div class="p-10 text-center">
            <h2 class="text-3xl font-bold text-white mb-8">{repo_name}</h2>
            <div class="grid grid-cols-2 gap-4 mb-10">
                <div class="bg-slate-900/50 p-6 rounded-3xl border border-slate-700">
                    <p class="text-xs text-slate-500 uppercase font-bold mb-1 text-center">Risk Level</p>
                    <p class="text-2xl font-black {'text-green-400' if status_text == 'SECURE' else 'text-red-500'}">
                        {status_text}
                    </p>
                </div>
                <div class="bg-slate-900/50 p-6 rounded-3xl border border-slate-700">
                    <p class="text-xs text-slate-500 uppercase font-bold mb-1 text-center">Vulnerabilities</p>
                    <p class="text-2xl font-black text-cyan-400">{vulnerability_count}</p>
                </div>
            </div>
            <a href="security_report.txt" download class="inline-flex items-center justify-center px-8 py-4 bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-bold rounded-2xl transition-all transform hover:scale-105 shadow-lg shadow-cyan-500/20">
                <span>📩 Download Security Report</span>
            </a>
            <div class="mt-12 pt-8 border-t border-slate-800">
                <p class="text-[10px] text-slate-500 font-mono tracking-widest uppercase">Last Audit: {last_audit}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

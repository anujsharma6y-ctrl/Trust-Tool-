import os
from github import Github, Auth
from datetime import datetime, timedelta

# 1. Connection setup
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# 2. AAPKI REPO KA NAAM (Yahan dhyan dein!)
# Ise "username/repository" format mein hi rakhein
repo_name = "anujsharma6y-ctrl/Trust-Tool-" 

try:
    repo = g.get_repo(repo_name)
    stars = repo.stargazers_count
    
    # Vulnerabilities Logic
    try:
        advisories = repo.get_advisories()
        vulnerability_count = sum(1 for a in advisories if a.state == "published")
    except:
        vulnerability_count = 0

    is_protected = repo.get_branch("main").protected
    last_audit = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Next Update Time (24 hours after now)
    next_audit = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    status_text = "SECURE" if vulnerability_count == 0 else "ACTION REQUIRED"
    risk_color = "text-green-400" if vulnerability_count == 0 else "text-red-500"

except Exception as e:
    # Agar error aaye toh ye dikhega
    repo_name = "Error: Repo Not Found"
    stars = 0
    vulnerability_count = "N/A"
    status_text = "ERROR"
    risk_color = "text-red-500"
    last_audit = "N/A"
    next_audit = "Manual Check Required"

# 3. Create Text Report for Download
report_content = f"""
TRUSTSHIELD SECURITY AUDIT REPORT
---------------------------------
Repository: {repo_name}
Audit Time: {last_audit}
Next Scheduled Audit: {next_audit}
Status: {status_text}

FINDINGS:
1. Vulnerabilities: {vulnerability_count} found.
2. Branch Protection: {'Enabled' if 'repo' in locals() and is_protected else 'Disabled'}
3. Stars: {stars}

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
    <title>TrustShield PRO | Live Audit</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-slate-200 font-sans min-h-screen flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-[#1e293b] rounded-[2rem] shadow-2xl overflow-hidden border border-slate-700">
        <div class="bg-gradient-to-r from-cyan-600 to-blue-700 p-10 text-center">
            <h1 class="text-4xl font-black italic text-white tracking-tighter">TrustShield<span class="text-cyan-200 text-2xl not-italic ml-1">PRO</span></h1>
            <p class="text-cyan-100 mt-1 text-[10px] font-bold tracking-[0.3em] uppercase">Certified Security Audit</p>
        </div>
        <div class="p-10 text-center">
            <h2 class="text-3xl font-bold text-white mb-8 tracking-tight">{repo_name}</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
                <div class="bg-slate-900/50 p-8 rounded-3xl border border-slate-700">
                    <p class="text-[10px] text-slate-500 uppercase font-bold mb-2 tracking-widest">Risk Level</p>
                    <p class="text-3xl font-black {risk_color}">{status_text}</p>
                </div>
                <div class="bg-slate-900/50 p-8 rounded-3xl border border-slate-700">
                    <p class="text-[10px] text-slate-500 uppercase font-bold mb-2 tracking-widest">Vulnerabilities</p>
                    <p class="text-3xl font-black text-cyan-400">{vulnerability_count}</p>
                </div>
            </div>

            <a href="security_report.txt" download class="w-full md:w-auto inline-flex items-center justify-center px-10 py-5 bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-bold rounded-2xl transition-all transform hover:scale-105 shadow-lg shadow-cyan-500/20 mb-8">
                <span>📩 Download Security Report</span>
            </a>

            <div class="pt-8 border-t border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4">
                <p class="text-[9px] text-slate-500 font-mono uppercase">Last Audit: {last_audit}</p>
                <p class="text-[9px] text-cyan-500/70 font-mono uppercase font-bold">Next Auto Update: {next_audit}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
    

# 2. Backend Repo Name (Ise mat badalna)
repo_name = "anujsharma6y-ctrl/Trust-Tool-" 

# 3. Website par dikhne wala NAAM (Ise aap jo chahe badal dein)
display_name = "ANUJ SHARMA SECURITY LABS" # <-- Yahan apna naam likhein

# ... (baaki logic wahi rahega)

# 4. HTML Dashboard mein display_name use karein
# Jahan niche <h2>{repo_name}</h2> likha tha, wahan ab <h2>{display_name}</h2> hoga



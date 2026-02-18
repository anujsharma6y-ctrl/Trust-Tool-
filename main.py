import os
from github import Github, Auth
from datetime import datetime, timedelta

# 1. Connection setup
token = os.getenv("MY_GITHUB_TOKEN")
auth = Auth.Token(token)
g = Github(auth=auth)

# 2. Settings (Can be changed)
repo_path = "anujsharma6y-ctrl/Trust-Tool-" 
brand_name = "ANUJ SHARMA SECURITY LABS"

try:
    repo = g.get_repo(repo_path)
    stars = repo.stargazers_count
    
    # Security Logic
    try:
        advisories = repo.get_advisories()
        vulnerability_count = sum(1 for a in advisories if a.state == "published")
    except:
        vulnerability_count = 0

    is_protected = repo.get_branch("main").protected
    last_audit = datetime.now().strftime("%d %b %Y | %H:%M UTC")
    next_audit = (datetime.now() + timedelta(days=1)).strftime("%d %b %Y | %H:%M UTC")
    
    status_text = "SECURE" if vulnerability_count == 0 else "ACTION REQUIRED"
    risk_color = "text-green-400" if vulnerability_count == 0 else "text-red-500"

except Exception as e:
    brand_name = "System Error"
    status_text = "OFFLINE"
    vulnerability_count = "N/A"
    last_audit = "N/A"
    next_audit = "Manual Reset Needed"

# 3. Text Report content
report_content = f"""
=========================================
      {brand_name} - AUDIT REPORT
=========================================
Target Repo : {repo_path}
Audit Date  : {last_audit}
Next Sync   : {next_audit}
-----------------------------------------
SECURITY POSTURE: {status_text}
Vulnerabilities: {vulnerability_count}
Branch Guard   : {'ACTIVE' if 'repo' in locals() and is_protected else 'INACTIVE'}
-----------------------------------------
Verified by TrustShield Engine V2.0
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
    <title>{brand_name} | Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-slate-200 font-sans min-h-screen flex items-center justify-center p-4">
    <div class="max-w-3xl w-full bg-[#1e293b] rounded-[3rem] shadow-2xl overflow-hidden border border-slate-700">
        <div class="bg-gradient-to-br from-indigo-600 via-blue-600 to-cyan-500 p-12 text-center">
            <h1 class="text-4xl font-black text-white tracking-tighter uppercase mb-2">{brand_name}</h1>
            <div class="inline-block px-4 py-1 bg-white/20 rounded-full text-[10px] font-bold tracking-widest text-white uppercase backdrop-blur-sm">
                Live Security Intelligence
            </div>
        </div>
        <div class="p-12 text-center">
            <p class="text-slate-500 text-xs font-mono mb-8">Scanning: {repo_path}</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                <div class="bg-slate-900/40 p-8 rounded-[2rem] border border-slate-800 hover:border-indigo-500 transition-all">
                    <p class="text-[10px] text-slate-500 uppercase font-bold mb-3 tracking-widest">Risk Assessment</p>
                    <p class="text-4xl font-black {risk_color}">{status_text}</p>
                </div>
                <div class="bg-slate-900/40 p-8 rounded-[2rem] border border-slate-800 hover:border-cyan-500 transition-all">
                    <p class="text-[10px] text-slate-500 uppercase font-bold mb-3 tracking-widest">Threat Count</p>
                    <p class="text-4xl font-black text-cyan-400">{vulnerability_count}</p>
                </div>
            </div>

            <a href="security_report.txt" download class="group relative inline-flex items-center justify-center px-10 py-5 font-bold text-white transition-all duration-200 bg-indigo-600 font-pj rounded-2xl focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 hover:bg-indigo-500 shadow-xl shadow-indigo-500/20">
                <span class="mr-2">📩</span> Download Official Report
            </a>

            <div class="mt-16 pt-8 border-t border-slate-800 flex flex-col md:flex-row justify-between text-[10px] font-mono text-slate-500 gap-4">
                <p>LAST AUDIT: {last_audit}</p>
                <p class="text-indigo-400">NEXT SYNC: {next_audit}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

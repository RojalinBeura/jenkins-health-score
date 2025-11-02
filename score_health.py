import random, os

# Simulated build health data
build_success = random.randint(80, 100)
vulnerabilities = random.randint(0, 5)
score = build_success - (vulnerabilities * 5)

os.makedirs("reports", exist_ok=True)
with open("reports/index.html", "w") as f:
    f.write("<h1>Jenkins Health and Security Score Report</h1>")
    f.write(f"<p><b>Build Success:</b> {build_success}%</p>")
    f.write(f"<p><b>Vulnerabilities Found:</b> {vulnerabilities}</p>")
    f.write(f"<p><b>Final Score:</b> {score}</p>")

print("Report generated successfully!")
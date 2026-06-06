import json
from rules import RULES

with open("alerts.json", "r") as file:
    alerts = json.load(file)

results = []

print("=== AI Security Triage Agent ===")

for item in alerts:

    alert = item["alert"]

    severity = "Unknown"
    action = "Manual Review"

    for keyword, data in RULES.items():

        if keyword.lower() in alert.lower():

            severity = data["severity"]
            action = data["action"]
            break

    result = {
        "alert": alert,
        "severity": severity,
        "action": action
    }

    results.append(result)

    print(result)

# Save memory

with open("memory.json", "w") as memory_file:
    json.dump(results, memory_file, indent=4)

# Generate report

with open("outputs/report.txt", "w") as report:

    report.write("AI SECURITY TRIAGE REPORT\n\n")

    for item in results:

        report.write(f"Alert: {item['alert']}\n")
        report.write(f"Severity: {item['severity']}\n")
        report.write(f"Action: {item['action']}\n")
        report.write("----------------------\n")

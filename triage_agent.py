import json
from rules import RULES

with open("alerts.json", "r") as file:
    alerts = json.load(file)

print("=== AI Security Triage Agent ===")

for item in alerts:

    alert = item["alert"]

    print("\nAlert:", alert)

    matched = False

    for keyword, data in RULES.items():

        if keyword.lower() in alert.lower():

            print("Severity:", data["severity"])
            print("Recommended Action:", data["action"])

            matched = True
            break

    if not matched:
        print("Severity: Unknown")
        print("Recommended Action: Manual Review")

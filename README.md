# ai-security-triage-agent
Agentic AI security triage assistant that classifies security findings and recommends actions.
# AI Security Triage Agent

AI-powered security triage system that automatically analyzes security alerts, classifies severity levels, recommends remediation actions, maintains investigation records, and generates security reports through an automated GitHub Actions workflow.

## Key Features

- Automated security alert processing
- Severity classification (Medium, High, Critical)
- Remediation recommendation engine
- Persistent findings storage
- Automated report generation
- GitHub Actions workflow automation
- Human-in-the-loop escalation for unknown findings

## Architecture

```text
Security Alert
      ↓
Triage Engine
      ↓
Severity Assessment
      ↓
Remediation Recommendation
      ↓
Memory Storage
      ↓
Report Generation
```

## Technology Stack

- Python
- GitHub Actions
- JSON Data Storage
- Workflow Automation
- Agent-Based Decision Logic

## Project Structure

```text
ai-security-triage-agent
│
├── alerts.json          # Security alert inputs
├── rules.py             # Classification logic
├── triage_agent.py      # Core triage engine
├── memory.json          # Persistent findings storage
│
└── outputs/
    └── report.txt       # Generated reports
```

## Workflow

1. Ingest security alerts
2. Analyze alert content
3. Assign severity classification
4. Generate remediation recommendations
5. Store findings in memory
6. Produce investigation reports
7. Escalate unknown findings for manual review

## Example Finding

**Alert:** AWS API key exposed on GitHub

**Severity:** Critical

**Recommended Action:** Rotate key immediately and investigate potential unauthorized access.

## Automation

The triage engine executes automatically through GitHub Actions whenever changes are pushed to the repository.

```text
Git Push
    ↓
GitHub Actions
    ↓
Security Triage Agent
    ↓
Report Generation
```

## Agentic AI Concepts Demonstrated

- Autonomous task execution
- Rule-based reasoning
- Decision making
- Persistent memory
- Tool usage
- Workflow orchestration
- Guardrails and escalation paths
- Human-in-the-loop review

## Future Enhancements

- LLM-powered alert analysis
- Threat intelligence integration
- Risk scoring engine
- Slack and Microsoft Teams notifications
- Security dashboard and analytics
- SIEM integration


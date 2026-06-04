# 🔍 Mini SIEM Log Search Tool

> A lightweight Python-based Security Information and Event Management (SIEM) simulation tool designed for log ingestion, analysis, and threat hunting.

---

## 🚀 Features

### 📂 Multi-Format Log Support

* Supports multiple log formats:
  * `.txt`
  * `.log`
  * `.http`
  * `.dns`
  * `.ftp`
  * `.sh`

### 🔎 Log Analysis Capabilities

* Recursive directory scanning
* Keyword-based searching
* Case-insensitive matching
* Multi-file log analysis
* Lightweight and fast execution

### 📊 Detailed Output

For every match found, the tool displays:

* File Name
* Line Number
* Matching Log Entry

Example:

```text
[access.log] Line 2: Failed login from 192.168.1.10
[access.log] Line 4: Failed login from 192.168.1.20

Total Matches: 2
```

---

## 🎯 Use Cases

### SOC (Security Operations Center)

* Failed login detection
* Security event monitoring
* Log review and investigation
* Initial incident triage

### Threat Hunting

* Search for suspicious keywords
* Hunt Indicators of Compromise (IOCs)
* Investigate abnormal activities
* Analyze attacker behavior

### Incident Response

* Historical log review
* Security event correlation
* Evidence collection
* Basic forensic investigations

---

## 🛠 Technologies Used

* **Python 3**
* **OS Module**
* **File Handling**
* **Directory Traversal**
* **String Matching**

---

## 📈 Workflow

```text
Log Files
   ↓
Directory Scan
   ↓
Log Ingestion
   ↓
Keyword Search
   ↓
Result Analysis
   ↓
Security Findings
```

---

## ⭐ Key Highlights

* **Beginner-Friendly SIEM Simulation**
* **Cross-Platform Python Application**
* **Supports Multiple Log Sources**
* **Useful for SOC Analyst Practice**
* **Demonstrates Log Ingestion & Search Concepts**

---

## 🔮 Future Enhancements

### Detection & Alerting

- [ ] Custom Detection Rules
- [ ] Sigma-like Rule Engine
- [ ] Alert Generation
- [ ] Severity Classification

### Threat Hunting

- [ ] IP Address Extraction
- [ ] IOC Matching
- [ ] Domain Extraction
- [ ] Threat Intelligence Integration

### Reporting

- [ ] TXT Report Export
- [ ] CSV Export
- [ ] Investigation Reports
- [ ] Alert Summaries

### Visualization

- [ ] Dashboard
- [ ] Log Analytics
- [ ] Event Statistics
- [ ] Security Metrics

---

## 🎓 Learning Objectives

This project demonstrates fundamental SIEM concepts including:

> Log Ingestion

> Log Analysis

> Threat Hunting

> Event Searching

> Security Monitoring

> Incident Investigation

---

## 💡 Why This Project?

**Mini SIEM Log Search Tool** was built as a hands-on cybersecurity learning project to understand how modern SIEM solutions operate behind the scenes.

### Skills Demonstrated

* Python Programming
* Log Analysis
* Threat Hunting
* Security Monitoring
* SOC Operations
* Incident Response Fundamentals

---

## 🏷️ Tags

`python` `cybersecurity` `siem` `log-analysis` `soc-analyst` `incident-response` `threat-hunting` `blue-team` `security-monitoring` `log-ingestion`

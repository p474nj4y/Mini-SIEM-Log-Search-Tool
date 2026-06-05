## ⚠️ Important Usage Note

### 📁 Folder Path Requirement

> **This tool requires a DIRECTORY PATH containing log files, NOT the path to an individual log file.**

#### ✅ Correct Input

```text
/Users/pipo/Desktop/Logs
```

#### ❌ Incorrect Input

```text
/Users/pipo/Desktop/Logs/access.log
```

> The application uses recursive directory scanning (`os.walk()`) to locate and analyze all supported log files inside the specified folder and its subdirectories.

---

## 📂 Supported Log Formats

* `.txt`
* `.log`
* `.http`
* `.dns`
* `.ftp`
* `.sh`

---

## ▶️ Getting Started

### Step 1: Run the Program

```bash
python3 log_ingester.py
```

### Step 2: Enter the Folder Path

```text
Folder Path: /Users/pipo/Desktop/Logs
```

### Step 3: Enter a Search Keyword

```text
Search Keyword: Failed
```

### Step 4: Review Results

```text
<<<<<<< RESULTS >>>>>>>

[access.log] Line 2: Failed login from 192.168.1.10
[access.log] Line 4: Failed login from 192.168.1.20

Total Matches: 2
```

---

## 📝 Sample Log File

### access.log

```text
User login successful
Failed login from 192.168.1.10
Admin login successful
Failed login from 192.168.1.20
```

---

## 📂 Sample Directory Structure

```text
Logs/
└── access.log
```

Provide the following path when prompted:

```text
/Users/pipo/Desktop/Logs
```

---

## 📊 Sample Output

```text
<<<<<<< RESULTS >>>>>>>

[access.log] Line 2: Failed login from 192.168.1.10
[access.log] Line 4: Failed login from 192.168.1.20

Total Matches: 2
```

---

## 📋 Report Generation

> Future versions will support exporting findings into investigation reports for SOC and Incident Response workflows.

Example Report:

```text
=============================
Mini SIEM Investigation Report
=============================

Keyword Searched: Failed

Match 1:
File: access.log
Line: 2
Event: Failed login from 192.168.1.10

Match 2:
File: access.log
Line: 4
Event: Failed login from 192.168.1.20

Total Matches: 2
```

---

## 🔥 Planned Enhancements

### Detection & Alerting

- [ ] Custom Detection Rules
- [ ] Sigma-like Detection Engine
- [ ] Alert Generation
- [ ] Severity Classification

### Threat Hunting

- [ ] IOC Matching
- [ ] IP Address Extraction
- [ ] Domain Extraction
- [ ] Threat Intelligence Integration

### Reporting

- [ ] TXT Report Export
- [ ] CSV Export
- [ ] Investigation Reports
- [ ] Alert Summaries

### Visualization

- [ ] Dashboard Interface
- [ ] Log Analytics
- [ ] Event Statistics
- [ ] Security Metrics

---

## 💡 Usage Tips

> Always provide the **folder path** containing log files.

> Do **NOT** provide the path to an individual log file.

> The tool automatically scans all supported files inside the selected directory.

> Useful for SOC Analyst training, Threat Hunting exercises, and Incident Response practice.

---

## 🏷️ Tags

`python`
`cybersecurity`
`siem`
`log-analysis`
`soc-analyst`
`incident-response`
`threat-hunting`
`blue-team`
`security-monitoring`
`log-ingestion`

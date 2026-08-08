# 🛡️ PhishGuard

## Phishing Awareness & Threat Analysis Tool

PhishGuard is a cybersecurity awareness tool developed for DecodeLabs Internship Project 3.

The application analyzes suspicious emails and messages using a rule-based detection engine. It identifies common phishing indicators such as suspicious keywords, urgency, credential requests, financial requests, threatening language, suspicious attachments, and potentially unsafe URLs.

---

## 🎯 Project Objective

The objective of this project is to develop a practical phishing-awareness tool capable of:

- Identifying suspicious links and keywords
- Detecting common phishing red flags
- Providing a risk assessment
- Explaining why a message may be unsafe
- Providing recommended security actions

---

## ✨ Features

### 🔎 Keyword Detection

Detects suspicious terms commonly associated with phishing messages.

### ⏱️ Urgency Detection

Identifies pressure tactics such as:

- Urgent
- Immediately
- Act now
- Within 24 hours
- Final warning

### 🔑 Credential Detection

Detects requests involving:

- Passwords
- Usernames
- Login information
- Credentials
- Account verification

### 💳 Financial Detection

Identifies references to:

- Payments
- Credit cards
- Bank accounts
- Transfers
- Billing
- Refunds

### ⚠️ Threat Detection

Identifies threatening language such as:

- Account suspension
- Account termination
- Legal action
- Blocked accounts

### 📎 Attachment Detection

Detects potentially dangerous file extensions including:

- .exe
- .scr
- .bat
- .cmd
- .vbs
- .js
- .jar
- .msi
- .ps1

### 🔗 URL Analysis

Analyzes URLs for characteristics including:

- HTTP instead of HTTPS
- IP addresses
- URL shorteners
- Suspicious top-level domains
- Excessive subdomains
- Sensitive keywords in domains

### 📊 Risk Scoring

Messages receive a score from 0–100.

| Score | Risk |
|---|---|
| 0–24 | LOW |
| 25–49 | MEDIUM |
| 50–74 | HIGH |
| 75–100 | CRITICAL |

---

## 🛠️ Technologies

- Python
- Streamlit
- Regular Expressions
- URL Parsing
- Rule-Based Detection

---

## 📁 Project Structure

```text
Project-3-Phishing-Awareness/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── .gitignore
│
├── samples/
│
├── screenshots/
│
└── report/
# SMTP Mail Client Testing Documentation

## Overview

This document outlines the testing process and outcomes for the SMTP client implemented using Python sockets and the `ssl` module. The client connects to a real-world SMTP server (smtp2go.com), upgrades the connection using STARTTLS, authenticates via AUTH LOGIN, and sends a plain text email message.

---

## ✅ Test Cases

### 1. Connection Test (TCP Socket)
**Expected**: Server returns a `220` greeting upon establishing TCP connection.  
**Result**: Passed ✅

### 2. EHLO Command (Before STARTTLS)
**Expected**: Server responds with `250` and lists supported extensions including `STARTTLS`.  
**Result**: Passed ✅

### 3. STARTTLS Command
**Expected**: Server responds with `220 TLS go ahead`, indicating readiness for secure connection upgrade.  
**Result**: Passed ✅

### 4. TLS Handshake
**Expected**: TLS context wraps the socket successfully without certificate errors after disabling verification (for testing purposes).  
**Result**: Passed ✅

### 5. EHLO Command (After TLS)
**Expected**: Server responds with `250` again and advertises `AUTH LOGIN` as a supported authentication mechanism.  
**Result**: Passed ✅

### 6. AUTH LOGIN (Username + Password)
**Expected**: Server prompts with `334` codes and returns `235 Authentication successful` after credentials are accepted.  
**Result**: Passed ✅

### 7. MAIL FROM Command
**Expected**: Server responds with `250 sender ok`.  
**Result**: Passed ✅

### 8. RCPT TO Command
**Expected**: Server responds with `250 recipient ok`.  
**Result**: Passed ✅

### 9. DATA Command
**Expected**: Server responds with `354 Start mail input`.  
**Result**: Passed ✅

### 10. Message Body Transmission
**Expected**: Message body is sent and completed with `\r\n.\r\n`. Server responds with `250 OK id=...` indicating acceptance.  
**Result**: Passed ✅

### 11. QUIT Command
**Expected**: Server responds with `221 Bye` and closes the session.  
**Result**: Passed ✅

---

## 🔧 Testing Environment

- **SMTP Server**: mail.smtp2go.com
- **Port**: 587 (supports STARTTLS)
- **Encryption**: STARTTLS (TLS 1.2+ via Python `ssl` module)
- **Authentication**: AUTH LOGIN (Base64 encoded username/password)
- **Python Version**: 3.12
- **Platform**: macOS (Apple Silicon, macOS Ventura)
- **Network**: Home Wi-Fi (stable)

---

## ⚠️ Troubleshooting Log

- **SSL Certificate Verification Error**:  
  `SSLCertVerificationError` was resolved by disabling certificate verification for this experiment using:
  ```python
  context.check_hostname = False
  context.verify_mode = ssl.CERT_NONE

- **Relay Access Denied**:
  This occurred before authentication was implemented. Resolved by correctly sending AUTH LOGIN with valid credentials.

- **Auth failures**:
  Initially tested with incorrect ports and wrong auth order. Correct flow: EHLO → STARTTLS → EHLO → AUTH.


## Edge Case Handling
	•	Server response codes are parsed and printed for every SMTP stage.
	•	Unexpected errors are caught and logged with meaningful messages.
	•	TLS errors are handled with custom context setup.
	•	Socket is properly closed after QUIT, even on exception.

## 📧 Email Verification
	•	Final email was successfully received at wangxueqi08@gmail.com (check Inbox or Spam).
	•	Subject line: SMTP Lab Test
	•	Body: I love computer networks!
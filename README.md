# SMTP Mail Client

## 📌 Overview

This project implements a secure SMTP mail client using raw Python `socket` and `ssl` modules. The client connects to the `smtp2go.com` mail server, upgrades the connection using the `STARTTLS` command, performs SMTP authentication using `AUTH LOGIN`, and sends a plain text email to a recipient following the standard SMTP protocol step-by-step.

⚠️ The client **does not use any high-level libraries like `smtplib`**, fully complying with the assignment requirement to expose and manually control SMTP behavior.

---

## 🛠 Requirements

- Python 3.10+ (tested on Python 3.12)
- Internet connection
- A free account from [smtp2go.com](https://www.smtp2go.com)
- One **verified sender email** (e.g. Gmail, Outlook, Hotmail)
- One **valid recipient email** (can be your own other email)

---

## 📁 File Structure

```text
smtp_lab/
├── smtp_client_tls_socket.py     # ✅ Main program (pure socket + TLS)
├── README.md                     # 📄 This documentation
├── TESTING.md                    # ✅ Testing summary and results
├── screenshots/                  # 📸 Screenshot folder
│   ├── smtp_terminal.png         # Full SMTP command/response
│   ├── email_received.png        # Final received email
│   └── quit_response.png         # QUIT command confirmation
└── legacy_client.py              # (Optional) legacy version without TLS
```

---

## ▶️ How to Run

1.	Open smtp_client_tls_socket.py and update the following lines with your own credentials:

```python
username = "your_smtp2go_username"
password = "your_smtp2go_password"
sender_email = "your_verified_sender@example.com"
receiver_email = "recipient@example.com"
```

2.	Save the file and open a terminal in the project folder.
3.	Run the script:
    
```bash
python3 smtp_client_tls_socket.py
```

4.	If successful, you will see:
• Server greeting 220
• TLS handshake success
• SMTP authentication (235 Authentication successful)
• Message accepted (250 OK)
• QUIT response (221 Bye)
5.	Check your receiver_email inbox (or spam) for the email.

## ⚙️ Configuration Notes

	•	SMTP server: mail.smtp2go.com
	•	Port: 587
	•	Encryption: STARTTLS
	•	Authentication method: AUTH LOGIN with base64 encoding

SSL certificate verification is disabled in this educational context for compatibility:

```python
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
```

This bypasses self-signed certificate warnings, which are common in educational/test SMTP servers. This approach is not recommended in production systems.

## 💡 Expected Output
	•	SMTP connection starts with EHLO, followed by STARTTLS, authentication, and SMTP commands.
	•	All command–response pairs (e.g. MAIL FROM, RCPT TO, DATA, QUIT) are printed to the terminal.
	•	The final email appears in the recipient’s mailbox with subject SMTP Lab Test and body I love computer networks!

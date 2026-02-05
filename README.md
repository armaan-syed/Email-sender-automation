# Email-sender-automation
This Python program automates sending emails to multiple recipients at once. It asks the user to enter their Gmail address and app password for secure login. The user then provides recipient email addresses in a comma-separated format, along with the email subject and message content.
# 📧 Python Bulk Email Sender

A simple Python program that allows users to send emails to multiple recipients at once using Gmail SMTP. The script accepts comma-separated email addresses, a subject, and a message, then delivers the email securely using Gmail App Password authentication.

---

## 🚀 Features

- Send emails to multiple recipients at once  
- Accepts comma-separated email input  
- Secure login using Gmail App Password  
- Simple command-line interface  
- Basic error handling  

---

## 🛠️ Requirements

- Python 3.x
- Internet connection
- Gmail account
- Gmail App Password enabled

---

## 🔐 How To Generate Gmail App Password

1. Go to Google Account Security Settings  
2. Enable **2-Step Verification**  
3. Open **App Passwords**  
4. Select:
   - App → Mail  
   - Device → Other  
5. Generate password and copy it  

---

## ▶️ How To Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name

python sendmail.py

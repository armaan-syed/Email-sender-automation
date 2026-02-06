import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    # taking sender info
    sender_email = input("Enter your Gmail address: ").strip()
    app_password = input("Enter your Gmail App Password: ").strip()

    # taking receiver emails
    emails_input = input("Enter recipient emails separated by commas:\n")
    
    # Convert string -> list
    receivers = [email.strip() for email in emails_input.split(",") if email.strip()]

    if not receivers:
        print("No valid email addresses entered.")
        exit()

    # taking subject & body
    subject = input("Enter subject: ")
    body = input("Enter message: ")

    # SMTP setup
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    print("\n Email sent successfully to:")

    # sending mails individually (acts like BCC)
    for email in receivers:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, email, message.as_string())

        print("✔", email)

except Exception as e:
    print("\n Error occurred:", e)

finally:
    try:
        server.quit()
    except:
        pass

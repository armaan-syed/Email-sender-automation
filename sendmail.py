import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    #taking senders info
    sender_email = input("Enter your Gmail address: ").strip()
    app_password = input("Enter your Gmail App Password: ").strip()

    # taking recievers email
    emails_input = input("Enter recipient emails separated by commas:\n")
    
    # Convert'ing string -> list
    receivers = [email.strip() for email in emails_input.split(",") if email.strip()]

    if not receivers:
        print("No valid email addresses entered.")
        exit()

    # taking subject
    subject = input("Enter subject: ")
    body = input("Enter message: ")

    # creating email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # SMPT
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    # sending the mails
    server.sendmail(sender_email, receivers, message.as_string())

    print("\n Email sent successfully to:")
    for email in receivers:
        print("✔", email)

except Exception as e:
    print("\n Error occurred:", e)

finally:
    try:
        server.quit()
    except:
        pass

import smtplib
from email.mime.text import MIMEText

email_sender = input("Enter your email id: ")
email_receiver = input("Enter receiver email id: ")
subject = input("Enter subject of email: ")
body = input("Enter your message: ")
message = MIMEText(body)
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject

smtp_server = "smtp.mailtrap.io"
smtp_port = 465
smtp_user = "9049cc92ea84f6"
smtp_pass = "9f0981aa7a2621"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(email_sender, email_receiver, message.as_string())
    print("Email sent succeccfully.")
    
except SMTPException:
    print("Error in sending email.")
server.quit()
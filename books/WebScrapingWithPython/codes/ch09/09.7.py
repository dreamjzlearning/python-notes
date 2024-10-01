# 09.7.py
# Sending Email

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email")

msg["Subject"] = "An Email Alert"
msg["From"] = "xxx"
msg["To"] = "xxx"

try:
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login("xxx", "xxx")
        server.sendmail("xxx", "xxx", msg.as_string())
        print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")

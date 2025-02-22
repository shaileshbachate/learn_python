import os
from email.message import EmailMessage
import smtplib
import ssl
import datetime

sender_email = os.environ.get("MY_EMAIL") or ""
password = os.environ.get("EMAIL_PASSWORD") or ""
receiver_email = os.environ.get("MY_EMAIL")

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test email"
body = f"<h1>Test email sent at: {datetime.datetime.now()}</h1>"
# msg.set_content(body)
msg.set_content(body, subtype="html") # this method sends the message in html format. set_content() sends the message in plain text format by default.

ssl_context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context) as smtp:
    smtp.login(sender_email, password)
    smtp.send_message(msg)
    # smtp.sendmail(sender_email, receiver_email, msg.as_string()) # this method sends the message in binary format. as_string() converts the message to a string
    print("Email sent successfully")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template
from pathlib import Path
# from dotenv import load_dotenv
import os

MAIL_SMTP_SERVER = os.getenv('MAIL_SMTP_SERVER')
MAIL_SMTP_PORT = 587
MAIL_SMTP_USERNAME = os.getenv('MAIL_SMTP_USERNAME')  # Your email address
MAIL_SMTP_PASSWORD = os.getenv('MAIL_SMTP_PASSWORD')  # Your email password
MAIL_DISPLAY_NAME = os.getenv('MAIL_DISPLAY_NAME')  # Your desired display name

def send_mail(mail_id, otp):
    print("inside send mail", mail_id, otp)
    file_path = Path(__file__).parent / 'email_template.html'
    # Load the email template from a file
    with open(file_path) as file:
        template_content = file.read()

    template = Template(template_content)

    # Set up the email body using the template and dynamic data
    context = {'otp' : otp}

    email_body = template.substitute(context)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = f"{MAIL_DISPLAY_NAME} <{MAIL_SMTP_USERNAME}>"
    message['To'] = mail_id  # Replace with the recipient's email address
    message['Subject'] = 'Your OTP for Email Verification'  # Set the email subject

    # Attach the email body as HTML
    message.attach(MIMEText(email_body, 'html'))

    # Send the email using the SMTP server
    with smtplib.SMTP(MAIL_SMTP_SERVER, MAIL_SMTP_PORT) as server:
        server.starttls()
        server.login(MAIL_SMTP_USERNAME, MAIL_SMTP_PASSWORD)
        server.sendmail(MAIL_SMTP_USERNAME, [message['To']], message.as_string())

    return "Email sent successfully"

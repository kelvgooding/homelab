"""
Author: Kelvin Gooding
Created: 2022-10-11
Updated: 2023-10-19
Version: 1.3
"""

# Modules

import smtplib
from email.message import EmailMessage
from . import auth

def send_email(recipient, subject, body):

    # Variables

    server = smtplib.SMTP(auth.smtp_auth['server'], auth.smtp_auth['port'])
    server.starttls()

    # Log into SMTP Server

    server.login(auth.smtp_auth['email'], auth.smtp_auth['password'])

    # Create/Generate Email

    msg = EmailMessage()

    msg["Subject"] = f"{subject}"
    msg["From"] = auth.smtp_auth['email']
    msg["To"] = recipient
    msg.set_content(body)
    server.send_message(msg)

    print(f'Email has been sent successfully to {recipient}')

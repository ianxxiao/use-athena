from email.mime.text import MIMEText
from configs import secret_stuff, email_config
import smtplib


def send_email(email_addr):
    '''
    this function sends an email to a user
    inputs:
        email (str): email address of the recipient
    '''

    # Get sender credential
    from_email = secret_stuff.FROM_EMAIL
    from_password = secret_stuff.EMAIL_PW
    to_email = email_addr

    # Create email content and recipient info
    msg = MIMEText(email_config.EMAIL_CONTENT, 'html')
    msg['Subject'] = email_config.EMAIL_SUBJECT
    msg['To'] = to_email
    msg['From'] = from_email

    # send the email
    gmail = smtplib.SMTP(email_config.EMAIL_SERVER, email_config.EMAIL_SERVER_PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

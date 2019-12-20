from email.mime.text import MIMEText
from configs import secret_stuff
import smtplib


def send_email(email):
    '''
    this function sends an email to a user
    inputs:
        email (str): email address of the recipient
    '''

    from_email = secret_stuff.FROM_EMAIL
    from_password = secret_stuff.EMAIL_PW
    to_email = email

    subject = "Athena Analytics | Your Personalized Report"
    message = "this is a test report. <strong>Enjoy.</strong>"

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

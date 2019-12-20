from email.mime.text import MIMEText
from configs import secret_stuff, email_config
import smtplib


def send_email(email_addr, ranked_ideas):
    '''
    this function sends an email to a user
    inputs:
        email (str): email address of the recipient
        ranked_ideas (list): a ranked list of ideas with score (highest first)
    '''

    # Get sender credential
    from_email = secret_stuff.FROM_EMAIL
    from_password = secret_stuff.EMAIL_PW
    to_email = email_addr

    # Create email content and recipient info
    msg = make_content(ranked_ideas)
    msg['Subject'] = email_config.EMAIL_SUBJECT
    msg['To'] = to_email
    msg['From'] = from_email

    # send the email
    gmail = smtplib.SMTP(email_config.EMAIL_SERVER, email_config.EMAIL_SERVER_PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


def make_content(ranked_ideas):
    """
    This function create email content based on the ranked ideas and placeholder.
    Inputs:
        ranked_ideas (list): a ranked list of ideas with score (highest first)
    Output:
        msg = HTML email content
    """

    introduction = "Hiya, this is Athena. Here is what I think your ideas will do based on my Athena Score. <br>"
    first = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[0][0], ranked_ideas[0][1])
    second = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[1][0], ranked_ideas[1][1])
    third = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[2][0], ranked_ideas[2][1])
    explain = "<br> The Athena Score is based on trends and opportunities on various popular publication sites."
    outro = "<br> Enjoy writing. See you next time. <br> <strong>Athena</strong>"

    msg_str = introduction + first + second + third + explain + outro

    return MIMEText(msg_str, 'html')

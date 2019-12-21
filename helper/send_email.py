from email.mime.text import MIMEText
from configs import secret_stuff, email_config
import smtplib


def send_email(email_addr, name, ranked_ideas, results):
    '''
    this function sends an email to a user
    inputs:
        email (str): email address of the recipient
        name (str): first name of the recipient
        ranked_ideas (list): a ranked list of ideas with score (highest first)
    '''

    # Get sender credential
    from_email = secret_stuff.FROM_EMAIL
    from_password = secret_stuff.EMAIL_PW
    to_email = email_addr

    # Create email content and recipient info
    msg = make_content(ranked_ideas, name, results)
    msg['Subject'] = email_config.EMAIL_SUBJECT
    msg['To'] = to_email
    msg['From'] = from_email

    # send the email
    gmail = smtplib.SMTP(email_config.EMAIL_SERVER, email_config.EMAIL_SERVER_PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


def make_content(ranked_ideas, name, results):
    """
    This function create email content based on the ranked ideas and placeholder.
    Inputs:
        ranked_ideas (list): a ranked list of ideas with score (highest first)
        name(str): the first time of the recipient
        results(list): a nested list of top search results per ideas
    Output:
        msg = HTML email content
    """

    introduction = "Hiya {}, this is Athena. Here is what I think of your ideas based on my Athena Score. <br>" \
        .format(name)

    first = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[0][0], ranked_ideas[0][1])
    second = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[1][0], ranked_ideas[1][1])
    third = "<li> <strong>{}</strong>: {} </li>".format(ranked_ideas[2][0], ranked_ideas[2][1])

    first_articles = "<br> Here are the top articles related to <strong>{}</strong>: <br>".format(ranked_ideas[0][0])
    first_links = "<li>{}</li> <li>{}</li> <li>{}</li>".format(results[0][0], results[0][1], results[0][2])

    second_articles = "<br> Here are the top articles related to <strong>{}</strong>: <br>".format(ranked_ideas[1][0])
    second_links = "<li>{}</li> <li>{}</li> <li>{}</li>".format(results[1][0], results[1][1], results[1][2])

    third_articles = "<br> Here are the top articles related to <strong>{}</strong>: <br>".format(ranked_ideas[2][0])
    third_links = "<li>{}</li> <li>{}</li> <li>{}</li>".format(results[2][0], results[2][1], results[2][2])

    explain = "<br> The Athena Score is based on trends and opportunities on various popular publication sites."
    outro = "<br> Enjoy writing. See you next time. <br> <strong>Athena</strong>"

    msg_str = introduction + first + second + third \
              + first_articles + first_links \
              + second_articles + second_links \
              + third_articles + third_links \
              + explain + outro

    return MIMEText(msg_str, 'html')

from email.mime.text import MIMEText
from athena.configs import email_config
import smtplib
import os
from flask import url_for


def send_email(email_addr, name, ranked_ideas, results):
    '''
    this function sends an email to a user
    inputs:
        email (str): email address of the recipient
        name (str): first name of the recipient
        ranked_ideas (list): a ranked list of ideas with score (highest first)
        results (dict): a dictionary of search terms, top n results, and corresponding title and url
    '''

    # Get sender credential
    from_email = os.getenv("FROM_EMAIL")
    from_password = os.getenv("EMAIL_PW")
    to_email = email_addr

    # Create email content and recipient info
    msg = make_report_content(ranked_ideas, name, results)
    msg['Subject'] = email_config.EMAIL_SUBJECT
    msg['To'] = to_email
    msg['From'] = from_email

    # send the email
    gmail = smtplib.SMTP(email_config.EMAIL_SERVER, email_config.EMAIL_SERVER_PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


def make_report_content(ranked_ideas, name, results):
    """
    This function create email content based on the ranked ideas and placeholder.
    Inputs:
        ranked_ideas (list): a ranked list of ideas with score (highest first)
        name(str): the first time of the recipient
        results(list): a nested list of top search results per ideas
    Output:
        msg = HTML email content
    """

    introduction = "Hiya {}, this is Athena. Here is what I think of your ideas based on my Athena Score (alpha). " \
                   "The Athena Score is based on trends and opportunities from various popular publication sites.<br>" \
        .format(name)

    ranks = ""
    for i in ranked_ideas:
        ranks += "<li> <strong>{}</strong>: {} </li> ".format(i[0], i[1])

    links = ""
    for idx, search_term in enumerate(ranked_ideas):
        links += "<br> Here are the top articles related to <strong>{}</strong>: <br> ".format(search_term[0])
        titles = results.get(search_term[0])
        links += "<li><a href = {}>{}</a></li>" \
                 "<li><a href = {}>{}</a></li>" \
                 "<li><a href = {}>{}</a></li>".format(titles[0][0], titles[0][1],
                                                       titles[1][0], titles[1][1],
                                                       titles[2][0], titles[2][1])

    end = "<br> The Athena Score is based on trends and opportunities from various popular publication sites." \
          + "<br> Enjoy writing. See you next time. <br><br> <strong>Athena</strong>"

    msg_str = introduction + ranks + links + end

    return MIMEText(msg_str, 'html')


def send_password_reset(user):
    # Get sender credential
    from_email = os.getenv("FROM_EMAIL")
    from_password = os.getenv("EMAIL_PW")
    to_email = user.email

    # Create email content and recipient info
    msg = make_reset_content(user.get_reset_token())
    msg['Subject'] = 'Athena | Password Reset - Do not Reply'
    msg['To'] = to_email
    msg['From'] = from_email

    # send the email
    gmail = smtplib.SMTP(email_config.EMAIL_SERVER, email_config.EMAIL_SERVER_PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


def make_reset_content(token):
    msg_str = "this your password reset link: <br><br>" \
              "{} <br><br>" \
              "If you didn't request this, please ignore.".format(url_for('reset_token', token=token, _external=True))

    return MIMEText(msg_str, 'html')

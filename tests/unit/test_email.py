# this function tests email capability

import sys
sys.path.append('../use-athena')
import pytest
from configs import back_end_config
from send_email import send_email
from configs import secret_stuff
import smtplib
from email.mime.text import MIMEText
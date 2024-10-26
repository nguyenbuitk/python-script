import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "buinguyen23112k@gmail.com"
    # somerealpass
    password = os.environ.get('password')

    receiver = "buinguyen23112k@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        
send_mail("Hi there")
import os
import project_path as pp
from mail import mail
import smtplib
import ssl
import getpass

credentials = {}


def get_credentials():
    credentials['id'] = input('Enter your Gmail ID:')
    credentials['password'] = getpass.getpass('Enter your Gmail Password:')


def main():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
        server.login(credentials['id'], credentials['password'])

    mail_contents = mail()
    mail_contents.set_recipient()
    mail_contents.set_subject('Test Mail')
    mail_contents.set_body()


if __name__ == '__main__':
    main()

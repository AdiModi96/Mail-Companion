import os
import project_path as pp
from mail_composer import mail_composer
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
from email import encoders
import ssl
import getpass

credentials = {}


def get_credentials():
    while True:
        credentials['id'] = input('Enter your Gmail ID: ')
        if credentials['id'].endswith('@gmail.com'):
            break
        print('Your Gmail ID must end with "@gmail.com". Try again')
    credentials['pthrowawayinsometime@gmail.comassword'] = getpass.getpass(prompt='Enter your Gmail Password: ')


def main():
    # get_credentials()

    credentials = {
        'id': 'correspondent.automated@gmail.com',
        'password': 'correspondent.automated@15042020'
    }

    message_body_1 = '''Message Body'''
    message_body_2 = '''
    <html>
      <body>
        <p>Hi,
        <br>
           How are you?
           <br>
           I'm Cool!.
        </p>
      </body>
    </html>
    '''

    message = MIMEMultipart('alternative')
    message['Subject'] = 'Subject 2'
    message['From'] = 'correspondent.automated@gmail.com'
    message['To'] = 'aditya.modi.in@gmail.com'
    message['Cc'] = 'aditya.modi.in@live.in, 14bce003@nirmauni.ac.in'
    message['Bcc'] = '18305R007@iitb.ac.in, adimodi@cse.iitb.ac.in'
    message.attach(MIMEText(message_body_2, 'html'))

    filename1 = '1.jpg'
    filename2 = '2.pdf'

    # Open PDF file in binary mode
    with open(filename2, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename={}".format(filename2),
    )

    # Add attachment to message and convert message to string
    message.attach(part)


    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
            server.login(credentials['id'], credentials['password'])
            server.sendmail(credentials['id'], message['To'], message.as_string())
    except smtplib.SMTPAuthenticationError:
        print('Authentication Failed!')


if __name__ == '__main__':
    main()

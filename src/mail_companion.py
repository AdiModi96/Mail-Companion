import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
from email import encoders
import ssl
import getpass

credentials = {}


class mail:
    _sender_email_id = 'correspondent.automated@gmail.com'

    def __init__(self):
        self._sender_email_id = None
        self._receiver_email_id = None
        self._receiver_email_cc_ids = []
        self._receiver_email_bcc_ids = []
        self._subject = ''
        self._body = ''''''
        self._html = False
        self._message_body = None
        self._mime_message = None
        self._attachments_file_paths = []

    def set_receiver_email_id(self, receiver_email_id):
        self._receiver_email_id = receiver_email_id

    def add_receiver_cc_email_id(self, receiver_email_cc_ids):
        if type(receiver_email_cc_ids) == list:
            for idx in range(len(receiver_email_cc_ids)):
                self._receiver_email_cc_ids.append(receiver_email_cc_ids[idx])
        elif type(receiver_email_cc_ids) == str:
            self._receiver_email_cc_ids.append(receiver_email_cc_ids)

    def set_subject(self, subject):
        self._subject = subject

    def set_body(self, body='''''', html=False):
        self._body = body
        self._html = html

    def compose_message(self):
        self._mime_message = MIMEMultipart('alternative')
        self._mime_message['Subject'] = self._subject
        self._mime_message['From'] = mail._sender_email_id
        self._mime_message['To'] = self._receiver_email_id
        self._mime_message['Cc'] = str(self._receiver_email_cc_ids) \
            .replace('[', '') \
            .replace(']', '') \
            .replace('\'', '') \
            .replace('"', '')
        self._mime_message['Bcc'] = str(self._receiver_email_bcc_ids) \
            .replace('[', '') \
            .replace(']', '') \
            .replace('\'', '') \
            .replace('"', '')
        self._mime_message.attach(MIMEText(self._message_body, 'html' if self._html else 'plain'))

        for attachment_file_path in self._attachments_file_paths:
            file_name = attachment_file_path[attachment_file_path.rindex(os.path.sep) + 1:]
            try:
                with open(attachment_file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
            except:
                print('Error: Unable to attach file: {}'.format(attachment_file_path))

            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                "attachment; filename={}".format(file_name),
            )
            self._mime_message.attach(part)


class mailer:

    def __init__(self, mail_object):
        self.mail_object = mail_object
        self.password = ''
        self.context = ssl.create_default_context()

        try:
            for i in range(3):
                password = getpass.getpass(prompt='Enter your Gmail Password: ')
                try:
                    with smtplib.SMTP_SSL("smtp.gmail.com", context=self.context) as server:
                        server.login(mail._sender_email_id, password)
                        self.password = password
                        break
                except smtplib.SMTPAuthenticationError:
                    print('Error: Authentication Failed!')
                    print('{} attempts left'.format(i - 1))

            with smtplib.SMTP_SSL("smtp.gmail.com", context=self.context) as server:
                server.login(mail._sender_email_id, self.password)
                server.sendmail(mail._sender_email_id, mail_object._receiver_email_id, mail_object._mime_message.as_String())
        except:
            print('Error: Unexpected Error!')

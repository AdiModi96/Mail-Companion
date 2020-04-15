import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
from email import encoders
import ssl
import getpass

credentials = {}


class mail_composer:
    _sender_email_id = 'correspondent.automated@gmail.com'
    _sender_signature = '''
    
    --
    I am a digital reporter built by Aditya Modi to provide status updates for background experiments, etc.
    My source code is freely available on GitHub: https://github.com/AdiModi96/Mail-Companion
    '''

    def __init__(self):
        self._sender_email_id = None
        self._receiver_email_id = None
        self._receiver_email_cc_ids = []
        self._receiver_email_bcc_ids = []
        self._subject = ''
        self._message_body = ''''''
        self._html = False
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

    def add_receiver_bcc_email_id(self, receiver_email_bcc_ids):
        if type(receiver_email_bcc_ids) == list:
            for idx in range(len(receiver_email_bcc_ids)):
                self._receiver_email_bcc_ids.append(receiver_email_bcc_ids[idx])
        elif type(receiver_email_bcc_ids) == str:
            self._receiver_email_bcc_ids.append(receiver_email_bcc_ids)

    def add_attachments(self, attachment_file_paths):
        if type(attachment_file_paths) == list:
            for idx in range(len(attachment_file_paths)):
                self._attachments_file_paths.append(attachment_file_paths[idx])
        elif type(attachment_file_paths) == str:
            self._attachments_file_paths.append(attachment_file_paths)

    def set_subject(self, subject):
        self._subject = subject

    def set_message_body(self, message_body='''''', html=False):
        self._message_body = message_body
        self._html = html

    def compose_message(self):
        self._mime_message = MIMEMultipart('alternative')
        self._mime_message['Subject'] = self._subject
        self._mime_message['From'] = mail_composer._sender_email_id
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
        self._mime_message.attach(MIMEText(self._message_body + mail_composer._sender_signature,
                                           'html' if self._html else 'plain'))

        self._all_receiver_email_ids = [self._receiver_email_id]
        for _receiver_email_cc_id in self._receiver_email_cc_ids:
            self._all_receiver_email_ids.append(_receiver_email_cc_id)
        for _receiver_email_bcc_id in self._receiver_email_bcc_ids:
            self._all_receiver_email_ids.append(_receiver_email_bcc_id)

        for attachment_file_path in self._attachments_file_paths:
            file_name = os.path.basename(attachment_file_path)
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
        print('Mail composed successfully!')


class mailer:

    def __init__(self):
        self._mail_composer = None
        self._password = ''
        self.context = ssl.create_default_context()

        try:
            for i in range(3):
                password = getpass.getpass(
                    prompt='Enter your password for account "{}": '.format(mail_composer._sender_email_id))
                try:
                    with smtplib.SMTP_SSL("smtp.gmail.com", context=self.context) as server:
                        server.login(mail_composer._sender_email_id, password)
                        self._password = password
                        break
                except smtplib.SMTPAuthenticationError:
                    print('Error: Authentication Failed!')
                    print('{} attempts left'.format(i - 1))

        except:
            print('Error: Unexpected Error!')

    def set_mail_composer(self, mail_composer):
        self._mail_composer = mail_composer

    def send(self):
        if mail_composer != None:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", context=self.context) as server:
                    server.login(mail_composer._sender_email_id, self._password)
                    server.sendmail(mail_composer._sender_email_id,
                                    self._mail_composer._all_receiver_email_ids,
                                    self._mail_composer._mime_message.as_string())
                print('Mail sent successfully!')
            except:
                print('Error: Unexpected Error!')
        else:
            print('Error: Compose a mail first!')

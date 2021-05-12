import json
import paths
import os
import sys
import smtplib
from mail_companion import MailComposer, Mailer

# Checking availability of parameters file
try:
    with open(os.path.join(paths.resrc_folder_path, 'credentials.json')) as credentials_file:
        credentials = json.load(credentials_file)
except IOError:
    print('Error: Parameters file missing or corrupted')
    sys.exit(0)

# Creating mailer instance and simultaneously logging in
try:
    mailer = Mailer(sender_email_id=credentials['sender_email_id'], password=credentials['password'])
except smtplib.SMTPAuthenticationError:
    print('Error: Authentication failed for provided ID/password combination!')
    print('Note: This error could also arise if you haven\'t turned on access to less secure apps from your sender gmail account.\nYou can turn on from this link: https://myaccount.google.com/lesssecureapps')
    sys.exit(0)
except:
    print('Error: Unexpected Error!')
    sys.exit(0)

# Composing a message
mail_composer = MailComposer()
mail_composer.set_sender_email_id(credentials['sender_email_id'])
mail_composer.set_receiver_email_id('receiver_email_id@gmail.com')
# mc.add_receiver_cc_email_id(['receiver_cc_email1@gmail.com', '...'])
# mc.add_receiver_bcc_email_id(['receiver_bcc_email@gmail.com', '...'])
mail_composer.set_subject(subject='Test Mail')
mail_composer.set_message_body(message_body='Hello, This is a test mail!', html=False)
# mc.add_attachments(['attachment1', 'attachment2', '...'])
mail_composer.compose_message()

# Sending composed mail
try:
    mailer.send(mail_composer)
    print('Mail sent successfully!')
except:
    print('Error: Unable to send mail')

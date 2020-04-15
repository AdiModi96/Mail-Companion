from mail_companion import mail_composer, mailer

mc = mail_composer()
mc.set_receiver_email_id('email1@gmail.com')
# mc.add_receiver_cc_email_id(['cc_email1@gmail.com', '...'])
# mc.add_receiver_bcc_email_id(['bcc_email@gmail.com', '...'])
mc.set_subject(subject='Test Mail')
mc.set_message_body(
    message_body='''
    Hello,
    This is a test mail.
    ''', html=False)
# mc.add_attachments(['attachment1', 'attachment2', '...'])
mc.compose_message()

mmc = mailer()
mmc.set_mail_composer(mc)
mmc.send()

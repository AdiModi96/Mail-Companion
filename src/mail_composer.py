# https://developers.google.com/gmail/api/quickstart/python
class mail_composer:
    def __init__(self):
        self._sender_email_id = None
        self._receiver_email_ids = []
        self._subject = None
        self._body = None
        self._message = None

    def __repr__(self):
        pass

    def __str__(self):
        return 'Hello'

    def set_sender_email_id(self, sender_email_id):
        self._sender_email_id = sender_email_id

    def get_receiver_email_ids(self):
        return self._receiver_email_ids.copy()

    def set_receiver_email_ids(self, receiver_email_ids):
        self._receiver_email_ids = receiver_email_ids

    def add_receiver_email_id(self, receiver_email_id):
        self._receiver_email_ids.append(receiver_email_id)

    def set_subject(self, subject):
        self._subject = subject

    def set_body(self, body=''''''):
        self._body = body

    def compose_message(self):
        self._message = 'From: %s\r\n" % fromaddr' \
                        '"To: %s\r\n" % toaddr' \
                        '"CC: %s\r\n" % ",".join(cc)' \
                        '"Subject: %s\r\n" % message_subject' \
                        '"\r\n"' \
                        'message_text'.format(self._subject, self._body)

    def get_message(self):
        return self._message
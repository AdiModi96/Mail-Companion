# https://developers.google.com/gmail/api/quickstart/python
class mail:
    def __init__(self, sender_email_id, receiver_email_id=None, subject='', body=''''''):
        self.sender_email_id = sender_email_id
        self.receiver_email_id = receiver_email_id
        self.subject = subject
        self.body = body

    def __repr__(self):
        pass

    def __str__(self):
        return 'Hello'

    def set_receiver_email_id(self, receiver_email_id):
        self.receiver_email_id = receiver_email_id
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_body(self, body=''''''):
        self.body = body
        return self
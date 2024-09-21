from datetime import datetime
from imaplib import IMAP4_SSL
from email import message_from_bytes

from inbox.config import Credentials
from inbox.attachments import Attachment
from helpers.formatters import safe_attachment_filename

class InboxConnection():
    def __init__(self):
        self.config = Credentials()
        self.new_emails = list(self.get_unread_messages())
        self.attachments_found = list(self.get_attachments())

    def get_unread_messages(self):
        print(f'\nTime stamp: {datetime.now().strftime("%x at %X")}')
        print(f'[ ] Connecting to \'{self.config.address}\' inbox...')

        with IMAP4_SSL(self.config.server) as connection:
            connection.login(self.config.address, self.config.password)
            connection.select('INBOX')

            response, email_ids_raw_list = connection.search(None, 'UNSEEN')

            if response != 'OK':
                raise Exception('Error retrieving inbox information.')
            else:
                email_ids = email_ids_raw_list[0].split()

                print('[ ] Fetching content from unread emails...')
                for email_id in email_ids:
                    response, content = connection.fetch(email_id, '(RFC822)')
                    if response != 'OK':
                        raise Exception('Error fetching emails\' content.')
                    else:
                        email = message_from_bytes(content[0][1])
                        connection.store(email_id, '+FLAGS', '\\Seen')
                        yield email

    def get_attachments(self):
        att_number = 0
        for email in self.new_emails:
            for email_section in email.walk():
                if email_section.get_content_disposition() == 'attachment' or email_section.get_content_type() == 'application/pdf':
                    att_number += 1
                    raw_filename = email_section.get_filename()
                    filename = safe_attachment_filename(raw_filename)
                    filebytes = email_section.get_payload(decode=True)
                    yield Attachment(filename, filebytes)
        print(f'[*] Attachments found: {att_number}')

    def refresh(self):
        self.new_emails = list(self.get_unread_messages())
        self.attachments_found = list(self.get_attachments())


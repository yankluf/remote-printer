import os
import time
from inbox.connect import InboxConnection

class PrintingService():
    def __init__(self):
        self.inbox_connection = InboxConnection()
        self.print_attachments_found()

    def print_attachments_found(self):
        attachments = self.inbox_connection.attachments_found
        if len(attachments) != 0:
            print(f'\nReady to print {len(attachments)} attachment(s)...')
            for attachment in attachments:
                attachment.save_file()
                os.system(f'lp "{attachment.path}"') #This could be handled with python-cups
                attachment.delete_file()

    def loop(self):
        while True:
            time.sleep(30)
            self.inbox_connection.refresh()
            self.print_attachments_found()


if __name__ == '__main__':
    print('============================')
    print('REMOTE PRINTING SERVICE V1.0')
    print('============================')
    ps = PrintingService()
    ps.loop()
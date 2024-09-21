import os
from dotenv import load_dotenv

class Credentials():
    def __init__(self):
        load_dotenv()
        self.server = os.getenv('EMAIL_SERVER')
        self.address = os.getenv('EMAIL_ADDRESS')
        self.password = os.getenv('EMAIL_PASSWORD')
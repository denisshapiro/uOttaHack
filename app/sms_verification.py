from twilio.rest import Client
from .config import TWILIO_SID, TWILIO_TOKEN

class SMS:
    def __init__ (self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    

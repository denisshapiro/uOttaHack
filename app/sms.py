from twilio.rest import Client
from .config import TWILIO_SID, TWILIO_TOKEN

class SMS:
    def __init__ (self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send(self, user):
        car = user.car
        message = self.client.messages \
                        .create(
                             body=f"Car Model: {car.model}\nCar Year: {car.year}\nCar Colour: {car.colour}",
                             from_='+13437006148',
                             to='+16136179842'
                         )
        print(message)

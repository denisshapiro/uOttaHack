# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC46cafcbc424716216c5b045274df8bf1'
auth_token = '7cdaeba7037902b8a0f1e5a2c9a208c0'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13437006148',
                     to='+16136179842'
                 )

print(message.sid)
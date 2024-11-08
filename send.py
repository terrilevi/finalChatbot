import twilio

from twilio.rest import Client

account_sid = 'xxx'  # Identifies your Twilio account
auth_token = 'xxx'     # Secret key for authentication

# Initialize client
client = Client(account_sid, auth_token)

# Send message
message = client.messages.create(
    from_='whatsapp:+14155238886',  # Twilio sandbox number
    body='Hola, buenos dias',              # Your simple message
    to='whatsapp:+51947533008'       # Recipient's number with country code
)

print(message.sid)

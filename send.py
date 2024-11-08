import twilio

from twilio.rest import Client

account_sid = 'ACe3f2f5a5a421a8e8d3ddccf451d36f68'  # Identifies your Twilio account
auth_token = 'e831805998cd8e478a5e708a7958881f'     # Secret key for authentication

# Initialize client
client = Client(account_sid, auth_token)

# Send message
message = client.messages.create(
    from_='whatsapp:+14155238886',  # Twilio sandbox number
    body='bbita',              # Your simple message
    to='whatsapp:+51947533008'       # Recipient's number with country code
)

print(message.sid)
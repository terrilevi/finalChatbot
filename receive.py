from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Your Twilio credentials

account_sid = 'ACe3f2f5a5a421a8e8d3ddccf451d36f68'  
auth_token = 'e831805998cd8e478a5e708a7958881f'   
client = Client(account_sid, auth_token)

@app.route("/webhook", methods=['POST'])
def webhook():
    # Get the message content
    incoming_msg = request.values.get('Body', '').lower()
    # Get the sender's WhatsApp number
    sender = request.values.get('From', '')
    
    print(f"Received message: {incoming_msg} from {sender}", flush=True)
    
    # Create a response (optional)
    resp = MessagingResponse()
    resp.message(f"I received your message: {incoming_msg}")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
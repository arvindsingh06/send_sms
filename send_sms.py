from twilio.rest import Client

# Your Twilio account credentials
account_sid = 'twilio ssid'       # Replace with your actual Account SID
auth_token = 'twilio token'         # Replace with your actual Auth Token

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body='Hello Arvind! how are you 🚀',
    from_='+190000',  # ✅ Your Twilio number (USA-based)
    to='+9170000000'     # ✅ Your verified number (India-based)
)

print("✅ Message sent successfully!")
print("🆔 Message SID:", message.sid)

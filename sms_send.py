from twilio.rest import Client


def send_sms(message, phone):
    """Send SMS message to user with message."""
    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="+YOUR_TWILIO_NUMBER",
        to=f"{phone}"
    )

import firebase_admin
from firebase_admin import credentials, messaging

def send_push_notification(token, title, message, payload=None):
    if token :
        notification = messaging.Notification(
            title=title,
            body=message,
        )
        message = messaging.Message(
            notification=notification,
            token=token,
            data=payload,  # add the payload to the message object
        )
        try:
            response = messaging.send(message)
            print('Successfully sent message:', response)
        except Exception as e:
            print('Failed to send message:', e)
            pass
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
        response = messaging.send(message)
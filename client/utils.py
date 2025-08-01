# client/utils.py
import base64

def encode_message(message):
    return base64.urlsafe_b64encode(message.encode()).decode().rstrip('=')

def decode_message(encoded):
    padded = encoded + '=' * (-len(encoded) % 4)
    return base64.urlsafe_b64decode(padded.encode()).decode()

from twilio.rest import TwilioRestClient
import os
from sqlalchemy import func


def send_unsafe_text(user_id):

    # get users friend info and send the text that user is feeling unsafe
    # along with their geolocation 
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    sender = os.environ["SENDER"]

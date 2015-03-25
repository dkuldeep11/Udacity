# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe46626bc279be3719cf0cb9d9451abf3"
auth_token  = "17f856c9e59ccfa43c0a13cf71c073c2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Yo this is my 1st text from Python code!",
    to="+16073720119",    # Replace with your phone number
    from_="+19192298260") # Replace with your Twilio number
print message.sid
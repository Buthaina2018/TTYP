from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "Hi, let's connect: linkedin.com/in/bethhdc/ I'm also tweeting at twitter.com/bethahdc3"

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)

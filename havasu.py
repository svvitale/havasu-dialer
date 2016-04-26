import os
import time

import django_shim
import sys
from twilio.rest import TwilioRestClient

# put your own credentials here
from havasu.models import Call
from havasu.views import TwilioView

ACCOUNT_SID = os.environ.get('TWILIO_SID')
AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def start_call(dest):
    return client.calls.create(
        to=dest,
        from_="+14054096241",
        url='https://havasu.herokuapp.com/twilio/',
        method="GET",
        fallback_method="GET",
        status_callback='https://havasu.herokuapp.com/twilio/',
        status_callback_method="POST",
        record="false"
    )

numbers_to_call = [
    '+19284482141',
    '+19284482121',
    '+19284482174',
    '+19284482180'
]

# Drop all prior call statuses
Call.objects.all().delete()

while not Call.objects.filter(status=TwilioView.SUCCESS_STATUS).exists():

    for number in numbers_to_call:

        if not Call.objects.filter(number=number, in_progress=True).exists():
            print("Calling %s" % (number,))
            call_id = start_call(number)
            Call.objects.create(number=number,
                                call_id=call_id.sid,
                                status='queued',
                                in_progress=True)

    time.sleep(1)

print("Call succeeded on %s, exiting" % (Call.objects.get(status=TwilioView.SUCCESS_STATUS).number,))

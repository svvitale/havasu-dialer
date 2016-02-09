from django.http import HttpResponse
from django.views.generic import View

from havasu.models import Call


class TwilioView(View):

    CALL_IN_PROGRESS_STATUS = [
        'queued',
        'ringing',
        'in-progress'
    ]

    CALL_COMPLETED_STATUS = [
        'busy',
        'failed',
        'no-answer',
        'canceled'
    ]

    SUCCESS_STATUS = 'completed'

    def get(self, request):
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hi! We are going to connect you to... Kate Vitale</Say>
    <Dial>+17202886336</Dial>
</Response>"""
        return HttpResponse(response, content_type='text/xml')

    def post(self, request):

        print("Call to %s is %s" % (request.POST['To'], request.POST['CallStatus']))
        call = Call.objects.get(call_id=request.POST['CallSid'])
        call.status = request.POST['CallStatus']
        call.in_progress = call.status in TwilioView.CALL_IN_PROGRESS_STATUS
        call.save()

        return HttpResponse()

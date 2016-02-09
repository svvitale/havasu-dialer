from django.http import HttpResponse
from django.views.generic import View


class TwilioView(View):
    def get(self, request):
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hi! We are going to connect you to... Kate Vitale</Say>
    <Dial>+17202886336</Dial>
</Response>"""
        return HttpResponse(response, content_type='text/xml')

    def post(self, request):
        for key, val in request.POST.items():
            print('%s = %s' % (key, val))
        return HttpResponse()

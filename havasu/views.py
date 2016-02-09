from django.http import HttpResponse
from django.views.generic import View


class TwilioView(View):
    def get(self, request):
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hi! We are going to connect you to... Kate Vitale</Say>
    <Dial>+13038425418</Dial>
</Response>"""
        return HttpResponse(response, content_type='text/xml')

    def post(self, request):
        print(request.body)
        return HttpResponse()

from django.http import HttpResponse
from django.views.generic import View


class TwilioView(View):
    def get(self, request):
        return HttpResponse("working")

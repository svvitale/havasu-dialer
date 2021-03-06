from django.db import models


class Call(models.Model):
    call_id = models.CharField("call ID generated by twilio", max_length=64)
    status = models.CharField("call status", max_length=32)
    number = models.CharField("phone number called", max_length=15)
    in_progress = models.BooleanField(default=True)

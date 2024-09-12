from django.shortcuts import render

from attempt.models import Attempt
from mailing.models import Mailing


def attempt_list(request):
    mailings = Mailing.objects.all()
    mailing_id = request.GET.get("mailing")
    if mailing_id:
        attempts = Attempt.objects.filter(mailing_id=mailing_id)
    else:
        attempts = Attempt.objects.all()
    context = {
        "object_list": attempts,
        "mailings": mailings,
    }
    return render(request, "attempt/attempt_list.html", context)


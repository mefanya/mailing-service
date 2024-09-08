from django.shortcuts import render

from attempt.models import Attempt


def attempt_list(request):
    context = {
        "object_list": Attempt.objects.all(),
    }
    return render(request, "index.html", context)

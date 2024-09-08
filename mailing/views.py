from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ("send_at", "frequency", "periodicity", "status")
    success_url = reverse_lazy("mailing:list")


class MailingUpdateView(UpdateView):
    fields = ("send_at", "frequency", "periodicity", "status")
    success_url = reverse_lazy("mailing:list")


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:list")

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from message.models import Message


class MessageListView(ListView):
    model = Message


class MailingDetailView(DetailView):
    model = Message


class MailingCreateView(CreateView):
    model = Message
    fields = ("subject", "textbox")
    success_url = reverse_lazy("message:message_list")


class MailingUpdateView(UpdateView):
    model = Message
    fields = ("subject", "textbox")
    success_url = reverse_lazy("message:message_list")


class MailingDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("message:message_list")

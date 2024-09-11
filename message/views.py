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


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ("subject", "textbox")
    success_url = reverse_lazy("message:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("subject", "textbox")
    success_url = reverse_lazy("message:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("message:message_list")

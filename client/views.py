from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ("last_name", "first_name", "middle_name", "email", "comment")
    success_url = reverse_lazy("client:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("last_name", "first_name", "middle_name", "email", "comment")
    success_url = reverse_lazy("client:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("client:client_list")

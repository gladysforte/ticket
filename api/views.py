from django.shortcuts import render
from rest_framework import viewsets
from .models import (Accounts, User_Type, Tickets,
                     Tickets_Form, Status, Classification)
from .serializers import (AccountsSerializer, UserTypeSerializer,
                          TicketSerializer, TicketsFormSerializer,
                          StatusSerializer, ClassificationSerializer)

# Create your views here.


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = User_Type.objects.all()
    serializer_class = UserTypeSerializer


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer


class TicketFormViewSet(viewsets.ModelViewSet):
    queryset = Tickets_Form.objects.all()
    serializer_class = TicketsFormSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer

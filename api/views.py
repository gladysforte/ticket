from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (Account, UserType, Ticket,
                     TicketForm, Status, Classification)
from .serializers import (AccountsSerializer, UserTypeSerializer,
                          TicketSerializer, TicketsFormSerializer,
                          StatusSerializer, ClassificationSerializer)

# Create your views here.


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        queryset = Ticket.objects.filter(status=2)
        page = self.paginate_queryset(self.filter_queryset(queryset))

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class TicketsViewSet1(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('customer_email')
    serializer_class = TicketSerializer


class TicketFormViewSet(viewsets.ModelViewSet):
    queryset = TicketForm.objects.all()
    serializer_class = TicketsFormSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer

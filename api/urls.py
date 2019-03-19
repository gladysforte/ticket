from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AccountsViewSet, UserTypeViewSet, TicketsViewSet,
                    TicketFormViewSet, StatusViewSet, ClassificationViewSet,
                    TicketsViewSet1)


router = DefaultRouter()
router.register(r'user_type', UserTypeViewSet, basename="user_type")
router.register(r'accounts', AccountsViewSet, basename="accounts")
router.register(r'ticketform', TicketFormViewSet, basename="ticketform")
router.register(r'classification', ClassificationViewSet,
                basename="classification")
router.register(r'status', StatusViewSet, basename="status")
router.register(r'tickets', TicketsViewSet, basename="tickets")
router.register(r'tickets1', TicketsViewSet1, basename="tickets1")


urlpatterns = [
    path('', include(router.urls)),
]

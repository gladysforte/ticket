from rest_framework import serializers
from .models import (Status, Ticket, TicketForm, Classification,
                     Account, UserType)
from .utils import unique_id_generator
from django.contrib.auth.hashers import make_password


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = (
            'id',
            'name',
            'code',
            'description',
            'created_at',
            'updated_at',
            'deleted_at'
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'user_type',
            'image',
            'username',
            'password',
            'created_at',
            'updated_at',
            'deleted_at'
        )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        accounts = Account.objects.create(password=password, **validated_data)
        accounts.save()
        return accounts


class TicketsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketForm
        fields = (
            'id',
            'first_name',
            'last_name',
            'designation',
            'phone_no',
            'email',
            'address',
            'company_name',
            'model_no',
            'serial_no'
        )


class TicketSerializer(serializers.ModelSerializer):
    tickets = serializers.SerializerMethodField()
    # assist = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = (
            'id',
            'ref_no',
            'customer_email',
            'status',
            'assist_by',
            'remarks',
            'resolution',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'tickets_form',
            'tickets',
            # 'assist',
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

    def get_tickets(self, obj):
        tickets = TicketForm.objects.get(
            id=obj.tickets_form_id
        )
        serializer = TicketsFormSerializer(tickets)
        return serializer.data

    # def get_assist(self, obj):
    #     assist = Accounts.objects.get(
    #         id=obj.assist_by_id
    #     )
    #     serializer = AccountsSerializer(assist)
    #     return serializer.data

    def create(self, validated_data):
        tickets = Ticket.objects.create(**validated_data)
        tickets.ref_no = unique_id_generator(tickets.id)
        tickets.save()
        return tickets


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'id',
            'name',
            'code',
            'classification',
            'description',
            'created_at',
            'updated_at',
            'deleted_at'
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = (
            'id',
            'name',
            'code',
            'description',
            'created_at',
            'updated_at',
            'deleted_at'
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

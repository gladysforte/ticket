from rest_framework import serializers
from .models import (Status, Tickets, Tickets_Form, Classification,
                     Accounts, User_Type)
from .utils import unique_id_generator
from django.contrib.auth.hashers import make_password


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Type
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
        model = Accounts

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
        # extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        accounts = Accounts.objects.create(password=password, **validated_data)
        accounts.save()
        return accounts


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets
        fields = (
            'id',
            'ref_no',
            'customer_email',
            'status',
            'tickets_form',
            'assist_by',
            'remarks',
            'resolution',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at'
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

    def create(self, validated_data):
        tickets = Tickets.objects.create(**validated_data)
        tickets.ref_no = unique_id_generator(tickets.id)
        tickets.save()
        return tickets


class TicketsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets_Form
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

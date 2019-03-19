from django.db import models
from django.utils import timezone
# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=20, unique=True)
# name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_types'


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    image = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'accounts'


class TicketForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    company_name = models.CharField(max_length=50)
    model_no = models.CharField(max_length=50)
    serial_no = models.CharField(max_length=50)

    class Meta:
        db_table = 'ticket_forms'

    def __str__(self):
        return self.first_name


class Classification(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classifications'


class Status(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    classification = models.ForeignKey(Classification,
                                       on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'


class Ticket(models.Model):
    ref_no = models.CharField(max_length=50,
                              editable=False)
    customer_email = models.EmailField()
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    tickets_form = models.ForeignKey(TicketForm, on_delete=models.DO_NOTHING)
    assist_by = models.ForeignKey(Account,
                                  on_delete=models.DO_NOTHING)
    remarks = models.CharField(max_length=50, null=True, blank=True)
    resolution = models.CharField(max_length=250, null=True, blank=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tickets'

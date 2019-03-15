from django.db import models
from django.utils import timezone
# Create your models here.


class User_Type(models.Model):
    name = models.CharField(max_length=20, unique=True)
# name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_type'


class Accounts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(User_Type, on_delete=models.DO_NOTHING)
    image = models.ImageField()
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


class Tickets_Form(models.Model):
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
        db_table = 'tickets_form'

    def __str__(self):
        return self.first_name


class Classification(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classification'


class Status(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    classification = models.ForeignKey(Classification,
                                       on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=250)
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


class Tickets(models.Model):
    ref_no = models.CharField(max_length=50,
                              editable=False)
    customer_email = models.EmailField()
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    tickets_form = models.ForeignKey(Tickets_Form, on_delete=models.DO_NOTHING)
    assist_by = models.ForeignKey(Accounts,
                                  on_delete=models.DO_NOTHING)
    remarks = models.CharField(max_length=50)
    resolution = models.CharField(max_length=250)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tickets'

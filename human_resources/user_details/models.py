from django.utils import timezone

from django.core.validators import MinLengthValidator
from django.db import models
import uuid
from django.contrib.auth import get_user_model

from inventory.branches.models import Branch
from locations.addresses.models import Location


# Create your models here.


class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="phone_numbers")
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.user.first_name + ", " + self.phone_number


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=True)


class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, user__is_active=True)


class UserDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, related_name="user_details")
    national_id = models.CharField(null=True, max_length=14, unique=True, validators=[MinLengthValidator(14)])
    start_work_date = models.DateField(null=True)
    end_work_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    birthdate = models.DateField(null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    home_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    branch = models.ManyToManyField(Branch)
    created_at = models.DateField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    active = UserManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.user.is_active = False
        self.save()

    def __str__(self):
        return self.role.name + '---' + self.user.get_short_name()

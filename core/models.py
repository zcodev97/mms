import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=255, unique=True)
    # userType= models.ForeignKey(UserType,on_delete=models.PROTECT)


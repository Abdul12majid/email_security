from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_esp = models.BooleanField(default=False)
    has_priority_support = models.BooleanField(default=False)
    subscribed_to_cert_bundle = models.BooleanField(default=False)
    subscription_expiry = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username



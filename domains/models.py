from django.db import models
from django.conf import settings

class Domain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    last_checked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.domain_name

class DNSRecordStatus(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='dns_records')
    record_type = models.CharField(max_length=10)
    value = models.TextField()
    is_valid = models.BooleanField(default=False)
    checked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain.domain_name} - {self.record_type}"

import uuid
from django.db import models
from django.conf import settings


class Container(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InvoiceType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# Create your models here.
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_id = models.CharField(max_length=10, unique=True, editable=False)
    container = models.ForeignKey(Container,on_delete=models.CASCADE)
    company_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_type = models.ForeignKey(InvoiceType, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    mr = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    price_in_dinar = models.FloatField()
    price_in_dollar = models.FloatField()
    description = models.TextField(max_length=2000)
    accounter = models.CharField(max_length=255)
    receiver =  models.CharField(max_length=255)

    def __str__(self):
        return self.invoice_id

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            # Generate a short and secure invoice ID
            self.invoice_id = self.generate_invoice_id()
        super().save(*args, **kwargs)

    def generate_invoice_id(self):
        # Customize the prefix or length as needed
        prefix = "INV"
        unique_id = str(uuid.uuid4().int)[:6]  # Extract 6 characters from the UUID
        return f"{prefix}-{unique_id}"

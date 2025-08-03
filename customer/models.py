from django.db import models
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True)
    customer_phone = models.CharField(max_length=15, unique=True)
    customer_address = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when customer was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update
    def __str__(self):
        return f"{self.customer_name}"


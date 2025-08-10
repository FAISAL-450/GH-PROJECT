from django.db import models
class RoleOverride(models.Model):
    email = models.EmailField(unique=True)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} → {self.group_name}"




from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom user model that extends the built-in abstract user model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        # Set the related name for groups and user_permissions to avoid conflicts
        permissions = [
            # Define custom permissions here if needed
        ]
        # Override default related names to avoid clashes
        verbose_name = "custom user"
        verbose_name_plural = "custom users"
        # Ensure related_name for groups and user_permissions don't conflict
        permissions = [
            ('view_customuser', 'Can view custom user'),
        ]
        default_related_name = 'custom_user'

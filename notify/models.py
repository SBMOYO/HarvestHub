from django.db import models

class WhatsAppUser(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    profile_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

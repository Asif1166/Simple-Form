from django.db import models

class UserManagment(models.Model):
    email = models.EmailField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email

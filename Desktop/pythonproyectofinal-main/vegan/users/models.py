from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    social_media = models.URLField(max_length=300, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)               
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'
    
    def __str__(self):
        return f"{self.user} - {self.avatar}"

    







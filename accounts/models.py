from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=15, blank=True ,null=True, default='')
    description = models.TextField(max_length=500, blank=True ,null=True, default='')
    userphoto   = models.ImageField(upload_to='userImage/', blank=True ,null=True)
    def __str__(self):
        return str(self.user)

##### Create User Profile By Signals ######

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
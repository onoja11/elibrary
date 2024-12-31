from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save#allows us to automaticallly create a new profile when user signsup
class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        status=models.CharField(max_length=50, default="non- library staff")
        phone_number=models.CharField(max_length=11, blank=True)
        def __str__(self):
            return self.user.username
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
#automte it
post_save.connect(create_profile, sender=User)

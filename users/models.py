from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    userType = models.IntegerField(default=3)


    def __unicode__(self):
        return self.user.username

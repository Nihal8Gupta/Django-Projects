from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=300,blank=True)
    pic = models.ImageField(upload_to='user_pic')
    def __str__(self) :
        return self.user.username
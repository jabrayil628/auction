from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(models.Model):
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    budget=models.IntegerField(default=0)
    user=models.OneToOneField(
        User, related_name='my_user',
        on_delete=models.CASCADE,default=''
    )
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Message(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=255)
    content=models.TextField()
    # message_date=models.DateTimeField(auto_now=True,default='')

    def __str__(self):
        return self.name



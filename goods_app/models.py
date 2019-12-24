from django.db import models
from user_app.models import MyUser
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Goods(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo = models.ImageField(upload_to='photos', blank=True)
    description=models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name='Goods'
        verbose_name_plural='Goods'

    def __str__(self):
        return self.name



    
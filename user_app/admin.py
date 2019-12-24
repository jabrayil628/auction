from django.contrib import admin
from .models import MyUser,Message
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Message)
from django.contrib.auth.models import User
from django import forms
from .models import MyUser,Message
from goods_app.models import Goods

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
class Myloginform(AuthenticationForm):
    username=forms.CharField(
                    max_length=50,
                    widget=forms.TextInput(attrs={
                                            "placeholder":"Username",
                                            'class':'form-control'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={
        "placeholder":"Password",
           'class':'form-control'}))

class UserCreateForm(UserCreationForm):

    username = forms.CharField(
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"Username"})
    )
    password1 = forms.CharField(
        help_text='',
        widget=forms.PasswordInput(attrs={"placeholder":"Password",'class':'form-control'})
    )
    password2 = forms.CharField(
        help_text='',
        widget=forms.PasswordInput(attrs={"placeholder":"Repeat Password",'class':'form-control'})
    )


class MyUserForm(forms.ModelForm):
    # name = forms.CharField(
    #     label='',
    #     help_text='',
    #     widget=forms.TextInput(attrs={"placeholder":"Name",'class':'form-control'})
    # )
    # surname = forms.CharField(
    #     label='',
    #     help_text='',
    #     widget=forms.TextInput(attrs={"placeholder":"Surname",'class':'form-control'})
    # )
    
    phone = forms.CharField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"Phone number",'class':'form-control'})
    )
    email = forms.EmailField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"Email",'class':'form-control'})
    )
    class Meta:
        model = MyUser
        fields = ('address','phone','email')

class MyGoodsForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"Good name",'class':'form-control'})
    )
    price = forms.IntegerField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"price",'class':'form-control'})
    )
    auctionDeadLine = forms.DateTimeField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={'class':'form-control','type':'date'})
    )

    description = forms.CharField(
        label='',
        help_text='',
        widget=forms.TextInput(attrs={"placeholder":"Description",'class':'form-control'})
    )
    class Meta:
        model = Goods
        fields = '__all__'
    # description=models.CharField(max_length=255)
    # owner=models.ForeignKey(User,on_delete=models.CASCADE)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
    )


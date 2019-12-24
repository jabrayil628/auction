from django import forms
from .models import Goods
class GoodsUploadForm(forms.ModelForm):
    class Meta:
        model=Goods
        fields=['name','price','photo','description']
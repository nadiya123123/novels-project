from django import forms
from .models import new

class novelform(forms.ModelForm):
    class Meta:
        model=new
        fields=['name','year','desc','img']
from django import forms
from .models import *
class SForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['message','audio']
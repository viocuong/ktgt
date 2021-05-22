from django import forms
from .models import *
class SForm(forms.ModelForm):
    CHOICES = (('wavsteg','wavsteg'),('mp3stego','mp3stego'))
    tool = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = File
        fields = ['message','audio']
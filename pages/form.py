from django import forms
from .models import *

class imageform(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['Name','Image']

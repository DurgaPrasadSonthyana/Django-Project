from django import forms
from .models import ResumeBuilder

class CreateResume(forms.ModelForm):
    class Meta:
        model = ResumeBuilder
        fields = ['name','title','email','address','number','linkedin']  # Include other fields as necessary

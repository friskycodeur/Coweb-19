from django import forms
from django.core import validators
class FormName(forms.Form):
  name=forms.CharField()
  aadhar=forms.CharField(max_length=16)
  email=forms.EmailField()
  city=forms.CharField(max_length=64)
  date=forms.DateField()
  reason=forms.CharField(widget=forms.Textarea)
  botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

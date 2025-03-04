from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
  return render(request,'basicapp/index.html')

def advisory(request):
  return render(request,'basicapp/advisory.html')

def docbot(request):
  return render(request,'basicapp/docbot.html')

def tracker(request):
  return render(request,'basicapp/tracker.html')

def form_name_view(request):
  form=forms.FormName()
  if request.method=='POST':
    form=forms.FormName(request.POST)
    if form.is_valid():
      print("Validation Success!")
      print("Name : "+form.cleaned_data['name'])
      print("Email : "+form.cleaned_data['email'])
      print("Text : "+form.cleaned_data['text'])
  return render(request,'basicapp/form_page.html',{'form':form})
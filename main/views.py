from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from .forms import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
# Create your views here.

def home(request):
    os.system("cd static_cdn && touch ttt.cpp")
    return HttpResponse(BASE_DIR)    
def index(request):
    if request.method == 'POST':
        form = SForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            file = File()
            file.set_data(data['message'],request.FILES['audio'])
            file.save()
        return render(request,'app/result.html',{
            'file_name':'cafe2.jpg'
        })
    form = SForm()
    return render(request,'app/home.html',{'form':form})
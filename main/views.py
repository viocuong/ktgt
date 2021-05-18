from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
# Create your views here.
def home(request):
    os.system("cd static_cdn && touch ttt.cpp")
    return HttpResponse(BASE_DIR)    

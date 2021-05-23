from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from .forms import *
import subprocess
import time
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

def home(request):
    os.system("cd static_cdn && touch ttt.cpp")
    return HttpResponse(BASE_DIR)    
def index(request):
    if request.method == 'POST':
        output = tool = message = fileName = url = password= sulfix=''
        file = File()
        form = SForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            file.set_data(data['message'],request.FILES['audio'])
            file.save()
            fileName = file.audio.name.split('.')[0] #file_name
            tool = data['tool']
            message = data['message']
            f = open("media/message.txt", "a")
            f.write(message)
            f.close()
            if tool == 'wavsteg':
                sulfix = '_wavsteg.wav'
                # os.system("/home/cuongnv/project/ktgt/ktgt_env/bin/python3")
                # os.system('export PYTHONPATH="/home/cuongnv/project/ktgt/ktgt_env/bin/python3"')
                # os.system('which python')
                # os.system('which python3')
                # os.system('/home/cuongnv/project/ktgt/ktgt_env/bin/stegolsb --help')
                # os.system("source ~/project/ktgt/ktgt_env/bin/activate")
                os.system(f"/home/cuongnv/project/ktgt/ktgt_env/bin/stegolsb wavsteg -h -i /home/cuongnv/project/ktgt/media/{fileName}.wav  -s /home/cuongnv/project/ktgt/media/message.txt -o /home/cuongnv/project/ktgt/media/{fileName}_wavsteg.wav -n 1")
                # output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
                url = f'/media/{fileName}_wavsteg.wav' 
            elif tool == 'mp3stego':
                sulfix = '_stego.mp3'
                os.system("id")
                password = request.POST['password']
                cmd = f"wine media/mp3stego/MP3Stego/encode -E /home/cuongnv/project/ktgt/media/message.txt -P {password} /home/cuongnv/project/ktgt/media/{fileName}.wav /home/cuongnv/project/ktgt/media/{fileName}_mp3stego.mp3"
                # subprocess.Popen("sudo -S", shell=True, stdout=subprocess.PIPE)
                # subprocess.Popen("280299", shell=True, stdout=subprocess.PIPE)
                subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                
                url = f"/media/{fileName}_mp3stego.mp3"
                # if "ERROR" in o:
                #     return HttpResponse("File không đúng định dạng")
            f = open("media/message.txt", "r+")
            f.seek(0)
            f.truncate()
            f.close() 
        return render(request,'app/result.html',{
            'output':output,
            'tool_name':tool,
            'file_name':fileName +sulfix,
            'url':url
        })
    form = SForm()
    return render(request,'app/home.html',{'form':form})
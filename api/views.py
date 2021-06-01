from api.models import Music, Singer
from os import error
from api.serializers import MusicSerializer, RegisterSerializer, SingerSerializer
from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse
def singer(request):
    id = request.GET['id']
    singer = Singer.objects.filter(pk=id)[0]
    return HttpResponse(singer.name)

class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            person = serializer.save()
            data['response']=['success']
        else: 
            data = serializer.errors
        return Response(data)
class Musics(APIView):
    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer(music,many=True)
    
        return Response(serializer.data)
class Singers(APIView):
    def get(self, request):
        singers = Singer.objects.all()
        serializers = SingerSerializer(singers,many=True)
        return Response(serializers.data)
        
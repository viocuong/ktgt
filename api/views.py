from django.db.models import manager
from api.models import Music, Singer
from os import error
from api.serializers import FavouriteSerialize, MusicSerializer, RegisterSerializer, SingerSerializer
from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse, response
def search(request):
    key = request.GET['key']
    musics = Music.objects.filter(name__contains=key)
    serializers = MusicSerializer(musics, many=True)
    return Response(serializers.data)
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
class MusicBySinger(APIView):
    def get(self, request):
        singer = request.data
        # print(f"{singer}")
        # print(type(singer))
        musics = Music.objects.filter(singer__name__exact=singer)
        print(musics)
        serializers = MusicSerializer(musics, many=True)
        return Response(serializers.data)
    def post(self, request):
        singer = request.data['name']
        musics = Music.objects.filter(singer__name__exact=singer)
        serializers = MusicSerializer(musics, many=True)
        return Response(serializers.data)
class Search(APIView):
    def get(self, request):
        key = request.GET['key']
        musics = Music.objects.filter(name__contains=key)
        serializers = MusicSerializer(musics, many=True)
        return Response(serializers.data)
        
    def post(self, request):
        key = request.data['key']
        musics = Music.objects.filter(name__contains=key)
        serializers = MusicSerializer(musics, many=True)
        return Response(serializers.data)
class View(APIView):
    def post(self, request):
        musicName = request.data['name']
        musics = Music.objects.filter(name__contains=musicName)[0]
        old_view = musics.view
        musics.view = old_view+1
        musics.save()
        response = {
            "resonse":musics.view
        }
        return Response(response)
class RankByView(APIView):
    def get(self, request):
        musics = Music.objects.order_by('-view')
        musicSerializes = MusicSerializer(musics, many=True)
        return Response(musicSerializes.data)
class Favourite(APIView):
    def post(self, request):
        person = request.data['person_uid']
        music = request.data['music_name']
        res = {"reponse":"đã thích"}
        q = Favourite.objects.filter(person__name__exact=person, music__name_exact=music)
        if q.count()==0:
            music = Musics.objects.filter(uid=person)[0]
            fav_old = music.num_favourite
            music.num_favourite = fav_old+1
            music.save()
            serializers = FavouriteSerialize(data=request.data)
            serializers.save()
        return Response(res)





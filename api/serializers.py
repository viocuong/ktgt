from django.db.models import fields
from api.models import Category, Favourite, Music, Person, Singer
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['uid', 'name', 'photo_url', 'email', 'password']
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['singer_name','singer_url','singer_dob','category_name','name','file_url','img_url','view','num_favourite']
class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['name','img_url','dob']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
class FavouriteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['person_uid','music_name']


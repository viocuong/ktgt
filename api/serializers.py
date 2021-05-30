from django.db.models import fields
from api.models import Category, Music, Person, Singer
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['uid', 'name', 'photo_url', 'email', 'password']
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['singer_name','category_name','name','file_url','img_url']
class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['name','url','dob']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

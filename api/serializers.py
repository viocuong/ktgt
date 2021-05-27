from api.models import Person
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['uid', 'name', 'photo_url', 'email', 'password']

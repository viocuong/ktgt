from django.db import models
from django.db.models.fields import CharField
class Person(models.Model):
    uid = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50,default='')
    def __str__(self):
        return f"{self.name} {self.uid} | {self.photo_url} "
class Music(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()
    img = models.FileField()
    def  __str__(self):
        return f"{self.name} | {self.file.url} | {self.img.url}"

class Singer(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField()
    dob = CharField(max_length=30, default='')
    def __str__(self):
        return f"{self.name} | {self.img.url} | {self.dob}"


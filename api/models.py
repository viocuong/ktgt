from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields import CharField
HOST = 'cackythuatgiautinn5.xyz:8001'
class Singer(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField()
    dob = CharField(max_length=30, default='')
    def __str__(self):
        return f"{self.name} | {self.img.url} | {self.dob}"
    @property
    def img_url(self):
        return f"{HOST}/media/{self.img}"
class Category(models.Model):
    name = models.CharField(default="Nhạc trẻ",max_length=30)
class Music(models.Model):
    singer = models.ForeignKey(Singer,on_delete=CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=CASCADE,null=True)
    name = models.CharField(max_length=100)
    file = models.FileField()
    img = models.FileField()
    def  __str__(self):
        return f"{self.name} | {self.file.url} | {self.img.url}"
    @property
    def singer_name(self):
        return self.singer.name
    @property
    def category_name(self):
        return self.category.name
    @property
    def file_url(self):
        return f"{HOST}/media/{self.file}"
    @property
    def img_url(self):
        return f"{HOST}/media/{self.img}"
    @property
    def singer_url(self):
        url = self.singer.img
        return f"{HOST}/media/{url}"
    @property
    def singer_dob(self):
        return self.singer.dob
class Person(models.Model):
    uid = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50,default='')
    def __str__(self):
        return f"{self.name} {self.uid} | {self.photo_url} "
class Comment(models.Model):
    content = models.CharField(max_length=100)
    person = models.ForeignKey(Person,on_delete=CASCADE)
    music = models.ForeignKey(Music,on_delete=CASCADE)
class Favourite(models.Model):
    person = models.ForeignKey(Person,on_delete=CASCADE)
    music = models.ForeignKey(Music,on_delete=CASCADE)
    num = models.IntegerField(default=0)
class Follow(models.Model):
    person = models.ForeignKey(Person,on_delete=CASCADE)
    singer = models.ForeignKey(Singer,on_delete=CASCADE)


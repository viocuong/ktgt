from django.db import models

# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    urli = models.CharField(max_length=200)
    audio = models.FileField()
    def set_data(self, m, a):
        self.message = m
        self.audio = a
    def __str__(self):
        return f"{self.message} {self.urli}"
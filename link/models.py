from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    amazon=models.URLField(max_length=200,default="", blank=True)
    airbnb=models.URLField(max_length=200,default="", blank=True)
    blog=models.URLField(max_length=200,default="", blank=True)
    book=models.URLField(max_length=200,default="", blank=True)
    cloud=models.URLField(max_length=200,default="", blank=True)
    codepen=models.URLField(max_length=200,default="", blank=True)
    discord=models.URLField(max_length=200,default="", blank=True)
    email=models.URLField(max_length=200,default="", blank=True)
    facebook=models.URLField(max_length=200,default="", blank=True)
    github=models.URLField(max_length=200,default="", blank=True)
    google_drive=models.URLField(max_length=200,default="", blank=True)
    google_play=models.URLField(max_length=200,default="", blank=True)
    google_forms=models.URLField(max_length=200,default="", blank=True)
    hackerRank=models.URLField(max_length=200,default="", blank=True)
    instagram=models.URLField(max_length=200,default="", blank=True)
    linkedin=models.URLField(max_length=200,default="", blank=True)
    qr_code=models.URLField(max_length=200,default="", blank=True)
    quora=models.URLField(max_length=200,default="", blank=True)
    reddit=models.URLField(max_length=200,default="", blank=True)
    slideshare=models.URLField(max_length=200,default="", blank=True)
    snapchat=models.URLField(max_length=200,default="", blank=True)
    spotify=models.URLField(max_length=200,default="", blank=True)
    telegram=models.URLField(max_length=200,default="", blank=True)
    twitch=models.URLField(max_length=200,default="", blank=True)
    twitter=models.URLField(max_length=200,default="", blank=True)
    vimeo=models.URLField(max_length=200,default="", blank=True)
    whatsapp=models.URLField(max_length=200,default="", blank=True)
    website=models.URLField(max_length=200,default="", blank=True)
    youtube=models.URLField(max_length=200,default="", blank=True)
    owner=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
         return str(self.owner)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=3000, default="")

    def __str__(self):
        return self.name         
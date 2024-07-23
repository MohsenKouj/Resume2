from django.db import models

# Create your models here.
class api_us(models.Model):
    username=models.CharField(max_length=255)
    image=models.ImageField(max_length=255,upload_to="posts-img",default='posts-img/upic.png')
    password=models.CharField(max_length=255)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    tellNumber=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    location=models.TextField(max_length=500,null=True)
    birthday=models.DateField(max_length=100)
    about=models.TextField(default="",null=True)
    education=models.CharField(max_length=255,default="",null=True)
    langs=models.CharField(max_length=255,default="",null=True)
    t_p=models.IntegerField(default=0,null=True)
    cod_posti=models.CharField(max_length=255,default="",null=True)
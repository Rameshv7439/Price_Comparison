from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50)
class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile= models.CharField(max_length=20)
    status= models.CharField(max_length=20,null=True)
    con_password= models.CharField(max_length=50, null=True)

class Wish_List(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title= models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    status= models.CharField(max_length=100,null=True)

class Amazon_Wish(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title= models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    status= models.CharField(max_length=100,null=True)

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment = models.CharField(max_length=50, null=True)
    reply= models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)

class Wish_list_values(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title= models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    site = models.CharField(max_length=50, null=True)
    status= models.CharField(max_length=100,null=True)

class View_Wish_list_values(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title= models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True,max_length=500)
    site = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100, null=True)
    status= models.CharField(max_length=100,null=True)
    nam= models.CharField(max_length=100,null=True)

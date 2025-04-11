from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class contactclass(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    msg=models.CharField(max_length=400)
    def __str__(self):
        return self.firstname
class staticcontentclass(models.Model):
    key=models.CharField(max_length=10)
    #txt=models.TextField()
    txt=RichTextField()
    title=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.key
class categoryclass(models.Model):
    title=models.CharField(max_length=30)  
    img=models.ImageField(upload_to="photo")
    description=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title
class servicesclass(models.Model):
    title=models.CharField(max_length=100) 
    category=models.ForeignKey(categoryclass,on_delete=models.CASCADE)   
    description=models.TextField()
    def __str__(self):
        return self.title
class homepage(models.Model):
    img=models.ImageField(upload_to="photo")    
    text1=models.CharField(max_length=50)
    text2=models.CharField(max_length=50)
    text3=models.CharField(max_length=50)
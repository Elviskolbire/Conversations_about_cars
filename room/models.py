from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField (max_length=200, null =True)
    email = models.EmailField(unique=True)
    bio = models.TextField( null=True)
    # username = models.CharField(null= True, max_length=200)

    avatar = models.ImageField(null=True, default= "avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length= 250)
    
    def __str__(self):
        return self.name


class room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    paticipants = models.ManyToManyField(User, related_name= 'paticipants', blank=True) 
    name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField( auto_now= False, auto_now_add=True)
    updated = models.DateTimeField( auto_now= True, auto_now_add= False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created','-updated'] 

class Message(models.Model):
    Room = models.ForeignKey(room, on_delete= 
    models.CASCADE)
    user = models.ForeignKey(User, on_delete= 
    models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField( auto_now= False, auto_now_add=True)
    updated = models.DateTimeField( auto_now= True, auto_now_add= False)

    def __str__(self):
        return (self.body[0:50])

       
    
    


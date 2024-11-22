from django.contrib import admin
from  . models import room, Topic,Message,User

# Register your models here.
admin.site.register(room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)

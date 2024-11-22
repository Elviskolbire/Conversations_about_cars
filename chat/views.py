
from django.db.models import Q
from django.shortcuts import render
from  room.models import room, Topic, Message
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    q = request.GET.get('q',)

    if request.GET.get('q') != None :
        room_message = Message.objects.all().order_by("-created").filter(Q(Room__topic__name__icontains = q)) 
        Room = room.objects.filter(
        Q(topic__name__icontains= q) |
        Q(description__icontains=q) |
        Q(name__icontains= q))
        room_count =Room.count()

    else:
        Room = room.objects.all()
        room_count =Room.count()
        room_message = Message.objects.all().order_by("-created")
        
    topic = Topic.objects.all()[0:5]
    return render(request,'room/home.html', {'Room' :Room, 'topic': topic, 'room_count':room_count,'room_message' : room_message })

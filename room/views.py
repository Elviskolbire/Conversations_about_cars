from django.shortcuts import render,redirect,get_object_or_404
from . forms import userform
from . models import room,Message,Topic,User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
@login_required
def rooms(request,pk):
    ROOM = room.objects.get(id= pk) 
    room_messages = ROOM.message_set.all().order_by('-created')
    paticipants = ROOM.paticipants.all()
    if request.method == "POST":
        message = Message.objects.create( 
            user=request.user,
            Room =ROOM,
            body= request.POST.get('body')
            )
        ROOM.paticipants.add(request.user,) 
        return redirect('room', pk= ROOM.id)
    return render(request,'room/room.html', {'ROOM' : ROOM, 'room_messages' : room_messages, 'paticipants' : paticipants})


@login_required(login_url= 'login')
def create_room(request):
    form = userform()
    topics = Topic.objects.all()
    if request.method == 'POST':
       form = userform(request.POST)
       topic_name = request.POST.get('topic')
       topic, created = Topic.objects.get_or_create(name=topic_name)
       room.objects.create(
            host =request.user,
            topic=topic,
            name =request.POST.get('name'),
            description =request.POST.get('description')
        )
      
       return redirect('home')
    
    return render(request,'room/update_change.html', {"form": form, 'topics': topics})


@login_required(login_url='login')
def update_room(request,pk):
    ROOM = room.objects.get(id = pk)
    form = userform(instance=ROOM)
    topics = Topic.objects.all()
    if request.user != ROOM.host:
        return HttpResponse('you are not allowed here')
    if request.method == 'POST':

       topic_name = request.POST.get('topic')
       topic, created = Topic.objects.get_or_create(name=topic_name)
       ROOM.name = request.POST.get('name')
       ROOM.topic = topic
       ROOM.description = request.POST.get('description')
       ROOM.save()
       
       return redirect('home',)
    
    return render(request,'room/update_change.html', {'form': form, 'topics' : topics, 'ROOM' : ROOM})


@login_required(login_url='login')
def delete_room(request,pk):
    try: 
        room.objects.get(id = pk)
    except room.DoesNotExist:
        messages.error(request, "Room doest not exist!!!")
        return redirect("home")
    Room = room.objects.get(id = pk)
    if request.method == "POST":
       Room.delete() 
       return redirect('home')
    return render(request,"room/delete.html",{'obj': Room})


@login_required(login_url='login')
def delete_message(request,pk):
    
    try: 
        Message.objects.get(id = pk)
    except Message.DoesNotExist:
        messages.error(request, "Message doest not exist!!!")
        return redirect("home")
    message = Message.objects.get(id = pk)

    if request.user != message.user:
        messages.error(request, "You are not allowed here")
        redirect("home")
    if request.method == "POST":
        message.delete() 
        messages.success(request,"Message deleted sucessfully")
        return redirect('home',)
    return render(request,"room/delete.html",{'obj': message})

@login_required(login_url= 'login')
def profile_user(request, pk):
    if request.method == "GET":
        
        if not pk:
            return redirect("home")

       
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return HttpResponse("PAGE NOT FOUND 404") 

       
        user = User.objects.get(id=pk)
        Room = user.room_set.all
        room_message =user.message_set.all() 
        topic = Topic.objects.all()
       
    return render(request, 'room/profile.html', {
            'user': user,
            'Room': Room,
            'room_message': room_message,
            'topic': topic,
        })


def topicsPage(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topic = Topic.objects.filter(name__icontains = q)
    return render(request, "room/topics.html", {'topic': topic})


def activity2(request):
    room_message = Message.objects.all()
    return render(request,'room/activity.html', {'room_message' : room_message})
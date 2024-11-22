from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import room
from . serializers import roomSerializer

@api_view(['GET'])
def geetroutes(request):
    routes=[
        'GET /api/',
        'GET /api/cars',
        'GET /api/cars/:id'
    ]
    return Response(routes,)

@api_view(['GET'])
def getcars(request):
    ROOM = room.objects.all()
    serializer = roomSerializer(ROOM,many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getcar(request,pk):
    ROOM1 = room.objects.get(id =pk)
    serializer = roomSerializer(ROOM1,many =False)
    return Response(serializer.data)
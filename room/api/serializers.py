from rest_framework.serializers import ModelSerializer
from room.models import room 


class roomSerializer(ModelSerializer):
    class Meta:
        model = room
        fields ='__all__'

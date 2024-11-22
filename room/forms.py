from django.forms import ModelForm
from . models import room,User
from django.contrib.auth.forms import UserCreationForm


class MainUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['name','username', 'email', 'password1', 'password2','avatar' ]


class userform(ModelForm):
    class Meta:
        model = room
        fields = '__all__'
        exclude = ['host', 'paticipants']

    
class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','name', 'email','bio', 'avatar']
       

    
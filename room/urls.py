from django.urls import path
from . import views

urlpatterns = [
    
    path('room/<int:pk>/',views.rooms,name= 'room'),
    path('create-room/',views.create_room,name= 'create_room'),
    path('update-room/<int:pk>/',views.update_room,name='update_room'),
    path('delete-room/<int:pk>/',views.delete_room,name='delete_room'),
    path('delete-message/<int:pk>/',views.delete_message,name='delete_message'),
    path('profile/<int:pk>/',views.profile_user,name= 'profile'),
    path('topicpage/', views.topicsPage, name= 'topic_page'),
    path('activity/',views.activity2, name = 'activity'),
]
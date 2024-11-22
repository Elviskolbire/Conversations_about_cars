from django.urls import path
from . import views

urlpatterns = [
    path('',views.geetroutes,name = 'api',
         
         ),
    path('cars/',views.getcars,name = 'api_cars',
         
         ),
    path('cars/<int:pk>/',views.getcar,name = 'api_car',
          
         ),
]



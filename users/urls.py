from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_page, name = 'logout'),
    path("register/",views.register, name = "register"),
    path('edit/', views.exit_user, name = 'edit_user')
    
]

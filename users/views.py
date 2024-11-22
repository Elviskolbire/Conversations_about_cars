from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from room.forms import EditForm,User,MainUserCreationForm  
 


# Create your views here.
def login_page(request):
    page_name = 'login'
    if request.user.is_authenticated:
       return redirect("home")
    if request.method =='POST':
      email = request.POST.get('email').lower()
      password = request.POST.get("password")

      try:
         User.objects.get(email = email)

      except:
         messages.error(request, 'User name or password does not exist!!!')
         return render(request,'users/login.html', {'page_name': page_name})
       

      user = authenticate(request, email=email, password=password)
      if user is None:
         messages.error(request,'User name or password does not exist!!!')
         return render(request,'users/login.html', {'page_name': page_name})
         
      else:
         login(request, user)
         return redirect('home')
    else:
       return render(request,'users/login.html',{'page_name': page_name})
    

def logout_page(request):
   logout(request)
   messages.success(request,"You have sucessfully logout")
   return redirect('login')

def register(request):
   page_name ="register"
   form = MainUserCreationForm()
   if request.method == 'POST':
      form = MainUserCreationForm(request.POST, request.FILES,)
      if form.is_valid():
         user = form.save(commit = False)
         user.username = user.username.lower()
         user.save()
         login(request,user)
         return redirect("home")
      else:
       messages.error(request, "An occured during registeration")
   return render(request, 'users/login.html', {'page_name': page_name, 'form': form})

@login_required(login_url='login')
def exit_user(request):
   user = request.user
   form = EditForm(instance=user)
   if request.method == "POST":
      form = EditForm(request.POST, request.FILES, instance=user)
      if form.is_valid():
         form.save()
         return redirect('profile', pk=user.id)

   return render(request, 'users/update-user.html', {'form': form})
       
   
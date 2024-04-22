from django.shortcuts import render
from django.http import HttpResponse
from .models import Lobby
from django.contrib.auth.models import User
# Create your views here.

def canvas_view(request):
    return render(request, 'canvas.html')

def lobby_view(request):

    lobby = Lobby.objects.first()  


    users = User.objects.all()


    if request.method == 'POST':
        user_id = request.POST.get('user_id')  
        role = request.POST.get('role') 

        if user_id and role:
            user = User.objects.get(pk=user_id)
            lobby.add_user(user, role)
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id') 
        new_role = request.POST.get('new_role')  

        if user_id and new_role:
            user = User.objects.get(pk=user_id)
            lobby.change_role(user, new_role)

    return render(request, 'lobby.html', {'users': users, 'lobby': lobby})
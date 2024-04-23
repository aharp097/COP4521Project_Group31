from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Lobby, Canvas
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import CreateLobbyForm
from django.db import IntegrityError
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('canvas:home') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('canvas:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('canvas:home')


@login_required
def create_lobby(request):
    if request.method == 'POST':
        form = CreateLobbyForm(request.POST)
        if form.is_valid():
            lobby_name = form.cleaned_data['lobby_name']
            existing_lobby = Lobby.objects.filter(name=lobby_name).first()
            if existing_lobby:
                form.add_error('name', 'A lobby with this name already exists.')
            else:
                try:
                    lobby = Lobby.objects.create(name=lobby_name, creator=request.user)
                    lobby.add_user(request.user, 'Owner')
                    return redirect('canvas:lobby', lobby_name=lobby.name)
                except IntegrityError:
                    form.add_error('name', 'A lobby with this name already exists.')

            

    else:
        form = CreateLobbyForm()
    
    return render(request, 'create_lobby.html', {'form': form})

@login_required
def join_lobby(request):
    if request.method == 'POST':
        lobby_name = request.POST.get('lobby_name')
        try:
            lobby = Lobby.objects.get(name=lobby_name)
        except Lobby.DoesNotExist:
            return render(request, 'join_lobby.html', {'error': 'Lobby not found.'})
        if request.user not in lobby.users.all():
            lobby.add_user(request.user, 'Guest') #lobby owner or admin must permit participation
        return redirect('canvas:lobby', lobby_name=lobby.name)

    return render(request, 'join_lobby.html')

@login_required
def canvas_view(request, lobby_name):
    lobby = get_object_or_404(Lobby, name=lobby_name)
    canvas = lobby.canvas
    users = lobby.users.all()
    is_creator = request.user == lobby.creator
    return render(request, 'canvas.html', {'lobby': lobby, 'canvas': canvas, 'users': users, 'is_creator': is_creator})



def lobby_view(request, lobby_name):
    lobby = get_object_or_404(Lobby, name=lobby_name)

    users = lobby.users.all()
    is_creator = request.user == lobby.creator

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role = request.POST.get('role')
        new_role = request.POST.get('new_role')

        if user_id and role:
            user = User.objects.get(pk=user_id)
            lobby.add_user(user, role)
        elif user_id and new_role:
            user = User.objects.get(pk=user_id)
            lobby.change_role(user, new_role)

        users = lobby.users.all()

    user_roles = {}
    if lobby.roles:
        user_roles = lobby.roles

    return render(request, 'lobby.html', {'lobby': lobby, 'users': users, 'is_creator': is_creator, 'user_roles': user_roles})
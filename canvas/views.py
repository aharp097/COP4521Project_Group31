from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Lobby, Canvas
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import CreateLobbyForm
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
            lobby_name = form.cleaned_data['name']
            lobby = Lobby.objects.create(name=lobby_name, creator=request.user)

            return redirect('canvas:lobby', lobby_id=lobby.id)
    else:
        form = CreateLobbyForm()
    
    return render(request, 'create_lobby.html', {'form': form})

@login_required
def join_lobby(request):
    if request.method == 'POST':
        lobby_id = request.POST.get('lobby_id')
        try:
            lobby = Lobby.objects.get(id=lobby_id)
        except Lobby.DoesNotExist:
            return render(request, 'join_lobby.html', {'error': 'Lobby does not exist.'})
        return redirect('canvas_page', lobby_id=lobby.id)
    return render(request, 'join_lobby.html')

@login_required
def canvas_view(request):
    return render(request, 'canvas.html')



def lobby_view(request, lobby_id):
    lobby = get_object_or_404(Lobby, id=lobby_id)

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

    return render(request, 'lobby.html', {'users': users, 'lobby': lobby, 'is_creator': is_creator})

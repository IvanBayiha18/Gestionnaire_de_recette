from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

# Create your views here.

def register(request):
    """Vue pour l'inscription"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Crée automatiquement un UserProfile
            UserProfile.objects.create(user=user)
            
            # Connecte l'utilisateur directement
            login(request, user)
            messages.success(request, 'Compte créé avec succès ! Bienvenue sur RecipeMaster.')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'profiles/register.html', {'form': form})

def login_view(request):
    """Vue pour la connexion"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bonjour {username} ! Vous êtes maintenant connecté.')
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'profiles/login.html', {'form': form})

def logout_view(request):
    """Vue pour la déconnexion"""
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('home')

@login_required
def profile(request):
    """Vue pour le profil utilisateur"""
    user_profile = UserProfile.objects.get(user=request.user)
    favorites = user_profile.favorites.all()
    
    context = {
        'user_profile': user_profile,
        'favorites': favorites,
    }
    return render(request, 'profiles/profile.html', context)
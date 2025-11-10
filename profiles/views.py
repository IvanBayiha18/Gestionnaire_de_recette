from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.forms import UserForm, UserProfileForm
from recipes.models import Recipe
from .models import Favorite, UserProfile

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
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        # Récupère les favoris avec les recettes associées
        favorites = Favorite.objects.filter(user_profile=user_profile).select_related('recipe')
    except UserProfile.DoesNotExist:
        # Crée un profil si il n'existe pas (sécurité)
        user_profile = UserProfile.objects.create(user=request.user)
        favorites = []
    
    context = {
        'user_profile': user_profile,
        'favorites': favorites,
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def toggle_favorite(request, recipe_id):
    """Ajouter ou retirer une recette des favoris"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user_profile = UserProfile.objects.get(user=request.user)
    
    # Vérifie si la recette est déjà en favori
    favorite_exists = Favorite.objects.filter(
        user_profile=user_profile, 
        recipe=recipe
    ).exists()
    
    if favorite_exists:
        # Retirer des favoris
        Favorite.objects.filter(user_profile=user_profile, recipe=recipe).delete()
        messages.success(request, f'"{recipe.titre}" a été retiré de vos favoris.')
    else:
        # Ajouter aux favoris
        Favorite.objects.create(user_profile=user_profile, recipe=recipe)
        messages.success(request, f'"{recipe.titre}" a été ajouté à vos favoris.')
    
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def favorite_list(request):
    """Afficher la liste des favoris"""
    user_profile = UserProfile.objects.get(user=request.user)
    favorites = Favorite.objects.filter(user_profile=user_profile).select_related('recipe')
    
    context = {
        'favorites': favorites,
    }
    return render(request, 'profiles/favorite_list.html', context)

@login_required
def edit_profile(request):
    """Vue pour éditer le profil utilisateur"""
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, 
            request.FILES,  # Important pour l'upload d'image
            instance=user_profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profil a été mis à jour avec succès !')
            return redirect('profile')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'profiles/edit_profile.html', context)
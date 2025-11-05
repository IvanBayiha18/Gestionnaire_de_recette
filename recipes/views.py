from django.shortcuts import render
from .models import Recipe, Category

def home(request):
    """Vue pour la page d'accueil"""
    # Récupère les dernières recettes (limité à 8)
    derniere_recettes = Recipe.objects.all().order_by('-date_creation')[:8]
    
    context = {
        'derniere_recettes': derniere_recettes,
    }
    
    return render(request, 'recipes/home.html', context)
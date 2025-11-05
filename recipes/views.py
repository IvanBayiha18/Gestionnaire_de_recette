from django.shortcuts import get_object_or_404, render
from .models import Recipe, Category

def home(request):
    """Vue pour la page d'accueil"""
    # Récupère les dernières recettes (limité à 8)
    derniere_recettes = Recipe.objects.all().order_by('-date_creation')[:8]
    
    context = {
        'derniere_recettes': derniere_recettes,
    }
    
    return render(request, 'recipes/home.html', context)

def recipe_detail(request, recipe_id):
    """Vue pour le détail d'une recette"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Récupère les ingrédients et étapes liés
    ingredients = recipe.ingredients_recette.all()
    etapes = recipe.etapes.all().order_by('ordre')
    
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'etapes': etapes,
    }
    
    return render(request, 'recipes/recipe_detail.html', context)
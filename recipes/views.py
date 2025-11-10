from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from profiles.models import Favorite, UserProfile
from .models import Recipe, Category
from django.db.models import Q

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

def recipe_list(request):
    """Vue pour la liste complète des recettes"""
    # Récupère toutes les recettes
    recipes_list = Recipe.objects.all().order_by('-date_creation')
    
    # Pagination - 12 recettes par page
    paginator = Paginator(recipes_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'recipes/recipe_list.html', context)

def recipe_search(request):
    """Vue pour la recherche de recettes"""
    # Récupère les paramètres de recherche
    query = request.GET.get('q', '')  # Recherche texte
    categorie_id = request.GET.get('categorie', '')
    difficulte = request.GET.get('difficulte', '')
    temps_max = request.GET.get('temps_max', '')
    
    # Commence avec toutes les recettes
    recipes = Recipe.objects.all()
    
    # Filtre par recherche texte (titre OU description)
    if query:
        recipes = recipes.filter(
            Q(titre__icontains=query) | 
            Q(description__icontains=query)
        )
    
    # Filtre par catégorie
    if categorie_id:
        recipes = recipes.filter(categorie_id=categorie_id)
    
    # Filtre par difficulté
    if difficulte:
        recipes = recipes.filter(difficulte=difficulte)
    
    # Filtre par temps maximum
    if temps_max:
        recipes = recipes.filter(temps_preparation__lte=temps_max)
    
    # Tri par défaut
    recipes = recipes.order_by('-date_creation')
    
    # Pagination
    paginator = Paginator(recipes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Récupère les catégories pour les filtres
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'selected_categorie': categorie_id,
        'selected_difficulte': difficulte,
        'selected_temps_max': temps_max,
        'search_performed': any([query, categorie_id, difficulte, temps_max]),
    }
    return render(request, 'recipes/recipe_search.html', context)

def recipe_detail(request, recipe_id):
    """Vue pour le détail d'une recette"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Vérifie si la recette est en favori pour l'utilisateur connecté
    recipe_is_favorite = False
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            recipe_is_favorite = Favorite.objects.filter(
                user_profile=user_profile, 
                recipe=recipe
            ).exists()
        except UserProfile.DoesNotExist:
            pass
    
    ingredients = recipe.ingredients_recette.all()
    etapes = recipe.etapes.all().order_by('ordre')
    
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'etapes': etapes,
        'recipe_is_favorite': recipe_is_favorite,  # Nouveau contexte
    }
    
    return render(request, 'recipes/recipe_detail.html', context)
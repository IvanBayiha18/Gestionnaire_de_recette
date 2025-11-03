from django.contrib import admin
from .models import Ingredient

# Register your models here.
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Interface admin pour les ingrédients"""
    
    # Champs affichés dans la liste
    list_display = ('nom', 'categorie', 'date_creation')
    
    # Filtres latéraux
    list_filter = ('categorie', 'date_creation')
    
    # Barre de recherche
    search_fields = ('nom',)
    
    # Tri par défaut
    ordering = ('nom',)
    
    # Champs en lecture seule
    readonly_fields = ('date_creation', 'date_modification')
    
    # Groupement des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations principales', {
            'fields': ('nom', 'categorie')
        }),
        ('Dates', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',)  # Peut être réduit
        }),
    )
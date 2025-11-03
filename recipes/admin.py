from django.contrib import admin
from .models import Recipe, Category, RecipeStep, RecipeIngredient

# 1. D'ABORD on définit les Inlines
class RecipeStepInline(admin.TabularInline):
    """Inline pour les étapes de préparation"""
    model = RecipeStep
    extra = 1  # Une ligne vide par défaut
    ordering = ('ordre',)

class RecipeIngredientInline(admin.TabularInline):
    """Inline pour les ingrédients avec quantités"""
    model = RecipeIngredient
    extra = 3  # Trois lignes vides par défaut
    ordering = ('ingredient__nom',)

# 2. ENSUITE on définit RecipeAdmin UNE SEULE FOIS
@admin.register(Recipe)  # ← UNE SEULE inscription avec @admin.register
class RecipeAdmin(admin.ModelAdmin):
    """Interface admin pour les recettes - UNE SEULE DÉFINITION"""
    
    list_display = (
        'titre', 
        'categorie', 
        'difficulte', 
        'temps_preparation', 
        'date_creation'
    )
    
    list_filter = ('date_creation', 'categorie', 'difficulte')
    search_fields = ('titre', 'description')
    ordering = ('titre', 'date_creation')
    readonly_fields = ('date_creation', 'date_modification')
    
    # AJOUT IMPORTANT : Les inlines pour étapes et ingrédients
    inlines = [RecipeStepInline, RecipeIngredientInline]

    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'categorie', 'difficulte', 'temps_preparation')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Dates', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',)
        }),
    )

# 3. Admin pour Category (séparé)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
    ordering = ('nom',)
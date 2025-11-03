from django.contrib import admin
from .models import UserProfile, Favorite

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Interface admin pour les profils"""
    
    # Champs affichés dans la liste
    list_display = ('user', 'get_username', 'birth_date', 'localisation')
    
    # Filtres latéraux
    list_filter = ('user', 'birth_date', 'localisation')
    
    # Barre de recherche
    search_fields = ('user__username','birth_date', 'localisation')
    
    # Tri par défaut
    ordering = ('user__username','birth_date')
    
    # Groupement des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations de l\'utilisateur', {
            'fields': ('user', 'localisation', 'avatar', 'bio')
        }),
        ('Date de naissance', {
            'fields': ('birth_date',),
            'classes': ('collapse',)  # Peut être réduit
        }),
    )

     # ✅ AJOUT : Méthode pour afficher le username dans list_display
    def get_username(self, obj): #obj est une instance de userProfile
        return obj.user.username
    get_username.short_description = 'Username'  # Nom de colonne

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Interface admin pour les favoris"""
    
    # Champs affichés
    list_display = ('user_profile', 'recipe', 'date_added')
    
    # Filtres utiles
    list_filter = ('date_added',)
    
    # Recherche
    search_fields = ('user_profile__user__username', 'recipe__titre')
    
    # Tri par défaut
    ordering = ('date_added',)  # Plus récents en premier
    
    # Champs en lecture seule
    readonly_fields = ('date_added',)
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Favorite

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    
    # Rendre l'email obligatoire et unique
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['email'].required = True
        return form

# UN SEUL admin.register pour UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Interface admin pour les profils"""
    
    # Champs affichés dans la liste
    list_display = ('user', 'get_username', 'localisation', 'birth_date')
    
    # Filtres latéraux
    list_filter = ('localisation', 'birth_date')
    
    # Barre de recherche
    search_fields = ('user__username', 'localisation')
    
    # Tri par défaut
    ordering = ('user__username', 'birth_date')
    
    # Groupement des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations de l\'utilisateur', {
            'fields': ('user', 'localisation', 'avatar', 'bio')
        }),
        ('Date de naissance', {
            'fields': ('birth_date',),
            'classes': ('collapse',)
        }),
    )

    # Méthode pour afficher le username dans list_display
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Interface admin pour les favoris"""
    
    list_display = ('user_profile', 'recipe', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('user_profile__user__username', 'recipe__titre')
    ordering = ('-date_added',)  # Plus récents en premier
    readonly_fields = ('date_added',)

# ✅ Réenregistrer UserAdmin APRÈS toutes les autres classes
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
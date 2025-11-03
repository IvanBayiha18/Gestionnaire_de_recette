from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.
class UserProfile(models.Model):
    """
    Étend le modèle User de Django avec des informations supplémentaires
    Relation : OneToOne (1 User = 1 UserProfile)
    """
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        related_name='user_profile',
        verbose_name='Utilisateur'
    )

    bio = models.TextField(
        max_length=500, 
        verbose_name='Biographie',
        blank=True
        )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de naissance"
        )

    localisation = models.CharField(
        max_length=100, 
        verbose_name='Localisation',
        blank=True
        )

    avatar = models.ImageField(
        upload_to = 'avatars/', # Dossier de stockage
        verbose_name="Photo de profile",
        null=True,
        blank=True
        )

    def __str__(self):
        return f"Profil de {self.user.username}" # Retourne le username
    
    class Meta:
        verbose_name = 'Profil utilisateur'
        verbose_name_plural = 'Profils utilisateurs'
        ordering = ['user__username']  # ✅ Trie par username


class Favorite(models.Model):
    """
    Modèle intermédiaire pour les recettes favorites
    Relation : UserProfile ← Favorite → Recipe
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='favorites',  # ✅ user_profile.favorites_relation.all()
        verbose_name='Profil utilisateur'
    )
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorited_by',  # ✅ recipe.favorited_by.all()
        verbose_name='Recette'
    )
    
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date d\'ajout'
    )

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoris'
        unique_together = ['user_profile', 'recipe']  # ✅ Évite les doublons

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.recipe.titre}"

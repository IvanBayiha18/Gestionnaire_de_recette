from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    """Modèle pour les commentaires de recettes"""
    
    # Relation avec la recette au lieu de l'article
    recipe = models.ForeignKey(
        'recipes.Recipe',  # Référence à l'app recipes
        on_delete=models.CASCADE,
        related_name='comments',  # Permet d'accéder aux commentaires via recipe.comments.all()
        verbose_name="Recette"
    )
    
    # Auteur du commentaire (inchangé)
    auteur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Auteur"
    )
    
    # Contenu du commentaire (inchangé)
    contenu = models.TextField(
        max_length=1000,
        verbose_name="Commentaire"
    )
    
    # Dates (inchangé)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    # Modération (inchangé)
    approuve = models.BooleanField(
        default=False,
        verbose_name="Commentaire approuvé"
    )
    
    class Meta:
        ordering = ['date_creation']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
    
    # ✅ CHANGÉ : Adaptation du __str__
    def __str__(self):
        return f"Commentaire par {self.auteur.username} sur {self.recipe.titre}"
    
    def est_recent(self):
        """Vérifie si le commentaire a été créé récemment"""
        return (timezone.now() - self.date_creation).days < 1
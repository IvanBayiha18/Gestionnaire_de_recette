from django.db import models
from ingredients.models import Ingredient

# Create your models here.
class Category(models.Model):
    """Catégorie de recettes (entrée, plat, dessert...)"""
    nom = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Nom de la catégorie"
    )
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
        ordering = ['nom']
class Recipe(models.Model):
    DIFFICULTE_CHOICES = [
        ('facile', 'Facile'),
        ('moyen', 'Moyen'),
        ('difficile', 'Dificile')
    ]

        # Relation avec Category (une recette → une catégorie)
    categorie = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # Si on supprime la catégorie, la recette garde sa catégorie vide
        null=True,
        blank=True,
        related_name='recettes',
        verbose_name='Catégorie'
    )

    titre = models.CharField(
        max_length=100, unique= True, verbose_name="Titre de la recète"
        )

    ingredient = models.ForeignKey(
        'ingredients.Ingredient',
        on_delete= models.CASCADE,
        related_name= 'Recète',
        verbose_name= 'Ingrédient'
    )

    quantity = models.IntegerChoices(names='Quantité')

    description = models.TextField(max_length=1000, verbose_name='Description')

    temps = models.models.TimeField(("Temps de préparation"), auto_now=False, auto_now_add=False)

    difficulte = models.CharField(
        max_length=20,
        choices=DIFFICULTE_CHOICES,
        default='moyen',
        verbose_name="Niveau de difficulté"
    )

    date_creation = models.DateTimeField(auto_now_add= True)
    date_modification = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Recètte'
        verbose_name_plural = 'recèttes'
        ordering = ['nom']
class RecipeIngredient(models.Model):
    """Modèle intermédiaire pour gérer les quantités d'ingrédients"""
    recette = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_recette'
    )
    
    ingredient = models.ForeignKey(
        'ingredients.Ingredient',  # Référence à l'app ingredients
        on_delete=models.CASCADE
    )
    
    quantite = models.DecimalField(  #  Pour gérer 0.5, 2.5, etc.
        max_digits=6, 
        decimal_places=2,
        verbose_name="Quantité"
    )
    
    unite = models.CharField(
        max_length=20,
        verbose_name="Unité de mesure",
        help_text="Ex: g, kg, ml, L, cuillère à soupe, pincée..."
    )
    class Meta:
        unique_together = ['recette', 'ingredient']  #  Évite les doublons

class RecipeStep(models.Model):  # 
    """Étapes de préparation d'une recette"""
    recette = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='etapes'
    )
    
    ordre = models.PositiveIntegerField(verbose_name="Ordre de l'étape")
    
    description = models.TextField(
        verbose_name="Description de l'étape"
    )
    
    class Meta:
        verbose_name = 'Étape de préparation'
        verbose_name_plural = 'Étapes de préparation'
        ordering = ['recette', 'ordre']  # ✅ Trie par recette puis ordre

    def __str__(self):
        return f"Étape {self.ordre} - {self.recette.titre}"

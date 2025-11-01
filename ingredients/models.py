from django.db import models

# Create your models here.
class Ingredient (models.Model):
    nom = models.CharField(
         max_length=50, unique= True, verbose_name= "Nom de l'ingrédient"
         )
 
    categorie = models.CharField(
        max_length=30,
        choices=[
            ('legume', 'Légume'),
            ('fruit', 'Fruit'),
            ('viande', 'Viande'),
            ('poisson', 'Poisson'),
            ('epice', 'Épice'),
            ('laitier', 'Laitier'),
            ('feculent', 'Féculent'),
        ],
        default='legume',
        verbose_name="Catégorie alimentaire"
    )

    date_creation = models.DateTimeField(auto_now_add= True)
    date_modification = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Ingrédient"
        verbose_name_plural = "Ingrédients"
        ordering = ['nom'] #Trier par nom par défaut
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, Category, RecipeStep
from ingredients.models import Ingredient

class RecipeModelTest(TestCase):
    def setUp(self):
        """Setup pour tous les tests"""
        self.category = Category.objects.create(nom="Dessert")
        self.recette = Recipe.objects.create(
            titre="Gâteau au chocolat",
            categorie=self.category,
            description="Un délicieux gâteau au chocolat",
            temps_preparation=45,
            difficulte="facile"
        )
    
    def test_creation_recette(self):
        """Test qu'une recette peut être créée"""
        self.assertEqual(self.recette.titre, "Gâteau au chocolat")
        self.assertEqual(self.recette.categorie.nom, "Dessert")
        self.assertEqual(self.recette.difficulte, "facile")
    
    def test_str_representation(self):
        """Test la représentation en string"""
        self.assertEqual(str(self.recette), "Gâteau au chocolat")

# Test très simple pour commencer
def test_exemple_simple(self):
    """Un test tout simple pour vérifier que les tests fonctionnent"""
    self.assertEqual(1 + 1, 2)
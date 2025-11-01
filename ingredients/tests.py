from django.test import TestCase
from .models import Ingredient

class IngredientModelTest(TestCase):
    def setUp(self):
        """Setup pour tous les tests"""
        self.ingredient = Ingredient.objects.create(
            nom="Tomate",
            categorie="legume"
        )
    
    def test_creation_ingredient(self):
        """Test qu'un ingrédient peut être créé"""
        self.assertEqual(self.ingredient.nom, "Tomate")
        self.assertEqual(self.ingredient.categorie, "legume")
        self.assertIsNotNone(self.ingredient.date_creation)
    
    def test_str_representation(self):
        """Test la représentation en string"""
        self.assertEqual(str(self.ingredient), "Tomate")
    
    def test_nom_unique(self):
        """Test que deux ingrédients ne peuvent avoir le même nom"""
        with self.assertRaises(Exception):  # Should raise integrity error
            Ingredient.objects.create(nom="Tomate", categorie="fruit")

# Create your tests here.

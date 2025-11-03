from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Favorite
from recipes.models import Recipe, Category

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            bio='Bio de test',
            localisation='Paris'
        )
    
    def test_user_profile_creation(self):
        """Test la création d'un profil utilisateur"""
        self.assertEqual(self.user_profile.user.username, 'testuser')
        self.assertEqual(self.user_profile.bio, 'Bio de test')
        # ✅ CORRIGÉ : utilise user_profile au lieu de profile
        self.assertEqual(self.user.user_profile, self.user_profile)
    
    def test_favorite_creation(self):
        """Test l'ajout d'une recette en favori"""
        category = Category.objects.create(nom='Dessert')
        recipe = Recipe.objects.create(
            titre='Gâteau au chocolat',
            categorie=category,
            description='Un délicieux gâteau',
            temps_preparation=45,
            difficulte='facile'
        )
        
        favorite = Favorite.objects.create(
            user_profile=self.user_profile,
            recipe=recipe
        )
        
        self.assertEqual(self.user_profile.favorites.count(), 1)
        self.assertEqual(recipe.favorited_by.count(), 1)
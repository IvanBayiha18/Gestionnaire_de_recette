from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment
from recipes.models import Recipe, Category

# Create your tests here.
class CommentModelTest(TestCase):
    def setUp(self):
        # Création des données de test
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        self.category = Category.objects.create(nom='Dessert')
        
        self.recipe = Recipe.objects.create(
            titre='Gâteau au chocolat',
            categorie=self.category,
            description='Un délicieux gâteau',
            temps_preparation=45,
            difficulte='facile'
        )
    
    def test_comment_creation(self):
        """Test la création d'un commentaire sur une recette"""
        comment = Comment.objects.create(
            recipe=self.recipe,
            auteur=self.user,
            contenu='Cette recette est excellente !'
        )
        
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.recipe, self.recipe)
        self.assertEqual(comment.auteur, self.user)
        self.assertEqual(comment.contenu, 'Cette recette est excellente !')
        self.assertFalse(comment.approuve)  # Par défaut non approuvé
    
    def test_comment_str_representation(self):
        """Test la représentation en string du commentaire"""
        comment = Comment.objects.create(
            recipe=self.recipe,
            auteur=self.user,
            contenu='Test'
        )
        
        expected_str = f"Commentaire par {self.user.username} sur {self.recipe.titre}"
        self.assertEqual(str(comment), expected_str)
    
    def test_comment_recent(self):
        """Test la méthode est_recent"""
        comment = Comment.objects.create(
            recipe=self.recipe,
            auteur=self.user,
            contenu='Test'
        )
        
        self.assertTrue(comment.est_recent())
    
    def test_recipe_comments_relation(self):
        """Test la relation inverse (recipe.comments)"""
        comment1 = Comment.objects.create(
            recipe=self.recipe,
            auteur=self.user,
            contenu='Premier commentaire'
        )
        
        comment2 = Comment.objects.create(
            recipe=self.recipe,
            auteur=self.user,
            contenu='Deuxième commentaire'
        )
        
        # Vérifie qu'on peut accéder aux commentaires via la recette
        self.assertEqual(self.recipe.comments.count(), 2)
        self.assertIn(comment1, self.recipe.comments.all())
        self.assertIn(comment2, self.recipe.comments.all())
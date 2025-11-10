from django import forms
from .models import Recipe, RecipeIngredient, RecipeStep, Category

class RecipeForm(forms.ModelForm):
    """Formulaire pour créer et modifier une recette"""
    
    class Meta:
        model = Recipe
        fields = ['titre', 'categorie', 'description', 'temps_preparation', 'difficulte']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de votre recette...'
            }),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Décrivez votre recette...'
            }),
            'temps_preparation': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Temps en minutes'
            }),
            'difficulte': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'titre': 'Titre de la recette',
            'categorie': 'Catégorie',
            'description': 'Description',
            'temps_preparation': 'Temps de préparation (minutes)',
            'difficulte': 'Niveau de difficulté',
        }

class RecipeIngredientForm(forms.ModelForm):
    """Formulaire pour un ingrédient"""
    
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantite', 'unite']
        widgets = {
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Quantité'
            }),
            'unite': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'g, kg, ml, L, cuillère...'
            }),
        }

class RecipeStepForm(forms.ModelForm):
    """Formulaire pour une étape de préparation"""
    
    class Meta:
        model = RecipeStep
        fields = ['ordre', 'description']
        widgets = {
            'ordre': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Décrivez cette étape...'
            }),
        }
        labels = {
            'ordre': 'Numéro de l\'étape',
            'description': 'Description de l\'étape',
        }
from django.contrib import admin
from .models import Comment
from django.utils.html import format_html
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Configuration de l'interface de l'admin pour les commentaires"""
    
    # Configuration de la liste
    list_display = (
        'recipe', 
        'auteur', 
        'contenu',
        'contenu_tronque',
        'date_creation', 
        'approuve',
        'statut_badge'
    )
    list_display_links = ('contenu_tronque',)
    list_filter = ('approuve', 'date_creation', 'contenu', 'auteur')
    list_editable = ('approuve',)
    search_fields = ('contenu', 'auteurusername', 'articletitre')
    date_hierarchy = 'date_creation'
    list_per_page = 20
    
    # Actions personnalisées
    actions = ['approuver_commentaires', 'desapprouver_commentaires']
    
    def contenu_tronque(self, obj):
        """Affiche un extrait du contenu du commentaire"""
        return obj.contenu[:75] + '...' if len(obj.contenu) > 75 else obj.contenu
    contenu_tronque.short_description = 'Commentaire'
    
    def statut_badge(self, obj):
        """Affiche un badge coloré pour le statut d'approbation"""
        if obj.approuve:
            return format_html('<span style="color: white; background-color: #4CAF50; padding: 3px 8px; border-radius: 10px; font-size: 0.8em;">✅ Approuvé</span>')
        else:
            return  format_html('<span style="color: white; background-color: #ff9800; padding: 3px 8px; border-radius: 10px; font-size: 0.8em;">⏳ En attente</span>')
    statut_badge.short_description = 'Statut'
    
    def approuver_commentaires(self, request, queryset):
        """Action pour approuver plusieurs commentaires"""
        updated = queryset.update(approuve=True)
        self.message_user(request, f"{updated} commentaire(s) approuvé(s) avec succès.")
    approuver_commentaires.short_description = "Approuver les commentaires sélectionnés"
    
    def desapprouver_commentaires(self, request, queryset):
        """Action pour désapprouver plusieurs commentaires"""
        updated = queryset.update(approuve=False)
        self.message_user(request, f"{updated} commentaire(s) désapprouvé(s).")
    desapprouver_commentaires.short_description = "Désapprouver les commentaires sélectionnés"
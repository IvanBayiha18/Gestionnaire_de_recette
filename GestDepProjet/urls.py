"""
URL configuration for GestDepProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from GestDepProjet import settings
from recipes.views import home, recipe_detail, recipe_list, recipe_search
from profiles.views import edit_profile, register, login_view, logout_view, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('recette/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recettes/', recipe_list, name='recipe_list'),
    path('recherche/', recipe_search, name='recipe_search'),

     # URLs d'authentification
    path('inscription/', register, name='register'),
    path('connexion/', login_view, name='login'),
    path('deconnexion/', logout_view, name='logout'),
    path('profil/', profile, name='profile'),
    path('profil/editer/', edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import include, path

from .views import anasayfa

urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    
]
from django.urls import path

from .views import hakkimizda,hizmetlerimiz,kazanimlarimiz


urlpatterns = [
    path('hakkimizda', hakkimizda, name="hakkimizda"),
    path('hizmetlerimiz', hizmetlerimiz, name="hizmetlerimiz"),
    path('kazanimlarimiz', kazanimlarimiz, name="kazanimlarimiz"),
]
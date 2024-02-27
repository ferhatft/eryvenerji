from django.urls import include, path
from .views import (
    contacview
)

urlpatterns = [
    path('' , contacview, name="iletisim"),   
]


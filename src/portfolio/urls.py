from django.urls import path

from .views import portfolio,portfoliodetail,projelerimiz


urlpatterns = [
    path('ürünlerimiz/', portfolio, name="portfolio"),
    path('projelerimiz/', projelerimiz, name="projelerimiz"),
    path('ürünlerimiz/<slug:slug>', portfoliodetail, name="portfoliodetail"),

]
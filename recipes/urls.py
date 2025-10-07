from django.urls import path
from recipes.views import home, contato, about


urlpatterns = [
    path('', home),
    path('contact/', contato),
]
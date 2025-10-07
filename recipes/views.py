from django.shortcuts import render
from django.http import HttpResponse

# adicionar o app criado a projeto (settings.py)
def home(request):
    return render(request, 'recipes/pages/home.html')

def contato(request):
    return render(request, 'recipes/pages/contact.html')





# Create your views here.

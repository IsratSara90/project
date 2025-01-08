from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe/detail.html', {'recipe': recipe})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]

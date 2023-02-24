from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_food_stats, name='food-show-stats'),
]
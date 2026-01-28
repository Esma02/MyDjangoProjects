from django.urls import path
from .import views

urlpatterns = [
    path('',views.home ),
    path('coffees', views.coffee, name='coffee_list'),
    path('desserts', views.dessert, name='dessert_list'),
]

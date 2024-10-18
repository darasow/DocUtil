from django.urls import path
from . import views

# app_name = 'teste'

urlpatterns = [
    path('hello/<str:name>/', views.teste, name='teste'),
]

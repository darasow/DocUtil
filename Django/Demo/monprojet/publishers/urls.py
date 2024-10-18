from django.urls import path
from . import views

app_name = 'publishers'

urlpatterns = [
    path('', views.publisher_list, name='publisher_list'),
    path('<int:id>/', views.publisher_detail, name='publisher_detail'),
    path('delete_publisher/<int:id>/', views.delete_publisher, name='delete_publisher'),
    path('update_publisher/<int:id>/', views.update_publisher, name='update_publisher'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
]

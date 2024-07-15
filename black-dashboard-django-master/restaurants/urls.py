from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/new/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/<int:pk>/edit/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),

    path('restaurant/<int:restaurant_id>/menu/new/', views.menu_item_create, name='menu_item_create'),
    path('restaurant/<int:restaurant_id>/menu/<int:pk>/edit/', views.menu_item_update, name='menu_item_update'),
    path('restaurant/<int:restaurant_id>/menu/<int:pk>/delete/', views.menu_item_delete, name='menu_item_delete'),
]

# In StoreTeck/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # User Authentication URLs
    path('register/', views.user_register, name='register'),  # Corrected to user_register
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # User Profile Management URLs
    path('profile/', views.user_profile, name='profile'),

    # Products Management URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Corrected parameter name
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:pk>/update/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),

    # Categories Management URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:pk>/update/', views.update_category, name='update_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),

    # Order Management URLs
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.view_orders, name='view_orders'),

    # Other Authentication URLs
    path('change_password/', views.change_password, name='change_password'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/products/', views.product_data, name='product_data'),
]
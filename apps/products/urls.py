from django.urls import path
from apps.products import views


urlpatterns = [
   path('product/<str:slug>/', views.detail_product, name='product_detail'),
]
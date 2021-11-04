from django.urls import path
from apps.products import views


urlpatterns = [
   path('product/<str:slug>/', views.ProductIndexView.as_view(), name='product_detail'),
]
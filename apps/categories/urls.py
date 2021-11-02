from django.urls import path
from apps.categories import views


urlpatterns = [
   path('', views.CategoryIndexView.as_view(), name='category_index'),
]
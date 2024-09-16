from django.urls import path
from catalog import views

urlpatterns = [
    path('product/', views.ProductDetailView.as_view()),
    path('products/', views.ProductsView.as_view()),
    path('category/', views.CategorysView.as_view()),
]

from django.urls import path
from catalog import views

urlpatterns = [
    path('product/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('products/', views.ProductsView.as_view(), name = 'products-post'),
    path('category/', views.CategorysView.as_view(), name = 'categories-get'),
]

from django.urls import path
from cart import views

urlpatterns = [
    path('cart/', views.CartDetailView.as_view())
]

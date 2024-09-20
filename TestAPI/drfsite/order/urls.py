from django.urls import path
from order import views

urlpatterns = [
    path('order/', views.OrderView.as_view(), name = 'create-order'),
]

from django.urls import path, include
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('api/order/', OrderListView.as_view(), name='order-list'),
    path('api/order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    
]


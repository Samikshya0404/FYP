from django.urls import path, include
from .views import EventListView, EventDetailView

urlpatterns = [
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    
]

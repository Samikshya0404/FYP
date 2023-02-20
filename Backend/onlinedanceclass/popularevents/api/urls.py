

from django.urls import path
from popularevents.api.views import EventList

urlpatterns = [
    path('get_event_list', EventList.as_view(), name="event_list"),
    # path('get_blog_details/<int:pk>', BlogDetailView.as_view(), name="blog_details"),

]



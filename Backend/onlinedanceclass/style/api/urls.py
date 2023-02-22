from django.urls import path

from style.api.views import StyleListAPI

urlpatterns = [
    path('get_styles_list/', StyleListAPI.as_view(), name="styles_list"),
]
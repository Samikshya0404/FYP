from django.urls import path

from style.api.views import StyleListAPI , StyleRetrieveAPI
# from video

urlpatterns = [
    path('get_styles_list/', StyleListAPI.as_view(), name="styles_list"),
    path('get_style/<str:name>/', StyleRetrieveAPI.as_view())
]
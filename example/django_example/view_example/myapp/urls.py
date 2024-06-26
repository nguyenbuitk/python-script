from django.urls import path
from .views import hello_world_view, hello_world_http_response

urlpatterns = [
    path('hello/', hello_world_view, name='hello_world'),
    path('http/', hello_world_http_response, name='hello_world_http_response')
]

from django.urls import path
from .views import person_list_view

urlpatterns = [
    path('people/', person_list_view, name='person_list'),
]

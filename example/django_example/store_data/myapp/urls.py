from django.urls import path
from .views import job_application_view

urlpatterns = [
    path('apply/', job_application_view, name='job_application'),
]

from django.urls import path
from .views import lead_create_view, success_view

urlpatterns = [
    path('', lead_create_view, name='lead_create_page'),
    path('success/', success_view, name='success_page'),
]
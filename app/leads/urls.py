from django.urls import path
from .views import lead_create_view, success_view

urlpatterns = [
    # A URL raiz ('') será atendida pela nossa view de criação de lead
    path('', lead_create_view, name='lead_create_page'),
    # A URL '/success/' será atendida pela view de sucesso
    path('success/', success_view, name='success_page'),
]
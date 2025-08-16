from django.urls import path
from .views import lead_create_view, success_view, lead_list_view, lead_detail_view

urlpatterns = [
    path('', lead_create_view, name='lead_create_page'),
    path('success/', success_view, name='success_page'),
    path('leads/', lead_list_view, name='lead_list_page'),
    path('leads/<int:pk>/', lead_detail_view, name='lead_detail'),
]
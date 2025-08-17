from django.contrib import admin
from .models import Lead

# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'status', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('nome', 'email', 'empresa')
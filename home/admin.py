from django.contrib import admin
from .models import RoleOverride
@admin.register(RoleOverride)
class RoleOverrideAdmin(admin.ModelAdmin):
    list_display = ('email', 'group_name')

from django.contrib import admin
from .models import Style
# Register your models here.
@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    pass
    list_display = ("name", "thumbnail", "created_at", "updated_at")

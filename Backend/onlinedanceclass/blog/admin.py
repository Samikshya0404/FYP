# from django.contrib import admin
# from .models import Blog
# # Register your models here.
# admin.site.register(Blog)




from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class Party_Wise_Vote(admin.ModelAdmin):
    pass
    list_display = ('title', 'decription', 'created_at', 'updated_at')
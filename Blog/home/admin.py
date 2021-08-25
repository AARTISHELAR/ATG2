from django.contrib import admin
from home.models import blog, Mode
# Register your models here.
@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','owner','mode','image','created_at']

@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

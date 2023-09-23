from django.contrib import admin
from .models import Project, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)


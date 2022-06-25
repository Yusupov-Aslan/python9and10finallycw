from django.contrib import admin

from ad.models import Ad, Category


class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_filter = ['author']
    search_fields = ['title']
    fields = ['photo', 'title', 'text', 'coast', 'author', 'status',
              'category', 'created_at', 'updated_at', 'publication_date']
    readonly_fields = ['created_at', 'updated_at', 'publication_date']


admin.site.register(Ad, AdAdmin)
admin.site.register(Category)

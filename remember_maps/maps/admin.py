from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'pub_date', 'text', 'point', 'lonlatstr')
    list_editable = ('author', 'lonlatstr')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author', )
    empty_value_display = '-пусто-'

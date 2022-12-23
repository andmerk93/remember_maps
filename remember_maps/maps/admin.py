from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'pub_date', 'text',)
    list_editable = ('author',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'author', )
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)

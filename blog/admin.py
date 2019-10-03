from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief', 'date_added', 'tags')
    ordering = ('title',)
    search_fields = ('title', 'brief', 'date_added', 'tags')


admin.site.register(Post, PostAdmin)

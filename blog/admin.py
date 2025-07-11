from django.contrib import admin
from .models import Post, Category, AboutUs


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('category','created_at',)
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(AboutUs)
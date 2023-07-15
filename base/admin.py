from django.contrib import admin
from base.models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('disease','severity', 'id',  'author', 'original_image','segmented_image','detected_image', 'locations', 'date',)
    prepopulated_fields = {'disease': ('severity',), }



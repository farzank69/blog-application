from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags') # Add filters for author, date, and tags in the admin list view.
    prepopulated_fields = {'slug': ('title',)} # Automatically populate the slug field based on the title field.
    list_display = ('title', 'author', 'date')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user_name", "post"]

admin.site.register(Post, PostAdmin) # Register Post model with custom PostAdmin
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
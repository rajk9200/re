from django.contrib import admin
from .models import Posts,PostCot,ResultLink
# Register your models here.

admin.site.register(PostCot)
admin.site.register(ResultLink)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('name','title', 'update_date')
    list_filter = ('title', 'update_date','id','name')


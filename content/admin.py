from django.contrib import admin

# Register your models here.
from content.models import Category, Content
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter= ["title"]

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','category','image']
    list_filter= ["title","category"]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Content,ContentAdmin)
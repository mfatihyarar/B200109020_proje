from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

# Register your models here.
from content.models import Category, Content, Images
class ContentImageInline(admin.TabularInline):
    model=Images
    extra=5
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'status','image_tag']
    readonly_fields = ('image_tag',)
    list_filter= ["status"]

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','category','image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter= ["status","category"]
    inlines= [ContentImageInline]
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_contents_count', 'related_contents_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Content,
                'category',
                'contents_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Content,
                 'category',
                 'contents_count',
                 cumulative=False)
        return qs

    def related_contents_count(self, instance):
        return instance.contents_count
    related_contents_count.short_description = 'Related contents (for this specific category)'

    def related_contents_cumulative_count(self, instance):
        return instance.contents_cumulative_count
    related_contents_cumulative_count.short_description = 'Related contents (in tree)'


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Content,ContentAdmin)
admin.site.register(Images,ImagesAdmin)
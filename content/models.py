from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    STATUS=(
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title=models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(blank=True, max_length=100)
    status=models.CharField(blank=True,max_length=10, choices=STATUS)
    parent=models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = "Image"

class Content(models.Model):
    STATUS=(
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    detail=RichTextUploadingField(blank=True)
    type=models.CharField(blank=True,max_length=50)
    city=models.CharField(blank=True,max_length=50)
    country=models.CharField(blank=True,max_length=50)
    konum=models.CharField(blank=True,max_length=255)
    slug=models.SlugField(blank=True,max_length=100)
    status=models.CharField(blank=True,max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.title
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description="Image"

class Images(models.Model):
    content=models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = "Image"


from django.contrib import admin

from home.models import Setting, ContactFormMessage

class ContactForMessageAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","note","status"]
    list_filter = ["status"]

# Register your models here.
admin.site.register(ContactFormMessage,ContactForMessageAdmin)
admin.site.register(Setting)

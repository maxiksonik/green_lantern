from django.contrib import admin

# Register your models here.
from apps.newsletters.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass

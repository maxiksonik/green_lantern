from django.contrib import admin

# Register your models here.
from apps.dealers.models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass

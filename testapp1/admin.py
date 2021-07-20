from django.contrib import admin
from .models import Registration
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['user_id','item_id','rating','timestamp','title']
admin.site.register(Registration,RegistrationAdmin)
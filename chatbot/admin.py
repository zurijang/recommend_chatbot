from django.contrib import admin
from .models import AddressData, AlgorithmData
# Register your models here.

class AddressDataAdmin(admin.ModelAdmin):
    list_display=['search_name']
    search_fields=['search_name']

class AlgorithmDataAdmin(admin.ModelAdmin):
    list_display=['search_name']
    search_fields=['search_name']

admin.site.register(AddressData, AddressDataAdmin)
admin.site.register(AlgorithmData, AlgorithmDataAdmin)
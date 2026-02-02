from django.contrib import admin
from .models import Farmer, CropRecord, SoilRecord, WaterRecord


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'location', 'created_at')
    search_fields = ('name', 'phone', 'location')


@admin.register(CropRecord)
class CropRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop_name', 'farmer', 'yield_kg', 'planted_on')
    search_fields = ('crop_name', 'farmer__name')


@admin.register(SoilRecord)
class SoilRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmer', 'ph', 'nitrogen', 'phosphorus', 'recorded_at')
    search_fields = ('farmer__name',)


@admin.register(WaterRecord)
class WaterRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmer', 'ph', 'ec', 'tds', 'recorded_at')
    search_fields = ('farmer__name',)

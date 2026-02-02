from django.db import models


class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class CropRecord(models.Model):
    id = models.AutoField(primary_key=True)
    
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crops')
    crop_name = models.CharField(max_length=255, null=False)
    yield_kg = models.FloatField(blank=True, null=True)
    date_recorded = models.CharField(max_length=255, blank=True, null=True)
    planted_on = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.crop_name} - {self.farmer.name}"

    class Meta:
        ordering = ['-planted_on']


class WaterRecord(models.Model):
    id = models.AutoField(primary_key=True)

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='water_records')
    ph = models.FloatField(blank=True, null=True)
    ec = models.FloatField(blank=True, null=True)
    tds = models.FloatField(blank=True, null=True)
    amount_l = models.FloatField(blank=True, null=True)
    date_recorded = models.CharField(max_length=255, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Water Record - {self.farmer.name} ({self.recorded_at})"

    class Meta:
        ordering = ['-recorded_at']


class SoilRecord(models.Model):
    id = models.AutoField(primary_key=True)

    # Foreign key to Farmer model
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='soil_records')

    ph = models.FloatField(blank=True, null=True)
    nitrogen = models.FloatField(blank=True, null=True)
    phosphorus = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    moisture = models.FloatField(blank=True, null=True)
    soil_type = models.CharField(max_length=100, blank=True, null=True)
    date_recorded = models.CharField(max_length=255, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Soil Record - {self.farmer.name} ({self.recorded_at})"

    class Meta:
        ordering = ['-recorded_at']

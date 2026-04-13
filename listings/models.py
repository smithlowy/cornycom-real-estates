from django.db import models

class Plot(models.Model):
    dimensions = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='plots/', null=True, blank=True)
    google_maps_link = models.URLField(max_length=500, null=True, blank=True)
    description = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dimensions} in {self.district}"
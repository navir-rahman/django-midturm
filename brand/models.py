from django.db import models

# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length=20)
    brand_owner = models.CharField(max_length=20)

    def __str__(self):
        return self.brand_name
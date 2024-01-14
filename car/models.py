from django.db import models
from brand.models import BrandModel
# Create your models here.
class CarModel(models.Model):
    car_name = models.CharField(max_length=20)
    car_img = models.ImageField()
    car_price = models.IntegerField()
    discription = models.TextField( blank=True)
    quantity = models.IntegerField(blank=True, default=10)
    brand = models.ForeignKey( BrandModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name
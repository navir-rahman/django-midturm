from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.
class CarModel(models.Model):
    # ordered_by = models.ForeignKey(User, related_name = 'user_account', on_delete = models.CASCADE)
    car_name = models.CharField(max_length=20)
    car_img = models.ImageField()
    car_price = models.IntegerField()
    discription = models.TextField( blank=True)
    quantity = models.IntegerField(blank=True, default=10)
    brand = models.ForeignKey( BrandModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} for {self.car.car_name} on {self.order_date}"


class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    Comment = models.CharField(max_length=100)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE )

    def __str__(self):
        return f'user_name: {self.user_name} comment: {self.Comment}'
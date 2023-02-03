from django.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Restaurants'
        verbose_name_plural = 'Restaurants'
           
class Location(models.Model):
    locationame = models.CharField(max_length=100)
    type_shop = models.CharField(max_length=100) #cambiar choise
    name_shop = models.CharField(max_length=100)
    
class Market(models.Model):
    name_market = models.CharField(max_length=100)
    name_product = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.FloatField()
    image_product = models.ImageField(upload_to='market', null=True, blank=True)
    notes = models.TextField(max_length=1000, blank=True, null=True)


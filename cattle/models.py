from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class StockType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Cattle(models.Model):
    enterprise = models.ForeignKey('Enterprise', null=True, blank=True, on_delete=models.SET_NULL)
    stock_type = models.ForeignKey('StockType', null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.CharField(max_length=15)
    name = models.CharField(max_length=254, null=True, blank=True)
    breed = models.ForeignKey('Breed', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.IntegerField()
    star_rating = models.IntegerField(null=True, blank=True)
    cbv = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.tag
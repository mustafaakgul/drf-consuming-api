from django.db import models


class SavedEmbeds(models.Model):
    type = models.CharField(max_length=15)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    html = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    thumbnail_url = models.URLField()
    thumbnail_width = models.IntegerField()
    thumbnail_height = models.IntegerField()
    author_url = models.URLField()
    author_name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=2)


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


class Test(models.Model):
    product_name = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)

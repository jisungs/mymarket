from django.db import models

# Create your models here.
class Product(models.Model):
    #id = models.Autofield()
    title = models.CharField(max_length=220)
    subtitle = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    discountPrice = models.IntegerField(default=0)



from decimal import Decimal
from django.db import models
from django.conf import settings
# Create your models here.

from .storates import ProtectedStorage

User = settings.AUTH_USER_MODEL
class Product(models.Model):
    #id = models.Autofield()
    user = models.ForeignKey(User, null= True, on_delete= models.SET_NULL)
    # user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products/', null= True, blank=True)
    media = models.FileField(storage=ProtectedStorage, upload_to='products/', null=True, blank=True)
    title = models.CharField(max_length=220)
    subtitle = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    discountPrice = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def has_inventory(self):
        return self.inventory > 0 #True or false 

    def remove_items_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory
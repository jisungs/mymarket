from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
class Product(models.Model):
    #id = models.Autofield()
    user = models.ForeignKey(User, null= True, on_delete= models.SET_NULL)
    # user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length=220)
    subtitle = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    discountPrice = models.IntegerField(default=0)


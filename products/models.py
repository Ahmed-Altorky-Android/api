from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=99.99)
    
    #@property
    def __str__(self):
       return self.title

    def get_descount(self):
       return "122"

from django.db import models
from home.models import BaseModel
import uuid
# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Products', null= True, related_name='related_categories')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    
    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

from django.db import models
import uuid

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'pictures/{new_file_name}'

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_available = models.PositiveBigIntegerField()
    quantity_type = models.ForeignKey(QuantityVariant , blank=True, null=True , on_delete=models.PROTECT)
    image = models.ImageField(upload_to=uniq_name_upload, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

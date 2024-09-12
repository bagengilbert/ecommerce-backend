from django.db import models

# Create your models here.
# model to represent product categories
class Categoty(models.Model):
    name = models.CharField(max_length=100)
##human redable string defines how objected should be represented as string 
def __str__(self):
    return self.name

# model to represent products 
class product(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveBigIntegerField()
    category = models.ForeignKey(Categoty,related_name="products",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/',blank=True,null=True)

def __str__(self):
    return self.name


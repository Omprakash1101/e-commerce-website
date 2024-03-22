from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
def validate_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")
class category(models.Model):
    name = models.CharField(max_length=255)
    class meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class seller(models.Model):
    seller_id = models.AutoField(primary_key = True, null=False, blank=True, verbose_name="seller ID")
    seller_name = models.CharField(max_length=200,default="")
    email = models.EmailField(validators =[validate_mail],null=False, blank=True)
    phone = models.PositiveBigIntegerField(null=False, blank=True)
    address = models.TextField(default="",null=False, blank=True)
    def __str__(self):
        return str(self.seller_id)
class Product(models.Model):
    product_id = models.AutoField(primary_key = True, null=False, blank=True, editable=True,verbose_name="seller ID")
    category = models.ForeignKey("category",related_name="product", on_delete=models.CASCADE,null=False,blank=True,editable=True)
    product_name = models.CharField(max_length=255, null=False, blank=True)
    seller_id = models.ForeignKey("seller",related_name="product", on_delete=models.CASCADE,null=False,blank=True,editable=True)
    product_image= models.ImageField(default="",null=False, blank=True)
    description = models.TextField(default="",null=False, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000, validators=([MinValueValidator(0.01)]), null=False, blank=True)
    available_stock = models.PositiveIntegerField(null=False, blank=True,default=0)
    def __str__(self):
        return str(self.product_id)

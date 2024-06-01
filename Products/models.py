from django.db import models
import uuid
from django.utils import timezone
# Create your models here.
# we are using inheritance to implement Do Not Repeat Yourself (DRY)
class BaseModel(models.Model):
  id = models.UUIDField(default = uuid.uuid4, editable = False, primary_key = True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class Product(BaseModel):
  product_name = models.CharField(max_length = 120)
  product_slug = models.SlugField(unique = True)
  product_description = models.TextField()
  product_price = models.IntegerField(default = 0)
  product_demo_price = models.IntegerField(default = 0)
  product_image = models.ImageField(upload_to = "public/static/", default="FoodOrderingSystem/public/static/myPassportSizePhoto.jpeg")
  quantity = models.IntegerField(null = True, blank = True)

class ProductMetaInfoarmation(BaseModel):
  product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name = "meta_info")
  product_quantity = models.CharField(max_length = 200, null=True, blank=True)
  is_restrict = models.BooleanField(default = False)
  restrict_quantity = models.IntegerField()


class ProductImages(BaseModel):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "images")
  product_image = models.ImageField(upload_to = "products")

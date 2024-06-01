import uuid
from datetime import datetime
from Products.models import Product, ProductMetaInfoarmation, ProductImages
from django.utils.text import slugify

def create_dummy_data():
    # Create a Product instance
    product = Product.objects.create(
        product_name="Vada Paw",
        product_slug=slugify("httpsaddress"),
        product_description="Vada Paw is a best Maharashtrian Dish",
        product_price=15,
        product_demo_price=0,
        quantity=1,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    # Create a ProductMetaInfoarmation instance
    product_meta_info = ProductMetaInfoarmation.objects.create(
        product=product,
        product_quantity="50 units",
        is_restrict=False,
        restrict_quantity=10,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    # Create a ProductImages instance
    product_image = ProductImages.objects.create(
        product=product,
        product_image="path/to/image.jpg",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    print("Dummy data created successfully")

def delete_Product_Data():
  Product.objects.all().delete()
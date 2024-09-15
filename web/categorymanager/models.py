from django.db import models

# Create your models here.



class CategoryModel(models.Model):
    category_name= models.CharField(max_length=100)
    category_state = models.BooleanField(default=True)


class SubcategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="subcategory_category")
    subcategory_name= models.CharField(max_length=100)
    subcategory_state = models.BooleanField(default=True)
    image_thumbnail = models.ImageField(upload_to='images/', default='')
    video_thumbnail = models.ImageField(upload_to='images/', default='')
    price =   models.CharField(max_length=100)
    
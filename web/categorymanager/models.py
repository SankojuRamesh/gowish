from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.



class CategoryModel(models.Model):
    category_name= models.CharField(max_length=100)
    category_state = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='images/', default='')
    image_thumbnail = models.ImageField(upload_to='thumbnails/', default='')
    video_thumbnail = models.ImageField(upload_to='video_thumbnails/', default='')

    def save(self, *args, **kwargs):
        # Save the original image
        #     super().save(*args, **kwargs)

        # Create and save the thumbnail in WebP format
        if self.thumbnail:
            self.image_thumbnail = self.make_thumbnail(self.thumbnail)
            super().save(*args, **kwargs)
        
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)        
        # Resize image maintaining the aspect ratio
        img.thumbnail(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            background = Image.new("RGB", img.size, (255, 255, 255))  # White background
            background.paste(img, mask=img.split()[3])  # Paste image using transparency mask
            img = background 
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG')  # Save as JPEG format

        # Return a Django File object
        thumbnail = File(thumb_io, name=image.name.replace('.png', '.jpg'))
        return thumbnail


class SubcategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="subcategory_category")
    subcategory_name= models.CharField(max_length=100)
    subcategory_state = models.BooleanField(default=True)
    image_thumbnail = models.ImageField(upload_to='images/', default='')
    video_thumbnail = models.ImageField(upload_to='images/', default='')
    price =   models.CharField(max_length=100)

    def save(self, *args, **kwargs): 
        if self.thumbnail:
            self.image_thumbnail = self.make_thumbnail(self.thumbnail)
            super().save(*args, **kwargs)
        
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)        
        # Resize image maintaining the aspect ratio
        img.thumbnail(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            background = Image.new("RGB", img.size, (255, 255, 255))  # White background
            background.paste(img, mask=img.split()[3])  # Paste image using transparency mask
            img = background

        # Save the image to BytesIO
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG')  # Save as JPEG format

        # Return a Django File object
        thumbnail = File(thumb_io, name=image.name.replace('.png', '.jpg'))
        return thumbnail
    
    
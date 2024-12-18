from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()



class StoreModel(models.Model):
    title = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    email= models.EmailField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_user')
    address = models.TextField(default='')




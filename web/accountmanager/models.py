from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser  
from django.contrib.auth import models as auth_models
# Create your models here.


class RolesModel(models.Model):
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=True)

class UserManager(BaseUserManager): 
    def create_user(self, phone, password= None,roles=None, **extra_fields):
         
        if not phone:
            raise ValueError("plese enter phone number")
        if not roles:
            roles = RolesModel.objects.get(id=1)
        user = self.model(phone=phone,roles=roles, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_employee(self, phone, password= None,roles=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        if not phone:
            raise ValueError("plese enter phone number")
        if not roles:
            roles = RolesModel.objects.get(id=2)
        user = self.model(phone=phone,roles=roles, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_storeadmin(self, phone, password= None,roles=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        if not phone:
            raise ValueError("plese enter phone number")
        if not roles:
            roles = RolesModel.objects.get(id=3)
        user = self.model(phone=phone,roles=roles, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,phone, password= None, **extra_fields):
         
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        roles = RolesModel.objects.get(id=1)
        if extra_fields.get('is_staff') is not True:
            raise ValueError( 'Superuser must have is_staff=True.')
            
        if extra_fields.get('is_superuser') is not True:
            raise ValueError( 'Superuser must have is_superuser=True.') 
             

        return self.create_user(phone, password, roles, **extra_fields)




class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin ):  
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, unique=True)

    email = models.EmailField(max_length=64, unique=True)

    address = models.CharField(max_length=100, blank=True, null=True)

    contact = models.CharField(max_length=100, blank=True, null=True)

    profile_pic = models.ImageField(  upload_to='profile/', blank=True, null=True)

    roles = models.ForeignKey(RolesModel, default=None,  on_delete=models.CASCADE, related_name= "usersroles")
    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = ('phone',) 
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_roles(self):
        if self.roles:
            return self.roles.name
    



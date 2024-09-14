from django.db import models
from django.contrib.auth import get_user_model
from templatemanager.models import TemplateModel

# Create your models here.

User = get_user_model()



class UserTemplatesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_template = models.ForeignKey(TemplateModel, on_delete=models.CASCADE)
    templaate_state = models.CharField(max_length=200, default="Edited",choices = (("Edited", "Edited"), ("Standed", "Standed")) )
    order_id = models.CharField(default=None, bool=True, max_length=200)



class UserTemplatesComposModel(models.Model):
    main_template = models.ForeignKey(TemplateModel, on_delete=models.CASCADE)
    template_order_modelId = models.ForeignKey(UserTemplatesModel, on_delete=models.CASCADE)
    composit_name = models.CharField(max_length=200)
    duration= models.CharField(max_length=200)
    startTime= models.CharField(max_length=200)
    frameRate= models.CharField(max_length=200)
    width= models.CharField(max_length=200)
    height= models.CharField(max_length=200)
    workAreaStartTime= models.CharField(max_length=200)
    workAreaEndTime= models.CharField(max_length=200)
    opacity= models.CharField(max_length=200)
    isLocked= models.CharField(max_length=200)



class UserTemplatesLayerModel(models.Model):
    main_template = models.ForeignKey(TemplateModel, on_delete=models.CASCADE)
    UserTemplatesCompositId = models.ForeignKey(UserTemplatesModel, on_delete=models.CASCADE)
    name  =   models.CharField(max_length=200)
    mainsrc  = models.CharField(max_length=200, null=True, blank=True)
    image  = models.FileField(upload_to='uploads/',default=None, null=True, blank=True)
    width  =models.CharField(max_length=200, null=True, blank=True)
    height  = models.CharField(max_length=200, null=True, blank=True)
    scalX  =  models.CharField(max_length=200, null=True, blank=True)
    scalY  =  models.CharField(max_length=200, null=True, blank=True)
    position  =  models.CharField(max_length=200, null=True, blank=True)  
    opacity  =  models.CharField(max_length=200, null=True, blank=True)
    rotation  = models.CharField(max_length=200, null=True, blank=True)
    anchorPoint  = models.CharField(max_length=200, null=True, blank=True)
    isLocked  =  models.CharField(max_length=200, null=True, blank=True)
    show  =  models.CharField(max_length=200, null=True, blank=True)
    type  =  models.CharField(max_length=200, null=True, blank=True)   
    text =  models.CharField(max_length=200, null=True, blank=True)
    size  =  models.CharField(max_length=200, null=True, blank=True)
    color =  models.CharField(max_length=200, null=True, blank=True)
    font =  models.CharField(max_length=200, null=True, blank=True)     
    inPoin =  models.CharField(max_length=200, null=True, blank=True)
    outPoint =  models.CharField(max_length=200, null=True, blank=True)


class WishListModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(TemplateModel)
    added_at = models.DateTimeField(auto_now=True)

class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(TemplateModel, on_delete=models.CASCADE)


class UserCreditsModel(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    credits = models.CharField(max_length=200, default='')
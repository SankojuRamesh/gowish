from django.db import models
from django.contrib.auth import get_user_model
from templatemanager.models import TemplateModel


User = get_user_model()

# Create your models here.


# class ProjectModel(models.Model) :
#     project_name = models.CharField(max_length=200)
#     project_path=  models.CharField(max_length=200)
#     status = models.BooleanField(default=True)
#     creatd_at = models.DateTimeField(auto_now=True)


class  CompositModel(models.Model) :
    project_id = models.ForeignKey(TemplateModel, on_delete=models.CASCADE, related_name=  "project_composit" )
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



class LayerModel(models.Model) :
    projectid = models.ForeignKey(TemplateModel, on_delete=models.CASCADE, related_name=  "project_layer" )
    compositid =  models.ForeignKey(CompositModel, on_delete=models.CASCADE, related_name=  "project_composit_layer" )
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

 



class UserTemplates(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    template_data = models.TextField(null=True, blank=True)
    
   


    


from django.db import models
import uuid
# Create your models here.

class Team(models.Model):
    # owner : 
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    designation = models.CharField(max_length=200,blank=True,null=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='profile_pics/%Y/%m/%d/', default='avatar/avatar-11.jpg')
    facebook_link = models.URLField(null=True,blank=True,max_length=120)
    twitter_link = models.URLField(null=True,blank=True,max_length=120,)
    google_link = models.URLField(null=True,blank=True,max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')

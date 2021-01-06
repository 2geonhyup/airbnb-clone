from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """
   
    created = models.DateTimeField(auto_now_add=True) # new model
    updated = models.DateTimeField(auto_now=True)   # update model

    class Meta:
        abstract = True 
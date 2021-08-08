from django.db import models
from django.utils.translation import deactivate

# Create your models here.
class Word(models.Model):
    value           = models.CharField(max_length=60)
    synonym         = models.CharField(max_length=60,default='')
    antonym         = models.CharField(max_length=60,default='') 
    partOfSpeech    = models.CharField(max_length=60,default='') 
    meaning         = models.CharField(max_length=120,default='')
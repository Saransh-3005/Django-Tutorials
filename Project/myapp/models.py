from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Feature(models.Model):
    head = models.CharField(max_length= 100)
    
   

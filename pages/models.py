from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')

def __str__(self):
    return self.title

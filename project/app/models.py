from django.db import models

# Create your models here.
class MyTestModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    sn_link = models.URLField()
    
    def __str__(self):
        return self.name
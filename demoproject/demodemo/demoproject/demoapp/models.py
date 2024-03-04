from django.db import models

# Create your models here.
class travel(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    detail = models.TextField()

    def __str__(self):
        return self.name

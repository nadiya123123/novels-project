from django.db import models

# Create your models here.
class new(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

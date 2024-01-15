from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="img_category")

    def __str__(self):
        return self.name
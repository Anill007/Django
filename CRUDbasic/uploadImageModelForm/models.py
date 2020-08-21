from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 30)
    image = models.FileField(upload_to = 'Products/functionView/')
    description = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
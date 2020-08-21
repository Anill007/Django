from django.db import models

# Create your models here.


class Product(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=40)
    Image = models.ImageField(
        upload_to='one/', default='try1.png')

    ModelFile = models.FileField(upload_to='two/', default='try_models.glb')

    def __str__(self):
        return self.Title

    def delete(self, *args, **kwargs):
        self.Image.delete()
        self.ModelFile.delete()
        super().delete(*args, **kwargs)

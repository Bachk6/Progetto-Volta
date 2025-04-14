from django.db import models

class Opera(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100) # opzionale
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)
    model_3D = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.title

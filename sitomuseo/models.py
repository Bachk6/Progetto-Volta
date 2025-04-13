from django.db import models

class Opera(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='opere/', blank=True, null=True)

    def __str__(self):
        return self.title

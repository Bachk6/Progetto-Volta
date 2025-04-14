from django.db import models

class Autore(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    birth_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.name

class Opera(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Autore ,on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)
    model_3D = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.title

class Crosswords(models.Model):
    opera = models.OneToOneField(Opera, on_delete=models.CASCADE)
    autore = models.OneToOneField(Autore, on_delete=models.CASCADE)
    field = models.CharField(max_length=200)
    # matrix = . . .

    def __str__(self):
        return f"Crosswords arguments: {self.opera.title} and {self.autore.name}"


    

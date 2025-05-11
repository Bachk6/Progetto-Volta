from django.db import models
 
#Modello Autore
class Autore(models.Model): 
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    nation = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.name+" "+self.surname
    
# Modello opera
class Opera(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Autore, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.title
    



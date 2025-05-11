from django.db import models
 
#Modello Autore

class Autore(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    birth_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.name+" "+self.surname

class Opera(models.Model):
    title = models.CharField(max_length=200)
    author = models.OneToOneField(Autore,on_delete=models.CASCADE);
    #models.ForeignKey(Autore ,on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)
    #model_3D = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)

    def __str__(self):
        return self.title

class Crossword(models.Model):
    opera = models.OneToOneField(Opera, on_delete=models.CASCADE)
    autore = models.OneToOneField(Autore, on_delete=models.CASCADE)
    field = models.CharField(max_length=200)
    matrix = models.JSONField()

    def __str__(self):
        return f"Crosswords arguments: {self.opera.title} and {self.autore.name}"

class Utente(models.Model):
    username = models.CharField(max_length=200)
    icona = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)
    hash = models.CharField(max_length=257)
    crosswords = models.ManyToManyField('Crossword')
    achievements = models.ManyToManyField('Achievement')

    def __str__(self):
        return self.username
    
class Achievement(models.Model):
    nome = models.CharField(max_length=200)
    icona = models.ImageField(upload_to='media/imgsrc/', blank=True, null=True)
    description = models.TextField()
    condition = models.TextField()

    def __str__(self):
        return self.nome

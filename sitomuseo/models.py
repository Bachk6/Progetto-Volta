from django.db import models

# Create your models here.
class Spostamento (models.Model):
    coordinates = models.CharField(max_length=100)

    def where(self):
        return self.coordinates

class Sala (models.Model):
    # spheric_img = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def get_desc(self):
        return self.description

    def get_model(self):
        return self.spheric_img

class PuntoDiInteresse (models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)

    def where(self):
        return self.coordinates

    def get_name(self):
        return self.name

class Opera (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # model3D = models.CharField(max_length=100)

    def get_desc(self):
        return self.description

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model3D

class Collezione (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def get_desc(self):
        return self.description

    def get_name(self):
        return self.name

class Autore (models.Model):
    name = models.CharField(max_length=100)
    descrizione = models.CharField(max_length=100)
    nazionalita = models.CharField(max_length=100)
    data_nascita = models.CharField(max_length=100)
    data_morte = models.CharField(max_length=100)
    eta = models.CharField(max_length=100)

    def get_desc(self):
        return self.description

    def get_name(self):
        return self.name

    def get_nazionalita(self):
        return self.nazionalita

    def get_data_nascita(self):
        return self.data_nascita

    def get_data_morte(self):
        return self.data_morte

    '''
    def get_eta(self):
        return self.eta
    '''

